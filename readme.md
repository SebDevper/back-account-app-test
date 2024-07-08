para hacerlo funcionar en local:

source env/bin/activate
fastapi dev main.py

# Production tests:

## register
`https https://back-account-app-test.onrender.com/create-user/ user_name=waripolo user_email=waripolio@waripas.cl user_key=chocolate45`

## login
`https POST https://back-account-app-test.onrender.com/login/ user_email=waripolio@waripas.cl user_key=chocolate45`

## get accounts
`https https://back-account-app-test.onrender.com/get_accounts_by_bank/ token:soy_un_token`



# Local test:
## register
`
http POST http://127.0.0.1:8000/create-user/ user_name=waripolo user_email=waripolio@waripas.cl user_key=chocolate45
`
## login
`
http POST http://127.0.0.1:8000/login/ user_email=waripolio@waripas.cl user_key=chocolate45
`
## Get accounts
`
http http://127.0.0.1:8000/get_accounts_by_bank/ token:soy_un_token
`

TODO:
-api login
-api registro
-api listar bancos
-api listar cuentas según banco

# Source
https://dashboard.belvo.com/sandbox/

# Iinfo publicación

Publicado en render

revisar deploys:
https://dashboard.render.com/

# BD squalingo
https://dashboard.scalingo.com/
conectado a la app back-account-app-test

