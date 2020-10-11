#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Check_MK GitLab Runner Status plugin
#
# Copyright 2020, Andrea Mancuso <andrea@fusilab.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

group = "agents/" + _("Agent Plugins")

register_rule(group,
    "agent_config:gitlab_runner",
    DropdownChoice(
        title = _("GitLab Runner Status (Linux)"),
        help = _("This will deploy the agent plugin <tt>gitlab_runner</tt> for monitoring "
                 "the status of GitLab Runner daemon."),
        choices = [
                    ( True,   _("Deploy GitLab Runner Status plugin") ),
                    ( False, _("Do not deploy GitLab Runner Status plugin") ),
        ]
    )
)
