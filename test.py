import os
from Translate import trans


files = []
good_chars = ["&0","&1","&2","&3","&4","&5","&6","&7","&8","&9","&a","&b","&c","&e","&l","&m","&n","&o",'\n']
bad_chars = ["&","%","/","<",">","[","]","{","}"]
strange_char = [')"\n', 'Â» ', "'\n", '"\n', '| ', ]
trailing_chars = ["\n", " ", '"', "'", "#", '|']


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
            if i == len(indexes)-1:
                if (len(line[indexes[i] + 2:])) > 1 and (line[indexes[i] + 2:] != " "):
                    array_to_trans.append([[indexes[i]+2, indexes[i]+len(line[indexes[i] + 2:])],line[indexes[i] + 2:]])
                    #print([[indexes[i]+2, indexes[i]+len(line[indexes[i] + 2:])],line[indexes[i] + 2:]])
    return array_to_trans

# queda por filtrar cuando sale CharacterEncoding=utf8, #ID, IP, UUID
def filter(extracted):
    filtered = []
    for word in extracted:
        if len(word) > 1:
            line_num = 0
            for elt in word:
                try:
                    if type(elt) == type(2):
                        line_num = elt
                    elif elt[1] in strange_char:
                        pass
                    elif elt[1][-1] in trailing_chars:
                        if elt[1][-2] in trailing_chars:
                            filtered.append([line_num, [elt[0][0], elt[0][1]-1],elt[1][:-2]])
                        else:
                            filtered.append([line_num, [elt[0][0], elt[0][1] - 2], elt[1][:-1]])
                    else:
                        filtered.append([line_num, elt[0], elt[1]])
                except Exception as e:
                    raise e
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
    output = []
    for i in files:
        strings = [i]
        text = open(i, "r")
        lines = text.readlines()
        text.close()
        for n,line in enumerate(lines):
            index_extract = extract(line)
            index_extract.insert(0,n)
            strings.append(index_extract)
        output.append(strings)
    return output

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
final = []
for file_and_string in resultado:
    name = file_and_string[0]
    file_and_string = filter(file_and_string[1:])
    file_and_string.insert(0,name)
    final.append(file_and_string)

for elt in final:
    for x in elt:
        print(x)

# quedan algunas palabrs ezoecifica que no se si filtrar, lo pone encima de la funcio de filtrar
# lo siguiente es implementar la traducción
# hay que reworkear el insert por que está hecho para funcionar differente

#get_string("./archivos/Quests/quests/collect66rawrabbit.yml")
#print(insert("hello world", [[0,4],[6,11]]))


