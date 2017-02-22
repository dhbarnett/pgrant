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
        z = Zeppelin('test/invalid.json')


def test_zeppelin_created_valid_json():
    z = Zeppelin('test/valid.json')
    assert(isinstance(z, Zeppelin))


def test_zeppelin_no_category():
    z = Zeppelin('test/emptynote.json')
    assert('', z.get_category())


def test_zeppelin_with_category():
    z = Zeppelin('test/NoteWithData.json')
    assert('foo|bar|baz', z.get_category())


def test_zeppelin_no_team():
    z = Zeppelin('test/emptynote.json')
    assert('', z.get_team())


def test_zeppelin_with_team():
    z = Zeppelin('test/NoteWithData.json')
    assert('team1', z.get_team())
