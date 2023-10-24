import os

from dotenv import load_dotenv

from langchain.llms import OpenAI

load_dotenv()

OPEN_API_KEY = os.environ.get("OPEN_API_KEY")

def main():
    llm = OpenAI(openai_api_key=OPEN_API_KEY)
    result = llm.predict("give me 5 business ideas")

    print(result)

    pass

if __name__ == "__main__":
    main()

