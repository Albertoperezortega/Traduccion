from googletrans import Translator, constants

# init the Google API translator
translator = Translator()
def trans(text):
    translation = translator.translate(text, dest="es", src="en")
    return translation.text

#print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
# print(translation.extra_data)
# le puedes meter una lista de frases al translator.translate
# hay una posibilidad de que si haces demasiados requests google banee tu dirección IP