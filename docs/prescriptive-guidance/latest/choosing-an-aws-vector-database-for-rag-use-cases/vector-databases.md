---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/vector-databases.html
---

# Overview of vector databases
<a name="vector-databases"></a>

A vector database is a specialized system that stores and queries high-dimensional vectors efficiently. These databases are fundamental for Retrieval Augmented Generation (RAG) applications.

Vector databases handle data conversion and storage in the following ways:
+ Objects (such as audio, images, and text files) are converted to vectors by using embedding models.
+ Vectors are stored in specialized data formats.
+ Vector databases enable rapid similarity searches.

Vector databases offer several key advantages over traditional databases, making them particularly well-suited for modern data challenges. They are specifically optimized for vector operations and handle high-dimensional data efficiently. They also specialize in similarity searches that traditional databases struggle with. Beyond these core capabilities, vector databases are built to meet the evolving demands of ML and generative AI applications. They excel at large-scale vector storage and use distributed computing to balance workloads across multiple nodes. This provides scalability and performance as data volumes grow.

The following diagram shows a RAG implementation:

1. Content, such as documents, PDFs, or text files, is fed into the embedding model as raw data for processing.

1. The embedding model transforms the raw data into numerical vectors, which represent the semantic meaning of the content.

1. The generated vector embeddings are stored in a vector database that is optimized for the storage and retrieval of high-dimensional vectors.

1. Applications can now query the vector database in response to use cases such as semantic search and content recommendation.

![Embedding model converts content to vector embeddings stored in vector db to respond to queries.](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/images/guide-img/34bd35bb-382d-4951-8f14-111521edb094/images/7ee46b17-983e-46a9-a10a-1dd44cb7d6ff.png)

Choosing an inappropriate vector database for a RAG solution can lead to significant struggles and limitations including the following:
+ Poor query performance
+ Scalability bottlenecks
+ Data ingestion challenges
+ Lack of advanced features, such as filtering and ranking
+ Integration difficulties with other systems
+ Persistence and durability concerns
+ Concurrency and consistency issues in environments with multiple users
+ Higher licensing costs or vendor lock-in
+ Limited community support and resources
+ Potential security and compliance risks
