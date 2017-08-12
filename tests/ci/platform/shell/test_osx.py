import unittest

import nose

import ci


class Test(unittest.TestCase):

    def test_shell(self):
        nose.tools.assert_equals(
            ci.Platform('osx', 'ci1').shell.execute('whoami'),
            (0, b'ci1\n', b''))
