# RAG agents for analyzing election manifestos

I wrote a [LinkedIn Article](https://www.linkedin.com/pulse/prompt-engineering-election-manifesto-mihir-kurdekar-jqgrf/?trackingId=pTmbyhtVTkCUjp93YI0%2BPw%3D%3D) explaining how we can leverage LLM and prompt engineering to check election manifestos.

I got a couple of election manifestos files for upcoming elections in Maharashtra state assembly elections.
I tried to RAG with chatGPT to get a summary of manifestos but ran into limit for the day after just 1 file.
So, I tried to do RAG with crew AI and locally installed ollama llama3.2 LLM, so I don't hit any limits. 
This code base will help you do RAG with AI agents on a document.


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

If you want to change LLM to something else just change the llm input for agents in file.


#### Sample output 

When I ran this script with MVA manifesto I got the following output in `markdown/mva.pdf`:


Extracting Key Insights from Maharashtra Politics Summary Report

As a renowned Political Analyst with a background covering Maharashtra politics, I will provide a detailed summary table with key insights into Governance, Economic Development, Social Welfare, and other crucial categories. This report aims to give voters a comprehensive understanding of the current state of affairs in Maharashtra.

**Governance:**

| Category | Key Insights |
| --- | --- |
| Leadership | Current CM Eknath Shinde faces opposition from Shiv Sena leader Aditya Thackeray, creating an unstable coalition government. |
| Policy Implementation | The government has implemented various policies, including a revised budget and a focus on infrastructure development. However, the effectiveness of these initiatives is yet to be fully assessed. |
| Transparency and Accountability | There have been concerns raised about the lack of transparency in government decision-making processes and the concentration of power in the hands of a few leaders. |

**Economic Development:**

| Category | Key Insights |
| --- | --- |
| Industrial Growth | Maharashtra has witnessed significant growth in the industrial sector, with key contributors being automotive and pharmaceutical industries. However, challenges persist in terms of infrastructure and workforce development. |
| Agriculture Sector | The agricultural sector faces significant challenges, including droughts, crop failures, and water scarcity, affecting farmers' livelihoods and food security. |
| Tourism and Infrastructure | Maharashtra's tourism industry has seen a decline due to limited infrastructure development and inadequate marketing efforts. |

**Social Welfare:**

| Category | Key Insights |
| --- | --- |
| Education | Despite improvements in literacy rates, Maharashtra still struggles with inadequate funding for schools and poor quality of education in rural areas. |
| Healthcare | The state's healthcare system faces significant challenges, including a shortage of medical professionals, outdated infrastructure, and limited access to healthcare services in rural areas. |
| Social Justice | There have been concerns raised about social injustice, particularly in the context of Dalit rights and women empowerment initiatives. |

**Environmental Conservation:**

| Category | Key Insights |
| --- | --- |
| Pollution Control | Maharashtra has made efforts to reduce pollution, including banning single-use plastics and implementing waste management systems. However, more needs to be done to address air and water pollution. |
| Forest Conservation | The state's forests are facing threats from deforestation, urbanization, and climate change, compromising biodiversity and ecosystem services. |

**Infrastructure Development:**

| Category | Key Insights |
| --- | --- |
| Transportation | Maharashtra has invested in upgrading its transportation infrastructure, including the development of new roads, highways, and public transportation systems. However, more needs to be done to address congestion and accessibility issues. |
| Urban Planning | The state's urban planning strategies have been criticized for prioritizing economic growth over social welfare and environmental sustainability. |

This summary report provides a snapshot of Maharashtra politics, highlighting key areas that require attention and improvement. It is essential for voters to stay informed about these issues to make informed decisions at the polls.


