from tkinter import *
from tkinter import ttk

# work around to allow use of spinbox in GUI to choose group size
class Spinbox(ttk.Entry):

	def __init__(self, master=None, **kw):
		ttk.Entry.__init__(self, master, "ttk::spinbox", **kw)

	def current(self, newindex=None):
		return self.tk.call(self._w, 'current', index)

	def set(self, value):
		return self.tk.call(self._w, 'set', value)
