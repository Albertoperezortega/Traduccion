from tkinter import *
from tkinter.ttk import *
import os


class Result:

    def __init__(self, window, text, folder, similarity):
        self.text = text
        self.text_label = Label(window)
        self.text_label.config(text=text)
        self.folder = folder
        self.folder_label = Label(window)
        self.folder_label.config(text=folder)
        self.similarity = similarity
        self.similarity_label = Label(window)
        self.similarity_label.config(text=similarity)

    def bind(self, command):
        self.text_label.bind("<Button-1>", command)
        self.folder_label.bind("<Button-1>", command)
        self.similarity_label.bind("<Button-1>", command)

    def draw(self,row, start_col=0):
        self.text_label.grid(row=row, column=start_col,pady=2, padx=2)
        self.folder_label.grid(row=row, column=1+start_col,pady=2, padx=2)
        self.similarity_label.grid(row=row, column=2+start_col,pady=2, padx=2)


class Table:

    def __init__(self, window):
        self.results = []
        self.window = window

    def insert(self, text, folder, similarity,func):
        new_result = Result(self.window, text, folder, similarity)
        new_result.bind(lambda e:func(text))
        for i,elt in enumerate(self.results):
            if similarity > elt.similarity:
                self.results.insert(i,new_result)
                break
            if i+1 == len(self.results):
                self.results.append(new_result)
        self.results = self.results[:10]

    def draw(self,row, col):
        encabezado = Result(self.window, "resultado", "archivo", "% de similitud")
        encabezado.draw(row, col)
        for i,resultado in enumerate(self.results):
            resultado.draw(row+i+1, col)


def find_matches(files, text, match_threshold=0.5):
    output = []
    split_text = text.split()
    for i in files:
        text = open(i, "r")
        lines = text.readlines()
        text.close()
        for line in lines:
            split_line = line.split()
            matches = 0
            for i in range(len(split_text)):
                if i > len(split_line):
                    pass
                elif split_text[i] == split_line[i]:
                    matches += 1
            similarity = matches/len(split_text)
            if similarity > match_threshold:
                output.append([line,i,similarity])
    return output


def reader(dir):
    if dir is None:
        dir = './archivos'
    try:
        arr = os.listdir(f'{dir}')
    except Exception as e:
        print(e)
        return
    output = []
    for i in arr:
        if ".yml" in i:
            output.append(f"{dir}/{i}")
        if "." not in i:
            output = output + reader(f"{dir}/{i}")
    return output


def search_files(search_text, table, display, dir=None):
    files = reader(dir)
    matches = find_matches(files, search_text)
    for elt in matches:
        table.inser(elt[0], elt[1], elt[2], display_item_setup(display))
    #table.insert("a","b","c",display_item_setup(display))
    table.draw(4,0)


def display_item_setup(label):

    def label_display(text):
        label.config(text=text)

    return label_display


def main():
    # creating main tkinter window/toplevel
    master = Tk()
    master.geometry("655x450")

    table = Table(master)

    search = Entry(master)
    search.grid(row=0, column=1, pady=5, padx=5)

    selected = Label(master, text="")
    selected.grid(row=2, column=0)

    button = Button(master, text="Buscar", command=lambda: search_files(table,selected))
    button.grid(row=0, column=2, pady=5, padx=5)

    selected_label = Label(master, text="Texto seleccionado")
    selected_label.grid(row=1, column=0)

    arrow = Label(master, text="->")
    arrow.grid(row=2, column=1)

    replacement_label = Label(master, text="Reemplazo")
    replacement_label.grid(row=1, column=2)

    replace_button = Button(master, text="Reemplazar")
    replace_button.grid(row=3, column=1)

    replacement = Entry(master)
    replacement.grid(row=2, column=2)

    table.draw(4, 0)

    # infinite loop which can be terminated by keyboard
    # or mouse interrupt
    mainloop()

# y luego tienes un text box con un botton de sustituir
# despues de eso viene implementación de las funciones
#  - primero buscar por los archivos por un match
#  - luego sustituirlo

main()