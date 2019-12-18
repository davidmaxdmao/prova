from cliente import Cliente
from pycpfcnpj import cpfcnpj

class ClienteJuridico(Cliente):

    def __init__(self, nome, data_cadastro, cnpj):
        self.cnpj = cnpj
        Cliente.__init__(self, nome, data_cadastro)


    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj):

        if cpfcnpj.validate(cnpj):
            self._cnpj = cnpj
        else:
            raise ValueError('CNPJ invalido!')