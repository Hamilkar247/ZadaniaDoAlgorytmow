#! python3
# backUpScript.py
# a ZIP file whose filename increments

import zipfile, os

def backUpScript(folder):
	#Backup the entire contents of "folder" into a ZIP file

	folder = os.path.abspath(folder) #make sure folder is absolute
	
	#figure out the filename this coe should use base on
	#what files alreadu exist
	number = 1
	
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename)
			break
		number = number + 1
		
	#TODO: Create the ZIP file.
	
	#TODO: Walk the entire folder tree and compress the files in each folder print('Done.')
	
backupToZip('K:\Informacyje\ZadaniaDoAlgorytmow')