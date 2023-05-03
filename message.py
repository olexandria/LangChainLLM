from datetime import datetime

from LLM import text_splitter
from schemas import Message


def add_message(request: Message, documents: list):
    message_dict = request.dict()
    message_dict["timestamp"] = datetime.timestamp(message_dict["timestamp"])
    if message_dict["thread_timestamp"] is not None:
        message_dict["thread_timestamp"] = datetime.timestamp(message_dict["thread_timestamp"])

    message_texts = text_splitter.create_documents([str(message_dict)])
    for i in range(len(message_texts)):
        documents.append(message_texts[i])

    return {"Successfully added!"}
