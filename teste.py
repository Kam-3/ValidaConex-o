from google import genai

GOOGLE_API_KEY = "COLOQUE_SUA_CHAVE_AQUI"

def validar_conexao():
    try:
        client = genai.Client(api_key=GOOGLE_API_KEY)

        print("Testando conexão com a API do Gemini...")
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents="Responda apenas com a palavra: 'Conectado!'"
        )
        
        if response.text:
            print(f"Sucesso! Retorno da API: {response.text}")
            return True
            
    except Exception as e:
        print(f"Erro ao conectar na API: {e}")
        return False

if __name__ == "__main__":
    validar_conexao()