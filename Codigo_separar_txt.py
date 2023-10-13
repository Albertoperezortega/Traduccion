
line = "&cUsage &7&o/notes [Name] <Page> &cor &7&o/notes <Page>"
line2 = '&aThe cache has been exported to the file &f{FILE}&a!'

good_chars = ["&0","&1","&2","&3","&4","&5","&6","&7","&8","&9","&a","&b","&c","&e","&l","&m","&n","&o",'\n']
bad_chars = ["&","%","/","<",">","[","]","{","}"]


def extract(line):
    indexes = []
    array_to_trans = []
    #este for loop crea una lista llamada indexes con la posicion de los chars raros (los de la lista bad_chars)
    for i in range(len(line)):
        if line[i] in bad_chars:
            indexes.append(i)
    print(indexes)

    #este loop coge todas las frases que hay entre los characteres raros 
    for i in range(len(indexes)):
        #pero en vd solo importan los que estan despues de & asin que solo coje esos
        if line[indexes[i]] == "&":
            a = (line[indexes[i]] + line[indexes[i]+1])
            if a in good_chars and indexes[-1] != indexes[i]:
                if (len(line[indexes[i] + 2:indexes[i+1]])) > 1 and (line[indexes[i] + 2:indexes[i+1]] != " "):
                    array_to_trans.append(line[indexes[i] + 2:indexes[i+1]])
            if indexes[-1] == indexes[i]:
                if (len(line[indexes[i] + 2:])) > 1 and (line[indexes[i] + 2:] != " "):
                    array_to_trans.append(line[indexes[i] + 2:])


        #No me he parado mucho a mirar casos pero si hay mas casos aparte del & son faciles de implementar como esta frase: "'&e➥ Left-Click to select'"
        #ejemplo: 
        """"if line[indexes[i]] == "/":
            for x in (line[indexes[i]:]):
                if x == " ":
                    pass"""""

        #De todas maneras me acabo de dar cuenta q tengo q entregar 2 proyectos pa la semana que viene asi q no voy a poder hacer mucho hasta la semana siguiente
    print(array_to_trans)
    
extract(line)
extract(line2)


