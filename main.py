from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()


prompt=ChatPromptTemplate.from_template("""
     "You are a beginner who has just learned about the topic \"{topic}\". "
            "Explain it in a simple, clear, and engaging manner as if you're sharing your understanding with a friend who is new to this topic. "
            "\n\n1. Start by introducing the topic and why it’s important."
            "\n2. Explain the key concepts in detail with examples from the real world."
            "\n3. Conclude with a summary and suggest why someone should learn this topic.\n\nTopic: \"{topic}\""
""")

llm=ChatOpenAI(model="gpt-4o")

output_parser=StrOutputParser()

chain=prompt|llm|output_parser

output=chain.invoke({"topic":"html basics"})

print(output)