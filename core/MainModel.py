from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

import markdown
#from GatherData import GetData

class Model():

    #def __init__(self):
        #self.llm = OllamaLLM(model = "gemma3n")
        #self.obj = GetData()
        #self.q1 = self.obj.get_data()

    def model(self, q1:dict) -> dict:
        llm = OllamaLLM(model = "gemma3n")

        template = """You are a literature and language specialist. I will provide you with articles and your job is to do two things:
        1. Summarize the article. Ensure it is clear, concise, and captures the key points. The summary must be shorter than the original article and suitable for a busy reader to grasp in under a minute.
        2.Create a relevant and engaging headline for the summarized article.

        Important instructions:
        Write the headline in bold and positioned before the summary.
        Write the summary in the first-person perspective, as if you are the original author.
        Do not include any introductions, closing statements, or comments like "I'm ready", "I hope this helps", "Please provide the article", etc.
        Only output the headline, followed by the summary. Nothing else.
        Question: {question}"""

        key = list(q1.keys())

        prompt = PromptTemplate(input_variables=['question'], template=template)
        chain = prompt | llm
        
        for i in key:
            
            response = chain.invoke({'question' : q1[i]})
            html_text = markdown.markdown(response)
            q1[i] = f"<div style='font-size:20px;'>{html_text}</div>"

        return q1

#obj1 = Model()
#obj1.model()