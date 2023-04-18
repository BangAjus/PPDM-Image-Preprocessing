from skimage import data, io, feature, util, transform
import numpy as np
from matplotlib import pyplot as plt
from skimage import color
import pandas as pd
from scipy.stats import kurtosis, skew, entropy
from scipy.ndimage import variance
import math
import os

def show_photo_preview(number, emotion):

    if emotion.lower() == 'happy':
        happy = "C:/Tugas/PPDM/Tugas 2/Pictures/Happy"

        for i in os.listdir(happy):
            if number in i:
                return happy + '/' + i
    
    if emotion.lower() == 'neutral':
        neutral = "C:/Tugas/PPDM/Tugas 2/Pictures/Neutral"

        for i in os.listdir(neutral):
            if number in i:
                return neutral + '/' + i
            
    if emotion.lower() == 'sad':        
        sad = "C:/Tugas/PPDM/Tugas 2/Pictures/Sad"

        for i in os.listdir(sad):
            if number in i:
                return sad + '/' + i
            

def make_matrix(photo):

    return io.imread(photo)


def data_for_stats(emotion):

    if emotion.lower() == 'happy':

        happy = "C:/Tugas/PPDM/Tugas 2/Pictures/Happy"
        happy = [happy + '/' + i for i in os.listdir(happy)]
        happy = [io.imread(i, pilmode='L') for i in happy]

        return happy

    if emotion.lower() == 'neutral':

        neutral = "C:/Tugas/PPDM/Tugas 2/Pictures/Neutral"
        neutral = [neutral + '/' + i for i in os.listdir(neutral)]
        neutral = [io.imread(i, pilmode='L') for i in neutral]

        return neutral

    if emotion.lower() == 'sad': 

        sad = "C:/Tugas/PPDM/Tugas 2/Pictures/Sad"
        sad = [sad + '/' + i for i in os.listdir(sad)]
        sad = [io.imread(i, pilmode='L') for i in sad]

        return sad

def image_hist(picture_dir):

    pic = io.imread(picture_dir, pilmode='L')
    plt.hist(pic.flatten(), bins=256)


def glcm_for_image(photo, angle):
    photo = io.imread(photo, pilmode='L')
    return feature.graycomatrix(photo, distances=[2], angles=angle,
                                levels=256, symmetric=True, normed=True).flatten().reshape(256, 256)
    

def calc_glcm_for_each_photo(photo, emotion):
    
    features = ['dissimilarity', 'correlation', 'homogeneity', 'contrast', 'ASM', 'energy']
    angle = [0, 45, 90, 135]

    def count_ent_and_idm(glcm):

        Ent = [0.0]*4
        Idm = [0.0]*4

        for angle in range(4):
            for i in range(256):
                for j in range(256):
                    Idm[angle] += glcm[i][j][0][angle] / (1 + ((i - j)**2))
                    if glcm[i][j][0][angle] > 0.0:
                        Ent[angle] += glcm[i][j][0][angle] * math.log(glcm[i][j][0][angle])
        return [-i for i in Ent], Idm
    
    props = {'Angle': angle,
             'Emotion': [emotion]*4}
    
    glcm = feature.graycomatrix(photo, distances=[2], angles=angle, levels=256,
                        symmetric=True, normed=True)
    
    for i in  features:
        props[i.capitalize()] = feature.graycoprops(glcm, prop=i).flatten()

    ent, idm = count_ent_and_idm(glcm)
    props['Entropy'] = ent
    props['IDM'] = idm

    props = pd.DataFrame(props)
    return props


def concat_calculation(photos, emotions):
    empty = {'Picture': [],
             'Angle':[],
             'Emotion':[]}
    features = ['dissimilarity', 'correlation', 'homogeneity', 'contrast', 'ASM', 'energy', 'entropy']

    for i in features:
        empty[i.capitalize()] = np.array([])
    empty = pd.DataFrame(empty)
    
    for x, y in zip(photos, emotions):
        data = calc_glcm_for_each_photo(x, y)
        empty = pd.concat([empty, data], ignore_index=True)
        
    a = 1
    j = 391
    for i in empty.index:
        empty.loc[i, 'Picture'] = emotions[0] + '-' + str(j)
        a += 1
        if a > 4 and a % 4 == 1:
            j += 1

    return empty


def first_order_stat(photos, emotion):

    empty = {'Picture':[emotion[0]  + '-' + str(i+391) for i in range(len(photos))],
             'Emotion':[i for i in emotion]}

    empty['Mean'] = [np.mean(photos[i].flatten()) for i in range(len(photos))]
    empty['Skewness'] = [skew(photos[i].flatten()) for i in range(len(photos))]
    empty['Kurtosis'] = [kurtosis(photos[i].flatten(), fisher=True) for i in range(len(photos))]
    empty['Variation'] = [variance(photos[i]) for i in range(len(photos))]
    empty['Entropy'] = [entropy(photos[i].flatten(), base=2) for i in range(len(photos))]

    return pd.DataFrame(empty)


def hist_for_photo(photo_dir):

    return io.imread(photo_dir, pilmode='L').flatten()
