# -*- coding: utf-8 -*- 
__title__ = 'Open Views'
__doc__ = """To save time for rendering each view, this button opens all selected views in one click
Context: Some views should be selected

Чтобы сэкономить время, которое тратится на рендеринг при открытии вида, эта кнопка открывает несколько выделенных видов одним нажатием.
Контекст: Должны быть выбраны несколько видов в браузере проекта или на листе"""
__context__ = 'Selection'

from revitutils import doc, uidoc, selection
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, View
from Autodesk.Revit.UI import TaskDialog

__helpurl__ = "https://github.com/apex-project/pyApex/wiki/Buttons#open-views"


sel = selection.elements
sel_count = len(sel)

errors = 0
for v in sel:
	try:
		uidoc.ActiveView = v
	except:
		errors += 1

# Show message if error occured or nothing selected
if sel_count == 0:
	TaskDialog.Show(__title__, "Select views to open")
elif errors == sel_count:
	TaskDialog.Show(__title__, "Unable to open selected views")
elif errors != 0:
	TaskDialog.Show(__title__, "%d of %d selected views were opened" % (sel_count - errors, sel_count))