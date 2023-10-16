import os
from Translate import trans


files = []
good_chars = ["&0","&1","&2","&3","&4","&5","&6","&7","&8","&9","&a","&b","&c","&e","&l","&m","&n","&o",'\n']
bad_chars = ["&","%","/","<",">","[","]","{","}"]
strange_char = [')"\n', 'Â» ', "'\n", '"\n', '| ']
trailing_chars = ["\n", " ", '"', "'", "#"]


def extract(line):
    indexes = []
    array_to_trans = []
    #este for loop crea una lista llamada indexes con la posicion de los chars raros (los de la lista bad_chars)
    for i in range(len(line)):
        if line[i] in bad_chars:
            indexes.append(i)

    #este loop coge todas las frases que hay entre los characteres raros
    for i in range(len(indexes)):
        #pero en vd solo importan los que estan despues de & asin que solo coje esos
        if line[indexes[i]] == "&":
            a = (line[indexes[i]] + line[indexes[i]+1])
            if a in good_chars and indexes[-1] != indexes[i]:
                if (len(line[indexes[i] + 2:indexes[i+1]])) > 1 and (line[indexes[i] + 2:indexes[i+1]] != " "):
                    array_to_trans.append([[indexes[i]+2, indexes[i+1]],line[indexes[i] + 2:indexes[i+1]]])
            if indexes[-1] == indexes[i]:
                if (len(line[indexes[i] + 2:])) > 1 and (line[indexes[i] + 2:] != " "):
                    array_to_trans.append([[indexes[i]+2, indexes[i]],line[indexes[i] + 2:]])
    return array_to_trans

def filter(extracted):
    filtered = []
    for word in extracted:
        if word:
            for elt in word:
                try:
                    if elt[1] in strange_char:
                        pass
                    elif elt[1][-1] in trailing_chars:
                        #print(f"{elt} -> {elt[1][:-1]}")
                        if elt[1][-2] in trailing_chars:
                            filtered.append([[elt[0][0], elt[0][1]-1],elt[1][:-2]])
                        else:
                            filtered.append([[elt[0][0], elt[0][1] - 2], elt[1][:-1]])
                    else:
                        filtered.append(elt)
                except Exception as e:
                    print(elt)
    return filtered


def insert(original_phrase, indexes):
    translated_phrase = original_phrase
    total_length_diff = 0
    length_diff = 0
    for i,chunk in enumerate(indexes):
        chunk_translated = trans(original_phrase[indexes[i][0]:indexes[i][1]])
        translated_phrase = translated_phrase[:(indexes[i][0] + total_length_diff)] + chunk_translated + translated_phrase[(indexes[i][1] + length_diff):]
        length_diff = len(chunk_translated) - indexes[i][1] + indexes[i][0]
        total_length_diff += length_diff
    return translated_phrase

def get_string(files):
    strings = []
    for i in files:
        text = open(i, "r")
        lines = text.readlines()
        text.close()
        for line in lines:
            strings.append(extract(line))
    return strings

def reader(dir):
    try:
        arr = os.listdir(f'{dir}')
    except Exception as e:
        return
    for i in arr:
        if ".yml" in i:
            files.append(f"{dir}/{i}")
        if "." not in i:
            reader(f"{dir}/{i}")

reader('./archivos')
resultado = get_string(files)
filtrado = filter(resultado)
for elt in filtrado:
    print(elt)

# hay algunas palabras en las que los indices estan de al reves o algo
# lo siguiente es implementar la traducción
# podemos hacer en dos pasadas al archivo o en cuanto encotremos las palabras (esta es la mejor pero va a ser un lio)

class phr:
    
    def __init__ (self, content, line_num, start_index, file_path):
        self.raw = content
        self.divided = []
        self.translated = ""
        self.line_num = line_num    
        self.start_index = start_index                                                                                      
        self.file_path = file_path

#get_string("./archivos/Quests/quests/collect66rawrabbit.yml")
#print(insert("hello world", [[0,4],[6,11]]))


