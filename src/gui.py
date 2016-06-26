# -*- coding:utf-8 -*-
import ttk
from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
from digraph import draw

class GUI:

    def __init__(self, automaton, word):
        self.automaton = automaton
        self.header_position = 1
        self.word = word
        self.win = Tk()
        self.win.title("Turign Magic")
        self.win.resizable(0, 0)
        self.contador = 0
        self.pf = Frame(
            self.win, width=850, height=600
        )
        self.df = Frame(
            self.pf, relief=GROOVE, borderwidth=1
        )
        self.df.place(
            relx=0.01, rely=0.02, width=500, height=460
        )
        Label(self.pf, text='Digrafo').place(relx=0.02, rely=0.02, anchor=W)

        self.asf = Frame(
            self.pf, relief=GROOVE, borderwidth=1
        )
        self.asf.place(
            relx=0.62, rely=0.02, width=300, height=580
        )
        Label(self.pf, text='Configuracion Automata').place(
            relx=0.64, rely=0.02, anchor=W
        )
        self.imgPath = 'temp/blank.gif'
        self.image = Image.open(self.imgPath)
        self.photo = ImageTk.PhotoImage(self.image)
        self.digraph_image = Label(self.pf, image=self.photo, bd=1)
        self.digraph_image.image = self.photo

        # == Componentes ==
        # ----- STATE
        self.new_state_string = StringVar()
        self.new_state = ttk.Entry(
            self.asf, width=17, textvariable=self.new_state_string, justify='center'
        )
        self.btn_new_state = Button(
            self.asf, text="New State", command=self.add_new_state
        )
        self.list_state = Listbox(self.asf, height=4, width=30)
        self.list_state.bind('<<ListboxSelect>>', self.select_init_state)
        # ----- alphabet
        self.new_character_string = StringVar()
        self.new_character = ttk.Entry(
            self.asf, width=14, textvariable=self.new_character_string, justify='center'
        )
        self.btn_new_character = Button(
            self.asf, text="New Character", command=self.add_new_character
        )
        self.list_character = Listbox(self.asf, height=4, width=30)
        # ----- transition
        self.new_tran_orig = StringVar()
        self.new_tran_read = StringVar()
        self.new_tran_dest = StringVar()
        self.new_orig = ttk.Entry(
            self.asf, width=3, textvariable=self.new_tran_orig, justify='center'
        )
        self.new_read = ttk.Entry(
            self.asf, width=3, textvariable=self.new_tran_read, justify='center'
        )
        self.new_dest = ttk.Entry(
            self.asf, width=3, textvariable=self.new_tran_dest, justify='center'
        )
        self.btn_new_transition = Button(
            self.asf, text="New Transition", command=self.add_new_transition
        )
        self.list_transition = Listbox(self.asf, height=4, width=30)
        # ----- final
        self.new_final_state_string = StringVar()
        self.new_final_state = ttk.Entry(
            self.asf, width=14, textvariable=self.new_final_state_string, justify='center'
        )
        self.btn_final_state = Button(
            self.asf, text="New Final", command=self.add_final_state
        )
        self.list_final_state = Listbox(self.asf, height=4, width=30)
        # -----
        self.btn_play = Button(
            self.asf, text="Play", command=self.play_read_string
        )
        self.btn_next = Button(
            self.asf, text=">", command=self.next_read_string
        )

        self.alpha_string = StringVar()
        self.alpha = ttk.Entry(
            self.pf, width=17, textvariable=self.alpha_string, justify='center'
        )
        self.alpha.bind('<KeyRelease>', self.test_input)

        self.list_run = Listbox(self.pf, height=6, width=35)
        self.alpha.place(relx=0.01, rely=0.80)
        self.list_run.place(relx=0.22, rely=0.80)

        # == Posiciones ==
        self.digraph_image.place(relx=0.05, rely=0.05)
        self.new_state.place(relx=0.03, rely=0.03)
        self.btn_new_state.place(relx=0.64, rely=0.03)
        self.list_state.place(relx=0.03, rely=0.10)
        self.new_character.place(relx=0.03, rely=0.25)
        self.btn_new_character.place(relx=0.55, rely=0.25)
        self.list_character.place(relx=0.03, rely=0.31)

        self.new_final_state.place(relx=0.03, rely=0.46)
        self.btn_final_state.place(relx=0.55, rely=0.46)
        self.list_final_state.place(relx=0.03, rely=0.52)

        self.new_orig.place(relx=0.03, rely=0.70)
        self.new_read.place(relx=0.22, rely=0.70)
        self.new_dest.place(relx=0.41, rely=0.70)
        self.btn_new_transition.place(relx=0.55, rely=0.70)
        self.list_transition.place(relx=0.03, rely=0.76)

        self.btn_play.place(relx=0.6, rely=0.90)
        self.btn_next.place(relx=0.8, rely=0.90)
        self.pf.pack()

    def test_input(self, evt):
        alphabet = self.alpha_string.get()
        result = True
        word_temp = []
        for x in alphabet:
            if x not in self.automaton.alfabet:
                result = False
            else:
                word_temp.append(x)
        if result:
            self.word = word_temp
        else:
            string_temp = ""
            for y in self.word:
                string_temp += y
            self.alpha_string.set(string_temp)


    def _msgBox(self):
       tkMessageBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2015.')

    def add_new_state(self):
        if self.automaton.add_state(self.new_state_string.get()):
            self.list_state.insert('end', self.new_state_string.get())

    def select_init_state(self, evt):
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        if self.automaton.set_init(value):
            print 'ok'

    def add_new_character(self):
        if self.automaton.add_character_alfabet(self.new_character_string.get()):
            self.list_character.insert('end', self.new_character_string.get())

    def add_new_transition(self):
        result = self.automaton.add_transition(
            self.new_tran_orig.get(), self.new_tran_read.get(), self.new_tran_dest.get()
        )
        if result:
            self.list_transition.insert(
                'end',
                'State: %s, Lee: %s -> Cambia: %s ' % (
                    self.new_tran_orig.get(), self.new_tran_read.get(), self.new_tran_dest.get()
                )
            )
            self.view_preview()

    def add_final_state(self):
        if self.automaton.add_final_state(self.new_final_state_string.get()):
            self.list_final_state.insert('end', self.new_final_state_string.get())


    def set_image_in_lbl_digraph(self, image):
        self.imgPath = image
        self.image = Image.open(self.imgPath)
        self.photo = ImageTk.PhotoImage(self.image)
        self.digraph_image = Label(self.pf, image=self.photo, bd=1)
        self.digraph_image.place(relx=0.05, rely=0.05)
        self.digraph_image.image = self.photo

    def view_preview(self):
        draw(
            self.automaton.alfabet,
            self.automaton.state,
            self.automaton.init,
            self.automaton.get_transition_table(),
            self.automaton.final,
            0
        )
        self.set_image_in_lbl_digraph("temp//blank.gif")
        self.set_image_in_lbl_digraph("temp//Digraph_0.gif")

    def play_read_string(self):
        self.header_position = 1
        self.select_init_state(self.automaton.init)
        for x in self.word:
            new_state_string = ''
            for y in self.word[:self.header_position-1]:
                new_state_string += y
            new_state_string += '[%s]' % x
            for y in self.word[self.header_position:]:
                new_state_string += y
            self.list_run.insert('end', new_state_string)
            draw(
                self.automaton.alfabet,
                self.automaton.get_state_mar_current(),
                self.automaton.init,
                self.automaton.read_character(x),
                self.automaton.final,
                self.header_position
            )
            self.header_position += 1
        self.set_image_in_lbl_digraph("temp//blank.gif")
        self.set_image_in_lbl_digraph(
            "temp//Digraph_" + str(self.header_position-1) + ".gif"
        )

    def next_read_string(self):
        if (self.header_position - 1) >= len(self.word):
            self.header_position = 1
            self.select_init_state(self.automaton.init)
        x = self.word[self.header_position-1]
        new_state_string = ''
        for y in self.word[:self.header_position-1]:
            new_state_string += y
        new_state_string += '[%s]' % x
        for y in self.word[self.header_position:]:
            new_state_string += y
        self.list_run.insert('end', new_state_string)
        draw(
            self.automaton.alfabet,
            self.automaton.get_state_mar_current(),
            self.automaton.init,
            self.automaton.read_character(x),
            self.automaton.final,
            self.header_position
        )
        self.set_image_in_lbl_digraph("temp//blank.gif")
        self.set_image_in_lbl_digraph(
            "temp//Digraph_" + str(self.header_position) + ".gif"
        )
        self.header_position += 1


    def show(self):
        self.win.mainloop()
