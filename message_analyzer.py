# from better_profanity import profanity
from model import ToxicityModel

class Attributes:
    def __init__(self):
        self.model = ToxicityModel() 
        self.attrs = None 
        self.attrs_dictionary = None
    
    def set_attributes(self, message: str): 
        self.attrs = self.model.get_analysis(message)
    
    def get_raw_attributes(self) -> list[float]: 
        return self.attrs
    
    def set_attrs_dictionary(self):
        if self.attrs:
            keys, values = self.model.get_df().columns[2: ], self.attrs
            self.attrs_dictionary = {keys, values}
            return self.attrs_dictionary
        raise "Message attributes have not be initalized call set_attributes(message)"  
    
    def get_attrs_dictionary(self): 
        if self.attrs_dictionary:
            return self.attrs_dictionary
        raise "attrs_dictionary has not been initalize call set_attrs_dictionary()" 
            
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

attrs = Attributes()
attrs.set_attributes("you fucking suck")
print(attrs.get_raw_attributes())
attrs.set_attrs_dictionary()
print(attrs.get_attrs_dictionary())