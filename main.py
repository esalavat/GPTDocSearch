import os

from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)

load_dotenv()

OPENAI_MODEL = os.getenv("OPENAI_MODEL", default="gpt-3.5-turbo")
OPENAI_API_KEY = os.environ.get("OPEN_API_KEY")

PROMPT_LANGUAGE_INFO = """
    Provide a 2 to 3 sentence summary about the programming language {language}.
"""

def main():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model=OPENAI_MODEL)
    
    language = input("Enter the name of a programming language: ")

    messages = []
    messages.append(HumanMessagePromptTemplate.from_template(template=PROMPT_LANGUAGE_INFO))
    chatPrompt = ChatPromptTemplate.from_messages(messages=messages)
    chatPromptWithValues = chatPrompt.format_prompt(language=language)

    result = llm(chatPromptWithValues.to_messages())
    print(result)

if __name__ == "__main__":
    main()

