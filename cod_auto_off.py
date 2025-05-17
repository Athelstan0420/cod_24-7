
"""

- Para rodar um programa 24/7;

- Para fazer isso você precisa fazer um deploy(Implantar);

- Temos como opções: Config seu PC ligado, agendador de tarefas; Mas para isso há (Necessidade do PC estar ligado);

---------------------------------------------------------------------------------------

# Dessa forma não precisa que seu PC esteja ligado:

- Vamos utilizar um servidor: HEROKU - site: https://www.heroku.com/ - (Criar uma conta)

- Instalar o HEROKU CLI no seu Pc; (heroku --version)

- instalar o Git; (git --version)

- Fazer login no heroku pelo terminal: heroku login; 

- Criar arq externo na pasta do projeto: Procfile (worker: /usr/bin/python /home/adriel/Documentos/24por7/cod_auto_off.py); 

- Verifica todas as lib instaladas do meu projeto: pip freeze;

- Para criar arq automatico .txt contendo todas as lib: pip freeze > requirements.txt (para add no heroku);

- Melhor utilizar o: pipreqs (pip install)

- depois, entre no diretorio do projeto pelo terminal e digite: pipreqs . --force

---------------------------------------------------------------------------------------

# Para criar seu repositório no heroku:

---------------------------------------------------------------------------------------

1. heroko login

2. entra na pasta que esta o seu projeto pelo terminal: cd /home/seu/projeto

3. no terminal dentro da pasta digite: git init (Para inciar)

4. Em seguida digite: heroku git:remote -a nomeapp.Ex.py 


---------------------------------------------------------------------------------------

# Etapas para atualizar seu projeto:

---------------------------------------------------------------------------------------
1. heroko login

2. adicionar todos os arquivos no git: git add .

3. git commit -am "Atualizando..."

4. git push heroku master

"""

#----------------------------------------------------------------------------------


import requests # pip install requests

from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()
cot_bitcoin = requisicao_dic["BTCBRL"]["bid"]

print(f"Cotação atualizada!\nData: {datetime.now()}\nValor da cotação: R${cot_bitcoin}")


#----------------------------------------------------------------------------------

