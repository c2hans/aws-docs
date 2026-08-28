---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/writing-best-practices-rag/understanding.html
---

# Understanding LLMs and RAG
<a name="understanding"></a>

To understand how enhancing source document quality enhances the quality of a RAG response, you must understand the internal workings of an LLM. The true power of LLMs lies in their ability to use self-attention mechanisms and transformer architectures. These advanced techniques enable the models to effectively process and relate different parts of the input sequence, regardless of their position or distance within the text. This capability is a stark contrast to traditional language models, which often struggle with long-range dependencies and context understanding. Furthermore, LLMs are trained on an unprecedented scale. Some of the largest models are comprised of trillions of parameters and have ingested terabytes of textual data from diverse sources. This massive scale allows LLMs to develop a rich understanding of language, capturing subtle nuances, idioms, and contextual cues that were previously challenging for AI systems. The result is a class of models that can generate coherent and fluent text and demonstrate remarkable capabilities in tasks such as question answering, text summarization, and even code generation.

To use these models, we can turn to services such as [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), which provides access to a variety of foundation models from Amazon and third-party providers, including Anthropic, Cohere, and Meta. You can use Amazon Bedrock to experiment with state-of-the-art models, customize and fine-tune them, or incorporate them into your generative AI-powered solutions through a single API.

Although LLMs excel at capturing patterns and generating coherent text, they often lack access to up-to-date or specialized information. RAG combines the generative power of LLMs with a retrieval component that can access and incorporate relevant information from external sources, as part of the materialized LLM prompt. Examples of external sources include [Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) for Amazon Bedrock, intelligent search systems such as [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html), or vector databases such as [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html).

![The workflow of how a RAG-based application answers a user's query.](http://docs.aws.amazon.com/prescriptive-guidance/latest/writing-best-practices-rag/images/guide-img/287ab470-c0b9-440f-83c9-fae640906b4c/images/be62a373-43d0-461b-90c3-87e5a6f770ec.png)

The diagram describes the following workflow:

1. The user submits a query to the RAG application.

1. The RAG application queries a vector database that contains knowledge sources, such as documents, data, or media.

1. The RAG application retrieves the relevant information from the vector database based on semantic similarities between the query and stored documents.

1. The RAG application augments the original prompt with the retrieved context and sends it to the LLM endpoint.

1. The LLM endpoint generates a response and returns it to the RAG application.

1. The RAG application returns the generated response to the user.

At its core, RAG employs a two-stage process. In the first stage, a retrieval model identifies and retrieves relevant documents or passages based on the input query. This retrieval model can be a traditional information retrieval system, a dense retrieval model, or a combination of both. In the second stage, the retrieved information and the original query are fed into an LLM as a fully materialized prompt template. LLMs depend heavily on the quality of the source content delivered by the retriever component. They apply a self-attention mechanism to mathematically encode how the retrieved content relates to the task. The LLM then generates a response based on both the query and the retrieved information. In RAG, controlling the quality of the retrieved source documents represents a direct means of improving an LLM's internal representation of a task. RAG effectively augments the LLM's training data with relevant external data. This approach allows RAG to take advantage of the strengths of both LLMs and retrieval systems, enabling the generation of more accurate and informed responses that incorporate current and specialized knowledge.

## Vectors and embeddings
<a name="understanding-vectors-embeddings"></a>

Vectors and embeddings are fundamental concepts in machine learning and natural language processing. *Vectors* are mathematical objects that represent quantities that have both magnitude and direction. In the context of natural language processing (NLP), words, sentences, or documents are often represented as vectors in high-dimensional vector spaces. *Embeddings*, on the other hand, are a way to represent objects like words or documents in a lower-dimensional vector space where the relationships between the vectors capture semantic or syntactic similarities. Word embeddings, for instance, allow words with similar meanings to have similar vector representations. This helps algorithms to understand and process language more effectively.

## Vector databases
<a name="understanding-vector-databases"></a>

In generative AI, a *vector database* is a database that stores and manages vector representations of documents, queries, or other objects. It is designed to efficiently store and retrieve vectors. This supports fast and scalable operations such as semantic search and similarity matching. Vector databases index vectors by using specialized data structures, such as Hierarchical Navigable Small World (HNSW) graphs or K-Nearest Neighbors (KNN) algorithms. These data structures allow for fast nearest-neighbor searches, making it possible to quickly find similar vectors in the database.

## Semantic search
<a name="understanding-semantic-search"></a>

*Semantic search* is a technique that improves the relevance of search results by understanding the intent and context of the query, rather than just matching keywords. In technical terms, semantic search involves comparing the vector representations of the query and the documents in the database to find the most relevant matches. Different retrieval strategies can be used for semantic search, including but not limited to:
+ **HNSW** – A graph-based data structure that organizes vectors in a way that makes it efficient to search for nearest neighbors.
+ **KNN** – An algorithm that finds the K closest vectors to a query vector based on a distance metric, such as cosine similarity.
+ **Cosine similarity** – A measure of similarity between two non-zero vectors that measures the cosine of the angle between them. It is often used in semantic search to compare the direction of vectors in a high-dimensional space.
+ **Locality-sensitive hashing (LSH)** – A technique that hashes similar vectors to the same or nearby buckets with high probability. This allows for approximate nearest-neighbor searches, which can be faster than exact searches in high-dimensional spaces.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
