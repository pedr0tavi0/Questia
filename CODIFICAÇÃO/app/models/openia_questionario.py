import openai, re
from app.models.user import User

class OpeniaQuestionario:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.gerar_perguntas_cache = {}

    def gerar_perguntas(self, tema):
        messages = [
            {"role": "system", "content": f"Você será um assistente que ira gerar  questões  cada uma com 4 alternativas, a,b,c e d, dependendo do {tema} . gerando sozinho apenas com o tema escolhido nada mais"},
            {"role": "user","content":f"o {tema} escolhido , gere 5 perguntas" }
        ]
        perguntas_cache = {}
        if tema in perguntas_cache:
            return perguntas_cache[tema] 
        else:
             while True:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    max_tokens=400,
                )
                # Extrair as perguntas do texto de resposta
                perguntas_text = response.choices[0].message.content

                # Remover os "** **" do texto
                perguntas_text = perguntas_text.replace("**", "")

                # Separar as perguntas em uma lista
                perguntas_separadas = []
                perguntas = perguntas_text.split("\n\n")
                for pergunta in perguntas[1:-1]:  # Remover a primeira e a última tupla
                    partes = pergunta.split('\n')
                    if len(partes) < 5:
                        continue
                    texto_pergunta = partes[0]
                    opcoes_resposta = partes[1:5]
                    perguntas_separadas.append((texto_pergunta, opcoes_resposta))

                # Verificar se exatamente 5 perguntas foram geradas
                if len(perguntas_separadas) == 5:
                    self.gerar_perguntas_cache[tema] = perguntas_separadas
                    return perguntas_separadas
    


    def obter_respostas_chat(self, tema):
        perguntas_originais = self.gerar_perguntas_cache.get(tema)
        print(f"Perguntas originais dentro da obter chat: {perguntas_originais}")
        
        if not perguntas_originais:
            return None

        messages = [
            {"role": "system", "content": f"Você será um assistente que responderá o questionário de {tema}. Forneça a resposta correta para cada pergunta."},
            {"role": "user", "content": "\n\n".join([f"{pergunta[0]}\n{', '.join(pergunta[1])}" for pergunta in perguntas_originais])}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=400
        )

        respostas_chat = response.choices[0].message.content.replace('\n', ' ').split("\n\n")
        print(f"Respostas do chat: {respostas_chat}")
    
        
        return respostas_chat






            
  


    
    def verificar_respostas(self, respostas_submetidas, respostas_corretas, username):
        resultados = []
        acertos = 0

        print(f"Respostas submetidas: {respostas_submetidas}")
        print(f"Respostas corretas: {respostas_corretas}")

        
        

        string_respostas = respostas_corretas[0]

       
        questoes = re.split(r'\d+\.\s', string_respostas)
    
    # Remover entradas vazias
        questoes = [q for q in questoes if q.strip()]

    # Lista para armazenar as respostas corretas    
        respostas_corretas_divididas = []

        # Iterar sobre as questões encontradas e adicionar à lista
        for questao in questoes:
            if 'Resposta:' in questao:
            # Dividir pela palavra "Resposta:" para pegar a parte correta
                partes = questao.split('Resposta:')
                pergunta = partes[0].strip()
                resposta = partes[1].strip()
            else:
                # Caso normal
                if ' ' in questao:
                    alternativa = questao.split(' ', 1)[0].strip()
                    resposta = questao.split(' ', 1)[1].strip()
                    resposta = f"{alternativa} {resposta}"
            
            respostas_corretas_divididas.append(resposta)

        print(f"Respostas corretas divididas: {respostas_corretas_divididas}")

    # Iterar sobre as questões encontradas e adicionar à lista
       
        for resposta_correta, (pergunta_submetida, resposta_submetida) in zip(respostas_corretas_divididas, respostas_submetidas.items()):
            print(f"Resposta correta: {resposta_correta}")
            print(f"Pergunta submetida: {pergunta_submetida}")
            print(f"Resposta submetida: {resposta_submetida}")

            # Extraindo apenas o conteúdo da resposta correta e da resposta submetida
            try:
            # Remover pontuação das respostas para comparar corretamente
                resposta_correta_contenido = re.sub(r'[^\w\s]', '', resposta_correta[resposta_correta.index(")")+2:].strip())
                resposta_submetida_contenido = re.sub(r'[^\w\s]', '', resposta_submetida[resposta_submetida.index(")")+2:].strip())

                # Verificando se a resposta submetida é correta
                acertou = resposta_submetida_contenido.lower() == resposta_correta_contenido.lower()
            except ValueError as e:
                # Caso ocorra um erro na extração, marcar como incorreta
                print(f"Erro ao extrair a resposta: {e}")
                acertou = False

            resultados.append((pergunta_submetida, resposta_submetida, resposta_correta, acertou))

            if acertou:
                acertos += 1

        print(f"Resultados: {resultados}")
        print(f"Acertos: {acertos}")

        user = User.query.filter_by(username=username).first()

        # Calcula a pontuação total baseada nos acertos
        pontos = acertos

        # Atualiza os pontos do usuário no banco de dados
        user.atualizar_pontos(pontos)

        return resultados, acertos



        
