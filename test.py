import os

files = []
bad_chars = ["&0","&1","&2","&3","&4","&5","&6","&7","&8","&9","&a","&b","&c","&l","&m","&n","&o"]

def tidy_up(value):
    if (value != "&") or (value != "/") or (value != "{") or (value != '"') or (value != "'"):
        True

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
            print(line[i] + line[i + 1] + line[i + 2])
            print(line)
            print("----")
              
def extract(line):
    elts = []
    while line != "" or line != '':
        print(line)
        phrase = line[line.index("&")+2:]
        try:
            next_and = phrase.index("&")
            phrase = phrase[:next_and]
        except:
            phrase = line[line.index("&")+2:]
            line = "  "
        if phrase == "" or phrase == '':
            pass
        else:
            elts.append(phrase)
        line = line[next_and + 2:]
    return elts
        

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

