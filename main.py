'''
    Este módulo integra o detector, extrator e o classificador
'''

#%%
import cv2
from mtcnn.mtcnn import MTCNN	
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import keras as K
import pandas as pd

