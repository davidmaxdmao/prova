from abc import ABC
from abc import abstractmethod
from datetime import datetime
import re

class Cliente(ABC):

    @abstractmethod
    def __init__(self, nome, data_cadastro):
        self.nome = nome
        self.data_cadastro = data_cadastro

    @property
    def nome(self):

        return self._nome

    @nome.setter
    def nome(self, nome):

        #verifica se o nome só possui letras ou espaços em branco
        result = re.findall('[0-9-+=*&$#@!/\|%§?;.:_,ªº°{}()[\]]', nome)
        if result:
            raise ValueError('O nome não pode conter números ou caracteres especiais ')
        else:
            self._nome = nome

    @property
    def data_cadastro(self):

        return self._data_cadastro

    @data_cadastro.setter
    def data_cadastro(self, data_cadastro):
        data_cadastro = datetime.strptime(data_cadastro, '%d/%m/%Y').date()
        self._data_cadastro = data_cadastro