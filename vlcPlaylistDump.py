import os, shutil

playlist = 'Path_To//Playlist.xspf'
mp3s = []

# grab data

startTag = '<location>file:///'
endTag = '</location>\n'

with open(playlist) as playlistFile:
	for line in playlistFile:
		if startTag in line:

			startIndex = line.index(startTag) + len(startTag)
			endIndex = line.index(endTag)

			mp3s.append(line[startIndex:endIndex])

# clean data

count = 0
while count < len(mp3s):
	if '%20' in mp3s[count]:
		mp3s[count] = mp3s[count].replace('%20', ' ')
	count += 1

# copy data

os.mkdir('playListDump')
os.chdir('playListDump')

for mp3 in mp3s:
	print mp3
	shutil.copy(mp3, os.getcwd())
