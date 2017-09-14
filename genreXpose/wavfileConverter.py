import wave
import os
import sunau
from utils import GENRE_DIR, CHART_DIR, GENRE_LIST
import struct
import random

chunk = 44100

def convertAUFileToWav(filename):
	auRead = sunau.open(filename, 'r')
	params = auRead.getparams()
	print params
	audio_frames = auRead.readframes(auRead.getnframes())

	new_file = os.path.splitext(filename)[0]+'.wav'
	#print new_file
	#open(new_file, 'w')

	waveWrite = wave.open(new_file, 'wb')
	waveWrite.setparams(params)
	waveWrite.writeframes(audio_frames)
	waveWrite.close()
	#data = struct.unpack('{}h'.format(chunk * channels), audio_frames)
	#print "Audio frames data: "
	# print data
	# new_file = os.path.splitext(filename)[0]+'.wav'
	# print new_file
	# open(new_file, 'w')

	# # write the file
	# print "--------Writing wav file--------"
	# waveWrite = wave.open(new_file, 'w')
	# waveWrite.setparams(params)
	# waveWrite.writeframes(data)
	# waveWrite.close()

def convertToWav():
	for subdir, dirs, files in os.walk(GENRE_DIR):
		for file in files:
			path = subdir+'/'+file
			print path


def testfiles():
	waveFile = wave.open('/Users/lucyzhang/Desktop/genres-project/genres/pop/pop.00000.wav', 'r')
	print waveFile.getparams()
	waveData = map(ord, list(waveFile.readframes(waveFile.getnframes())))
	wFile = open("waveOutput.txt", "w")
	wFile.write(str(waveData))

	print "-----------"
	auFile = sunau.open('/Users/lucyzhang/Desktop/genres-project/genres/pop/pop.00000.au')
	auData = map(ord, list(auFile.readframes(auFile.getnframes())))
	auFile = open("sunauOutput.txt", "w")
	auFile.write(str(auData))


if __name__ == '__main__':
	testfiles()
	#convertAUFileToWav('/Users/lucyzhang/Desktop/genres-project/genres/classical/classical.00000.au')