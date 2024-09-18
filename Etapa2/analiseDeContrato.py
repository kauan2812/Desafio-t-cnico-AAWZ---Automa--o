import re
import docx
import pandas as pd

def readDocx(filePath):
    doc = docx.Document(filePath)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)

def extractFemalePartnersInfo(text):
    pattern = r"(\d+\.\s)([\w\s]+),.*detentor[a] de (\d+) cotas"
    matches = re.findall(pattern, text)

    partners = []
    for match in matches:
        name = match[1].strip()
        quotas = int(match[2])
        partners.append({'Nome': name, 'Cotas': quotas})
    
    return partners
  
def extractMalePartnersInfo(text):
    pattern = r"(\d+\.\s)([\w\s]+),.*detentor de (\d+) cotas"
    matches = re.findall(pattern, text)

    partners = []
    for match in matches:
        name = match[1].strip()
        quotas = int(match[2])
        partners.append({'Nome': name, 'Cotas': quotas})
    
    return partners
  
def analiseDeContrato(filePath):
  
  text = readDocx(filePath)

  femalePartnersInfo = extractFemalePartnersInfo(text)
  malePartnersInfo = extractMalePartnersInfo(text)

  dff = pd.DataFrame(femalePartnersInfo)
  dfm = pd.DataFrame(malePartnersInfo)
  
  df = pd.concat([dff, dfm])
  
  return df

print(analiseDeContrato('Partnership.docx'))