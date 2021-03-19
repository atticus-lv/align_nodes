# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Align Nodes",
    "author" : "Kuldeep Singh",
    "description" : "This tool allows to align the nodes in any nodes editor.",
    "blender" : (2, 79, 0),
    "version" : (0, 0, 1),
    "location": "Nodes Editor",
    "category": "Node",
    "warning":  "This version is still in development."
}

from . import auto_load

def register():
    auto_load.register()

def unregister():
    auto_load.unregister()
