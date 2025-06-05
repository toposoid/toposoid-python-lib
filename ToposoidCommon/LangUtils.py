from langdetect import detect
import regex
from .model import DetectedLanguage

JAPANNESE_REGEX = regex.compile(r"^.*([ぁ-ん]|[\u30A1-\u30F4]|\p{sc=Han}).*$")

def detectLangage(text: str):

    if regex.search(JAPANNESE_REGEX, text):
        return DetectedLanguage(lang="ja_JP")
    else:
        lang = detect(text)
        if lang == "ja":
            return DetectedLanguage(lang="ja_JP")
        elif lang == "en":
            return DetectedLanguage(lang="en_US")
        else:
            raise Exception("This language is not covered by Toposoid")
        
