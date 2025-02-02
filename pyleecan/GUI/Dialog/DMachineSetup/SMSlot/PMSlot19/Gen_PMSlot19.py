# -*- coding: utf-8 -*-
"""File generated according to PMSlot19/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot19.Ui_PMSlot19 import Ui_PMSlot19


class Gen_PMSlot19(Ui_PMSlot19):
    def setupUi(self, PMSlot19):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PMSlot19.setupUi(self, PMSlot19)
        # Setup of in_W0
        txt = self.tr(u"""Slot/magnet width. (top)""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr(u"""Slot/magnet width. (top)""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_W1
        txt = self.tr(u"""Slot/magnet width. (bottom)""")
        self.in_W1.setWhatsThis(txt)
        self.in_W1.setToolTip(txt)

        # Setup of lf_W1
        self.lf_W1.validator().setBottom(0)
        txt = self.tr(u"""Slot/magnet width. (bottom)""")
        self.lf_W1.setWhatsThis(txt)
        self.lf_W1.setToolTip(txt)

        # Setup of in_Hmag
        txt = self.tr(u"""Magnet Height""")
        self.in_Hmag.setWhatsThis(txt)
        self.in_Hmag.setToolTip(txt)

        # Setup of lf_Hmag
        self.lf_Hmag.validator().setBottom(0)
        txt = self.tr(u"""Magnet Height""")
        self.lf_Hmag.setWhatsThis(txt)
        self.lf_Hmag.setToolTip(txt)
