# -*- coding: utf-8 -*-
# jsfsdb (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from unittest import TestCase
import os
import configparser
from pathlib import Path, PurePath

from . import jsfsdb



class BasicTestCase(TestCase):
    def setUp(self):
        self.db = jsfsdb(dbpath=os.environ["JSFSDB_PATH"])

    def tearDown(self):
        pass

    def test_basic(self):
        "ensure the minimum test works"
        self.db.create({"ok": True}, "test", id=1)
        self.db.create({"ok": True}, "test", id=2)
