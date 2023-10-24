import os

from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Language(BaseModel):
    released: str = Field(description="Year released.")
    creator: str = Field(description="Name of creator.")
    summary: str = Field(description="Short summary")


load_dotenv()

OPENAI_MODEL = os.getenv("OPENAI_MODEL", default="gpt-3.5-turbo")
OPENAI_API_KEY = os.environ.get("OPEN_API_KEY")

PROMPT_LANGUAGE_INFO = """
    Provide a 2 to 3 sentence summary about the programming language {language}.
    {format_instructions}
"""

def main():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model=OPENAI_MODEL)
    parser = PydanticOutputParser(pydantic_object=Language)

    language = input("Enter the name of a programming language: ")

    messages = []
    messages.append(HumanMessagePromptTemplate.from_template(template=PROMPT_LANGUAGE_INFO))
    chatPrompt = ChatPromptTemplate.from_messages(messages=messages)
    chatPromptWithValues = chatPrompt.format_prompt(language=language, format_instructions=parser.get_format_instructions())

    result = llm(chatPromptWithValues.to_messages())
    parsedResult = parser.parse(result.content)
    print(parsedResult)

if __name__ == "__main__":
    main()

