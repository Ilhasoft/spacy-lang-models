# coding: utf8
from __future__ import unicode_literals

from ...attrs import LIKE_NUM

_num_words = [
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
    "trinta",
    "quarenta",
    "cinquenta",
    "sessenta",
    "setenta",
    "oitenta",
    "noventa",
    "cem",
    "cento"
    "centena",
    "centenas",
    "mil",
    "milhares",
    "milhão",
    "milhões"
    "trilhão",
    "trilhões",
    "quadrilhão",
    "quadrilhões",
    "quintilhão",
    "quintilhões",
    "sextilhão",
    "sextilhões",
    "septilhão",
    "septilhões",
    "octilhão",
    "octilhões",
    "nonilhão",
    "nonilhões",
    "decilhão",
    "decilhões",
    "undecilhão",
    "undecilhões",
    "duodecilhão",
    "duodecilhões",
    "tredecilhão",
    "tredecilhões",
    "quatordecilhão",
    "quatordecilhões",
    "quindecilhão",
    "quindecilhões",
    "sexdecilhão",
    "sexdecilhões",
    "setedecilhão",
    "setedecilhões",
    "octodecilhão",
    "octodecilhões",
    "novedecilhão",
    "novedecilhões",
    "vigesilhão",
    "vigesilhões"
]


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    if text.lower() in _num_words:
        return True
return False

LEX_ATTRS = {LIKE_NUM: like_num}