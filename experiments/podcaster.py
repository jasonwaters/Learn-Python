def writeLine(line):
    file.write(line)
    file.write("\n")

def writeItem(title, url):
    writeLine('<item>')
    writeLine('<title>%s</title>' % title)
    writeLine('<enclosure url="%s" type="video/mp4"/>' % url)
    writeLine('</item>')


podcastTitle = 'CHISELED [ Bodylastics ]'
websiteUrl = 'http://bodylastics.com'
filename = "feed.xml"


file = open(filename, "w")

writeLine('<?xml version="1.0" encoding="UTF-8"?>')
writeLine('<rss version="2.0">')
writeLine('<channel>')
writeLine('<title>%s</title>' % podcastTitle)
writeLine('<link>%s</link>' % websiteUrl)


for i in range(219,301):
    writeItem('Episode %s' % i, 'http://bitcast-a.v1.sjc1.bitgravity.com/rlminc/vod/chiseled/videos/chiseled_%s.mp4' % i)

writeLine('</channel>')
writeLine('</rss>')

file.close()