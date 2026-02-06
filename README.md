# Conversational Knowledge Bot

* This bot is able to answer the user's questions by looking up the web through duckduckgo search api which results in providing factual answers. 

* It is also able to remember the previous messages of a conversation and provide answers for the follow up questions.

## Architecture
![architecture diagram](Conversational%20knowledge%20bot%20diagram.png)

## Tools used
* langchain
* langgraph
* duckduckgo-search


## How to run the project
* **Step 1:** clone this repo and cd into it

```bash
git clone https://github.com/Manideep0905/Soulpage-genai-assignment-manideep.git
```
***
<br>

* **Step 2:** Ensure uv is installed and run
```bash
uv sync
```
***
<br>

* **Step 3:** Activate your virtual environment

>If you are on linux/macos, run:
```bash
source .venv/bin/activate
```

>If you are on windows, run:
```bash
.venv\Scripts\activate
```
***
<br>

* **Step 4:** Here we are using a local model to answer the user's questions. This eliminates the need to use an api key for a model and it is free

>* Make sure [ollama](https://ollama.com/download) is installed and added to environment variables (if you are on windows):
>* Then run the command below
```bash
ollama pull llama3.2:3b
```
***
<br>

* **Step 5:** Now run
```bash
streamlit run app.py
```
