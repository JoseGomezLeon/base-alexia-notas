import os
from openai import OpenAI


def get_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analizar_error(error, contexto=""):
    try:
        client = get_client()

        prompt = f"""
        Eres un experto en testing automatizado con Playwright.

        Error:
        {error}

        Contexto:
        {contexto}

        Explica en pocas palabras la posible causa del error y una sugerencia.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error IA: {str(e)}"