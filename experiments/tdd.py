#!/usr/bin/env python
import unittest

class SendMessage():
    def send(self, *args):
        print args



class TestMessage(unittest.TestCase):
    def setUp(self):
        self.sm = SendMessage()


    def test_send(self):
        self.sm.send("joe@example.com", "Hi there!")
        self.assertTrue(True)

    def test_invalid_email(self):
        self.sm.send("joewithnoatsign", "Hi there!")

    def test_invalid_body(self):
        self.sm.send("joe@example.com")

    def test_send_multiple(self):
        self.sm.send("joe@example.com", "jane@example.com", "Hi there!")

    def test_multiple_invalid_email(self):
        self.sm.send("notvalidemail", "alsonotvalid", "Hi There!")

    def test_send_other_format(self):
        self.sm.send("-im", "alice@chat.example.com", "Hey There")

    def test_send_multiple_other_format(self):
        self.sm.send("-im", "alice@chat.com", "bob@chat.com", "hello.")

    def test_network_failure(self):
        self.sm.send("lisa@somewhere.com", "hi Lisa")


if __name__ == '__main__':
    unittest.main()