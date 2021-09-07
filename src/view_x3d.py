import os
import sys
from os.path import exists
from OCC.Extend.DataExchange import read_step_file_with_names_colors
from OCC.Display.WebGl import x3dom_renderer

# create the x3dom renderer
out_dir='render'
os.makedirs("/tmp/path/to/desired/directory", exist_ok=True)
my_renderer = x3dom_renderer.X3DomRenderer(path=out_dir)


def addStep(filename, renderer):
    if not exists(filename):
        raise Exception('Bad file path')

    shapes_labels_colors = read_step_file_with_names_colors(filename)

    # traverse shapes, render in "face" mode
    for shp, (_, c) in shapes_labels_colors.items():
        renderer.DisplayShape(shp, color=(c.Red(), c.Green(), c.Blue()), export_edges=False)

# temp hack to read two cli inputs for the left/right
for f in range(2):
    addStep(sys.argv[f+1], my_renderer)

my_renderer.render(addr='0.0.0.0', server_port=8000)
