import os
from googletrans import Translator

files = []
bad_chars = ["&0","&1","&2","&3","&4","&5","&6","&7","&8","&9","&a","&b","&c","&l","&m","&n","&o"]

def tidy_up(value):
    if (value != "&") or (value != "/") or (value != "{") or (value != '"') or (value != "'"):
        return True

def tidy_up_v2(value):
    if value not in ["&","/","{","}","'",'"']:
        return True

def filter_txt(line):
    if '"' in line:
        line = line[line.find('"'):]
    elif "'" in line:
        line = line[line.find("'"):]
    else:
        return
    position = [i for i,x in enumerate(line) if x == "&"] 
    for i in position:
        if line[i:i + 2] in bad_chars and line[i + 2].isalnum():    
            print(line)     
            print(extract(line))
            print("---------------------")
            print("---------------------")

def extract(line):
    elts = []
    next_and = 0
    while line != "" or line != '':
        phrase = line[line.index("&")+2:]
        try:
            next_and = phrase.index("&")
            phrase = phrase[:next_and]
        except:
            phrase = line[line.index("&")+2:]
            line = "  "
        for i in phrase:
            if phrase[0] == " " or phrase[0].isalnum():
                if phrase == "" or phrase == '':
                    pass
                else:
                    elts.append(phrase)
        
        line = line[next_and + 2:]
    return elts

def insert(original_phrase, indexes):
    translator = Translator() #creo que lo suyo sería sacar esto
    translated_phrase = original_phrase
    total_length_diff = 0
    length_diff = 0
    for i,chunk in enumerate(indexes):
        chunk_translated = translator.translate(original_phrase[indexes[i][0]:indexes[i][1]], dest="es", src="en").text
        translated_phrase = translated_phrase[:(indexes[i][0] + total_length_diff)] + chunk_translated + translated_phrase[(indexes[i][1] + length_diff):]
        length_diff = len(chunk_translated) - indexes[i][1] + indexes[i][0]
        total_length_diff += length_diff
    return translated_phrase

def get_string(files):
    for i in files:
        text = open(i, "r")
        lines = text.readlines()
        for line in lines:
            filter_txt(line)

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
get_string(files)



class phr:
    
    def __init__ (self, content, line_num, start_index, file_path):
        self.raw = content
        self.divided = []
        self.translated = ""
        self.line_num = line_num    
        self.start_index = start_index                                                                                      
        self.file_path = file_path

#get_string("./archivos/Quests/quests/collect66rawrabbit.yml")
print(insert("hello world", ["hello","world"], [[0,4],[6,11]]))


