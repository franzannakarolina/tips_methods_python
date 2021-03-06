from bs4 import BeautifulSoup
import requests


# carrega pagina com informações sobre o clima
html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp").content

# faz parser no html da pagina
soup = BeautifulSoup(html, 'html.parser')

# captura dados navegando nos elementos do html
resume = soup.find(class_='-gray -line-height-24 _center')
tempMin = soup.find(id='min-temp-1')
tempMax = soup.find(id='max-temp-1')

# mostra resultados
print('\n Resumo: ' + resume.text)
print(' Temp. Mínima: ' + tempMin.string)
print(' Temp. Máxima: ' + tempMax.string)