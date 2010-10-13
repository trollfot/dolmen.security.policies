# -*- coding: utf-8 -*-

import os
import re
import doctest
import unittest
import pprint

from zope.app.testing.functional import ZCMLLayer
from zope.testing import renormalizing

zcml = os.path.join(os.path.dirname(__file__), 'ftesting.zcml')
layer = ZCMLLayer(zcml, __name__, 'dolmen.security.policies')

checker = renormalizing.RENormalizing([
    # Accommodate to exception wrapping in newer versions of mechanize
    (re.compile(r'httperror_seek_wrapper:', re.M), 'HTTPError:')])


def test_suite():
    suite = unittest.TestSuite()
    files = ('README.txt',)
    for filename in files:
        docfile = doctest.DocFileSuite(
            filename,
            checker=checker,
            globs={'pprint': pprint.pprint},
            optionflags=(doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS))
        docfile.layer = layer
        suite.addTest(docfile)
    return suite
