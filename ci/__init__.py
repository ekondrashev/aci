
from itertools import starmap

from ci import platform


class Platform(object):

    def __init__(self, type, address, creds):
        self.type = type
        self.address = address
        self.creds = creds

    @classmethod
    def from_json(cls, details):
        return cls(details['type'], details['address'], details['credentials'])

    @property
    def shell(self):
        return platform.Shell.fork(self)


class Platforms(object):
    def __init__(self, platforms):
        self._platforms = starmap(Platform, platforms)

    @classmethod
    def from_json(cls, platforms):
        return map(Platform.from_json, platforms)

    def __iter__(self):
        return iter(self._platforms)



class Build(object):

    def __init__(self, commands, vars):
        self.commands = commands
        self.vars = vars

    def run(self, platform, vars=None):
        pass