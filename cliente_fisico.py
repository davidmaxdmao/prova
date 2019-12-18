from cliente import Cliente
import re

class ClienteFisico(Cliente):

    def __init__(self, nome, data_cadastro, cpf, sexo):
        self.cpf = cpf
        self.sexo = sexo
        super().__init__(nome, data_cadastro)

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):

        # tira os pontos e o traço do cpf
        cpf = re.sub('[^0-9]', '', cpf)

        # pega os primeiros nove digitos do cpf
        novo_cpf = cpf[:9]


        # verifica se os 9 primeiros digitos são iguais
        sequencia = cpf[0] * len(novo_cpf)
        if sequencia == novo_cpf:
            raise ValueError('CPF invalido')

        # efetua a validação com base nos dois ultimos digitos, utilizando a função valida_cpf.
        cpf_validado = self.valida_cpf(novo_cpf)
        cpf_validado = self.valida_cpf(cpf_validado)

        if cpf == cpf_validado:
            self._cpf = cpf_validado
        else:
            raise ValueError('CPF invalido')



    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    def valida_cpf(self, cpf):


        soma = 0
        for chave, multiplicador in enumerate(range(len(cpf) + 1, 1, -1)):
            soma += int(cpf[chave]) * multiplicador

        resto = 11 - (soma % 11)
        resto = resto if resto <= 9 else 0
        novo_cpf = cpf + str(resto)

        return novo_cpf
