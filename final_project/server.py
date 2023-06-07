from machinetranslation import Translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToSpanish():
    textToTranslate = request.args.get('textToTranslate')
    translator = Translator()
    translated_text = translator.translate(textToTranslate, "en", "es")
    return translated_text


@app.route("/frenchToEnglish")
def spanishToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translator = Translator()
    translated_text = translator.translate(textToTranslate, "es", "en")
    return translated_text


@app.route("/")
def renderIndexPage():
    # Write the code to render template

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
