---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rag-healthcare-use-cases/development.html
---

# Developing and orchestrating generative AI solutions for healthcare
<a name="development"></a>

To build the solutions in this guide, you must build a RAG architecture that uses fine-tuned LLMs to deliver augmented patient data, clinical and diagnostic insights, and predicted patient outcomes to healthcare providers. This requires the integration of multiple AWS services and tools to create a cohesive and efficient workflow. This section discusses the following:
+ [Amazon Q Developer](#development-amazon-q) – Use Amazon Q Developer to address engineering questions and code errors during the development process.
+ [Multi-retriever RAG design](#development-multi-retriever-rag) – Design and implement RAG solutions that use multiple retrievers to fetch the correct medical context for the user's question.
+ [ReAct agents](#development-react-agents) – Implement agents that combine reasoning with dynamic action.

## Amazon Q Developer
<a name="development-amazon-q"></a>

When building a generative AI solution, it can be difficult to create AI agents and the connect key services. However, [Amazon Q Developer](https://aws.amazon.com/q/developer/) helps data scientists and AI engineers by providing access to an advanced generative AI assistant. Amazon Q can quickly and accurately address user questions and code errors, which can help you optimize the LLM development process. Amazon Q offers significant advantages for developers creating applications that use Amazon Bedrock foundation models. It can streamline workflows and enhance code quality. It automates the generation of Python scripts and infrastructure as code (IaC) configurations, significantly reducing development time and effort. Through advanced refactoring capabilities, Amazon Q can improve code performance, identify security vulnerabilities, and make sure developers adhere to best practices. Additionally, it facilitates learning and adoption for beginners by providing context-aware suggestions and explanations, making complex coding tasks more accessible and efficient.

## Multi-retriever RAG design
<a name="development-multi-retriever-rag"></a>

In a generative AI application, a multi-retriever RAG pipeline can efficiently retrieve information from multiple data sources to help healthcare providers and clinicians answer medical questions. This pipeline uses different types of retrievers to pull relevant data from different knowledge bases. Each retriever is specialized in fetching a particular type of information, such as patient histories, diagnostic insights, clinical notes, or content from medical research and academic texts.

Use the nature of the data and the specific application requirements to determine what the correct backend knowledge base is correct for your use case. An Amazon OpenSearch Service vector database is well suited for large volumes of unstructured or semi-structured healthcare data, including image diagnosis assessment summaries, discharge summaries, clinical reports, medical research, and academic text content. On the other hand, a graph database service, such as Amazon Neptune, can be ideal for healthcare use cases that require deep exploration of the temporal relationships between entities, such as patient, patient history, healthcare provider, medicines, symptoms, and treatments.

A critical component of this pipeline is *user query intent prediction*. This makes sure that the system routes the query to the correct retriever chain. For example, if a clinician asks about a patient's treatment history, symptoms, interaction with the hospital, the likelihood of hospital re-admission, or potential patient outcomes, then the query intent prediction module identifies this intent. It directs the request to the retriever chain that can fetch patient records or chronological treatment data from the medical knowledge graph. Alternatively, if the question is about disease discovery, specific diagnostic assessments, or details of specific clinical procedures from academic textbooks, then the query is routed to the retriever chain that can fetch this information from the OpenSearch Service vector database. You can use the [tool-calling](https://python.langchain.com/docs/concepts/tool_calling/) functionality of LangChain to bind a custom tool to the Amazon Bedrock LLM that can classify a user question into predefined intents.

This multi-retriever RAG system includes LangChain agents that are designed to manage access to the specific knowledge base. You can use LangChain to orchestrate the interaction between the Amazon Bedrock LLM, the different retrievers, and tools. LangChain includes a tool-calling class that helps you create custom tools, such as an intent classifier, a retriever for Neptune, a retriever for OpenSearch Service, or any other tool that can be developed to classify the user intent and access data from a specific knowledge base in a structured format. You then feed these tools to the class to create a Reasoning and Acting (ReAct) agent. The ReAct agent processes the user question, plans the sequential steps  to answer the question, and then iteratively executes the available tools and processes the tool responses to finally answer the user query.

The following image shows how a multi-retriever RAG system that is designed for efficient knowledge retrieval and intelligent query resolution works. A LangChain ReAct agent analyzes the user's intent, formulates a structured plan for execution, and selects the most relevant retrieval tools. The system queries a previous questions cache and checks for similar queries based on key attributes, such as patient ID, medical condition, and visit date. If a highly similar question is found, the corresponding answer is retrieved directly. Otherwise, the agent executes the appropriate retriever. For retrieving patient-centric information, such as treatment history, symptoms, hospital interactions, or re-admission likelihood, the system uses a graph retriever. For diagnostic assessments, clinical procedures, and structured medical findings, the agent employs a vector database retriever. In scenarios that require a combination of contextual knowledge from both data stores, to generate a comprehensive response, the system uses a hybrid retrieval strategy that integrates results from both the knowledge graph and vector database.

![An architecture that uses multiple LangChain retrievers to perform Retrieval Augmented Generation.](http://docs.aws.amazon.com/prescriptive-guidance/latest/rag-healthcare-use-cases/images/guide-img/c2d53172-a932-4340-96f5-3132299b8691/images/db1d49c0-de1b-4a9d-bcb3-7d95acfec606.png)

## ReAct agents
<a name="development-react-agents"></a>

Reasoning and Acting (ReAct) agents are designed for multi-faceted RAG applications. These agents provide a powerful combination of reasoning and dynamic action, particularly for complex applications that involve step-by-step, logical information-retrieval workflows. For more information, see [ReAct: Synergizing Reasoning and Acting in Language Models](https://react-lm.github.io/).

In medical and healthcare contexts, queries from a clinician or doctor are often multi-faceted. For example, a clinician might ask "What treatments were given to similar patients with both hypertension and type 2 diabetes?" After identifying the user intent, which is to fetch the treatments for hypertension and type 2 diabetes, the AI agent needs to divide this query into subtasks and then choose the most efficient retrieval strategy. In this case, the AI agent should identify the most relevant nodes (such as patient age, sex, conditions, treatments, and medications) and then query the graph for these entities and their attributes and relationships. ReAct agents are very helpful because they combine the reasoning (logical inference) capability of an LLM with an action (querying or interacting with external resources or knowledge bases).

To answer the user query "What treatments were given to similar patients with both hypertension and type 2 diabetes?", the following example illustrates how a ReAct agent works:

1. **Agent** **reasoning** – The ReAct agent infers that the question involves retrieving information about conditions (diabetes and hypertension). It considers patient age, treatments, medications, and the period to analyze.

1. **Agent** **action** – The agent uses openCypher to query the knowledge graph for treatments that are specific to type 2 diabetes and hypertension. It also retrieves medications administered, dates of hospital visits, side effects of medications, known patient outcomes, and cross-reference data for similar patients (such as patients of the same gender and age).

1. **Agent observation** – From the knowledge graph, the agent retrieves the most recent six months of tabular data about treatments given to patients who have both hypertension and type 2 diabetes.

1. **Agent reasoning** – To rank the results from the retrieved records, the agent identifies important attributes, such as recency, side effects of medications, or known patient outcomes.

1. **Agent action** – The agent re-ranks the records based on identified attributes and pre-defined logic that is imparted through the system prompt.

1. **Response generation** – The LLM in** **Amazon Bedrock generates a response based on the context that the ReAct agent prepared.
