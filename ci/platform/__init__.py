import pipes

import collections


class Shell(object):
    def __init__(self, address, creds):
        self._address = address
        self.creds = creds

    def execute(self, cmdline, input=None, timeout=None):
        if isinstance(cmdline, (list, tuple)):
            cmdline = map(pipes.quote, cmdline)
        elif isinstance(cmdline, basestring):
            cmdline = pipes.quote(cmdline)
        else:
            raise ValueError('Invalid cmdline: %r' % cmdline)
        return self._execute(cmdline, input=input, timeout=timeout)

    def _execute(self, cmdline, input=None, timeout=None):
        raise NotImplementedError('execute')

    @staticmethod
    def fork(platform):
        from ci.platform import shell
        return {'osx': shell.OSX,
                'win7': shell.Win7,
                'win10': shell.Win7}.get(platform.type)(platform.address, Credentials(*platform.creds))


Credentials = collections.namedtuple('Credentials', 'user password')
