import pandas as pd
from .calculoDeComissoes import CalculoDeComissoes

def validarPagamentos(filePath): 
  
  docPagamentos = pd.read_excel(filePath, sheet_name='Pagamentos')
  
  totalCommissions = CalculoDeComissoes(filePath)

  docPagamentos.rename(columns={'Comissão': 'Pagamento Efetuado'}, inplace=True)

  mergedDf = pd.merge(docPagamentos, totalCommissions, on='Nome do Vendedor')

  mergedDf['Diferença'] = mergedDf['Comissao'] - mergedDf['Pagamento Efetuado']

  pagamentosErrados = mergedDf[mergedDf['Diferença'] != 0]

  pagamentosReduzidos = pagamentosErrados[['Nome do Vendedor', 'Pagamento Efetuado', 'Comissao']]
  
  return pagamentosReduzidos
