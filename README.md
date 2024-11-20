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




