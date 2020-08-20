# Align Nodes
![](./align_pie_img.png?raw=true "Align Pie menu")

This tool allows to align the nodes in any nodes editor *e.g., Shader Nodes Editor, Compositing Nodes Editor, Animation Nodes Editor, Sverchok Nodes Editor*.

**Installation:**
- Download the zip file [Align Nodes](https://github.com/3DSinghVFX/align_nodes/archive/master.zip) add-on.
- Open the Blender, go to `Edit -> Preferences -> Add-ons`.
- Press the `Install` button, locate the zip file of *Align Nodes* add-on, install it.

**How to Use:**
- Press the shortcut key `Shift + S` in any node-editor, an *Align Pie* menu will pop up.
- The *Align Pie* menu has eight nodes alignment operations:
  - *Dependent (Right)* - Aligns all dependent nodes w.r.t active node to its right side.
  - *Dependencies (Left)* - Aligns all dependencies nodes w.r.t active node to its left side.
  - *Selection (Top)* - Stacks up all selected nodes w.r.t active node.
  - *Selection (Down)* - Stacks down all selected nodes w.r.t active node.
  - *Selection (Top Right)* - Aligns only the header of all selected nodes w.r.t active node.
  - *Selection (Top Left)* - Aligns only the header of all selected nodes w.r.t active node.
  - *Selection (Bottom Right)* - Aligns only the side of all selected nodes w.r.t active node to its right side.
  - *Selection (Bottom Left)* - Aligns only the side of all selected nodes w.r.t active node to its left side.
- You can change the default *Horizontal Offset* (side distance between nodes) and *Vertical Offset* (height distance between nodes) from the preferences of the add-on.
