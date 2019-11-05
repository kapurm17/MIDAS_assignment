import os
import wave
import matplotlib.pyplot as plt
import pylab
import numpy as np

def get_info(wav_file):
    '''

    '''
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

def get_spec(wav_file, save_path):
    '''

    '''
    sound_info, frame_rate = get_info(wav_file)
    plt.figure(num = None, figsize= (6,6))
    plt.specgram(sound_info, Fs=frame_rate)
    plt.savefig(save_path)
    plt.close()
    return None

def a_to_i(folder_path):
    '''

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
