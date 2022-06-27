
strmn = open('devFiles/result2.json','r').read()

umap = {
    '\\u00e9': 'e',
    '\\u00e0': 'a ',
    '\\u00e8':'e',
    '\\u00e2':'a',
    '\\u00ee':'i',
    '\\u00ea':'e',
    '\\u00f9':'u',
    '\\u00f4':'o',
    '\\u00a4':' '
}

for key in umap:
    strmn = strmn.replace(key,umap[key])


with open('devFiles/result2-1.json','w') as fh:
    fh.write(strmn)