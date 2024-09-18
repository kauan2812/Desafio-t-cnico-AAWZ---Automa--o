from Etapa1.calculoDeComissoes import CalculoDeComissoes
from Etapa1.validacaoDePagamentos import validarPagamentos
from Etapa2.analiseDeContrato import analiseDeContrato

print('Calculo de Comissoes')
print(CalculoDeComissoes('Vendas.xlsx'))
print('-' * 60)
print('Validacao de Pagamentos')
print(validarPagamentos('Vendas.xlsx'))
print('-' * 60)
print('Analise de Contrato de Partnership')
print(analiseDeContrato('Partnership.docx'))

