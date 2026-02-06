# Conversational Knowledge Bot

* This bot is able to answer the user's questions by looking up the web through duckduckgo search api which results in providing factual answers. 

* It is also able to remember the previous messages of a conversation and provide answers for the follow up questions.

## Architecture
![architecture diagram](./Conversational\ knowledge\ bot\ diagram.png)

## Tools used
* langchain
* langgraph
* duckduckgo-search


## How to run the project
* **Step 1:** clone this repo

```bash
git clone git@github.com:Manideep0905/Soulpage-genai-assignment-manideep.git
```
***
<br>

* **Step 2:** Ensure uv is installed and run
```bash
uv add -r requirements.txt
```
***
<br>

* **Step 3:** Here we are using a local model to answer the user's questions. This eliminates the need to use an api key for a model and it is free

>Make sure [ollama](https://ollama.com/download) is installed and run the following command:
```bash
ollama pull llama3.2:3b
```
***
<br>

* **Step 4:** Now run
```bash
streamlit run app.py
```

## Sample chat logs
**User:** Who is the CEO of nvidia?

**Bot:** 
