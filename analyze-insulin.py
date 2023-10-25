seq = open("preproinsulin-seq.txt", 'r')
seq = ''.join(c for c in seq.read() if c.isalpha())
seqClean = ''.join(c for c in seq if c.isupper() == False)
 
seqCleanList = list(seqClean)
isinsulin = seqCleanList[0:24] 
binsulin = seqCleanList[24:54] 
cinsulin = seqCleanList[54:89]
ainsulin = seqCleanList[89:110]
 
print(str(isinsulin), '\n', len(isinsulin))
print('\n')
print(str(binsulin), '\n', len(binsulin))
print('\n')
print(str(cinsulin), '\n', len(cinsulin))
print('\n')
print(str(ainsulin), '\n', len(ainsulin))
