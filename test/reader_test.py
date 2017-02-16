#!/usr/bin/env python

import pytest
from zeppelin import Zeppelin


def test_zeppelin_invalid_notebook_name():
    with pytest.raises(IOError):
        z = Zeppelin('/notafile/zep.json')


def test_zeppelin_invalid_notebook():
    with pytest.raises(TypeError):
        z = Zeppelin(None)


def test_zeppelin_invalid_json():
    with pytest.raises(ValueError):
        z = Zeppelin('invalid.json')


def test_zeppelin_created_valid_json():
    z = Zeppelin('valid.json')
    assert(isinstance(z, Zeppelin))

def test_zeppelin_no_paragraphs
