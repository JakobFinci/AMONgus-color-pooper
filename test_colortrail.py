'''
unit tests for colortrail.py
'''
import pytest #pylint: disable=unused-import
from amon import Amon
from colortrail import Defecate

def test_color_trail_yellow():
    '''
    Test to see if changing the sprite color changes the trail color
    '''
    user = Amon()
    color_user = Defecate(user)
    user.edit_amon_stats(200, 200, "down","yellow")
    user.amon_passive_update()
    user.amon_passive_update()
    color_user.poop()
    assert color_user.poop() == ["yellow", (200, 200),3]

def test_color_trail_red():
    '''
    Test to see if changing the sprite color changes the trail color
    '''
    user = Amon()
    color_user = Defecate(user)
    user.edit_amon_stats(200, 200, "down","red")
    user.amon_passive_update()
    user.amon_passive_update()
    color_user.poop()
    assert color_user.poop() == ["red", (200, 200),3]

def test_color_trail_blue():
    '''
    Test to see if changing the sprite color changes the trail color
    '''
    user = Amon()
    color_user = Defecate(user)
    user.edit_amon_stats(200, 200, "down","blue")
    user.amon_passive_update()
    user.amon_passive_update()
    color_user.poop()
    assert color_user.poop() == ["blue", (200, 200),3]

def test_color_trail_white():
    '''
    Test to see if changing the sprite color changes the trail color
    '''
    user = Amon()
    color_user = Defecate(user)
    user.edit_amon_stats(200, 200, "down","white")
    user.amon_passive_update()
    user.amon_passive_update()
    color_user.poop()
    assert color_user.poop() == ["white", (200, 200),3]
    