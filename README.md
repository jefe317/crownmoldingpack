Custom Crown Molding in 3 seconds!
==================================

Blender Add-on with 17 custom helper functions, and 138 curves for quick, beautiful, easy to update crown molding and trim.

![](https://d1231c29xbpffx.cloudfront.net/cache/562bb421f58086bb1e8474587ff0c3a7.gif)

### Super Fast Crown Molding

Adding Crown Molding into your scene takes 3 seconds with the Crown Molding Tools. The Crown Molding Pack offers 138 options, so you'll find a crown molding or trim that fits your scene perfectly.

### Helper Tools to Put You In Control

Curves are powerful, and with the Crown Molding Tools Add-on, you'll be in full control of your scene.

![](https://d1231c29xbpffx.cloudfront.net/cache/b26cd0fa07c2d729f70d52e7077e7afe.jpg)

### Features

*   138 Easy to change Paths
    *   34 Crown Molding Paths
    *   26 Wall Base Paths
    *   25 Window Paths - great for picture frames, door frames, and tons more
    *   14 Panel Trim Paths - great for walls
    *   10 Wall Trim Paths - great for walls
    *   4 Rail Paths - perfect handrails every time
    *   20 Picture Frame Paths
    *   5 Miscellaneous Trim Paths - corner guards and ply caps
*   17 Powerful Tools
    *   Make crown molding in 3 seconds, with easy adjustments to perfect your scene
*   Video and Text Documentation
    *   Get up and running in 2 minutes
    *   Learn how each of the tools works

### Changelog

3.1.1 - Bugfix. Removed extra console logs, and fixed an error that happened when uninstalling the add-on.

3.1 - Bugfix. Updated variable names to avoid collisions with other addons. Thanks for the report, Trey!

3.0 - UI Update to show profile images, categories, append .blend file, select all paths, and set path actions, which are all user-requested features that should make things much easier for you!

2.4 - Bugfix. Undo after crown molding creation might crash blender. Added a undo step to the WM\_OT\_ConvertToCMP function to fix this. Thanks for the report, Piero!

2.3 - Bugfix. Faces with arbitrary rotation didn't convert to paths properly. Added Auto-rotate Curve checkbox to control if add-on tries to rotate the curve (legacy behavior, checkbox checked) or not (checkbox not checked). Thanks for the report, Piero!

2.2 - Add-on updated to add new "Next" and "Previous" buttons to cycle through provided curves. Can also be modified in python code. Added 19 new ceiling crown molding paths, and 20 picture frame paths. (138 unique paths, 163 total paths)

2.1 - Add-on updated for Blender 2.91 and 53 more paths (99 unique paths, 124 total paths). Renamed path objects for better organization.

2.0 - New Add-on and 29 more paths (46 unique paths, 71 total paths).

1.1 - Documentation Update.

*   Added Making Corners Text and Video Tutorial.
*   Added Complete Scene Video Tutorial.

1.0 - Initial Launch.

Getting Started
---------------

[Watch on YouTube](https://www.youtube.com/watch?v=Df_tjdnC_4E)

1.  Download the files onto your computer.
2.  Install and enable the Crown Molding Pack by installing the .zip file. You shouldn’t un-zip this file.
3.  Open the scene where you want to use the Crown Molding Pack.
4.  Press N in the 3D view to show the tool panel if it's hidden, click **Tool**, and expand the Crown Molding Tools panel if it's hidden.
5.  Click the **Append .blend File** button to automatically import the CrownMoldingPack collection. It will automatically be disabled in your scene so it doesn't affect your project.
6.  Pick which category of paths you’d like to view in the **Category** drop-down.
7.  In the large box below the Category section, click to select which path you’d like to choose. If you prefer a list of names, you can do so in the **Path Selection** drop-down.
8.  In edit mode, select the face of the object where you'd like to put crown molding, like the ceiling.
9.  Click the **Convert to CMP Path** button. That’s it!

Full Walkthrough
----------------

[Watch on YouTube](https://www.youtube.com/watch?v=k7-kuUkWLUQ)

Here's everything you need to know about the Crown Molding Pack and the Crown Molding Tools add-on.

*   Crown Molding Pack

*   **34 Crown Molding Paths** - Typically used where a wall meets the ceiling. You can also use these as a railing, under the edge of a table, as the edge to a picture frame, as the edge to a window or doorway, as the edge of a window pane, as an inset on a wall, door, cabinet, or ceiling, or stacked to create a double-sided railing. These objects are named **Ceiling-CrownXX**.
*   **25 Window Paths** - Can be used on a flat edge, like a door frame, window frame, or picture frame. There are 2 versions of each path, **Window-TrimbottomXX** and **Window-TrimtopXX**. This makes adjusting where the trim appears very simple, just change the name to get the other option.
*   **14 Panel Trim Paths** - Typically used on a wall, about 3 feet above the ground. Also used for insets and edges for tables. These objects are named **Panel-SomethingXX**.
*   **10 Wall Trim Paths** - Typically used on a wall, about 3 feet above the ground. Also used for insets and edges for tables. These objects are named **Wall-SomethingXX**.
*   **26 Floor Base Paths** - Typically used where a wall meets the floor. These objects are named **Floor-SomethingXX**.
*   **4 Rail Paths** - Used for a handrail. These objects are named **Rail-SomethingXX**.
*   **5 Corner Trim Paths** - 2 corner guards and 3 ply caps (for the top edge of wainscoting). These objects are named **Corner-SomethingXX.**
*   **20 Picture Frame Paths** - Used to create picture frames. These objects are named **Picture-FrameXX.**
*   **1 Trim Mesh Object** - Great for corners of middle trim paths. This object is named **za-Misc-Trimcap01**.
*   **Stats** \- 138 Unique Paths, 39 new paths since v2.1, 163 total paths.

*   Crown Molding Tools
    *   **Convert to CMP Path** - Works with single or multiple faces and edges. Converts mesh faces or edges to separate curves with the proper rotation, and sets the bevel object to the selected path.
    *   **Change Path** - Changes the bevel object of the selected paths to the current profile selection.
    *   **Select CMP Paths** - Selects all paths with bevel objects.
    *   **< Previous** - Changes the selected path to the previous option.
    *   **Next >** - Changes the selected path to the next option.
    *   **Tilt -** - Works with single or multiple 3D curves. Rotates selected 3D curves tilt by -90 degrees.
    *   **Tilt +** - Works with single or multiple 3D curves. Rotates selected 3D curves tilt by 90 degrees.
    *   **Tilt <>** - Works with single or multiple 3D curves. Rotates selected 3D curves tilt by 180 degrees.
    *   **Mirror X** - Works with all objects. Mirrors objects on the Global X Axis.
    *   **Mirror Y** - Works with all objects. Mirrors objects on the Global Y Axis.
    *   **Mirror Z** - Works with all objects. Mirrors objects on the Global Z Axis.
    *   **Scale -** - Works with single or multiple curves. Decreases the scale of curves without changing the path.
    *   **Scale +** - Works with single or multiple curves. Increases the scale of curves without changing the path.
    *   **<> Direction** - Works with single or multiple curves. Switches the direction of the curve, which will change what side the bevel object appears.
    *   **Curve 2D** - Works with single or multiple curves. Converts selected curves to 2D dimension.
    *   **Curve 3D** - Works with single or multiple curves. Converts selected curves to 3D dimension.
    *   **2D/3D** - Works with single or multiple curves. Converts selected curves to 2D dimension if they are 3D, and vice versa.
    *   **Auto-rotate Curve** - When enabled, the add-on attempts to rotate the curve so that 2D curves work better. Disable for paths that aren't on a flat X, Y, or Z plane.
    *   **Documentation** - Open the link to this documentation.

Adding Custom Profiles
----------------------

Watch on YouTube - [https://www.youtube.com/watch?v=Jk48TCMP--0](https://www.youtube.com/watch?v=Jk48TCMP--0)
