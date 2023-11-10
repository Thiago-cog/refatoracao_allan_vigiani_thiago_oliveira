import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class ZdgBot:
    def __init__(self, json):
        self.json = json
        self.dictMessages = json["data"]
        self.ultraAPIUrl = os.getenv('API_URL')
        self.token = os.getenv('TOKEN')

    def send_requests(self, type, data):
        url = f"{self.ultraAPIUrl}{type}?token={self.token}"
        headers = {"Content-type": "application/json"}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, chatID, text):
        data = {"to": chatID, "body": text}
        answer = self.send_requests("messages/chat", data)
        return answer

    def to_participate_ZDG(self, chatID):
        message = "Na *Comunidade ZDG* você vai integrar APIs, automações com chatbots e sistemas de atendimento multiusuário para whatsapp. Com *scripts para copiar e colar e suporte todos os dias no grupo de alunos*.\n\nhttps://comunidadezdg.com.br/ \n\n*⏱️ As inscrições estão ABERTAS*\n\nAssista o vídeo abaixo e entenda porque tanta gente comum está economizando tempo e ganhando dinheiro explorando a API do WPP, mesmo sem saber nada de programação.\n\n📺 https://www.youtube.com/watch?v=AoRhC_X6p5w"
        return self.send_message(chatID, message)

    def gift_ZDG(self, chatID):
        message = "Na Comunidade ZDG, você vai:\n\n- Utilizar códigos já testados para automatizar seu atendimento com chatbots no whatsapp\n- Criar e aplicativos para gestão de CRM e plataformas multiusuários para chats de atendimento\n- Aprender integrações com ferramentas e APIs que já foram testadas e aprovadas pela comunidade\n- Curadoria de plugins e ferramentas gratuitas para impulsionar o marketing de conversa no seu negócio\n- Se conectar a mais de 2.000 alunos que também estão estudando e implementando soluções de marketing de conversa\n- Grupo de alunos organizado por tópicos\n- Ter acesso ao meu suporte pessoal todos os dias"
        return self.send_message(chatID, message)

    def send_audio(self, chatID):
        data = {
            "to": chatID,
            "audio": "https://file-example.s3-accelerate.amazonaws.com/audio/2.mp3",
        }
        answer = self.send_requests("messages/audio", data)
        return answer
    
    def technologies_and_tools(self, chatID):
        message = "Essas são as principais APIs que a ZDG vai te ensinar a usar com o WhatsApp:\nBaileys, Venom-BOT, WPPConnect, WPPWeb-JS e Cloud API (Api Oficial)\n\n*Essas são as principais integrações que a ZDG vai te ensinar a fazer com o WhatsApp:*\nBubble, WordPress (WooCommerce e Elementor), Botpress, N8N, DialogFlow, ChatWoot e plataformas como Hotmart, Edduz, Monetizze, Rd Station, Mautic, Google Sheets, Active Campaing, entre outras."
        return self.send_message(chatID, message)

    def about_api(self, chatID):
        about_api = "*NOME CONTATO*, " + "aproveite o conteúdo e aprenda em poucos minutos como colocar sua API de WPP no ar, gratuitamente:\r\n\r\n🎥 https://youtu.be/sF9uJqVfWpg"
        return self.send_message(chatID, about_api)

    def send_schedule(self, chatID):
        data = {
            "to": chatID,
            "audio": "https://zdg-bot.s3.amazonaws.com/indice.pdf",
        }
        answer = self.send_requests("messages/document", data)
        return answer

    def success_cases(self, chatID):
        success_cases_message = "*NOME CONTATO*, " + ", que ótimo, vou te enviar alguns cases de sucesso:\n\n📺 https://youtu.be/KHGchIAZ5i0\nGustavo: A estratégia mais barata, eficiente e totalmente escalável.\n\n📺 https://youtu.be/S4Cwrnn_Llk\nNatália: Nós aumentamos o nosso faturamento e vendemos pra mais clientes com a estratégia ZDG.\n\n📺 https://youtu.be/XP2ns7TOdIQ\nYuri: A ferramenta me ajudou muito com as automações da minha loja online.\n\n📺 https://youtu.be/KBedG3TcBRw\nFrancisco: O Pedrinho pega na nossa mão. Se eu consegui, você também consegue.\n\n📺 https://youtu.be/L7dEoEwqv-0\nBruno: A Comunidade ZDG e o suporte do Pedrinho são incríveis. Depois que eu adquiri o curso eu deixei de gastar R$300,00 todo mês com outras automações.\n\n📺 https://youtu.be/StRiSLS5ckg\nRodrigo: Eu sou desenvolvedor de sistemas, e venho utilizando as soluções do Pedrinho para integrar nos meus sistemas, e o ganho de tempo é excepcional.\n\n📺 https://youtu.be/sAJUDsUHZOw\nDarley: A Comunidade ZDG democratizou o uso das APIs do WPP.\n\n📺 https://youtu.be/S4Cwrnn_Llk\nNatália: Nós aumentamos o nosso faturamento e vendemos pra mais clientes com a estratégia ZDG.\n\n📺 https://youtu.be/crO8iS4R-UU \nndré: O Pedrinho compartilha muitas informações na Comunidade ZDG.\n\n📺 https://youtu.be/LDHFX32AuN0\nEdson: O retorno que tenho no meu trabalho com as informações do Pedrinho, fez o meu investimento sair de graça.\n\n📺 https://youtu.be/F3YahjtE7q8\nDaniel: Conteúdo de muita qualidade. Obrigado, professor Pedrinho.\n\n📺 https://youtu.be/YtRpGgZKjWI\nMarcelo: Tenho uma agência digital e com o curso do Pedrinho nós criamos um novo produto e já estamos vendendor.\n\n📺 https://youtu.be/0DlOJCg_Eso\nKleber: O Pedrinho tem uma didática excelente e com o curso dele, consegui colocar minha API para rodar 24 horas e estou fazendo vendas todos os dias.\n\n📺 https://youtu.be/rsbUJrPqJeA\nMárcio: Antes de adquirir eu tinha pouco conhecimento, mas consegui aprender muito sobre API com o Pedrinho e o pessoal da comunidade.\n\n📺 https://youtu.be/YvlNd-dM9oo\nZé: O Pedrinho tem um conteúdo libertador. Foi o melhor investimento que eu fiz. Conteúdo surreal.\n\n📺 https://www.youtube.com/watch?v=mHqEQp94CiE\nLéo: Acoplamos o Método ZDG aos nossos lançamento e otimizamos os nossos resultados.\n\n📺 https://youtu.be/pu6PpNRJyoM\nRenato: A ZDG é um método que vai permitir você aumentar o seu faturamento em pelo menos 30%.\n\n📺 https://www.youtube.com/watch?v=08wzrPorZcI\nGabi: Implementei a estratégia sem saber nada de programação\n\n📺 https://youtu.be/10cR-c5rOKE\nDouglas: Depois de implementar as soluções do Pedrinho eu tive um aumento de 30% no meu faturamento, sem contar que na comunidade ZDG todos se ajudam.\n\n📺 https://youtu.be/kFPhpl5uyyU\nDanielle: Sem sombra de dúvida ter conhecido o Pedrinho e o seu conteúdo foi a melhor coisa que aconteceu comigo.\n\n📺 https://youtu.be/3TCPRstg5M0\nCalebe: O sistema Zap das Galáxias foi fundamental na elaboração e na execução das estratégias do meu negócio.\n\n📺 https://youtu.be/XfA8VZck5S0\nArtur: As soluções da comunidade me ajudaram muito a aumentar as minhas vendas e a interagir com os meus clientes de maneira automática. O suporte é incrível.\n\n📺 https://youtu.be/4M-P3gn9iqU\nSamuel: A Comunidade ZDG tem muito conteúdo legal, que da pra você utilizar no seu dia a dia pra meios profissionais. Depois que aprendi o método, nunca mais tive bloqueios."
        return self.send_message(chatID, success_cases_message)

    def about_the_duo(self, chatID):
        aboutTheDuo = "O trabalho foi feito pela dupla composta por Allan Vigiani e Thiago de Oliveira Santos, alunos do 7º período de Engenharia de Software pela Universidade de Vassouras - Maricá."
        return self.send_message(chatID, aboutTheDuo)
    
    def welcome(self, chatID, firstMessage=False):
        welcomeString = ""
        if firstMessage == False:
            welcomeString = "*COMUNIDADE ZDG*\n\n🤪 _Usar o WPP de maneira manual é prejudicial a saúde_\r\n\r\nhttps://comunidadezdg.com.br/ \r\n\r\n⏱️ As inscrições estão *ABERTAS* \r\n\r\n Esse é um atendimento automático, e não é monitorado por um humano. Caso queira falar com um atendente, escolha a opção 4. \r\n\r\nEscolha uma das opções abaixo para iniciarmos a nossa conversa: \r\n\r\n*[ 1 ]* - Quero garantir minha vaga na Comunidade ZDG. \r\n*[ 2 ]* - O que vou receber entrando para a turma da ZDG? \r\n*[ 3 ]*- Quais tecnologias e ferramentas eu vou aprender na comunidade ZDG? \r\n*[ 4 ]- Gostaria de falar com o Pedrinho, mas obrigado por tentar me ajudar.* \r\n*[ 5 ]*- Quero aprender como montar minha API de GRAÇA.\r\n*[ 6 ]*- Quero conhecer todo o conteúdo programático da Comunidade ZDG.\r\n*[ 7 ]*- Gostaria de conhecer alguns estudos de caso."
        else:
            welcomeString = "Esse é um atendimento automático, e não é monitorado por um humano. Caso queira falar com um atendente, escolha a opção 4. \r\n\r\nEscolha uma das opções abaixo para iniciarmos a nossa conversa: \r\n\r\n*[ 1 ]* - Quero garantir minha vaga na Comunidade ZDG. \r\n*[ 2 ]* - O que vou receber entrando para a turma da ZDG? \r\n*[ 3 ]*- Quais tecnologias e ferramentas eu vou aprender na comunidade ZDG? \r\n*[ 4 ]*- Gostaria de falar com o Pedrinho, mas obrigado por tentar me ajudar.* \r\n*[ 5 ]*- Quero aprender como montar minha API de GRAÇA.\r\n*[ 6 ]*- Quero conhecer todo o conteúdo programático da Comunidade ZDG.\r\n*[ 7 ]*- Gostaria de conhecer alguns estudos de caso."

        return self.send_message(chatID, welcomeString)

    def processRreceivedMessage(self):
        if self.dictMessages != []:
            message = self.dictMessages
            text = message["body"].split()
            if not message["fromMe"]:
                chatID = message["from"]
                if text[0].lower() == "oi":
                    return self.welcome(chatID)
                elif text[0].lower() == "1":
                    return self.to_participate_ZDG(chatID)
                elif text[0].lower() == "2":
                    return self.gift_ZDG(chatID)
                elif text[0].lower() == "3":
                    return self.technologies_and_tools(chatID)
                elif text[0].lower() == "4":
                    return self.about_api(chatID)
                elif text[0].lower() == "5":
                    return self.send_schedule(chatID)
                elif text[0].lower() == "6":
                    return self.success_cases(chatID)
                elif text[0].lower() == "7":
                    return self.about_the_duo(chatID)
                else:
                    return self.welcome(chatID, True)
            else:
                return "NoCommand"
