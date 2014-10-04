Surgiu a necessidade de enviar alguns tweets via linha de comando (console) no linux, então nada melhor do que arregaçar as mangas e fazer um Script Python para resolver esse problema.

Para usar esse script você vai precisar instalar o Tweepy https://github.com/tweepy/tweepy

Outra dependência é a criação de um Twitter App, para isso acesse https://apps.twitter.com e clique em "Create New App". Basta preencher o formulário e submeter. Então você precisará do Consumer Key, Consumer Secret, Access Token e Access Token Secret. De posse dessas informações é só substituí-las por suas respectivas variáveis dentro do script.

Para executa-lo::

	$ python twitter.py 'Texto que você quer twitar'

Como eu tenho que enviar uns tweets em horários específicos eu coloquei o comando acima no cron e ficou tudo lindo :D

Dúvidas e Sugestões favor mandar um e-mail falecom@guilhermejr.net