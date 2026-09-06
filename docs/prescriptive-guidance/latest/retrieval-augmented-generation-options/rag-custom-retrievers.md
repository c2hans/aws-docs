---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/rag-custom-retrievers.html
---

# Retrievers for RAG workflows
<a name="rag-custom-retrievers"></a>

This section explains how to build a retriever. You can use a fully managed semantic search solution, such as Amazon Kendra, or you can build a custom semantic search by using an AWS vector database.

Before you review the retriever options, make sure that you understand the three steps of the vector search process:

1. You separate the documents that need to be indexed into smaller parts. This is called *chunking*.

1. You use a process called [embedding](https://community.aws/concepts/vector-embeddings-and-rag-demystified#embeddings) to convert each chunk into a mathematical vector. Then, you index each vector in a vector database. The approach that you use to index the documents influences the speed and accuracy of the search. The indexing approach depends on the vector database and the configuration options that it provides.

1. You convert the user query into a vector by using the same process. The retriever searches the vector database for vectors that are similar to the user's query vector. [Similarity](https://community.aws/concepts/vector-embeddings-and-rag-demystified#distance-metrics-between-embeddings) is calculated by using metrics such as Euclidean distance, cosine distance, or dot product.

This guide describes how to use the following AWS services or third-party services to build a custom retrieval layer on AWS:
+ [Amazon Kendra](#rag-custom-kendra)
+ [Amazon OpenSearch Service](#rag-custom-opensearch)
+ [Amazon Aurora PostgreSQL and pgvector](#rag-custom-aurora)
+ [Amazon Neptune Analytics](#rag-custom-neptune)
+ [Amazon MemoryDB](#rag-custom-memorydb)
+ [Amazon DocumentDB](#rag-custom-docdb)
+ [Pinecone](#rag-custom-pinecone)
+ [MongoDB Atlas](#rag-custom-mongodb-atlas)
+ [Weaviate](#rag-custom-weaviate)

## Amazon Kendra
<a name="rag-custom-kendra"></a>

[Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html) is a fully managed, intelligent search service that uses natural language processing and advanced machine learning algorithms to return specific answers to search questions from your data. Amazon Kendra helps you directly ingest documents from multiple sources and query the documents after they have synced successfully. The syncing process creates the necessary infrastructure required to create a vector search on the ingested document. Therefore, Amazon Kendra does not require the traditional three steps of the vector search process. After the initial sync, you can use a defined schedule to handle ongoing ingestion.

The following are the advantages of using Amazon Kendra for RAG:
+ You do not have to maintain a vector database because Amazon Kendra handles the entire vector search process.
+ Amazon Kendra contains pre-built connectors for popular data sources, such as databases, website crawlers, Amazon S3 buckets, Microsoft SharePoint instances, and Atlassian Confluence instances. Connectors developed by AWS Partners are available, such as connectors for Box and GitLab.
+ Amazon Kendra provides access control list (ACL) filtering that returns only documents that the end user has access to.
+ Amazon Kendra can boost responses based on metadata, such as date or source repository.

The following image shows a sample architecture that uses Amazon Kendra as the retrieval layer of the RAG system. For more information, see [Quickly build high-accuracy Generative AI applications on enterprise data using Amazon Kendra, LangChain, and large language models](https://aws.amazon.com/blogs/machine-learning/quickly-build-high-accuracy-generative-ai-applications-on-enterprise-data-using-amazon-kendra-langchain-and-large-language-models/) (AWS blog post).

![Using Amazon Kendra as the retrieval layer for a RAG system on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/images/guide-img/22e94edd-d3e5-4e29-8c94-48e327306335/images/2807c4b1-dbb5-4715-8e31-b33c6f568109.png)

For the foundation model, you can use Amazon Bedrock or an LLM deployed through [Amazon SageMaker AI JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html). You can use AWS Lambda with [LangChain](https://python.langchain.com/docs/integrations/tools/awslambda/) to orchestrate the flow between the user, Amazon Kendra, and the LLM. To build a RAG system that uses Amazon Kendra, LangChain, and various LLMs, see the [Amazon Kendra LangChain Extensions](https://github.com/aws-samples/amazon-kendra-langchain-extensions) GitHub repository.

## Amazon OpenSearch Service
<a name="rag-custom-opensearch"></a>

[Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) provides built-in ML algorithms for [k-nearest neighbors (k-NN) search](https://opensearch.org/docs/latest/search-plugins/knn/index/) in order to perform a vector search. OpenSearch Service also provides a [vector engine for Amazon EMR Serverless](https://aws.amazon.com/opensearch-service/serverless-vector-engine/). You can use this vector engine to build a RAG system that has scalable and high-performing vector storage and search capabilities. For more information about how to build a RAG system by using OpenSearch Serverless, see [Build scalable and serverless RAG workflows with a vector engine for Amazon OpenSearch Serverless and Amazon Bedrock Claude models](https://aws.amazon.com/blogs/big-data/build-scalable-and-serverless-rag-workflows-with-a-vector-engine-for-amazon-opensearch-serverless-and-amazon-bedrock-claude-models/) (AWS blog post).

The following are the advantages of using OpenSearch Service for vector search:
+ It provides complete control over the vector database, including building a scalable vector search by using OpenSearch Serverless.
+ It provides control over the chunking strategy.
+ It uses approximate nearest neighbor (ANN) algorithms from the [Non-Metric Space Library (NMSLIB)](https://github.com/nmslib/nmslib), [Faiss](https://github.com/facebookresearch/faiss), and [Apache Lucene](https://lucene.apache.org/) libraries to power a k-NN search. You can change the algorithm based on the use case. For more information about the options for customizing vector search through OpenSearch Service, see [Amazon OpenSearch Service vector database capabilities explained](https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/) (AWS blog post).
+ OpenSearch Serverless integrates with Amazon Bedrock knowledge bases as a vector index.

## Amazon Aurora PostgreSQL and pgvector
<a name="rag-custom-aurora"></a>

[Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed relational database engine that helps you set up, operate, and scale PostgreSQL deployments. [pgvector](https://github.com/pgvector/pgvector/) is an open-source PostgreSQL extension that provides vector similarity search capabilities. This extension is available for both Aurora PostgreSQL-Compatible and for Amazon Relational Database Service (Amazon RDS) for PostgreSQL. For more information about how to build a RAG-based system that uses Aurora PostgreSQL-Compatible and pgvector, see the following AWS blog posts:
+ [Building AI-powered search in PostgreSQL using Amazon SageMaker AI and pgvector](https://aws.amazon.com/blogs/database/building-ai-powered-search-in-postgresql-using-amazon-sagemaker-and-pgvector/)
+ [Leverage pgvector and Amazon Aurora PostgreSQL for Natural Language Processing, Chatbots, and Sentiment Analysis](https://aws.amazon.com/blogs/database/leverage-pgvector-and-amazon-aurora-postgresql-for-natural-language-processing-chatbots-and-sentiment-analysis/)

The following are the advantages of using pgvector and Aurora PostgreSQL-Compatible:
+ It supports exact and approximate nearest neighbor search. It also supports the following similarity metrics: L2 distance, inner product, and cosine distance.
+ It supports [Inverted File with Flat Compression (IVFFlat)](https://github.com/pgvector/pgvector#ivfflat) and [Hierarchical Navigable Small Worlds (HNSW)](https://github.com/pgvector/pgvector#hnsw) indexing.
+ You can combine the vector search with queries over domain-specific data that is available in the same PostgreSQL instance.
+ Aurora PostgreSQL-Compatible is optimized for I/O and provides tiered caching. For workloads that exceed the available instance memory, pgvector can increase the queries per second for vector search by [up to 8 times](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.optimized.reads.html).

## Amazon Neptune Analytics
<a name="rag-custom-neptune"></a>

[Amazon Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html) is a memory-optimized graph database engine for analytics. It supports a library of optimized graph analytic algorithms, low-latency graph queries, and vector search capabilities within graph traversals. It also has built-in vector similarity search. It provides one endpoint to create a graph, load data, invoke queries, and perform vector similarity search. For more information about how to build a RAG-based system that uses Neptune Analytics, see [Using knowledge graphs to build GraphRAG applications with Amazon Bedrock and Amazon Neptune](https://aws.amazon.com/blogs/database/using-knowledge-graphs-to-build-graphrag-applications-with-amazon-bedrock-and-amazon-neptune/) (AWS blog post).

The following are the advantages of using Neptune Analytics:
+ You can store and search embeddings in graph queries.
+ If you integrate Neptune Analytics with LangChain, this architecture supports natural language graph queries.
+ This architecture stores large graph datasets in memory.

## Amazon MemoryDB
<a name="rag-custom-memorydb"></a>

[Amazon MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html) is a durable, in-memory database service that delivers ultra-fast performance. All of your data is stored in memory, which supports microsecond read, single-digit millisecond write latency, and high throughput. [Vector search for MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-overview.html) extends the functionality of MemoryDB and can be used in conjunction with existing MemoryDB functionality. For more information, see the [Question answering with LLM and RAG](https://github.com/aws-samples/rag-with-amazon-bedrock-and-memorydb/tree/main) repository on GitHub.

The following diagram shows a sample architecture that uses MemoryDB as the vector database.

![A generative AI application retrieving context from a MemoryDB vector database.](http://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/images/guide-img/22e94edd-d3e5-4e29-8c94-48e327306335/images/7e1fec2b-d6a6-4e64-8ec2-f36220d6c15b.png)

The following are the advantages of using MemoryDB:
+ It supports both Flat and HNSW indexing algorithms. For more information, see [Vector search for Amazon MemoryDB is now generally available](https://aws.amazon.com/blogs/aws/vector-search-for-amazon-memorydb-is-now-generally-available/) on the AWS News Blog
+ It can also act as a buffer memory for the foundation model. This means that previously answered questions are retrieved from the buffer instead of going through the retrieval and generation process again. The following diagram shows this process.
![Storing an answer in a MemoryDB database so that it can retrieved from buffer memory.](http://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/images/guide-img/22e94edd-d3e5-4e29-8c94-48e327306335/images/3d5e7357-d23e-4fa5-ab51-f8d496bcafb5.png)
+ Because it uses an in-memory database, this architecture provides single-digit millisecond query time for the semantic search.
+ It provides up to 33,000 queries per second at 95‐99% recall and 26,500 queries per second at greater than 99% recall. For more information, see the [AWS re:Invent 2023 - Ultra-low latency vector search for Amazon MemoryDB](https://www.youtube.com/watch?v=AaMh3rdu-p0) video on YouTube.

## Amazon DocumentDB
<a name="rag-custom-docdb"></a>

[Amazon DocumentDB (with MongoDB compatibility)](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html) is a fast, reliable, and fully managed database service. It makes it easy to set up, operate, and scale MongoDB-compatible databases in the cloud. [Vector search for Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/vector-search.html) combines the flexibility and rich querying capability of a JSON-based document database with the power of vector search. For more information, see the [Question answering with LLM and RAG](https://github.com/aws-samples/rag-with-amazon-bedrock-and-documentdb/tree/main) repository on GitHub.

The following diagram shows a sample architecture that uses Amazon DocumentDB as the vector database.

![A generative AI application retrieving context from a DocumentDB vector database.](http://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/images/guide-img/22e94edd-d3e5-4e29-8c94-48e327306335/images/03373973-042b-482c-8605-c89b7622243d.png)

The diagram shows the following workflow:

1. The user submits a query to the generative AI application.

1. The generative AI application performs a similarity search in the Amazon DocumentDB vector database and retrieves the relevant document extracts.

1. The generative AI application updates the user query with the retrieved context and submits the prompt to the target foundation model.

1. The foundation model uses the context to generate a response to the user's question and returns the response.

1. The generative AI application returns the response to the user.

The following are the advantages of using Amazon DocumentDB:
+ It supports both HNSW and IVFFlat indexing methods.
+ It supports up to 2,000 dimensions in the vector data and supports the Euclidean, cosine, and dot product distance metrics.
+ It provides millisecond response times.

## Pinecone
<a name="rag-custom-pinecone"></a>

[Pinecone](https://www.pinecone.io/) is a fully managed vector database that helps you add vector search to production applications. It is available through the [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-xhgyscinlz4jk). Billing is based on usage, and charges are calculated by multiplying the pod price by the pod count. For more information about how to build a RAG-based system that uses Pinecone, see the following AWS blog posts:
+ [Mitigate hallucinations through RAG using Pinecone vector database & Llama-2 from Amazon SageMaker AI JumpStart](https://aws.amazon.com/blogs/machine-learning/mitigate-hallucinations-through-retrieval-augmented-generation-using-pinecone-vector-database-llama-2-from-amazon-sagemaker-jumpstart/)
+ [Use Amazon SageMaker AI Studio to build a RAG question answering solution with Llama 2, LangChain, and Pinecone for fast experimentation](https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-studio-to-build-a-rag-question-answering-solution-with-llama-2-langchain-and-pinecone-for-fast-experimentation/)

The following diagram shows a sample architecture that uses Pinecone as the vector database.

![A generative AI application retrieving context from a Pinecone vector database.](http://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/images/guide-img/22e94edd-d3e5-4e29-8c94-48e327306335/images/d5306b01-e78e-4c00-837c-0521b96c80f2.png)

The diagram shows the following workflow:

1. The user submits a query to the generative AI application.

1. The generative AI application performs a similarity search in the Pinecone vector database and retrieves the relevant document extracts.

1. The generative AI application updates the user query with the retrieved context and submits the prompt to the target foundation model.

1. The foundation model uses the context to generate a response to the user's question and returns the response.

1. The generative AI application returns the response to the user.

The following are the advantages of using Pinecone:
+ It's a fully managed vector database and takes away the overhead of managing your own infrastructure.
+ It provides the additional features of filtering, live index updates, and keyword boosting (hybrid search).

## MongoDB Atlas
<a name="rag-custom-mongodb-atlas"></a>

[MongoDB Atlas](https://www.mongodb.com/lp/cloud/atlas/try4) is a fully managed cloud database that handles all the complexity of deploying and managing your deployments on AWS. You can use [Vector search for MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-vector-search) to store vector embeddings in your MongoDB database. Amazon Bedrock knowledge bases supports MongoDB Atlas for vector storage. For more information, see [Get Started with the Amazon Bedrock Knowledge Base Integration](https://www.mongodb.com/docs/atlas/atlas-vector-search/ai-integrations/amazon-bedrock/) in the MongoDB documentation.

For more information about how to use MongoDB Atlas vector search for RAG, see [Retrieval-Augmented Generation with LangChain, Amazon SageMaker AI JumpStart, and MongoDB Atlas Semantic Search](https://aws.amazon.com/blogs/machine-learning/retrieval-augmented-generation-with-langchain-amazon-sagemaker-jumpstart-and-mongodb-atlas-semantic-search/) (AWS blog post). The following diagram shows the solution architecture detailed in this blog post.

![Using MongoDB Atlas vector search to retrieve context for a RAG-based generative AI application.](http://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/images/guide-img/22e94edd-d3e5-4e29-8c94-48e327306335/images/7736f899-1356-4314-a3f8-9c56a677c324.png)

The following are the advantages of using MongoDB Atlas vector search:
+ You can use your existing implementation of MongoDB Atlas to store and search vector embeddings.
+ You can use the [MongoDB Query API](https://www.mongodb.com/docs/manual/query-api/) to query the vector embeddings.
+ You can independently scale the vector search and database.
+ Vector embeddings are stored near the source data (documents), which improves the indexing performance.

## Weaviate
<a name="rag-custom-weaviate"></a>

[Weaviate](https://weaviate.io/) is a popular open source, low-latency vector database that supports multimodal media types, such as text and images. The database stores both objects and vectors, which combines vector search with structured filtering. For more information about using Weaviate and Amazon Bedrock to build a RAG workflow, see [Build enterprise-ready generative AI solutions with Cohere foundation models in Amazon Bedrock and Weaviate vector database on AWS Marketplace](https://aws.amazon.com/blogs/machine-learning/build-enterprise-ready-generative-ai-solutions-with-cohere-foundation-models-in-amazon-bedrock-and-weaviate-vector-database-on-aws-marketplace/) (AWS blog post).

The following are the advantages of using Weaviate:
+ It is open source and backed by a strong community.
+ It is built for hybrid search (both vectors and keywords).
+ You can deploy it on AWS as a managed software as a service (SaaS) offering or as a Kubernetes cluster.
