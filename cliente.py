from abc import ABC
from abc import abstractmethod
from datetime import datetime

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
        self._nome = nome

    @property
    def data_cadastro(self):

        return self._data_cadastro

    @data_cadastro.setter
    def data_cadastro(self, data_cadastro):
        data_cadastro = datetime.strptime(data_cadastro, '%d/%m/%Y').date()
        self._data_cadastro = data_cadastro