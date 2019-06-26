import os
import shutil
os.chdir('K:\Google_Azimilik\Rozwój')
shutil.copy('cwiczenia.txt','K:\Informacyje\ZadaniaDoAlgorytmow')
os.chdir('K:\Google_Azimilik')
shutil.copytree('dlugi','K:\Informacyje\ZadaniaDoAlgorytmow\dlugi')
