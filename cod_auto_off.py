
"""

- Para rodar um programa 24/7;

- Para fazer isso você precisa fazer um deploy(Implantar);

- Temos como opções: Config seu PC ligado, agendador de tarefas; Mas para isso há (Necessidade do PC estar ligado);

---------------------------------------------------------------------------------------

# Dessa forma não precisa que seu PC esteja ligado:

- Vamos utilizar um servidor: HEROKU - site: https://www.heroku.com/ - Criar uma conta

- Instalar o HEROKU CLI no seu Pc; (heroku --version)

- instalar o Git; (git --version)

- Fazer login no heroku pelo terminal: heroku login; 

- Criar arq externo: Procfile; 

- Verifica todas as lib instaladas do meu projeto: pip freeze ;

- Para criar arq automatico .txt contendo todas as lib: pip freeze > requirements.txt

---------------------------------------------------------------------------------------



"""

#----------------------------------------------------------------------------------


import requests # pip install requests

from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()
cot_bitcoin = requisicao_dic["BTCBRL"]["bid"]

print(f"Cotação atualizada!\nData: {datetime.now()}\nValor da cotação: R${cot_bitcoin}")


#----------------------------------------------------------------------------------

