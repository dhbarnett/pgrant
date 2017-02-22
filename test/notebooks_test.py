#!/usr/bin/env python

import pytest
from pgrant import Pgrant


def test_zeppelin_notebooks():
    pg = Pgrant('pgrant.json')
    pg.process_notebooks()
    pass