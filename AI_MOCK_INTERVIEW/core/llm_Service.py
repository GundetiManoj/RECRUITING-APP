import openai
from utils.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def generate_completion(prompt: str, model: str = "gpt-3.5-turbo", max_tokens: int = 500, temperature: float = 0.7) -> str:
    """Generates a text completion using OpenAI's API."""
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error generating completion: {e}")
        return ""