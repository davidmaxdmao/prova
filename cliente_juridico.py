from cliente import Cliente

class ClienteJuridico(Cliente):

    def __init__(self, nome, data_cadastro, cnpj):
        self.cnpj = cnpj
        Cliente.__init__(self, nome, data_cadastro)


    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = cnpj