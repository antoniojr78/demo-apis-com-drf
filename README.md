# Contruindo APIs com Django Rest Framework / Building APIs with Django Rest Framework
Demonstração de API back-end em Django Rest Framework para ser consumida por front-ends:  

* [React + Bootstrap + Axios](https://github.com/antoniojr78/demo-apis-com-drf-react-ui)  
* [Vue + Bootstrap + Axios](https://github.com/antoniojr78/demo-apis-com-drf-vue-ui)  
* [Angular + Materialize](https://github.com/antoniojr78/demo-apis-com-drf-angular-ui)

1. Clone o repositório / Clone the repository: 
```bash
$ git clone -b develop https://github.com/antoniojr78/demo-apis-com-drf.git  
$ cd demo-apis-com-drf
```  

2. Criar ambiente virtual e ativar / Create virtual environment and activate: 
```bash
demo-apis-com-drf $ virtualenv -p /usr/bin/python3.6 venv  
demo-apis-com-drf $ . venv/bin/activate
(venv) demo-apis-com-drf $ 
```  

3. Instalar requerimentos do Projeto / Install Project requirements: 
```bash
(venv) demo-apis-com-drf $ pip install -r requirements.txt
```  

4. Aplicar as migrações de banco de dados / Apply database migrations
```bash
(venv)~/demo-apis-com-drf$ python my_project/manage.py migrate
```
5. Criar Super Usuário do Admin do Django / Create Django Admin Super User
```bash
(venv)~/demo-apis-com-drf$ python my_project/manage.py createsuperuser
```
6. Executar o Servidor Django / Run the Django server
```bash
(venv)~/demo-apis-com-drf$ python my_project/manage.py runserver
```  

7. São servidos os seguintes endpoints: / The following endpoints are served:  

http://localhost:8000/api/authors/  
http://localhost:8000/api/articles/  

Ainda temos nesse endpoint um exemplo de consumo da API com Django, Bootstrap e JQuery: /  
We still have in this endpoint an example of API consumption with Django, Bootstrap and JQuery:  

http://localhost:8000/