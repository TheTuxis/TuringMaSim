# -*- coding:utf-8 -*-
from digraph import draw
from automaton import Automaton
from gui import GUI

aut = Automaton()
palabra = []
gui = GUI(aut, palabra)
gui.show()
