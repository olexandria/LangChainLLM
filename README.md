## Chatbot using LLM and LangChain 🦜️

This project aims to develop a chatbot that provides responses based on a dataset from Slack/Notion. The chatbot will use LLM (Language Model) and LangChain for query processing.

### Installation
- Clone the repository.
- Create a virtual environment: python -m venv env.
- Activate the virtual environment: source env/bin/activate (Linux/Mac) or env\Scripts\activate (Windows).
- Install the dependencies: pip install -r requirements.txt.
- Run the application: **uvicorn main:app --reload**
> Note: Add your OpenAI API Key in main.py before started running



### Endpoints
*The endpoint for adding a message.*

    POST /add_message
    Example: http://127.0.0.1:8000/add_message

*The endpoint for get the answer to your question.*

    POST /ask
    Example: http://127.0.0.1:8000/ask
