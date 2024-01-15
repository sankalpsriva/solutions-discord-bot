# from better_profanity import profanity
from model import ToxicityModel
class Attributes:
    def __init__(self):
        self.model = ToxicityModel() 
        self.attrs: list = None 
        self.attrs_dictionary: dict = {}
        self.message = ""
    
    def set_attributes(self, message: str): 
        self.message = message
        self.attrs = self.model.get_analysis(message)
    
    def get_raw_attributes(self) -> list[float]: 
        return list(self.attrs)
    
    def set_attrs_dictionary(self):
        if self.attrs is not None:
            keys, values = self.model.get_df().columns[2: ], self.attrs
            
            for i in range(len(keys.values)): 
                self.attrs_dictionary[keys.values[i]] = values[i]

            return self.attrs_dictionary
        raise BaseException("Message attributes have not be initalized call set_attributes(message)")  
    
    def get_attrs_dictionary(self): 
        if self.attrs_dictionary is not {}:
            return self.attrs_dictionary
        raise BaseException("attrs_dictionary has not been initalized call set_attrs_dictionary()")
            
    def get_avg_toxicity_strength(self): 
        # get average between toxicity and severe toxicity as a percentage
        return ((self.attrs[0] + self.attrs[1]) / 2) * 100
    
    def get_obscenity_strength(self): 
        return self.attrs[2] * 100
    
    def get_threat_strength(self): 
        return self.attrs[3] * 100
        
    def get_insult_strength(self): 
        return self.attrs[4] * 100
    
    def get_identity_hate_strength(self): 
        return self.attrs[5] * 100
    
    def get_max_score(self): 
        if self.attrs_dictionary is not {}: 
            return max(self.attrs_dictionary.values()) * 100
        raise BaseException("attrs_dictionary has not been set, must call set_attrs_dictionary")

    def get_current_message(self): 
        return self.message
    
    def log_message(self):
        with open("sents.txt", "a") as file:
        #     file.write(f"Message: {self.message}, Attributes: {self.get_attrs_dictionary()}, Max Toxicity Score: {self.get_max_score()}\n")
            file.write(self.message + '\n')
             
        
    