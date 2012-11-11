#!/usr/bin/env python

import os, sys, pdb, re, shutil
import datetime
import transmissionrpc
from transmissionrpc.error import TransmissionError

class Organizer(object):
    def __init__(self):
        # Class Variables
        #------------------
        self.DOWNLOAD_FOLDER = "/Users/jasonwaters/Downloads"
        self.TV_FOLDER = "/Volumes/Blue/TV"
        self.MOVIE_FOLDER = "/Volumes/Blue/Movies"

        self.TRANSMISSION_HOST = "localhost"
        self.TRANSMISSION_PORT = 9091
        self.TRANSMISSION_USER = "admin"
        self.TRANSMISSION_PASSWORD = "user"

        self.PATTERN_EPISODE = re.compile(".*(([sS]\d+[eE]\d+)|(\d+x\d+)).*")
        self.PATTERN_VIDEO = re.compile("(^.+\.(avi|mp4|mkv)$)")
        self.PATTERN_RAR = re.compile("^.+\.(rar|r\d+)$")

        self.mark_file_name = '.unrared'
        self.extensions_unrar = ['.rar', '.r01']        # List of extensions for auto-extract to look for
        self.supported_filetypes = []                   # Filled by extensions_list function
        self.extensions_list()

        self.unrar_check()
        # Check that the download directory parameters is actually a directory
        self.removeFinishedTorrents()
        self.traverse_directories()

    def log(self, message):
        now = datetime.datetime.now()
        print "%s | %s\n" % (now.strftime("%Y-%m-%d %H:%M"), message)

    '''Creates the list of extensions supported by the script'''
    def extensions_list(self):
        self.supported_filetypes.extend(self.extensions_unrar)       # rar support

    '''Figures out what the unrar executable name should be'''
    def unrar_exe(self):
        self.unrar_name = 'unrar'

    '''Attempts to find unrar on the system path and return the directory unrar is found in'''
    def find_unrar(self):
        # Search the system path for the unrar executable
        for dir in os.getenv('PATH').split(os.pathsep):
            # Ensure the dir in the path is a real directory
            if os.path.exists(dir):
                files = os.listdir(dir)
                if self.unrar_name in files:
                    #self.log('Found ' + self.unrar_name +' in ' + dir)
                    return dir
            else:
                # The directory in the path does not exist
                pass
        # unrar not found on this system
        return False

    '''Sanity check to make sure unrar is found on the system'''
    def unrar_check(self):
        self.unrar_exe()
        self.unrar_path = self.find_unrar()
        if self.unrar_path != False:
            self.unrar_exe = os.path.join(self.unrar_path, self.unrar_name)
        else:
            self.log('Error: ' + self.unrar_name + ' not found in the system path')
            exit()

    '''Scan the download directory and its subdirectories'''
    def traverse_directories(self):
        # Search download directory and all subdirectories
        for dirname, dirnames, filenames in os.walk(self.DOWNLOAD_FOLDER):
            self.scan_for_archives(dirname)
            self.scan_for_videos(dirname)

    '''Check for rar files in each directory'''
    def scan_for_archives(self, dir):
        # Look for a .rar archive in dir
        dir_listing = os.listdir(dir)
        # First archive that is found with .rar extension is extracted
        # (for directories that have more than one archives in it)
        for filename in dir_listing:
            for ext in self.supported_filetypes:
                if filename.endswith(ext):
                    # If a .rar archive is found, check to see if it has been extracted previously
                    file_unrared = os.path.exists(os.path.join(dir, self.mark_file_name))
                    if not file_unrared:
                        self.log("Need to extract: " + filename)
                        # Start extracting file
                        self.start_unrar(dir, filename)
                    else:
                        self.log('Skipping archive ' + filename)
                        self.delete_rars(dir)
                    # .rar was found, dont need to search for .r01
                    break

    '''Check for video files in each directory and move them'''
    def scan_for_videos(self, dir):
        dir_listing = os.listdir(dir)

        for filename in dir_listing:
            if self.isValidVideoFile(filename):
                filePath = os.path.join(dir,filename)
                folder = ""
                self.log("Moving %s..." % filename)
                if self.isTVEpisode(filename):
                    shutil.move(filePath, self.TV_FOLDER)
                    folder = self.TV_FOLDER
                else:
                    shutil.move(filePath, self.MOVIE_FOLDER)
                    folder = self.MOVIE_FOLDER

                self.log("Moved %s to '%s' folder" % (filename, folder))

    def delete_rars(self, dir):
        self.log("Deleting RARs...")
        dir_listing = os.listdir(dir)

        for filename in dir_listing:
            if self.isRar(filename):
                self.log("deleted %s" % filename)
                os.remove(os.path.join(dir,filename))

    '''Extract a rar archive'''
    def start_unrar(self, dir, archive_name):
        # Create command line arguments for rar extractions
        cmd_args = ['','','','','']
        cmd_args[0] = self.unrar_name                   # unrar
        cmd_args[1] = 'e'                               # command line switches: e - extract
        cmd_args[2] = '-y'                              # y - assume yes to all queries (overwrite)
        cmd_args[3] = os.path.join(dir, archive_name)   # archive path
        cmd_args[4] = dir                               # destination

        try:
            os.spawnv(os.P_WAIT, self.unrar_exe, cmd_args)
        except OSError:
            self.log('Error: ' + self.unrar_name + ' not found in the given path.')
            exit()

        # Sucessfully extracted archive, mark the dir with a hidden file
        self.mark_dir(dir)
        self.delete_rars(dir)

    '''Creates a hidden file so the same archives will not be extracted again'''
    def mark_dir(self, dir):
        mark_file = os.path.join(dir, self.mark_file_name)
        f = open(mark_file,'w')
        f.close()
        self.log(self.mark_file_name + ' file created')

    def isRar(self, name):
        return self.PATTERN_RAR.match(name.lower()) is not None

    def isTVEpisode(self, name):
        return self.PATTERN_EPISODE.match(name.lower()) is not None

    def isValidVideoFile(self, name):
        return self.PATTERN_VIDEO.match(name.lower()) is not None and name.find('sample') == -1

    def removeFinishedTorrents(self):
        try:
            client = transmissionrpc.Client(address=self.TRANSMISSION_HOST, port=self.TRANSMISSION_PORT,user=self.TRANSMISSION_USER,password=self.TRANSMISSION_PASSWORD)
        except TransmissionError as error:
            self.log("Unable to connect to Transmission.")
            self.log(error)

        torrents = client.info()

        for tid, torrent in torrents.iteritems():
            if torrent.progress == 100:
                self.log('Removed   %s.' % torrent.name)
                client.remove(torrent.hashString, delete_data=False)


if __name__ == '__main__':
    obj = Organizer()
