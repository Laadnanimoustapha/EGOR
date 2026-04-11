import requests # for sending requests
import os 

PROMPT = """
First, summarize the provided text in 3 bullet points. 
Second, provide a short explanation of the overall meaning of the text.
Format your answer clearly.
"""

#---------------------------------------GEMINI---------------------------------#
def send_to_gemini (text:str) -> str :
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key : raise ValueError("GEMINI API KEY IS MESSING")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={api_key}"
    headers = {"Content-type":"application/json"}
    payload = {
        "contents":[{
            "parts":[{"text":f"{PROMPT}\n\nTEXT:\n{text}"}]
        }]
    }

    response = requests.post(url,json=payload,headers=headers)
    response.raise_for_status()
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

#---------------------------------------GROQ---------------------------------#

def send_to_groq(text:str) -> str :
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key: raise ValueError("GROQ_API_KEY IS MESSING")

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-type": "application/json"}
    payload = {
        "model": "openai/gpt-oss-120b",
        "messages":[
            {"role":"system","content": PROMPT},
            {"role":"user","content":text}
        ]
    }
    response = requests.post(url,json=payload,headers=headers)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

#---------------------------------------HUGGINGFACE🤗---------------------------------#
def send_to_hf_llama3(text : str) -> str :
    return send_to_huggingface(text,"meta-llama/Meta-Llama-3-8B-Instruct")

def send_to_hf_mistral(text : str) -> str :
    return send_to_huggingface(text,"mistralai/Mistral-7B-Instruct-v0.2")

def send_to_hf_zephyr(text : str) -> str :
    return send_to_huggingface(text,"HuggingFaceH4/zephyr-7b-beta")

def send_to_huggingface(text : str, hf_model_id : str) -> str :
    api_key = os.getenv("HUGGING_FACE_API_KEY")
    if not api_key : raise ValueError("HuggingFace api key is messing")

    url = f"https://api-inference.huggingface.co/models/{hf_model_id}"
    headers ={"Authorization": f"Bearer {api_key}","Content-type": "application/json" }
    payload = {
        "inputs":f"{PROMPT}\n\nTEXT :\n{text}"
    }

    response = requests.post(url,json=payload,headers=headers)
    response.raise_for_status()
    return response.json()[0]["generated_text"]



#-----------------------------------WHATER FALL LOGIC TO USE AI MODELS---------------------------------#
def get_summarize_and_explanation (text:str) -> dict :
    model_store = [
        {"name": "GEMINI 3 FLASH", "func":send_to_gemini},
        {"name": "GROQ", "func":send_to_groq},
        {"name": "Llama-3", "func":send_to_hf_llama3},
        {"name": "Mistral", "func":send_to_hf_mistral},
        {"name": "Zephyr", "func":send_to_hf_zephyr}
    ]

    for model in model_store :
        try:
            print(f"server is traying {model['name']}........ ")
            result = model["func"](text)
            return {
                        "status": "succes",
                        "model_used": model["name"],
                        "data" : result
                    }        
        except Exception as e :
            print(f"THE MODEL {model['name']} HASE FAILED DUE TO : {e} SWETCHING TO THE NEXT MODEL")
            continue
    raise ValueError("ALL MODELS ARE CURRENTLY DOWN OR MESSING API")