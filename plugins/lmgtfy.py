#!/usr/bin/python

# Deception IRC Bot
#
# Copyright (C) 2012 p1ra <p1ra@smashthestack.org>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.

'''
Deception IRC Bot - by p1ra <p1ra@smashthestack.org>

Let me google that for you

'''

# ----------------
# Command Handlers
# ----------------

def lmgtfy(session, cmd=None):
    ''' Send lmgtfy url '''
    if len(cmd.args) == 0:
        return False

    session.privmsg(cmd.target, "http://lmgtfy.com/?q='%s'" % cmd.args[0])

COMMAND_HANDLERS = {
    "lmgtfy": (lmgtfy, 0),
}
