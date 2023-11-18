# <pep8 compliant>
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

import bpy
from . import crownmoldingpack

#  Inspired by Danny Mac 3D
#  https://www.youtube.com/channel/UC10BuhxlV7Y53R0l9RJimmA
#  https://www.youtube.com/watch?v=dnlPidRHs1Q&lc=Ugzjf6_XUGrXcsRDTA94AaABAg
#  Special thanks to p2or on
#  https://blender.stackexchange.com/questions/57306/how-to-create-a-custom-ui

#  CHANGELOG
#  v 0.0.0 October 2015 Crown Molding Pack
#    ☒ Initial 15 crown molding path pack, 1 trim path, 1 wall path, no Add-on
#  v 0.0.1 September 2019 Crown Molding Pack v2
#    ☒ Inital Add-on, 29 more paths (46 unique paths, 71 total paths)
#        ☒ 15 Crown Molding Paths
#        ☒ 1 Wall Base Path
#        ☒ 25 Top Trim Paths (25 top and 25 bottom)
#        ☒ 5 Middle Trim Paths
#        ☒ 1 Trim Mesh Object
#        ☒ 46 Unique Paths
#        ☒ 71 Total Paths
#        ☒ 72 Total Objects
#    ☒ 13 Add-on features:
#        ☒ Convert to Crown Molding - Works with single or multipe faces and
#          edges. Converts mesh faces or edges to separate curves with the
#          proper rotation, and attempts to set the bevel object to a crown
#          molding path.
#        ☒ Tilt - - Works with single or multiple 3D curves. Rotates selected
#          3D curves tilt by -90 degrees.
#        ☒ Tilt + - Works with single or multiple 3D curves. Rotates selected
#          3D curves tilt by 90 degrees.
#        ☒ Tilt <> - Works with single or multiple 3D curves. Rotates selected
#          3D curves tilt by 180 degrees.
#        ☒ Mirror X - Works with all objects. Mirrors objects on the Global
#          X Axis.
#        ☒ Mirror Y - Works with all objects. Mirrors objects on the Global
#          Y Axis.
#        ☒ Mirror Z - Works with all objects. Mirrors objects on the Global
#          Z Axis.
#        ☒ Scale - - Works with single or multiple curves. Decreases the scale
#          of curves without changing the path.
#        ☒ Scale + - Works with single or multiple curves. Increases the scale
#          of curves without changing the path.
#        ☒ <> Direction - Works with single or multiple curves. Switches the
#          direciton of the curve, which will change what side the bevel object
#          appears.
#        ☒ Curve 2D - Works with single or multiple curves. Converts selected
#          curves to 2D dimension.
#        ☒ Curve 3D - Works with single or multiple curves. Converts selected
#          curves to 3D dimension.
#        ☒ 2D/3D - Works with single or multiple curves. Converts selected
#          curves to 2D dimension if they are 3D, and vice versa.
#  v 0.0.2 January 2021 Crown Molding Pack v2.1
#    ☒ Add-on updated for Blender 2.91 (bevel_mode = 'OBJECT') and 53 more
#        paths (99 unique paths, 124 total paths). Renamed path objects for
#        better organization.
#    ☒ 15 Crown Molding Paths - These objects are named Ceiling.CrownXX.
#    ☒ 26 Floor Base Paths - These objects are named Floor.SomethingXX.
#    ☒ 25 Window Paths - There are 2 versions of each path,
#      Window.TrimbottomXX and Window.TrimtopXX.
#    ☒ 14 Panel Trim Paths - These objects are named Panel.SomethingXX.
#    ☒ 10 Wall Trim Paths - These objects are named Wall.SomethingXX.
#    ☒ 4 Rail Paths - These objects are named Rail.SomethingXX.
#    ☒ 5 Miscellaneous Trim Paths - These objects are named
#      Misc.SomethingXX.
#    ☒ 1 Trim Mesh Object - This object is named Misc.Trimcap01.
#  v 0.0.3 October 2021 Crown Molding Pack v2.2
#    ☒ Add-on updated to add new "Next" and "Previous" buttons to cycle
#      through provided curves. Can also be modified in python code.
#    ☒ Added 19 new ceiling crown molding paths, and 20 picture frame paths.
#       (138 unique paths, 163 total paths)
#  v 0.0.4 January 2022 Crown Molding Pack v2.3
#    ☒ Fixed bug - faces with arbitrary rotation didn't convert to paths
#      properly. Added Auto-rotate Curve checkbox to control if add-on tries
#      to rotate the curve (legacy behavior, checkbox checked) or not (checkbox
#      not checked). Thanks for the report, Piero!
#  v 0.0.5 June 2022 Crown Molding Pack v2.4
#    ☒ Fixed bug - Undo after crown molding creation might crash blender.
#      Added a undo step to the WM_OT_ConvertToCMP function to fix this.
#      Thanks for the report, Piero!
#  v 3.0.0 July 2023 Crown Molding Pack 3.0
#    ☒ New UI for path selection
#    ☒ New version numbering for less confusion by Jeff.
#  v 3.1.0 October 2023
#    ☒ Changed some variable names to avoid collision with other add-ons.
#      Thanks for the report, Trey!
#  v 3.1.1 November 2023
#    ☒ Fixed an error with removing the add-on or uninstalling it.
#    ☒ Removed empty materials in the .blend from paths that were used in testing, which
#      also caused errors.
#    ☒ Cleaned up console logging to remove unnecessary logs.


bl_info = {
    "name": "Crown Molding Pack Tools",
    "description": "Helper tools for creating and "
    "manipulating crown molding in the 3D Viewport.",
    "author": "Jeff Lange @jefftml",
    "version": (3, 1, 1),
    "blender": (2, 80, 0),
    "location": "3D View > Tools",
    "warning": "",
    "category": "Object"
}


def register():
    crownmoldingpack.register()


def unregister():
    crownmoldingpack.unregister()


if __name__ == "__main__":
    register()
