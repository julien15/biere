# -*- coding: utf-8 -*-
# Author: Sébastien Combéfis
# Version: 5 Octobre 2015

from tkinter import *
import urllib.request
import json

# Class for the main frame
class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()
        self.createwidgets()
    
    def createwidgets(self):
        # Listbox for URLs
        self.__listbox = Listbox(self)
        self.__listbox.pack()
        result = urllib.request.urlopen("http://localhost:8080/links").read()
        database = json.loads(result.decode('utf-8'))
        for link in database['links']:
            self.__listbox.insert(END, link['name'])
        # Add a link control frame
        f = Frame(self)
        Label(f, text='Name').pack(side=LEFT)
        self.__name = Entry(f)
        self.__name.pack(side=LEFT)
        Label(f, text='URL').pack(side=LEFT)
        self.__url = Entry(f)
        self.__url.pack(side=LEFT)
        Button(f, text='Add', command=self.addlink).pack()
        f.pack()
    
    def addlink(self):
        # Add the link on the server
        name = self.__name.get()
        url = self.__url.get()
        data = json.dumps({'name': name, 'url': url, 'score': 0})
        urllib.request.urlopen("http://localhost:8080/addlink", data.encode('utf-8'))
        # Add the link in the listbox
        self.__listbox.insert(END, name)

# Launch the application
window = Tk()
app = App(window)
app.mainloop()