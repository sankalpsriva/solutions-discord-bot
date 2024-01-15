from keras.models import load_model, Sequential, Model
from keras.layers import TextVectorization
import pandas as pd 
import numpy as np
from pandas import DataFrame

class ToxicityModel: 
    def __init__(self):
        WORDS = 200000
        self.model: Model = load_model("toxicity_dectector.model")

        self.df = pd.read_csv("train.csv")
        self.df_X = self.df['comment_text']

        self.text_vec = TextVectorization(max_tokens=WORDS, output_sequence_length=180, output_mode='int')
        self.text_vec.adapt(self.df_X.values)

    def get_model(self) -> Model:
        return self.model 
    
    def get_df(self) -> DataFrame:
        return self.df
    
    def get_analysis(self, message: str) -> list[float]:
        message_vec = self.text_vec(message)
        return self.model.predict(np.expand_dims(message_vec, 0))[0]

class QuestionModel: 
    
    def __init__(self): 
        pass 
    
    def get_model(self):
        pass 
    
    def get_df(self): 
        pass 
    
    def get_analysis(self):
        pass 
    
