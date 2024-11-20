# RAG agents for political manifestos

I got a couple of election manifestos files for upcoming elections. I ran RAG to get a summary of manifestos.
I tried to do RAG with crew AI and locally installed ollama llama3.2 LLM.

## Hardware
Since we are doing everything locally the hardware component matters here.
I am working with following configuration:
* CPU - Apple M2 Pro chip
* GPU - comes embedded with processor
* Memory - 16 GB memory, I would recommend atleast 16 GB or more

In my experience this works best with Mac.
I have tried to run in Windows workstation we still get the output but process isn't as smooth.


## Prerequisites
You'll need following before starting 
* [Ollama](https://ollama.com/) - platform to deploy and manage LLMs locally
* [llama3.2](https://ollama.com/library/llama3.2) - llm runing in ollama, I got 3b version you can get higher if you have more memory available
* Python 3.11 - to run the code
* pip - to install dependencies
* Manifesto files for RAG

## Folder Structure

The project root has 2 python files which we will need for execution
```
RAGonManifestos
    |-- manifestos - this directory will have manifesto files to be processed
    |-- markdown - this directory will have result produced by RAG agent
    |-- convert_pdf_to_text.py - to convert pdf to text
    |-- manifesto_summary_workflow.py - main file to run the workflow
    |-- requirements.txt -- has list of all dependencies
    |-- README.md
```

## Run the project

### Download Manifest
I was able to get 2 manifest for 2024 Maharashtra Assembly elections 
* BJP: https://www.bjp.org/files/inline-documents/MANIFESTO-ENGLISH-2024-09-11-24_0.pdf 
* MVA: https://ugc.production.linktr.ee/2f64570e-38d5-4586-9e56-9a696775d789_MVA-Manifesto-English.pdf

Download these files and keep them in a directory called `manifestos` at project root.


### Convert pdf files to text
Since pdf files can't be processed directly we need to convert them to text format using `convert_pdf_to_text`
In the file you can see the path to pdf file at line 3 and path to save text file at line 7.
Edit the names as per you files and run script for all manifest files.
Once we have text files for all the manifesto files we are good to run AI agents.

### Run AI agent workflow 

I used [CrewAI](https://www.crewai.com/) as AI agent frameworks as it most easy to understand framework out there.
In my opnion crewAI is the best multi AI agent framework to get started quickly.

Before running this script make sure you local LLM working with ollama.

File `manifesto_summary_workflow.py` has the code written to initialize AI agents on text files and summarize the output in markdown.
You'll need to edit 2 lines before executing the script
* Line 19 has path to manifext text file
* Line 52 has path to output markdown file
Just verify these paths, and you can run the script.
  
You can see the output in markdown folder.




