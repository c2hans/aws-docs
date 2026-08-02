---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/what-is-rag.html
---

# Understanding Retrieval Augmented Generation
<a name="what-is-rag"></a>

Retrieval Augmented Generation (RAG) is a technique used to augment a large language model (LLM) with external data, such as a company's internal documents. This provides the model with the context it needs to produce accurate and useful output for your specific use case. RAG is a pragmatic and effective approach to using LLMs in an enterprise. The following diagram shows a high-level overview of how a RAG approach works.

![An orchestrator performs a semantic search on custom documents and then provides inputs to the LLM.](http://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/images/guide-img/22e94edd-d3e5-4e29-8c94-48e327306335/images/2dadb23f-cff6-4b90-9433-08c0d2e3d9cf.png)

Broadly speaking, the RAG process is four steps. The first step is done once, and the other three steps are done as many times as needed:

1. You create embeddings to ingest the internal documents into a vector database. *Embeddings* are numeric representations of text in the documents that capture the semantic or contextual meaning of the data. A *vector database* is essentially a database of these embeddings, and it is sometimes called a *vector store* or *vector index*. This step requires data cleaning, formatting, and chunking, but this is a one-time, upfront activity.

1. A human submits a query in natural language.

1. An orchestrator performs a similarity search in the vector database and retrieves the relevant data. The orchestrator adds the retrieved data (also known as *context*) to the prompt that contains the query.

1. The orchestrator sends the query and the context to the LLM. The LLM generates a response to the query by using the additional context.

From a user's perspective, RAG looks like interacting with any LLM. However, the system knows much more about the content in question and provides answers that are fine-tuned to the organization's knowledge base.

For more information about how a RAG approach works, see [What is RAG](https://aws.amazon.com/what-is/retrieval-augmented-generation/) on the AWS website.

## Components of production-level RAG systems
<a name="components"></a>

Building a production-level RAG system requires thinking through several different aspects of the RAG workflow. Conceptually, a production-level RAG workflow requires the following capabilities and components, regardless of the specific implementation:
+ **Connectors** — These connect different enterprise data sources with the vector database. Examples of structured data sources include transactional and analytical databases. Examples of unstructured data sources include object stores, code bases, and software as a service (SaaS) platforms. Each data source might require different connectivity patterns, licenses, and configurations.
+ **Data processing** – Data comes in many shapes and forms, such as PDFs, scanned images, documents, presentations, and Microsoft SharePoint files. You must use data processing techniques to extract, process, and prepare the data for indexing.
+ **Embeddings **— To perform a relevancy search, you must convert your documents and user queries into a compatible format. By using embedding language models, you convert the documents into numerical representation. These are essentially inputs for the underlying foundation model.
+ **Vector database** — The vector database is an index of the embeddings, the associated text, and metadata. The index is optimized for search and retrieval.
+ **Retriever** — For the user query, the retriever fetches the relevant context from the vector database and ranks the responses based on business requirements.
+ **Foundation model** — The foundation model for a RAG system is typically an LLM. By processing the context and the prompt, the foundation model generates and formats a response for the user.
+ **Guardrails** — Guardrails are designed to make sure that the query, prompt, retrieved context, and LLM response are accurate, responsible, ethical, and free of hallucinations and bias.
+ **Orchestrator** — The orchestrator is responsible for scheduling and managing the end-to-end workflow.
+ **User experience** — Typically, the user interacts with a conversational chat interface that has rich features, including displaying chat history and collecting user feedback about responses.
+ **Identity and user management** – It is critical to control user access to the application at fine granularity. In the AWS Cloud, policies, roles, and permissions are typically managed through [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

Clearly, there is significant amount of work to plan, develop, release, and manage a RAG system. [Fully managed services](rag-fully-managed.md), such as Amazon Bedrock or Amazon Q Business, can help you manage some of the undifferentiated heavy lifting. However, [custom RAG architectures](rag-custom.md) can provide more control over the components, such as the retriever or the vector database.
