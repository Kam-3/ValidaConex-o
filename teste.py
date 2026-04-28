from google import genai

GOOGLE_API_KEY = "AIzaSyDort8NrJdJHcvSbrD8X_ZcxMRc48C8wKQ"

def iniciar_chat():
    try:
        client = genai.Client(api_key=GOOGLE_API_KEY)
        print("Chat com o Gemini iniciado, digite 'sair' para encerrar")

        while True:
            pergunta = input("\nVocê: ")

            if pergunta.lower() in ["Sair", "exit", "quit"]:
                print("Encerrando chat")
                break

            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=pergunta
            )

            print(f"Gemini: {response.text}")

    except Exception as e:
        print(f"Erro na conexão: {e}")

if __name__ == "__main__":
    iniciar_chat()

