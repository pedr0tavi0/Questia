# Rede Social do Hackers do bem

Bem-vindo à nossa rede social exclusiva para hackers, entusiastas de segurança cibernética e programadores! Aqui, você pode aprender, compartilhar e colaborar com outros membros da comunidade.

## Funcionalidades Principais

### Perfis de Membros
- Cada membro tem um perfil personalizado.
- Adicione suas habilidades, interesses e experiência.
- Inclua links para blogs pessoais e redes sociais.

### Fóruns e Grupos
- Participe de discussões em fóruns temáticos.
- Crie grupos para explorar tópicos específicos.

### Biblioteca de Recursos
- Acesse artigos, tutoriais e vídeos relevantes.
- Contribua com seus próprios materiais.

### Desafios e CTFs
- Teste suas habilidades em desafios regulares.
- Explore categorias como criptografia e exploração de software.

### Eventos e Webinars
- Fique por dentro de eventos e conferências.
- Interaja com palestrantes e outros membros.

## Tecnologias Utilizadas

- Plataforma Web: Django ou Flask.
- Banco de Dados: PostgreSQL ou MySQL.
- Segurança: Implemente medidas robustas para proteger os dados dos usuários.

## Contato

Em caso de dúvidas ou sugestões, entre em contato com a equipe do projeto.

Divirta-se explorando a rede social e compartilhando conhecimento! 🚀🔐

## Requisitos para funcionamento do projeto

- 1º Baixar o repositório do github: Entre em uma pasta no seu sistema local, entre no cmd e coloque o seguinte comando git clone https://github.com/tbgbarros/PI_4SEM_2024.git
- 2º Ativar o arquivo .bat para ele criar uma virtualização: abra sua pasta onde foi clonado o repositório, encontre o arquivo virtualvenv2.0.bat e de dois clicks, ele automaticamente irá baixar os requerimentos e bibliotecas do projeto e criará a virtualização.
- 3º Abra o projeto no VSCODE e ative a venv: entre na pasta CODIFICAÇÂO pelo cmd do terminal, de os seguintes comandos C:PI_4SEM_2024\CODIFICAÇÃO>cd venv, C:PI_4SEM_2024\CODIFICAÇÃO\venv>cd Scripts, C: PI_4SEM_2024\CODIFICAÇÃO\venv\Scripts>activate. Assim sua venv será ativada, podendo retornar a pasta CODIFICAÇÂO.
- 4º Iniciar o projeto: entre na pasta codificação, e coloque o seguinte comando no cmd: pyton run.py.
- 5º Lembrando que para rodar o projeto precisamos de um banco ativado, para isso voce deve baixar o XAMPP, entrar no MYsql e criar o seguinte banco: flask_example. sua estrutura é a seguinte:
 > class User(db.Model, UserMixin):
 > id = db.Column(db.Integer, primary_key=True)
 > username = db.Column(db.String(64), index=True, unique=True)
 > password_encrypted = db.Column(db.LargeBinary)
 > hash = db.Column(db.String(44))  # Store the key as a base64 encoded string
- 6º Com o banco criado e ativado o projeto será alocado pelo servidor do xampp e rodara normalmente.

