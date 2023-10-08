from googletrans import Translator, constants

# init the Google API translator
translator = Translator()

translation = translator.translate("Acacia log", dest="es", src="en")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
# print(translation.extra_data)
# le puedes meter una lista de frases al translator.translate
# hay una posibilidad de que si haces demasiados requests google banee tu dirección IP