import zipfile, os
os.chdir('K:\Informacyje\ZadaniaDoAlgorytmow')
newZip = zipfile.ZipFile('cytaty.zip', 'w')
newZip.write('Cytaty.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


