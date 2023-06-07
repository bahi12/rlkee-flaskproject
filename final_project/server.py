# from machinetranslation import Translator
from flask import Flask, render_template, request
import json
import machinetranslation as MT

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToSpanish():
    textToTranslate = request.args.get('textToTranslate')
    translation = MT.translator.english_to_french(
        textToTranslate)
    return translation


@app.route("/frenchToEnglish")
def spanishToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = MT.translator.french_to_english(
        textToTranslate)
    return translation


@app.route("/")
def renderIndexPage():
    # Write the code to render template

    if __name__ == "__main__":
        app.run(host="localhost", port=8080)
