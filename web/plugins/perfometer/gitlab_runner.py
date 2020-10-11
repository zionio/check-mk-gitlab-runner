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


def perfometer_gitlab_runner(row, check_command, perf_data):
    display_value = int(perf_data[0][1])
    display_string = "%s runner" % display_value
    display_color = '#a3afc9'

    return display_string, perfometer_linear(display_value, display_color)

perfometers["check_mk-gitlab_runner"] = perfometer_gitlab_runner
