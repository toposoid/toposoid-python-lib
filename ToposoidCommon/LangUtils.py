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
    elif regex.search(ALPHABET_NUMBER_SYMBOL_REGEX, text):
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

#hoge = " Recent research, such as BitNet [WMD+23], is paving the way for a new era of 1-bit Large Language Models (LLMs). In this work, we introduce a 1-bit LLM variant, namely BitNet b1.58, in which every single parameter (or weight) of the LLM is ternary {-1, 0, 1}. It matches the full-precision (i.e., FP16 or BF16) Transformer LLM with the same model size and training tokens in terms of both perplexity and end-task performance, while being significantly more cost-effective in terms of latency, memory, throughput, and energy consumption. More profoundly, the 1.58-bit LLM defines a new scaling law and recipe for training new generations of LLMs that are both high-performance and cost-effective. Furthermore, it enables a new computation paradigm and opens the door for designing specific hardware optimized for 1-bit LLMs."
#print(detectLangage(hoge).lang)
