
# coding: utf-8

import numpy as np
import pickle
import sys
import os
import time
import glob

# library to deal with audio files
import librosa


SOUND_SAMPLE_LENGTH = 30*1000
HAMMING_SIZE = 100
HAMMING_STRIDE = 40

def die_with_usage():
	sys.exit(0)

def preprocessAudio(audioPath, ppFilePath):
	''' HELPER FUNCTION to preprocess the raw .wav audio file to MFCC'''
	
	print('Preprocessing ' + audioPath)
	
	featuresArray = []
	for i in range(0, SOUND_SAMPLE_LENGTH, HAMMING_STRIDE):
		if i + HAMMING_SIZE <= SOUND_SAMPLE_LENGTH - 1:
			y, sr = librosa.load(audioPath, offset = i/1000.0, duration = HAMMING_STRIDE/1000.0)
			
			# mel-scaled power spectrogram
			S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
			# convert to log scale (dB)
			log_S = librosa.amplitude_to_db(S)
			# MFCC
			mfcc = librosa.feature.mfcc(S=log_S, sr=sr, n_mfcc=13)
			featuresArray.append(mfcc)
			
			if len(featuresArray) == 599:
				break
	
	print('Storing pp file: ' + ppFilePath)
	
	f = open(ppFilePath, 'wb')
	f.write(pickle.dumps(featuresArray))
	f.close()

if __name__ == "__main__":
	if len(sys.argv) < 2:
		die_with_usage()

	audio_dir = sys.argv[1]

	os.chdir(audio_dir)

	for wav_file in glob.glob('*.wav'):
		# rename the post-processed file as *.pp
		ppFileName = os.path.splitext(os.path.basename(wav_file))[0] + '.pp'
	
		# ignore the file if already processed
		if os.path.isfile(ppFileName):
			continue
	
		# process the file
		try:
			start = time.time()
			preprocessAudio(wav_file, ppFileName)
			print ("Time elapsed: %.2f seconds" % (time.time() - start))
			print
		except Exception as e:
			print("Error occured" + str(e))

