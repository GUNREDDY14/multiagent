# agents.py
# OLD (⚠️ deprecated)
# from langchain.chat_models import ChatOpenAI

# NEW (✅ correct)
from langchain_openai import ChatOpenAI

from langchain.schema import HumanMessage, SystemMessage
import os

# Connect to LM Studio
os.environ["OPENAI_API_KEY"] = "lm-studio"

llm = ChatOpenAI(
    temperature=0,
    openai_api_base="http://192.168.0.192:1234/v1",
    openai_api_key="lm-studio",
    model="phi-3-mini-4k-instruct"
)

class CoderAgent:
    def generate_code(self, request_text):
        print("Coder is working on:", request_text)
        system_prompt = "You are a helpful Python programmer. Write clean and commented Python code for user requests."
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=request_text)
        ]
        try:
            response = llm.invoke(messages)
            return response.content
        except Exception as e:
            return f"⚠️ Error: {str(e)}"
