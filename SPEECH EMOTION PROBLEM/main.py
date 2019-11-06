import os
import pylab
import matplotlib.pyplot as plt
import get_spect
import keras
from keras.preprocesing.image import ImageDataGenerator

print("Enter test folder path")
folder_path = input()

get_spect.a_to_i(folder_path)

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

path = os.path.join(folder_path, 'spect_imgs')

# Creating a datagenerator
datagen = ImageDataGenerator(rescale=1/255)

test = datagen.flow_from_diretory()

predictions = loaded_model.predict_generator()
pred = predictions.argmax
df =pd.DataFrame(predictions)
df.to_excel('output.xlsx')
