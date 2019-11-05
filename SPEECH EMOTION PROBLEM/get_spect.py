import os
import wave
import matplotlib.pyplot as plt
import pylab
import numpy as np

def get_info(wav_file):
    '''
	Args:
	wav_file path

	Returns:
	Get the frame rate and sound_info array. 

    '''
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

def get_spec(wav_file, save_path):
    '''
	Plots the spectrogram and saves it.
	Args:
	wav_file: audio file path
	save_path: path at which the spectroram has to be saved

	Returns:
	None
    '''
    sound_info, frame_rate = get_info(wav_file)
    plt.figure(num = None, figsize= (3,3))
    plt.specgram(sound_info, Fs=frame_rate)
    plt.savefig(save_path)
    plt.close()
    return None

def a_to_i(folder_path):
    '''
	Main Audio to Image conversion
    '''
    os.chdir(folder_path)
    folders = os.listdir()
    for folder in folders:
        path = os.path.join(folder_path, folder)
        os.chdir(path)
        files = os.listdir()
        for f in files:
            if os.path.isdir(os.path.join(path, f))==True:
                pass
            else:
                wav_file=os.path.join(path, f)
                get_spec(wav_file, save_path= os.path.join(path, 'imgs', f[:-4]+ 'jpg'))
                print(os.path.join(path, folder, f))
    return None
