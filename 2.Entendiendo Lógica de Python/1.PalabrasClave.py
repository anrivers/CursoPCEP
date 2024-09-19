#import keyword

#print(keyword.kwlist)

import keyword

palabra_clave = ['else']

for palabra in keyword.kwlist:
    if palabra in palabra_clave:
        print(palabra)