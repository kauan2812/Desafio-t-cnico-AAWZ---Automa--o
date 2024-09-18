import pandas as pd
import re

def removeSpecialCharacter(value):
    value = re.sub(r'[R$]', '', value).strip()
    value = re.sub(r'\.', '', value)
    value = re.sub(r',', '.', value)
    return float(value)
  

def calcSalesCommission(row):
  commission = 0.10 * int(removeSpecialCharacter(str(row['Valor da Venda'])))
  
  if (row['Canal de Venda'] == 'Online'):
    commission *= 0.8
  
  return commission


def calcSalesCommissionWithoutFee(row): 
  commission = 0.10 * int(removeSpecialCharacter(str(row['Valor da Venda'])))
  return commission


def calcManagerCommission(row):
  
  commission = int(row['Comissao'])
  
  if commission >= 1500:
    commission *= 0.9
    return commission
  
  return commission


def CalculoDeComissoes(filePath):
  
  doc = pd.read_excel(filePath)
  
  doc['Comissao'] = doc.apply(calcSalesCommission, axis=1)
  doc['Comissao Sem Taxa'] = doc.apply(calcSalesCommissionWithoutFee, axis=1)

  commissionPerPerson = doc.groupby('Nome do Vendedor')['Comissao'].sum().reset_index()
  commissionPerPersonWithoutFee = doc.groupby('Nome do Vendedor')['Comissao Sem Taxa'].sum().reset_index()
  
  commissionPerPerson['Comissao'] = commissionPerPerson.apply(calcManagerCommission, axis=1)

  totalCommissions = pd.merge(commissionPerPerson, commissionPerPersonWithoutFee, on='Nome do Vendedor')

  return totalCommissions
