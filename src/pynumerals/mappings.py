CHAR_REPL = {
    # replace Charis SIL PUA characters
    "": "\u1DC4",  # U+F171 -> COMBINING MACRON-ACUTE
    "": "\u1DC5",  # U+F172 -> COMBINING GRAVE-MACRON
    "": "\u1DC6",  # U+F173 -> COMBINING MACRON-GRAVE
    "": "\u1DC7",  # U+F174 -> COMBINING ACUTE-MACRON
    "": "ꜛ",  # U+F19C
    "": "ꜜ",  # U+F19D
    "": "ȼ",  # U+F20B
    "": "ᵬ",  # U+F249
    "": "ᵭ",  # U+F24A

    # actually: MODIFIER LETTER SMALL RAMS HORN - no Unicode code point yet
    # found in language Kodia only
    "": "ɤ",  # U+F1B5

}

BASE_MAP = {
    "(2, 5) cyclic": "",
    "(2, 5, 20) cyclic": "",
    "(quinternary)": "quinary",
    "-2": "binary",
    "-5": "quinary",
    "-five": "quinary",
    "-six": "senary",
    "2-cycle": "",
    "5, 20": "quinary/vigesimal",
    "5-20": "quinary/vigesimal",
    "5-cycle": "",
    "7-vowel Bantu": "",
    "8": "octal",
    "14": "",
    "20": "vigesimal",
    "24": "tetravigesimal",
    "27": "body",
    "80": "",
    "a peculiar": "",
    "a vigesimal": "vigesimal",
    "Bantufive": "quinary",
    "basic vigesimal": "vigesimal",
    "binary": "binary",
    "body": "body",
    "body tally": "body",
    "body-part": "body",
    "body-part tally": "body",
    "body-tally": "body",
    "complex": "",
    "complex vigesimal": "vigesimal",
    "complextwenty": "vigesimal",
    "complicated": "",
    "d 35 body tally": "body",
    "d five-twenty": "quinary/vigesimal",
    "decimal": "decimal",
    "decimal of": "decimal",
    "deimal": "decimal",
    "decimal/vigesimal": "decimal/vigesimal",
    "digit-tally": "body",
    "duodecimal": "duodecimal",
    "five": "quinary",
    "five-": "quinary",
    "five-(quinternary)": "quinary",
    "five-and twenty-": "quinary/vigesimal",
    "five-d": "quinary",
    "hand": "",
    "hands": "",
    "has a vigesimal": "vigesimal",
    "ing": "",
    "modulo 24": "",
    "new decimal": "",
    "one,two,three,many": "",
    "partial quinary": "",
    "peculiar": "",
    "peculiar vigesimal": "vigesimal",
    "politeness": "decimal",
    "poor": "",
    "quaternary": "quaternary",
    "quianry, decimal": "quinary/decimal",
    "quianry, vigesimal": "quinary/vigesimal",
    "quianry-decimal": "quinary/decimal",
    "quinary": "quinary",
    "quinary (5)": "quinary",
    "quinary / decimal": "quinary/decimal",
    "quinary / vigesimal": "quinary/vigesimal",
    "quinary /decimal": "quinary/decimal",
    "quinary /vigesimal": "quinary/vigesimal",
    "quinary, decimal": "quinary/decimal",
    "quinary, vigesimal": "quinary/vigesimal",
    "quinary,-twenty": "quinary/vigesimal",
    "quinary-decimal": "quinary/decimal",
    "quinary-vigesimal": "quinary/vigesimal",
    "quinary/vigesimal": "quinary/vigesimal",
    "quinary/ decimal": "quinary/decimal",
    "quinary/decimal": "quinary/decimal",
    "quintenary": "quinary",
    "regular decimal": "decimal",
    "senary": "senary",
    "similar": "",
    "similar decimal": "",
    "six-": "senary",
    "six-cycle": "",
    "sixty": "body",
    "special": "",
    "special aboriginal": "",
    "tally": "",
    "ten": "decimal",
    "ten-d": "decimal",
    "twenty": "vigesimal",
    "two": "binary",
    "two-": "binary",
    "vegisimal": "vigesimal",
    "very": "",
    "very complex": "",
    "very particular": "",
    "very unusual": "",
    "vigesimal": "vigesimal",
    "vigesimal or20": "vigesimal",
    "vigesimal/decimal": "decimal/vigesimal",
    "–25": "pentavigesimal",
    "decimal AND vigesimal": "decimal AND vigesimal",
    "decimal OR vigesimal": "decimal OR vigesimal",
    "heptavigesimal": "heptavigesimal",
    "octal AND decimal": "octal AND decimal",
    "octal AND duodecimal AND hexadecimal AND vigesimal AND tetravigesimal": "octal AND duodecimal AND hexadecimal AND vigesimal AND tetravigesimal",
    "octal": "octal",
    "octogesimal": "octogesimal",
    "pentadecimal OR pentavigesimal": "pentadecimal OR pentavigesimal",
    "pentavigesimal": "pentavigesimal",
    "quaternary AND quinary AND vigesimal": "quaternary AND quinary AND vigesimal",
    "quaternary OR tetravigesimal": "quaternary OR tetravigesimal",
    "quinary AND decimal AND vigesimal": "quinary AND decimal AND vigesimal",
    "quinary AND decimal": "quinary AND decimal",
    "quinary AND double decimal": "quinary AND double decimal",
    "quinary AND vigesimal OR decimal": "quinary AND vigesimal OR decimal",
    "quinary AND vigesimal": "quinary AND vigesimal",
    "quinary OR decimal": "quinary OR decimal",
    "quinquagesimal": "quinquagesimal",
    "sexagesimal": "sexagesimal",
    "tetradecimal": "tetradecimal",
    "tetravigesimal": "tetravigesimal",
    "trigesimal": "trigesimal",
    "vigesimal AND quadragesimal AND quattrocentimal": "vigesimal AND quadragesimal AND quattrocentimal",
    "ternary": "ternary",
}
