## Comandos para inicializar
- py -m venv myvenv
- .\myvenv\Scripts\activate
- pip install -r requirements.txt
- py main.py

## Objeto retornado a cada mensagem
 - id, 
 - channel=[id, name, position, nsfw, news, category_id] 
 - type=[author=[name, global_name, bot, nick], guild=[name, shard_id, chunked, member_count]] 
 - flags=[value]>