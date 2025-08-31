#!/bin/sh
# Select unicode characters with fzf.

tab='	'

{
    python <<EOF
import unicodedata
for i in range(0x10fff):
    try:
        c = chr(i)
        print(c, unicodedata.name(c), sep="\t")
    except:
        pass
EOF
} | fzf --multi | cut -d "$tab" -f 1
