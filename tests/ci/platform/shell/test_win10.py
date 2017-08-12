# coding=utf-8
import unittest

import nose

import ci
from ci.platform import Credentials


class Test(unittest.TestCase):

    def test_shell(self):
        nose.tools.assert_equals(
            ci.Platform('win10', 'win10_en_ci_1',
                        Credentials('ci1', '1234')
                ).shell.execute('whoami'),
            (0, u'desktop-fvjv3dj\ci1\r\n', ''))