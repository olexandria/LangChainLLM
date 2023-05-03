import json

from langchain import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

template = """You are given the data from Slack channels and article. 
Use the id to get the person's name and Slack channel's name.
Use the following pieces of context to answer the question at the end. 
The answer should be short, exact and specific.{context}
Q:{question}
A:"""
PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)


def load_documents():
    with open('data/article.txt') as f:
        article = f.read()
    texts = text_splitter.create_documents([article])

    with open('data/data1.json') as f1:
        slack = f1.read()

    sList = json.loads(slack)
    for i in range(len(sList)):
        sList[i] = str(sList[i]).replace("\'", "")
    slack_texts = text_splitter.create_documents([sList])

    for i in range(len(slack_texts)):
        texts.append(slack_texts[i])

    return texts


def get_answer(question, docs):
    chain = load_qa_chain(llm=OpenAI(model_name="text-davinci-003"), chain_type="stuff", prompt=PROMPT)
    query = question
    result = chain.run(input_documents=docs, question=query)
    return result
