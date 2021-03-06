#!/usr/bin/env python3

class Report(object):
    """
    A ticketfrei report object.

    Toots, Tweets, and E-Mails can be formed into ticketfrei reports.

    """

    def __init__(self, author, source, text, id, timestamp):
        """
        Constructor of a ticketfrei report

        :param author: username of the author
        :param source: mastodon, twitter, or email
        :param text: the text of the report
        :param id: id in the network
        :param timestamp: time of the report
        """
        self.author = author
        self.type = source
        self.text = text
        self.timestamp = timestamp
        self.id = id

    def format(self):
        """
        Format the report for bot.post()

        :rtype: string
        :return: toot: text to be tooted, e.g. "_b3yond: There are
            uniformed controllers in the U2 at Opernhaus."
        """
        strng = self.author + ": " + self.text
        return strng
