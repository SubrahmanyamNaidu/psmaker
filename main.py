from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain_openai import ChatOpenAI

import json 
from dotenv import load_dotenv
load_dotenv()


# Load the JSON file containing topics
def load_topics(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def create_prompt_template():

     prompt=ChatPromptTemplate.from_template("""
          "You are a beginner who has just learned about the topic \"{topic}\". "
               "Explain it in a simple, clear, and engaging manner as if you're sharing your understanding with a friend who is new to this topic. "
               "\n\n1. Start by introducing the topic and why it’s important."
               "\n2. Explain the key concepts in detail with examples from the real world."
               "\n3. Conclude with a summary and suggest why someone should learn this topic.\n\nTopic: \"{topic}\""
     """)

     return prompt

def generate_explanations(topics):

     prompt=create_prompt_template()
     llm=ChatOpenAI(model="gpt-4o")

     output_parser=StrOutputParser()

     chain=prompt|llm|output_parser
     topic_number=1
     explations ={}
     for topic_entry in topics:
         topic=topic_entry['topic']
         explation=chain.invoke({"topic":topic})
         explations[f'topic-{topic_number}']={topic:explation}
         topic_number+=1

     return explations


# Save the output to a file
def save_explanations(output_path, explanations):
    with open(output_path, 'w') as f:
        json.dump(explanations, f, indent=4)


# Main function
if __name__ == "__main__":
    # Input JSON file with topics
    topics_file = "topics.json"
    output_file = "explanations.json"
    
    topics = load_topics(topics_file)
    explanations = generate_explanations(topics)
    save_explanations(output_file, explanations)
    print(f"Explanations saved to {output_file}")