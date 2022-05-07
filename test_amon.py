"""
Unit tests for amon.
"""
import io
import pytest
import amon
import pygame
from amon import Amon

'''
Rough idea for testing movement
'''

'''
def test_movement():
    initial_position=amon_stats()[0]
    user_input=pygame.K_LEFT
    movement(user_input)
    assert amon_stats()[0]==(initial_position-2)

'''
def test_does_amon_exist():
    '''
    '''
    user = Amon()
    assert user.amon_stats == [200, 200, "down","red"]
def test_out_of_bounds():
    '''
    '''
    user = Amon()
    user._xmovement = 500-200
    user._ymovement = 500-200
    user.amon_passive_update()
    user.amon_passive_update()
    assert user.amon_stats == [478,472,"down","red"]
def test_in_bounds():
    '''
    '''
    user = Amon()
    user._xmovement = 50
    user._ymovement = 50
    user.amon_passive_update()
    user.amon_passive_update()
    assert user.amon_stats == [250,250,"down","red"]