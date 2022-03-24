from mailbox import NotEmptyError
from xml.dom import NoModificationAllowedErr


class Quarto: 

    def __init__(self, nome = " ", dimensoes = " "):
        self.nome = nome
        self.dimensoes = dimensoes

    def __repr__(self):
        x = self.nome + ',' + self.dimensoes
        return x
        
class Mobilia:
    
    def __init__(self, nome = '', funcao = '', material = ''):
