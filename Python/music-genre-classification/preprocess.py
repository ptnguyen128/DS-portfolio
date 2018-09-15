
# coding: utf-8

import numpy as np
import pickle
import sys
import os

# library to deal with audio files
import librosa


SOUND_SAMPLE_LENGTH = 30000
HAMMING_SIZE = 100
HAMMING_STRIDE = 40

def die_with_usage():
    sys.exit(0)

def rreplace(s, old, new, occurence):
    ''' HELPER FUNCTION to replace the extension of a file '''
    
    li = s.rsplit(old, occurence)
    return new.join(li)


def preprocessAudio(audioPath, ppFilePath):
    ''' HELPER FUNCTION to preprocess the raw .mp3 audio file to MFCC'''
    
    print('Preprocessing' + audioPath)
    
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

    walk_dir = sys.argv[1]

    for root, subdirs, files in os.walk(walk_dir):
        for filename in files:
            if filename.endswith('.mp3'):
                file_path = os.path.join(root,filename)
                ppFileName = rreplace(file_path, '.mp3', '.pp', 1)
            
                if os.path.isfile(ppFileName):
                    continue
            
                try:
                    preprocessAudio(file_path, ppFileName)
                except Exception as e:
                    print("Error occured" + str(e))

