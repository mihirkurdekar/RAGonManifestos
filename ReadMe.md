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
* [llama3.2](https://ollama.com/library/llama3.2) - llm runing in ollama, I got 3b version
* Python 3.11 - to run the code
* pip - to install dependencies





