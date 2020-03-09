# GeometricDimensioningAndTolerancing gui init module
#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2016 Juan Vañó Cerdá <juavacer@inf.upv.es>              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

import FreeCADGui as gui
from FreeCAD import Console
from . import gdt
from .gdt import ICON_DIR, DIR

Log = Console.PrintLog
Msg = Console.PrintMessage

class GeometricDimensioningAndTolerancingWorkbench (gui.Workbench):
    Icon = str(ICON_DIR / 'GDT.svg')
    MenuText = 'GD&T'
    ToolTip = 'Geometric Dimensioning & Tolerancing'

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        # load the module
        # import GD&T tools
        try:
            from . import datum_feature
            from . import datum_system
            from . import geometric_tolerance
            from . import annotation_plane
            from . import inventory
        except ImportError:
            FreeCAD.Console.PrintWarning("Error: Initializing one or more of the GD&T modules failed, GD&T will not work as expected.\n")

        self.cmdList = ['dd_datumFeature','dd_datumSystem','dd_geometricTolerance','dd_annotationPlane']
        self.inventory = ['dd_inventory']
        self.appendToolbar("GD&T Tools",self.cmdList+self.inventory)
        self.appendMenu("GD&T Tools",self.cmdList+self.inventory)

        gui.addIconPath(str(ICON_DIR))
        gui.addPreferencePage(str(DIR / 'Resources' / 'ui' / 'preferences-gdt.ui') ,'GDT')

        Log ("Loading Geometric Dimensioning & Tolerancing... done\n")

    def Activated(self):
                # do something here if needed...
        Msg ("Geometric Dimensioning & Tolerancing workbench activated\n")

    def Deactivated(self):
                # do something here if needed...
        Msg ("Geometric Dimensioning & Tolerancing workbench desactivated\n")

    def ContextMenu(self, recipient):
        # "This is executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        showCmdList = True
        if gui.Selection.getSelection():
            for i in range(len(gui.Selection.getSelectionEx()[0].SubObjects)):
                if gui.Selection.getSelectionEx()[0].SubObjects[i].ShapeType == 'Face':
                    pass
                else:
                    showCmdList = False
        else:
            showCmdList = False
        if showCmdList:
            self.appendContextMenu("",self.cmdList) # add commands to the context menu
        self.appendContextMenu("",self.inventory)

gui.addWorkbench(GeometricDimensioningAndTolerancingWorkbench)