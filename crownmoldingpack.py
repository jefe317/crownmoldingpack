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

import re
import os
from bpy.types import (Panel, Operator, PropertyGroup)
from bpy.props import (BoolProperty, EnumProperty, PointerProperty)
import bpy.utils.previews

CMPlist = [
    'Ceiling-Crown01', 'Ceiling-Crown02', 'Ceiling-Crown03',
    'Ceiling-Crown04', 'Ceiling-Crown05', 'Ceiling-Crown06', 'Ceiling-Crown07',
    'Ceiling-Crown08', 'Ceiling-Crown09', 'Ceiling-Crown10', 'Ceiling-Crown11',
    'Ceiling-Crown12', 'Ceiling-Crown13', 'Ceiling-Crown14', 'Ceiling-Crown15',
    'Ceiling-Crown16', 'Ceiling-Crown17', 'Ceiling-Crown18', 'Ceiling-Crown19',
    'Ceiling-Crown20', 'Ceiling-Crown21', 'Ceiling-Crown22', 'Ceiling-Crown23',
    'Ceiling-Crown24', 'Ceiling-Crown25', 'Ceiling-Crown26', 'Ceiling-Crown27',
    'Ceiling-Crown28', 'Ceiling-Crown29', 'Ceiling-Crown30', 'Ceiling-Crown31',
    'Ceiling-Crown32', 'Ceiling-Crown33', 'Ceiling-Crown34',
    'Corner-Cornerguard01', 'Corner-Cornerguard02', 'Corner-Plycap01',
    'Corner-Plycap02', 'Corner-Plycap03', 'Floor-Base01', 'Floor-Base02',
    'Floor-Base03', 'Floor-Base04', 'Floor-Base05', 'Floor-Base06',
    'Floor-Base07', 'Floor-Base08', 'Floor-Base09', 'Floor-Base10',
    'Floor-Base11', 'Floor-Basecap01', 'Floor-Basecap02', 'Floor-Basecap03',
    'Floor-Basecap04', 'Floor-Basecap05', 'Floor-Basecap06', 'Floor-Lip01',
    'Floor-Lip02', 'Floor-Quarterround01', 'Floor-Shoe01', 'Floor-Shoe02',
    'Floor-Shoe03', 'Floor-Stair01', 'Floor-Stair02', 'Floor-Wallbase01',
    'Panel-Mullion01', 'Panel-Mullion02', 'Panel-Mullion03', 'Panel-Panel01',
    'Panel-Panel02', 'Panel-Panel03', 'Panel-Panel04', 'Panel-Panel05',
    'Panel-Panel06', 'Panel-Trimmid01', 'Panel-Trimmid02', 'Panel-Trimmid03',
    'Panel-Trimmid04', 'Panel-Trimmid05', 'Picture-Frame01', 'Picture-Frame02',
    'Picture-Frame03', 'Picture-Frame04', 'Picture-Frame05', 'Picture-Frame06',
    'Picture-Frame07', 'Picture-Frame08', 'Picture-Frame09', 'Picture-Frame10',
    'Picture-Frame11', 'Picture-Frame12', 'Picture-Frame13', 'Picture-Frame14',
    'Picture-Frame15', 'Picture-Frame16', 'Picture-Frame17', 'Picture-Frame18',
    'Picture-Frame19', 'Picture-Frame20', 'Rail-Round01', 'Rail-Top01',
    'Rail-Top02', 'Rail-Top03', 'Wall-Chairrail01', 'Wall-Chairrail02',
    'Wall-Chairrail03', 'Wall-Chairrail04', 'Wall-Chairrail05',
    'Wall-Chairrail06', 'Wall-Chairrail07', 'Wall-Chairrail08',
    'Wall-Chairrail09', 'Wall-Chairrail10', 'Window-Trimbottom01',
    'Window-Trimbottom02', 'Window-Trimbottom03', 'Window-Trimbottom04',
    'Window-Trimbottom05', 'Window-Trimbottom06', 'Window-Trimbottom07',
    'Window-Trimbottom08', 'Window-Trimbottom09', 'Window-Trimbottom10',
    'Window-Trimbottom11', 'Window-Trimbottom12', 'Window-Trimbottom13',
    'Window-Trimbottom14', 'Window-Trimbottom15', 'Window-Trimbottom16',
    'Window-Trimbottom17', 'Window-Trimbottom18', 'Window-Trimbottom19',
    'Window-Trimbottom20', 'Window-Trimbottom21', 'Window-Trimbottom22',
    'Window-Trimbottom23', 'Window-Trimbottom24', 'Window-Trimbottom25',
    'Window-Trimtop01', 'Window-Trimtop02', 'Window-Trimtop03',
    'Window-Trimtop04', 'Window-Trimtop05', 'Window-Trimtop06',
    'Window-Trimtop07', 'Window-Trimtop08', 'Window-Trimtop09',
    'Window-Trimtop10', 'Window-Trimtop11', 'Window-Trimtop12',
    'Window-Trimtop13', 'Window-Trimtop14', 'Window-Trimtop15',
    'Window-Trimtop16', 'Window-Trimtop17', 'Window-Trimtop18',
    'Window-Trimtop19', 'Window-Trimtop20', 'Window-Trimtop21',
    'Window-Trimtop22', 'Window-Trimtop23', 'Window-Trimtop24',
    'Window-Trimtop25'
]


# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------


class WM_OT_SelectAllCMP(Operator):
    """Select All CMP Paths"""
    bl_label = "Select CMP Paths"
    bl_idname = "wm.selallcmp"

    def execute(self, context):
        bpy.ops.object.select_by_type(type='CURVE')
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                try:
                    print(i.data.bevel_object.name)
                    # is cmp, do nothing really, don't delete the line above
                except AttributeError:
                    i.select_set(False)
        return {'FINISHED'}


class WM_OT_TiltCurvePositive(Operator):
    """Tilts Curve +90 Degrees"""
    bl_label = "Tilt +"
    bl_idname = "wm.tiltcurvepositive"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    if i.data.dimensions == '3D':
                        # select object
                        bpy.ops.object.select_all(action='DESELECT')
                        bcvo = bpy.context.view_layer.objects
                        bcvo.active.select_set(state=False)
                        bpy.data.objects[i.name].select_set(True)
                        bpy.context.view_layer.objects.active = i
                        # rotate it
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.curve.select_all(action='SELECT')
                        bpy.ops.transform.tilt(value=1.570796)
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                    else:
                        self.report(
                            {'ERROR'}, "Can't tilt " + i.name
                            + ". Convert curve to 3D.")
                    # reselect objects
                    for m in selectedobjects:
                        bpy.data.objects[m.name].select_set(True)
        return {'FINISHED'}


class WM_OT_TiltCurveNegative(Operator):
    """Tilts Curve -90 Degrees"""
    bl_label = "Tilt -"
    bl_idname = "wm.tiltcurvenegative"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    if i.data.dimensions == '3D':
                        # select object
                        bpy.ops.object.select_all(action='DESELECT')
                        bcvo = bpy.context.view_layer.objects
                        bcvo.active.select_set(state=False)
                        bpy.data.objects[i.name].select_set(True)
                        bpy.context.view_layer.objects.active = i
                        # rotate it
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.curve.select_all(action='SELECT')
                        bpy.ops.transform.tilt(value=-1.570796)
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                    else:
                        self.report(
                            {'ERROR'}, "Can't tilt " + i.name
                            + ". Convert curve to 3D.")
                    # reselect objects
                    for m in selectedobjects:
                        bpy.data.objects[m.name].select_set(True)
        return {'FINISHED'}


class WM_OT_TiltCurveFlip(Operator):
    """Tilts Curve 180 Degrees"""
    bl_label = "Tilt <>"
    bl_idname = "wm.tiltcurveflip"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    if i.data.dimensions == '3D':
                        # select object
                        bpy.ops.object.select_all(action='DESELECT')
                        bcvo = bpy.context.view_layer.objects
                        bcvo.active.select_set(state=False)
                        bpy.data.objects[i.name].select_set(True)
                        bpy.context.view_layer.objects.active = i
                        # rotate it
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.curve.select_all(action='SELECT')
                        bpy.ops.transform.tilt(value=3.141592)
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                    else:
                        self.report(
                            {'ERROR'}, "Can't tilt " + i.name
                            + ". Convert curve to 3D.")
                    # reselect objects
                    for m in selectedobjects:
                        bpy.data.objects[m.name].select_set(True)
        return {'FINISHED'}


class WM_OT_MirrorCurveX(Operator):
    """Mirror Object on X Axis"""
    bl_label = "Mirror X"
    bl_idname = "wm.mirrorcurvex"

    def execute(self, context):
        previouspivot = bpy.context.scene.tool_settings.transform_pivot_point
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
        bpy.ops.transform.mirror(
            orient_type='GLOBAL', orient_matrix=(
                (1, 0, 0), (0, 1, 0), (0, 0, 1)
            ), orient_matrix_type='GLOBAL',
            constraint_axis=(True, False, False))
        bpy.context.scene.tool_settings.transform_pivot_point = previouspivot
        return {'FINISHED'}


class WM_OT_MirrorCurveY(Operator):
    """Mirror Object on Y Axis"""
    bl_label = "Mirror Y"
    bl_idname = "wm.mirrorcurvey"

    def execute(self, context):
        previouspivot = bpy.context.scene.tool_settings.transform_pivot_point
        bcst = bpy.context.scene.tool_settings
        bcst.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
        bpy.ops.transform.mirror(
            orient_type='GLOBAL', orient_matrix=(
                (1, 0, 0), (0, 1, 0), (0, 0, 1)
            ), orient_matrix_type='GLOBAL',
            constraint_axis=(False, True, False))
        bpy.context.scene.tool_settings.transform_pivot_point = previouspivot

        return {'FINISHED'}


class WM_OT_MirrorCurveZ(Operator):
    """Mirror Object on Z Axis"""
    bl_label = "Mirror Z"
    bl_idname = "wm.mirrorcurvez"

    def execute(self, context):
        previouspivot = bpy.context.scene.tool_settings.transform_pivot_point
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
        bpy.ops.transform.mirror(
            orient_type='GLOBAL', orient_matrix=(
                (1, 0, 0), (0, 1, 0), (0, 0, 1)
            ), orient_matrix_type='GLOBAL',
            constraint_axis=(False, False, True))
        bpy.context.scene.tool_settings.transform_pivot_point = previouspivot
        return {'FINISHED'}


class WM_OT_ScaleCurvePositive(Operator):
    """Increase the Scale of the Curve Bevel"""
    bl_label = "Scale +"
    bl_idname = "wm.scalecurvepositive"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    # select object
                    bpy.ops.object.select_all(action='DESELECT')
                    bcvo = bpy.context.view_layer.objects
                    bcvo.active.select_set(state=False)
                    bpy.data.objects[i.name].select_set(True)
                    bpy.context.view_layer.objects.active = i
                    # scale it
                    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                    bpy.ops.curve.select_all(action='SELECT')
                    bpy.ops.transform.transform(
                        mode='CURVE_SHRINKFATTEN', value=(1.1, 0, 0, 0))
                    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                else:
                    self.report(
                        {'ERROR'}, "Can't scale " + i.name
                        + ". Not a curve.")
                # reselect objects
                for m in selectedobjects:
                    bpy.data.objects[m.name].select_set(True)
        return {'FINISHED'}


class WM_OT_ScaleCurveNegative(Operator):
    """Decrease the Scale of the Curve Bevel"""
    bl_label = "Scale -"
    bl_idname = "wm.scalecurvenegative"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    # select object
                    bpy.ops.object.select_all(action='DESELECT')
                    bcvo = bpy.context.view_layer.objects
                    bcvo.active.select_set(state=False)
                    bpy.data.objects[i.name].select_set(True)
                    bpy.context.view_layer.objects.active = i
                    # scale it
                    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                    bpy.ops.curve.select_all(action='SELECT')
                    bpy.ops.transform.transform(
                        mode='CURVE_SHRINKFATTEN', value=(0.9, 0, 0, 0))
                    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                else:
                    self.report(
                        {'ERROR'}, "Can't scale " + i.name
                        + ". Not a curve.")
                # reselect objects
                for m in selectedobjects:
                    bpy.data.objects[m.name].select_set(True)
        return {'FINISHED'}


class WM_OT_Curve3DToggle2D(Operator):
    """Toggle between 2D and 3D Curve Dimensions"""
    bl_label = "2D/3D"
    bl_idname = "wm.curve3dtoggle2d"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    if i.data.dimensions == '2D':
                        i.data.dimensions = '3D'
                    elif i.data.dimensions == '3D':
                        i.data.dimensions = '2D'
                else:
                    self.report(
                        {'ERROR'}, "Can't convert " + i.name
                        + ". Not a curve.")
        return {'FINISHED'}


class WM_OT_AllCurves3D(Operator):
    """Set all Curves to 3D Curve Dimension"""
    bl_label = "Curve 3D"
    bl_idname = "wm.curve3d"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    i.data.dimensions = '3D'
                else:
                    self.report(
                        {'ERROR'}, "Can't convert " + i.name
                        + ". Not a curve.")
        return {'FINISHED'}


class WM_OT_AllCurves2D(Operator):
    """Set all Curves to 2D Curve Dimension"""
    bl_label = "Curve 2D"
    bl_idname = "wm.curve2d"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    i.data.dimensions = '2D'
                else:
                    self.report(
                        {'ERROR'}, "Can't convert " + i.name
                        + ". Not a curve.")
        return {'FINISHED'}


class WM_OT_SwitchDirection(Operator):
    """Toggle Direction for Curves between 2D and 3D"""
    bl_label = "<> Direction"
    bl_idname = "wm.switchdirection"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    # select object
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.context.view_layer.objects.active.select_set(
                        state=False)
                    bpy.data.objects[i.name].select_set(True)
                    bpy.context.view_layer.objects.active = i
                    # switch curve direction
                    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                    bpy.ops.curve.switch_direction()
                    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                else:
                    self.report(
                        {'ERROR'}, "Can't edit " + i.name
                        + ". Not a curve.")
                # reselect objects
                for m in selectedobjects:
                    bpy.data.objects[m.name].select_set(True)
        return {'FINISHED'}


class WM_OT_ConvertToCMP(Operator):
    """Converts a selected face, edge loop,""" \
    """ or path into a crown molding path"""
    bl_label = "Convert to CMP Path"
    bl_idname = "wm.converttocmp"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        cmptool = scene.cmptool
        # gather current state
        previouspivot = bpy.context.scene.tool_settings.transform_pivot_point
        if bpy.context.active_object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            bpy.ops.object.transform_apply(
                location=False, rotation=False, scale=True)
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            bpy.ops.mesh.duplicate_move(
                MESH_OT_duplicate={"mode": 1},
                TRANSFORM_OT_translate={"value": (0, 0, 0)})
            bpy.ops.mesh.separate(type='SELECTED')
            bcvo = bpy.context.view_layer.objects.active
            bcvo.name = bpy.context.view_layer.objects.active.name + \
                "---ORIGINAL---"
            bpy.context.view_layer.objects.active.select_set(state=False)
            newActiveObjects = []
            for j in bpy.context.selected_objects:
                newActiveObjects.append(j.name)
            for k in newActiveObjects:
                nobj = bpy.data.objects.get(k)
                if nobj:
                    bpy.context.view_layer.objects.active = nobj
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.separate(type='LOOSE')
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.convert(target='CURVE')
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            bpy.ops.curve.select_all(action='SELECT')
            bpy.ops.curve.spline_type_set(type='BEZIER')
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            bpy.ops.object.transform_apply(
                location=False, rotation=True, scale=True)
            for b in bpy.context.visible_objects:
                if '---ORIGINAL---' in b.name:
                    b.name = re.sub('---ORIGINAL---', '', b.name)
            selectedobjects = bpy.context.selected_objects
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active.select_set(state=False)
            if selectedobjects:
                # loop through new objects
                for i in selectedobjects:
                    bpy.ops.object.select_all(action='DESELECT')
                    bcvo = bpy.context.view_layer.objects
                    bcvo.active.select_set(state=False)
                    bpy.data.objects[i.name].select_set(True)
                    # This was the last line of code for this v0.0.1 function
                    # a celebration commenced after figuring this out
                    bpy.context.view_layer.objects.active = i
                    bpy.ops.object.origin_set(
                        type='ORIGIN_GEOMETRY', center='MEDIAN')
                    # rotate to fix 2D path issues
                    if cmptool.advanced_rotate_curve:
                        curve = i.data
                        spline = curve.splines[0]
                        xGlobalPathPoints = []
                        yGlobalPathPoints = []
                        zGlobalPathPoints = []
                        for p in range(0, len(spline.bezier_points)):
                            if float(
                                "{:.3f}".format(float(i.location.x))
                            ) + 0 != 0:
                                xGlobalPathPoint = i.location.x * \
                                    spline.bezier_points[p].co.x
                            else:
                                xGlobalPathPoint = spline.bezier_points[p].co.x
                            xGlobalPathPoint = "{:.3f}".format(
                                float(xGlobalPathPoint))
                            xGlobalPathPoints.append(
                                float(xGlobalPathPoint) + 0)
                            if float(
                                "{:.3f}".format(float(i.location.y))
                            ) + 0 != 0:
                                yGlobalPathPoint = i.location.y * \
                                    spline.bezier_points[p].co.y
                            else:
                                yGlobalPathPoint = spline.bezier_points[p].co.y
                            yGlobalPathPoint = "{:.3f}".format(
                                float(yGlobalPathPoint))
                            yGlobalPathPoints.append(
                                float(yGlobalPathPoint) + 0)
                            if float(
                                "{:.3f}".format(float(i.location.z))
                            ) + 0 != 0:
                                zGlobalPathPoint = i.location.z * \
                                    spline.bezier_points[p].co.z
                            else:
                                zGlobalPathPoint = spline.bezier_points[p].co.z
                            zGlobalPathPoint = "{:.3f}".format(
                                float(zGlobalPathPoint))
                            zGlobalPathPoints.append(
                                float(zGlobalPathPoint) + 0)
                        if len(set(xGlobalPathPoints)) == 1:
                            # faces X
                            bcst = bpy.context.scene.tool_settings
                            bcst.transform_pivot_point = 'MEDIAN_POINT'
                            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                            bpy.ops.transform.rotate(
                                value=1.570796, orient_axis='Y',
                                orient_type='GLOBAL', orient_matrix=(
                                    (1, 0, 0), (0, 1, 0), (0, 0, 1)
                                ), orient_matrix_type='GLOBAL',
                                constraint_axis=(
                                    False, True, False), mirror=True)
                            bpy.ops.object.mode_set(
                                mode='OBJECT', toggle=False)
                            bpy.ops.transform.rotate(
                                value=-1.570796, orient_axis='Y',
                                orient_type='GLOBAL', orient_matrix=(
                                    (1, 0, 0), (0, 1, 0), (0, 0, 1)
                                ), orient_matrix_type='GLOBAL',
                                constraint_axis=(
                                    False, True, False), mirror=True)
                        if len(set(yGlobalPathPoints)) == 1:
                            # faces Y
                            bcst = bpy.context.scene.tool_settings
                            bcst.transform_pivot_point = 'MEDIAN_POINT'
                            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                            bpy.ops.transform.rotate(
                                value=1.570796, orient_axis='X',
                                orient_type='GLOBAL', orient_matrix=(
                                    (1, 0, 0), (0, 1, 0), (0, 0, 1)
                                ), orient_matrix_type='GLOBAL',
                                constraint_axis=(
                                    True, False, False), mirror=True)
                            bpy.ops.object.mode_set(
                                mode='OBJECT', toggle=False)
                            bpy.ops.transform.rotate(
                                value=-1.570796, orient_axis='X',
                                orient_type='GLOBAL', orient_matrix=(
                                    (1, 0, 0), (0, 1, 0), (0, 0, 1)
                                ), orient_matrix_type='GLOBAL',
                                constraint_axis=(
                                    True, False, False), mirror=True)
                        if len(set(zGlobalPathPoints)) == 1:
                            print("faces Z")
                            # Leave print or else you get error
                    # set bevel object
                    # new in 2.91, if current blender version is above
                    # 2.91.0, set bevel mode to object (previously default)
                    if (2, 91, 0) <= bpy.app.version:
                        i.data.bevel_mode = 'OBJECT'
                    # set bevel profile to crown molding
                    selection = bpy.data.window_managers["WinMan"]. \
                        cmpy_previews.replace(".png", "")
                    if bpy.data.objects.get(selection) is not None:
                        i.data.bevel_object = \
                            bpy.data.objects[selection]
                    else:
                        self.report(
                            {'ERROR'}, "Unable to auto add bevel object. "
                            + "Append the CrownMoldingPack .blend file to "
                            + "fix this in the future. Or, manually set "
                            + "in Path > Object Data > Geometry > Bevel "
                            + "> Object"
                        )
                    # make path look nice
                    i.data.use_fill_caps = True
                    bpy.ops.object.shade_smooth()
                    bpy.ops.object.modifier_add(type='EDGE_SPLIT')
                    if cmptool.advanced_rotate_curve:
                        i.data.dimensions = '2D'
                    else:
                        i.data.dimensions = '3D'
                    # rename object
                    needle = re.compile(r"\.\d{2,}")
                    if needle.search(bpy.context.object.name):
                        i.name = re.sub(r"(\.\d{2,})", r".CMP\1", i.name)
                    else:
                        i.name = i.name + ".CMP"
                    bpy.ops.object.select_all(action='DESELECT')
                # reselect new objects
                bcst = bpy.context.scene.tool_settings
                bcst.transform_pivot_point = previouspivot
                for m in selectedobjects:
                    bpy.data.objects[m.name].select_set(True)
        return {'FINISHED'}


class WM_OT_CycleBack(Operator):
    """Change the Curve Profile to the Previous Option"""
    bl_label = "< Previous"
    bl_idname = "wm.cycleback"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    if i.data.bevel_object.name in CMPlist:
                        # figure out the index of our current
                        currentindex = CMPlist.index(i.data.bevel_object.name)
                        previndex = currentindex - 1
                        if previndex < 0:
                            previndex = len(CMPlist) - 1
                        prevname = CMPlist[previndex]
                        # set bevel object to previous in list
                        i.data.bevel_object = bpy.data.objects[prevname]
                    else:
                        self.report(
                            {'ERROR'}, "Current Bevel Object not in " +
                            "defined list. Can't choose previous option." +
                            " Edit CMPlist in add-on python file.")
                else:
                    self.report(
                        {'ERROR'}, "Can't edit " + i.name +
                        ". Not a curve.")
                # reselect objects
                for m in selectedobjects:
                    bpy.data.objects[m.name].select_set(True)
        return {'FINISHED'}


class WM_OT_CycleForward(Operator):
    """Change the Curve Profile to the Next Option"""
    bl_label = "Next >"
    bl_idname = "wm.cycleforward"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    if i.data.bevel_object.name in CMPlist:
                        # figure out the index of our current
                        currentindex = CMPlist.index(i.data.bevel_object.name)
                        nextindex = currentindex + 1
                        if nextindex >= len(CMPlist):
                            nextindex = 0
                        nextname = CMPlist[nextindex]
                        # set bevel object to next in list
                        i.data.bevel_object = bpy.data.objects[nextname]
                    else:
                        self.report(
                            {'ERROR'}, "Current Bevel Object not in "
                            + "defined list. Can't choose next option. "
                            + "Edit CMPlist in add-on python file.")
                else:
                    self.report(
                        {'ERROR'}, "Can't edit " + i.name
                        + ". Not a curve.")
                # reselect objects
                for m in selectedobjects:
                    bpy.data.objects[m.name].select_set(True)
        return {'FINISHED'}


class WM_OT_ChangeSelected(Operator):
    """Change the curve profile to the picked option"""
    bl_label = "Change Path"
    bl_idname = "wm.changeselected"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    selection = bpy.data.window_managers["WinMan"]. \
                        cmpy_previews.replace(".png", "")
                    if bpy.data.objects.get(selection) is not None:
                        i.data.bevel_object = \
                            bpy.data.objects[selection]
                    else:
                        self.report(
                            {'ERROR'}, "Unable to auto add bevel object. "
                            + "You should let Jeff know if you see this."
                        )
                else:
                    self.report(
                        {'ERROR'}, "Can't edit " + i.name
                        + ". Not a curve.")
                # reselect objects
                for m in selectedobjects:
                    bpy.data.objects[m.name].select_set(True)
        return {'FINISHED'}


class WM_OT_SetOptions(Operator):
    # you can use this function to make a list of paths for the CMPlist
    """Append .blend"""
    bl_label = "Set Options"
    bl_idname = "wm.cycleset"

    def execute(self, context):
        selectedobjects = bpy.context.selected_objects
        cycleset = []
        if selectedobjects:
            for i in selectedobjects:
                if (i.type == 'CURVE'):
                    # build a list
                    cycleset.append(i.name)
                else:
                    self.report(
                        {'ERROR'}, "Cycleset Can't edit " + i.name
                        + ". Not a curve.")
                # reselect objects
                for m in selectedobjects:
                    bpy.data.objects[m.name].select_set(True)
            print(sorted(cycleset))
            # leave above print since that's the purpose of this class
        return {'FINISHED'}


class WM_OT_AppendCMP(Operator):
    # append .blend file, set collection to hidden / excluded so it doesn't
    # show up or render
    # https://blender.stackexchange.com/questions/264622/
    # https://blender.stackexchange.com/questions/34540/
    """Set Options to Pick From by Selecting All Desired Choices"""
    bl_label = "Append .blend File"
    bl_idname = "wm.appendcmp"

    def execute(self, context):
        cmpfilepath = os.path.join(os.path.dirname(__file__),
                                   "CrownMoldingPack-v3.1.blend")
        link = False
        # link all collections starting with 'MyCollection'
        with bpy.data.libraries. \
        load(cmpfilepath, link=link) as (data_from, data_to):
            data_to.collections = [c for c in data_from.collections]

        # link collection to scene collection
        for coll in data_to.collections:
            if coll is not None:
                bpy.context.scene.collection.children.link(coll)

        included_collection_list_names = [
            "CrownMoldingPack-v3.0", "CrownMoldingPack-v3.1",
            "CrownMoldingPack-v3.2"]
        layer_collections = list(
            bpy.context.view_layer.layer_collection.children)

        while layer_collections:
            layer_collection = layer_collections.pop(0)
            layer_collections.extend(layer_collection.children)
            layer_collection.exclude = layer_collection.name \
                in included_collection_list_names
        return {'FINISHED'}


# custom icons for dropdown
preview_collections = {}
CMPicons = bpy.utils.previews.new()
# the path is calculated relative to this py file inside the addon folder
# '..' goes up a level, seems to be needed when in dev?
cmpy_icons_dir = os.path.join(os.path.dirname(__file__), "cmp-icons")
ceil_dir = os.path.join(os.path.dirname(__file__),
                        "cmp-path-thumbnails/ceil")
flor_dir = os.path.join(os.path.dirname(__file__),
                        "cmp-path-thumbnails/flor")
corn_dir = os.path.join(os.path.dirname(__file__),
                        "cmp-path-thumbnails/corn")
panl_dir = os.path.join(os.path.dirname(__file__),
                        "cmp-path-thumbnails/panl")
picf_dir = os.path.join(os.path.dirname(__file__),
                        "cmp-path-thumbnails/picf")
rail_dir = os.path.join(os.path.dirname(__file__),
                        "cmp-path-thumbnails/rail")
wall_dir = os.path.join(os.path.dirname(__file__),
                        "cmp-path-thumbnails/wall")
wind_dir = os.path.join(os.path.dirname(__file__),
                        "cmp-path-thumbnails/wind")

# load a preview thumbnail of a file and store in the previews collection
CMPicons.load("icon_ceil",
              os.path.join(cmpy_icons_dir, "ceiling.png"), 'IMAGE')
CMPicons.load("icon_wind",
              os.path.join(cmpy_icons_dir, "window.png"), 'IMAGE')
CMPicons.load("icon_panl",
              os.path.join(cmpy_icons_dir, "panel.png"), 'IMAGE')
CMPicons.load("icon_wall",
              os.path.join(cmpy_icons_dir, "wall.png"), 'IMAGE')
CMPicons.load("icon_flor",
              os.path.join(cmpy_icons_dir, "floor.png"), 'IMAGE')
CMPicons.load("icon_rail",
              os.path.join(cmpy_icons_dir, "rail.png"), 'IMAGE')
CMPicons.load("icon_corn",
              os.path.join(cmpy_icons_dir, "corner.png"), 'IMAGE')
CMPicons.load("icon_picf",
              os.path.join(cmpy_icons_dir, "pictureframe.png"), 'IMAGE')
preview_collections["main"] = CMPicons
# create aliases for icon names
customicons = preview_collections["main"]
ic1 = customicons["icon_ceil"]
ic2 = customicons["icon_wind"]
ic3 = customicons["icon_panl"]
ic4 = customicons["icon_wall"]
ic5 = customicons["icon_flor"]
ic6 = customicons["icon_rail"]
ic7 = customicons["icon_corn"]
ic8 = customicons["icon_picf"]
# end custom icons for dropdown


class CrownMoldingProperties(PropertyGroup):

    advanced_rotate_curve: BoolProperty(
        name="Auto-rotate Curve",
        description="Disable to prevent add-on from rotating"
        + " the curve automatically. Helpful for arbitrarily"
        + " rotated faces. Manual Rotation with CTRL + T required"
        + " if disabled",
        default=True
    )

    curvecategory: EnumProperty(
        name="Curve Category:",
        description="Type of profiles to display",
        items=[('ceiling', "Ceiling",
                "Crown Molding and others aligned to top",
                ic1.icon_id, 1),
               ('window', "Window",
                "Window Trim in both top and bottom alignment",
                ic2.icon_id, 2),
               ('panel', "Panel",
                "panel edges for accents aligned to middle",
                ic3.icon_id, 3),
               ('wall', "Wall",
                "Chair rail for walls aligned to middle",
                ic4.icon_id, 4),
               ('floor', "Floor",
                "Base trim, stair lips mostly aligned to bottom",
                ic5.icon_id, 5),
               ('rail', "Rail",
                "Hand rails aligned to middle",
                ic6.icon_id, 6),
               ('corner', "Corner",
                "Corner gaurds and caps aligned to inset edge",
                ic7.icon_id, 7),
               ('pictureframe', "Picture Frame",
                "Frames for photos or art aligned to wall",
                ic8.icon_id, 8)
              ],
        default='ceiling'
    )


# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------


def enum_previews_from_directory_items(self, context):
    """EnumProperty callback"""
    enum_items = []

    if context is None:
        return enum_items

    scene = context.scene
    cmptool = scene.cmptool
    if cmptool.curvecategory == 'ceiling':
        directory = ceil_dir
    elif cmptool.curvecategory == 'window':
        directory = wind_dir
    elif cmptool.curvecategory == 'panel':
        directory = panl_dir
    elif cmptool.curvecategory == 'wall':
        directory = wall_dir
    elif cmptool.curvecategory == 'floor':
        directory = flor_dir
    elif cmptool.curvecategory == 'corner':
        directory = corn_dir
    elif cmptool.curvecategory == 'pictureframe':
        directory = picf_dir
    elif cmptool.curvecategory == 'rail':
        directory = rail_dir

    # Get the preview collection (defined in register func).
    pcoll = preview_collections["main"]

    if directory == pcoll.cmpy_previews_dir:
        return pcoll.cmpy_previews

    if directory and os.path.exists(directory):
        # Scan the directory for png files
        image_paths = []
        for fn in os.listdir(directory):
            if fn.lower().endswith(".png"):
                image_paths.append(fn)

        for i, name in enumerate(image_paths):
            # generates a thumbnail preview for a file.
            filepath = os.path.join(directory, name)
            icon = pcoll.get(name)
            if not icon:
                thumb = pcoll.load(name, filepath, 'IMAGE')
            else:
                thumb = pcoll[name]
            enum_items.append((name, name,
                               "Path Selection", thumb.icon_id, i))

    sorted_data = sorted(enum_items, key=lambda x: x[0])
    pcoll.cmpy_previews = sorted_data
    pcoll.cmpy_previews_dir = directory
    return pcoll.cmpy_previews


class OBJECT_PT_CrownMoldingTools(Panel):
    bl_label = "Crown Molding Tools v3.1"
    bl_idname = "OBJECT_PT_crown_molding_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"  # label in tab if different than defaults

    @classmethod
    def poll(self, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        cmptool = scene.cmptool
        wm = context.window_manager

        if bpy.data.objects.get('Ceiling-Crown01') is not None:
            # ====== BEGIN IMAGE SECTION ======
            row = layout.row()
            row.prop(cmptool, "curvecategory", text="Category")

            row = layout.row()
            row.template_icon_view(wm, "cmpy_previews")

            row = layout.row()
            row.prop(wm, "cmpy_previews", text="Path Selection")
            # ======  END IMAGE SECTION ======
            row = layout.row()
            row.operator("wm.converttocmp")

            row = layout.row()
            row.operator("wm.changeselected")
            row.operator("wm.selallcmp")

            row = layout.row()
            row.operator("wm.cycleback")
            # developer / custom use only
            # row.operator("wm.cycleset")
            row.operator("wm.cycleforward")

            row = layout.row()
            row.operator("wm.tiltcurvenegative")
            row.operator("wm.tiltcurveflip")
            row.operator("wm.tiltcurvepositive")

            row = layout.row()
            row.operator("wm.mirrorcurvex")
            row.operator("wm.mirrorcurvey")
            row.operator("wm.mirrorcurvez")

            row = layout.row()
            row.operator("wm.scalecurvenegative")
            row.operator("wm.switchdirection")
            row.operator("wm.scalecurvepositive")

            row = layout.row()
            row.operator("wm.curve2d")
            row.operator("wm.curve3dtoggle2d")
            row.operator("wm.curve3d")

            row = layout.row()
            row.prop(cmptool, "advanced_rotate_curve")
        else:
            row = layout.row()
            row.label(icon="ERROR", text="Paths Not Appended")
            row = layout.row()
            row.operator("wm.appendcmp")

        box = layout.box()
        box.label(text="Support")
        column = box.column()

        row = column.row()
        row.scale_y = 1.2
        row.operator("wm.url_open", text="Documentation",
                     icon='WORLD').url = "https://jefftml.com/cmp3doc"


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    CrownMoldingProperties,
    OBJECT_PT_CrownMoldingTools,
    WM_OT_AllCurves2D,
    WM_OT_AllCurves3D,
    WM_OT_AppendCMP,
    WM_OT_ChangeSelected,
    WM_OT_ConvertToCMP,
    WM_OT_Curve3DToggle2D,
    WM_OT_CycleBack,
    WM_OT_CycleForward,
    WM_OT_MirrorCurveX,
    WM_OT_MirrorCurveY,
    WM_OT_MirrorCurveZ,
    WM_OT_ScaleCurveNegative,
    WM_OT_ScaleCurvePositive,
    WM_OT_SelectAllCMP,
    WM_OT_SetOptions,
    WM_OT_SwitchDirection,
    WM_OT_TiltCurveFlip,
    WM_OT_TiltCurveNegative,
    WM_OT_TiltCurvePositive
)


def register():
    from bpy.utils import register_class
    from bpy.types import WindowManager
    from bpy.props import (StringProperty, EnumProperty)

    # ====== BEGIN IMAGE SECTION ======
    WindowManager.cmpy_previews_dir = StringProperty(
        name="Folder Path",
        subtype='DIR_PATH',
        default=""
    )
    WindowManager.ceil_dir = StringProperty(
        name="Ceiling Folder Path",
        subtype='DIR_PATH',
        default=""
    )
    WindowManager.flor_dir = StringProperty(
        name="Floor Folder Path",
        subtype='DIR_PATH',
        default=""
    )
    WindowManager.corn_dir = StringProperty(
        name="Corner Folder Path",
        subtype='DIR_PATH',
        default=""
    )
    WindowManager.panl_dir = StringProperty(
        name="Panel Folder Path",
        subtype='DIR_PATH',
        default=""
    )
    WindowManager.picf_dir = StringProperty(
        name="Picture Frame Folder Path",
        subtype='DIR_PATH',
        default=""
    )
    WindowManager.rail_dir = StringProperty(
        name="Rail  Folder Path",
        subtype='DIR_PATH',
        default=""
    )
    WindowManager.wall_dir = StringProperty(
        name="Wall Folder Path",
        subtype='DIR_PATH',
        default=""
    )
    WindowManager.wind_dir = StringProperty(
        name="Window Folder Path",
        subtype='DIR_PATH',
        default=""
    )

    WindowManager.cmpy_previews = EnumProperty(
        items=enum_previews_from_directory_items
    )
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()
    pcoll.cmpy_previews_dir = ""
    pcoll.cmpy_previews = ()

    preview_collections["main"] = pcoll
    # ======  END  IMAGE SECTION ======

    # registers list from above
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.cmptool = PointerProperty(type=CrownMoldingProperties)


def unregister():
    from bpy.utils import unregister_class
    from bpy.types import WindowManager

    # ====== BEGIN IMAGE SECTION ======
    del WindowManager.cmpy_previews
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
    # ====== END IMAGE SECTION ======

    # unregisters list from above
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.cmptool


if __name__ == "__main__":
    # The path of this text (if saved)
    __file__ = bpy.context.space_data.text.filepath
    register()
