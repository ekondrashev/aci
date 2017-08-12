# coding=utf-8
import pipes
import subprocess
from subprocess import PIPE

from ci.platform import Shell


class OSX(Shell):

    def _execute(self, cmdline, input=None, timeout=None):
        if isinstance(cmdline, (list, tuple)):
            cmdline = pipes.quote(' '.join(cmdline))
        else:
            cmdline = pipes.quote(cmdline)
        process = subprocess.Popen(
            ['ssh', pipes.quote(self._address), cmdline],
            stderr=PIPE, stdout=PIPE)
        out, err = process.communicate(input=input)
        return process.returncode, out, err



class Win7(Shell):
    def _execute(self, cmdline, input=None, timeout=None):
        import virtualbox
        vbox = virtualbox.VirtualBox()
        vm = vbox.find_machine(self._address)
        with vm.create_session() as session:
            with session.console.guest.create_session(self.creds.user, self.creds.password) as gs:
                arguments = ['/C']
                if isinstance(cmdline, basestring):
                    arguments.append(cmdline)
                else:
                    arguments.extend(cmdline)
                process, stdout, stderr = gs.execute('C:\\Windows\\System32\\cmd.exe', arguments)
                stdout = stdout.decode('cp866')
                print stdout
                stderr = stderr.decode('cp866')
                return process.exit_code, stdout, stderr
