# Music Genre Classification

Training and testing files were provided by Zalo Vietnam, but were not allowed to be taken out. The .mp3 files in the `Data` folder are for demonstrative purpose only.  

There were approximately 5000 audio files in the train set and 2000 audio files in the test set. Audio files were all in .mp3 format. There was also a .csv file containing the labels (1-10) for all songs in the train set corresponding to their genres. The goal is to build a classifier to predict the label of every song in the test set.  

First we need to convert the .mp3 files into .wav files for preprocessing. `wav_convert.ipynb` will re-encode the audio files into .wav and also only keep the middle 30 seconds of each song.   

For visualization, we can run `spectrogram.ipynb` to analyze sample songs to see the differences among different genres. This script will convert audio files into spectrograms for visual analysis.  

Then we can pre-process the .wav files by running `preprocess.py`, which extract [MFCCs](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum) from each song.  
 
`data_input.ipynb` reads in the processed data and matches each song with its correct label.  

Then all processed data were fed into a convolutional neural network in `CNN.ipynb` for prediction.
