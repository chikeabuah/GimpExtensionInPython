#!/usr/bin/env python

import math
from gimpfu import *

def python_frame(timg, tdrawable, offset=25, feather=50):

    width = timg.width
    height = timg.height
    pdb.gimp_rect_select (timg, 
                    offset,offset, 
                    width - 2*offset, height - 2*offset,
                    0, True, feather)
    pdb.gimp_selection_invert (timg)
    pdb.gimp_edit_fill (tdrawable, 0)
    pdb.gimp_selection_none (timg)


register(
        "python_fu_frame",
        "Frame the image",
        "Frame the image",
        "Chike Abuah",
        "Chike Abuah",
        "2011",
        "<Image>/Filters/Artistic/_FramePy...",
        "RGB*, GRAY*",
        [        
                (PF_INT, "offset", "Offset", 25),
                (PF_INT, "feather", "Feather", 50)
        ],
	[],
        python_frame)

main()
