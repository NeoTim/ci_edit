# Copyright 2016 The ci_edit Authors. All rights reserved.
# Use of this source code is governed by an Apache-style license that can be
# found in the LICENSE file.

import curses


CTRL_AT = 0x00
CTRL_SPACE = 0x00
CTRL_A = 0x01
CTRL_B = 0x02
CTRL_C = 0x03
CTRL_D = 0x04
CTRL_E = 0x05
CTRL_F = 0x06
CTRL_G = 0x07
CTRL_H = 0x08
CTRL_I = 0x09
CTRL_J = 0x0a
CTRL_K = 0x0b
CTRL_L = 0x0c
CTRL_M = 0x0d
CTRL_N = 0x0e
CTRL_O = 0x0f
CTRL_P = 0x10
CTRL_Q = 0x11
CTRL_R = 0x12
CTRL_S = 0x13
CTRL_T = 0x14
CTRL_U = 0x15
CTRL_V = 0x16
CTRL_W = 0x17
CTRL_X = 0x18
CTRL_Y = 0x19
CTRL_Z = 0x1a
CTRL_OPEN_BRACKET = 0x1b  # ^[
CTRL_BACKSLASH = 0x1c  # ^\
CTRL_CLOSE_BRACKET = 0x1d  # ^]
CTRL_CARROT = 0x1e  # ^^
CTRL_UNDERBAR = 0x1f  # ^_


def mouseButtonName(bstate):
  """Curses debugging. Prints readable name for state of mouse buttons."""
  result = ''
  if bstate & curses.BUTTON1_RELEASED:
    result += 'BUTTON1_RELEASED'
  if bstate & curses.BUTTON1_PRESSED:
    result += 'BUTTON1_PRESSED'
  if bstate & curses.BUTTON1_CLICKED:
    result += 'BUTTON1_CLICKED'
  if bstate & curses.BUTTON1_DOUBLE_CLICKED:
    result += 'BUTTON1_DOUBLE_CLICKED'

  if bstate & curses.BUTTON2_RELEASED:
    result += 'BUTTON2_RELEASED'
  if bstate & curses.BUTTON2_PRESSED:
    result += 'BUTTON2_PRESSED'
  if bstate & curses.BUTTON2_CLICKED:
    result += 'BUTTON2_CLICKED'
  if bstate & curses.BUTTON2_DOUBLE_CLICKED:
    result += 'BUTTON2_DOUBLE_CLICKED'

  if bstate & curses.BUTTON3_RELEASED:
    result += 'BUTTON3_RELEASED'
  if bstate & curses.BUTTON3_PRESSED:
    result += 'BUTTON3_PRESSED'
  if bstate & curses.BUTTON3_CLICKED:
    result += 'BUTTON3_CLICKED'
  if bstate & curses.BUTTON3_DOUBLE_CLICKED:
    result += 'BUTTON3_DOUBLE_CLICKED'

  if bstate & curses.BUTTON4_RELEASED:
    result += 'BUTTON4_RELEASED'
  if bstate & curses.BUTTON4_PRESSED:
    result += 'BUTTON4_PRESSED'
  if bstate & curses.BUTTON4_CLICKED:
    result += 'BUTTON4_CLICKED'
  if bstate & curses.BUTTON4_DOUBLE_CLICKED:
    result += 'BUTTON4_DOUBLE_CLICKED'

  if bstate & curses.REPORT_MOUSE_POSITION:
    result += 'REPORT_MOUSE_POSITION'

  if bstate & curses.BUTTON_SHIFT:
    result += ' SHIFT'
  if bstate & curses.BUTTON_CTRL:
    result += ' CTRL'
  if bstate & curses.BUTTON_ALT:
    result += ' ALT'
  return result