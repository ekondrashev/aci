# coding=utf-8
import unittest

import nose

import ci
from ci.platform import Credentials


class Test(unittest.TestCase):

    def test_shell(self):
        nose.tools.assert_equals(
            ci.Platform('win7', 'Win7', Credentials('ci1', '123')).shell.execute('whoami'),
            (0, '\xa5\xa2\xa3\xa5\xad\xa8\xa9-\xaf\xaa\\ci1\r\n', ''))