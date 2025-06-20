from langdetect import detect
import regex
from .model import DetectedLanguage

JAPANNESE_REGEX = regex.compile(r"^.*([ぁ-ん]|[\u30A1-\u30F4]|\p{sc=Han}).*$")
ALPHABET_NUMBER_SYMBOL_REGEX = regex.compile(r'^[ -~]+$')
SPECIAL_SYMBOL_REGEX1 = regex.compile(r"^NO_REFERENCE_[0-9a-f]{8}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{12}_[0-9]+$")

def detectLangage(text: str):

    if regex.search(SPECIAL_SYMBOL_REGEX1, text):
        return DetectedLanguage(lang="@@_#1")
    elif regex.search(JAPANNESE_REGEX, text):
        return DetectedLanguage(lang="ja_JP")
    elif regex.search(ALPHABET_NUMBER_SYMBOL_REGEX):
        return DetectedLanguage(lang="en_US")
    else:
        lang = detect(text)
        if lang == "ja":
            return DetectedLanguage(lang="ja_JP")
        elif lang == "en":
            return DetectedLanguage(lang="en_US")
        else:
            raise Exception("This language is not covered by Toposoid")
        
#hoge = "NO_REFERENCE_5d9afee2-4c10-11f0-9f26-acde48001122_10"
#print(detectLangage(hoge).lang)