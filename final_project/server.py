# from machinetranslation import Translator
from flask import Flask, render_template, request
import json
import machinetranslation as MT

app = Flask("Web Translator")


@app.route("/englishToFrench", methods=["POST"])
def englishTofrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = MT.translator.english_to_french(
        textToTranslate)
    return translation


@app.route("/frenchToEnglish", methods=["POST"])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = MT.translator.french_to_english(
        textToTranslate)
    return translation


@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
