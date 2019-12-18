# [X] criar classe abstrtata cliente que vai ser herdada pelo cliente fisico e cliente juridico
# [X] na classe cliente so vai ter o nome em comum e tb a data de cadastro
# [X] na ddata de cadastro inserir um campo instring e vai converter para um tipo date
# [X] na hora de inserir o cpf vai precisar validar se o cpf é real ou não msma coisa para o cnpj
# [X] caso n seja valido lançar um exceção de erro personalizado "cpf n é valido"
# [X] o nome so pode conter letras e espaço em branco.

from cliente_fisico import ClienteFisico
from cliente_juridico import ClienteJuridico


cf = ClienteFisico('davVid', '10/02/2018', '060.433.835-00', 'm')
cj = ClienteJuridico('max', '10/01/2018', '11.444.777/0001-61')

print(cf.nome, type(cf.data_cadastro), cf.cpf, cf.sexo)
print(cj.nome, type(cj.data_cadastro), cj.cnpj)

