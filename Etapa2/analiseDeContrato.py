import re
import docx
import pandas as pd

def readDocx(filePath):
    doc = docx.Document(filePath)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)

def extractPartnersInfo(text):
    pattern = r"(\d+\.\s)([\w\s]+),.*detentor[oa] de (\d+) cotas"
    matches = re.findall(pattern, text)

    partners = []
    for match in matches:
        name = match[1].strip()
        quotas = int(match[2])
        partners.append({'Nome': name, 'Cotas': quotas})
    
    return partners
  
def analiseDeContrato(filePath):
  
  text = readDocx(filePath)

  partnersInfo = extractPartnersInfo(text)

  df = pd.DataFrame(partnersInfo)

  return df
