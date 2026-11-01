---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/vector-database-guide.html
---

# Choosing a vector database for your generative AI applications
<a name="vector-database-guide"></a>

**Taking the first step**

|  |  |
| --- |--- |
| **Purpose** | Help you compare AWS vector database options for your generative AI workload. |
| **Last updated** | October 30, 2026 |
| **Covered services** |  + [Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.VectorDB.html)<br />+ [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)<br />+ [Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html)<br />+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)<br />+ [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)<br />+ [Amazon MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html)<br />+ [Amazon Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html)<br />+ [OpenSearch Managed Clusters](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html)<br />+ [OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.html)<br />+ [Amazon S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-getting-started.html)  |

## Introduction
<a name="vector-db-introduction"></a>

*Vectors* are numerical representations of data such as text, images, or audio. These representations, called *embeddings*, capture the meaning of the data by turning each item into a series of numbers that place similar items close together. An *embedding model* is a type of foundation model that creates these embeddings. On AWS, you can generate embeddings with models available through Amazon Bedrock, such as [Amazon Titan Text Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) and Cohere Embed. For the full list, see [Supported models for vector embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html).

A *vector database* stores these embeddings and runs similarity searches across them to return the most relevant results quickly, even across billions of vectors. On AWS, vector search is a capability you can add to many of the databases and services you might already run, rather than a separate database you must adopt. This idea, adding vectors where your data already lives, means that many workloads can keep embeddings next to their existing data instead of moving them into a dedicated store. For a new workload, a few requirements such as latency, scale, and cost point to a fit, and Amazon Bedrock Knowledge Bases offers a fully managed option when you want AWS to run the retrieval pipeline for you.

Similarity search over vectors is the foundation of Retrieval Augmented Generation (RAG), a technique that improves a foundation model's responses by retrieving relevant context from your own data. Teams use this pattern to power enterprise knowledge assistants, semantic document search, and recommendation systems. This guide focuses on vector search over unstructured data, such as documents and images that you convert into embeddings. If your data is structured and tabular, Amazon Bedrock Knowledge Bases can instead query it directly by converting natural language into SQL. For more information, see [Turning data into a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-data.html).

AWS offers more than 10 services that can store and search vectors, so the field can be hard to narrow. As you compare options, weigh the three tradeoffs that most affect the decision:
+ **Existing store versus new store** – You can add vector search to a data store you already run, which keeps vectors next to your existing data and skills, or you can adopt a store dedicated to vector search.
+ **Fully managed versus self-managed** – Amazon Bedrock Knowledge Bases runs the retrieval pipeline for you, whereas managing your own store gives you full control over configuration and tuning.
+ **Cost, latency, and scale** – In-memory stores return results fastest but cost more, while storage-tier options cost less at scale in exchange for higher latency. The volume of vectors you expect can narrow the options further.

## Understand
<a name="vector-db-understand"></a>

AWS provides vector search across many of the services and databases you might already run, so in many cases you can add vectors where your data already lives rather than adopt a separate vector database. It also offers a fully managed RAG option, Amazon Bedrock Knowledge Bases, when you want AWS to run the retrieval pipeline for you. These options fall into groups by design pattern: managed RAG, search and analytics, operational databases, in-memory stores, and low-cost storage. Each group optimizes for different priorities, such as setup effort, latency, scale, and how closely vectors sit to your operational data.

The following diagram shows how AWS has added vector search across its database and search services. Use the groups that follow to narrow your options.

![AWS vector search options grouped by managed RAG, search and analytics, operational databases, in-memory, and low-cost storage.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/vector-db-new.png)

------
#### [ Managed RAG ]

This option handles the RAG pipeline for you, covering embedding, storage, indexing, and retrieval. Amazon Bedrock Knowledge Bases is available in two forms:
+ **Managed knowledge base** – Amazon Bedrock also manages the vector store, so you don't select one.
+ **Customer-managed knowledge base** – Amazon Bedrock runs retrieval over a supported vector store that you choose, shown in the Amazon Bedrock Knowledge Bases column of the capabilities table.

| Service | What it does | Well suited for |
| --- | --- | --- |
| Amazon Bedrock Knowledge Bases | Managed RAG pipeline over a supported vector store, covering embedding, storage, and retrieval. | Teams that want AWS to run the retrieval pipeline with little setup. |

------
#### [ Search and analytics ]

These services are built for search and analytics over vectors.

| Service | What it does | Well suited for |
| --- | --- | --- |
| OpenSearch Serverless | Vector and hybrid lexical and semantic search that scales without cluster management. It supports both binary and floating-point vector embeddings; binary embeddings are unique to OpenSearch among these options. | A workload with no single dominant requirement that needs broad, general-purpose search. |
| OpenSearch Managed Clusters | Vector and hybrid search on dedicated OpenSearch domains with full control over cluster configuration. It also offers lower-cost storage tiers such as UltraWarm for less-frequently accessed data, and supports both binary and floating-point vector embeddings; binary embeddings are unique to OpenSearch among these options. | Teams that need cluster-level control or that already run OpenSearch domains. |
| Amazon Neptune Analytics | Graph and vector search combined. | GraphRAG – retrieval that uses entity relationships. |

------
#### [ Relational and NoSQL databases ]

These are relational (Amazon Aurora PostgreSQL) and NoSQL (Amazon DynamoDB, Amazon DocumentDB) databases where your application data already lives, so you can add vector search alongside your operational data.

| Service | What it does | Well suited for |
| --- | --- | --- |
| Amazon DynamoDB | Native vector search co-located with your operational data, serverless, with sub-10-millisecond reads at any scale. It also offers zero-ETL integration with OpenSearch when you need full-text search alongside vector search. | RAG and AI agent memory workloads whose operational data already lives in Amazon DynamoDB. |
| Amazon Aurora PostgreSQL (pgvector) | SQL-native vector search inside a relational database through pgvector. Amazon Aurora Optimized Reads can raise vector queries per second by up to 9x for workloads that exceed instance memory. | Teams with PostgreSQL expertise who need SQL and vector queries together. |
| Amazon DocumentDB | MongoDB-compatible vector search. | MongoDB-compatible workloads that need semantic search. |

------
#### [ In-memory ]

These services store vectors in memory for the lowest latency.

| Service | What it does | Well suited for |
| --- | --- | --- |
| Amazon ElastiCache (Valkey) | In-memory vector search with Valkey at microsecond latency, suited to semantic caching. | Real-time inference, caching, and session-based personalization. |
| Amazon MemoryDB | Durable in-memory vector search. | Low-latency search that also requires data durability. |

------
#### [ Low-cost storage and infrequent access ]

This option stores vectors at low cost for large collections with moderate query frequency.

| Service | What it does | Well suited for |
| --- | --- | --- |
| Amazon S3 Vectors | Low-cost vector storage in Amazon S3 with pay-per-query pricing and sub-second queries. | Large embedding collections with moderate query frequency at low cost. |
| OpenSearch Managed Clusters | Offers low-cost UltraWarm and cold storage tiers for infrequently accessed vectors, so you can keep large, rarely queried vector sets at lower cost. | Large, infrequently accessed vector sets that need low-cost storage tiers. |

------

### Vector search capabilities
<a name="vector-db-compare"></a>

The following table summarizes each option so you can match it to your needs.

| Service | Amazon Bedrock Knowledge Bases | Indexing | Max dimensions | Vector volume | QPS | Hybrid search | Read latency | Write latency |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OpenSearch Serverless | Yes (Quick Create) | HNSW (GPU-accelerated) | 16,000 | Hundreds of billions | Tens of thousands | Yes | 10–100 ms | Near real-time |
| OpenSearch Managed Clusters | Yes | HNSW, IVF (GPU-accelerated) | 16,000 | Hundreds of billions | Tens of thousands | Yes | 10–100 ms | Near real-time |
| Amazon Neptune Analytics | Yes (Quick Create) | Native graph and vector | Up to 65,535 | 2–3 billion | Hundreds to thousands | Graph and vector | 10–100 ms | Not specified |
| Amazon DynamoDB | No | HNSW (ANN) | 4,096 | Billions | Virtually unlimited (thousands per partition key) | No | Sub-10 ms | Near real-time |
| Amazon Aurora PostgreSQL (pgvector) | Yes (Quick Create) | HNSW, IVFFlat | 2,000 indexed | Hundreds of billions | Thousands | Partial (SQL) | 10–100 ms | Immediate |
| Amazon DocumentDB | No | HNSW, IVFFlat | 2,000 indexed | Millions | Not specified | Partial | Low ms | Not specified |
| Amazon ElastiCache (Valkey) | No | HNSW, FLAT | Not specified | 1 billion\+ | Thousands | Partial | Microsecond | Immediate |
| Amazon MemoryDB | No | HNSW | 32,768 | Millions | Not specified | Partial | Sub-10 ms | Near real-time |
| Amazon S3 Vectors | Yes | Automatic | 4,096 | 2 billion per index | Low hundreds per index | No | Sub-second | Batch |

The Amazon Bedrock Knowledge Bases column shows whether a store is supported by a customer-managed knowledge base, where Amazon Bedrock runs retrieval over the store you provide. With a managed knowledge base, Amazon Bedrock manages the vector store for you, so it isn't tied to a specific store in this column.

## Consider
<a name="vector-db-consider"></a>

When you add vector search on AWS, evaluate the following criteria. Each one describes a factor to think about and the options that relate to it.

------
#### [ Existing data store ]

Consider where your data already lives. If your data is already in an AWS store, you can add vector search there instead of adopting a separate vector database, which lets your team reuse the engine, skills, and tooling they already have. The following stores support vector search alongside your existing data:
+ Amazon DynamoDB
+ Amazon Aurora PostgreSQL
+ OpenSearch
+ Amazon ElastiCache
+ Amazon MemoryDB
+ Amazon Neptune Analytics
+ Amazon DocumentDB
+ Amazon S3

------
#### [ Managed or self-managed ]

Consider how much of the retrieval pipeline you want to own. Retrieval Augmented Generation (RAG) combines your data with a generative AI model to produce more accurate answers:
+ **Amazon Bedrock Managed Knowledge Base** – Amazon Bedrock manages the full RAG pipeline and the vector store, so you don't choose or operate a store.
+ **Customer-managed knowledge base** – Amazon Bedrock runs the RAG pipeline, and you choose, provision, and manage the supported vector store it uses.
+ **Self-managed vector search** – You run vector search directly in a store you operate, without Amazon Bedrock Knowledge Bases, for full control over indexing, ranking, and integration.

------
#### [ Read latency ]

Consider how quickly your application needs query results. Where vectors are stored, along with data size, index configuration, and scale, shapes retrieval time:
+ **In-memory stores** – Amazon ElastiCache (Valkey) and Amazon MemoryDB hold vectors in memory, which suits latency-sensitive, real-time applications such as semantic caching and session-based personalization.
+ **Databases and search services** – Amazon DynamoDB, Amazon Aurora PostgreSQL, OpenSearch Serverless, OpenSearch Managed Clusters, Amazon Neptune Analytics, and Amazon DocumentDB serve vector queries from the same engine that holds your operational or search data.
+ **Object storage** – Amazon S3 Vectors stores vectors durably at low cost, which suits large collections queried less frequently.

For each option's read latency, see the capabilities table in the Understand section.

------
#### [ Write latency ]

Consider how soon an inserted or updated vector must become searchable. A workload with a fixed set of vectors can tolerate slower inserts, while a workload that updates vectors continuously needs those changes reflected quickly:
+ **Reflected almost immediately** – Amazon ElastiCache (Valkey), which supports real-time vector updates, and Amazon Aurora PostgreSQL, where a committed row is queryable right away.
+ **Within seconds (near real-time)** – Amazon DynamoDB, Amazon MemoryDB, and OpenSearch, which update their vector indexes shortly after a write.
+ **Batch or rate-limited ingest** – Amazon S3 Vectors, which is optimized for ingesting large, relatively fixed sets of vectors.

------
#### [ Search capabilities ]

Consider what type of search your application needs:
+ **Hybrid (keyword and semantic)** – OpenSearch.
+ **Graph and vector (GraphRAG)** – Amazon Neptune Analytics.
+ **SQL and vector** – Amazon Aurora PostgreSQL.
+ **Pure vector similarity** – Amazon S3 Vectors, Amazon DynamoDB, Amazon ElastiCache, Amazon MemoryDB, and Amazon DocumentDB.

------
#### [ Scale and recall ]

Consider how many vectors you need to store, and how accurate your results must be. Recall is the share of true nearest neighbors that a search returns:
+ **Scale** – Vector volumes range from millions to hundreds of billions. Amazon DynamoDB scales to billions of vectors, OpenSearch scales to hundreds of billions, Amazon S3 Vectors scales to billions, and Amazon Aurora PostgreSQL scales to hundreds of billions.
+ **Recall** – Amazon ElastiCache (Valkey) reaches 95%\+ recall at microsecond latency, and Amazon DynamoDB reaches 99% recall at sub-10-millisecond latency.
+ **Durability** – Amazon S3 Vectors provides eleven nines (99.999999999%) of durability, the database options provide 99.99% multi-AZ durability, and Amazon MemoryDB adds multi-AZ durability to in-memory vector search.

------
#### [ Cost model ]

Consider how you want to pay, and match the pricing model to your workload's usage pattern:
+ **Pay-per-request or serverless** – Amazon S3 Vectors and Amazon DynamoDB (on-demand) charge for storage and requests with no idle cost, and OpenSearch Serverless can scale to zero for intermittent workloads.
+ **Capacity-based or instance-based** – Amazon Aurora, Amazon Neptune Analytics, Amazon ElastiCache, Amazon MemoryDB, and Amazon DocumentDB bill by provisioned capacity, instance, or node, so cost scales with the capacity you run.

For infrequent or low-QPS workloads, Amazon S3 Vectors offers pay-per-request pricing at low cost, and OpenSearch offers lower-cost storage tiers, such as UltraWarm and cold, for infrequently accessed data. OpenSearch Serverless can also scale to zero for intermittent workloads. Because pricing changes over time, confirm current rates on each service's pricing page.

------

## Choose
<a name="vector-db-choose"></a>

Now that you know the criteria, you can choose the AWS vector database that fits your workload. The following table maps common needs to an option and an alternative.

| Your primary need | Option | Other option |
| --- | --- | --- |
| Existing AWS data store | Add vector search to the store you already run | None |
| Fully managed RAG pipeline | Amazon Bedrock Knowledge Bases (over a supported store) | None |
| Hybrid keyword and semantic search | OpenSearch Serverless | OpenSearch Managed Clusters |
| Real-time, low-latency search | Amazon ElastiCache (Valkey) | Amazon MemoryDB or OpenSearch Managed Clusters |
| Low-latency vector search co-located with operational data | Amazon DynamoDB | Amazon Aurora PostgreSQL |
| Graph-aware retrieval (GraphRAG) | Amazon Neptune Analytics | None |
| Relational data with SQL | Amazon Aurora PostgreSQL (pgvector) | None |
| Low-cost storage and infrequent access or low QPS | Amazon S3 Vectors | OpenSearch Managed Clusters (UltraWarm and cold tiers) or OpenSearch Serverless |
| New workload with no single dominant requirement | OpenSearch Serverless | OpenSearch Managed Clusters |

**Compare options by the level of management you want**
Amazon Bedrock Knowledge Bases is a managed option that runs the RAG pipeline for you over a supported vector store, which reduces setup and operational work. Running your own vector database gives you more control over the retrieval pipeline. Setup effort and control are the two factors that shape this choice.

## Use
<a name="vector-db-use"></a>

After you choose a vector database, use these resources to get started. The tabs group the options by the same categories as the Understand section.

------
#### [ Managed RAG ]
+  **Amazon Bedrock Knowledge Bases**

  Fully managed RAG that connects Amazon Bedrock models to a supported vector store with minimal setup.

   [Get started](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)

------
#### [ Search and analytics ]
+  **OpenSearch Serverless**

  Vector and hybrid keyword and semantic search that scales without cluster management, with GPU-accelerated indexing and scale-to-zero capacity.

   [Get started](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.html)
+  **OpenSearch Managed Clusters**

  Vector and hybrid search on dedicated OpenSearch domains with full control over cluster configuration.

   [Get started](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html)
+  **Amazon Neptune Analytics**

  Combined graph and vector search for GraphRAG that uses entity relationships.

   [Get started](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html)

------
#### [ Relational and NoSQL databases ]
+  **Amazon DynamoDB**

  Native vector search co-located with your operational data at sub-10-millisecond latency and very large scale.

   [Get started](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/VectorSearchWorkingWith.html)
+  **Amazon Aurora PostgreSQL (pgvector)**

  Vector search within a relational database, with HNSW and IVFFlat indexing through pgvector.

   [Get started](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.VectorDB.html)
+  **Amazon DocumentDB**

  Vector search for MongoDB-compatible workloads that need semantic search.

   [Get started](https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html)

------
#### [ In-memory ]
+  **Amazon ElastiCache**

  In-memory vector search with Valkey at microsecond latency and 95%\+ recall.

   [Get started](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.html)
+  **Amazon MemoryDB**

  Durable in-memory vector search at sub-10-millisecond latency with high recall.

   [Get started](https://docs.aws.amazon.com/memorydb/latest/devguide/getting-started.html)

------
#### [ Low-cost storage and infrequent access ]
+  **Amazon S3 Vectors**

  Low-cost vector storage for large embedding collections with moderate query frequency.

   [Get started](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-getting-started.html)
+  **OpenSearch Managed Clusters**

  Low-cost UltraWarm and cold storage tiers for infrequently accessed vectors.

   [Get started](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html)

------

## Explore
<a name="vector-db-resources"></a>

Explore these resources for deeper comparisons and RAG guidance.
+ [Choosing an AWS vector database for RAG use cases](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/introduction.html) – AWS Prescriptive Guidance. A deep technical comparison for data scientists, MLOps engineers, and AI researchers that covers specs, indexing, and cost.
+ [Retrieval Augmented Generation options and architectures on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/introduction.html) – AWS Prescriptive Guidance. A framework to choose managed or custom RAG.
+ [Key considerations when choosing a database for your generative AI applications](https://aws.amazon.com/blogs/database/key-considerations-when-choosing-a-database-for-your-generative-ai-applications/) – AWS Database Blog. How to pick a database for generative AI.
+ [Amazon OpenSearch Service vector database capabilities revisited](https://aws.amazon.com/blogs/big-data/amazon-opensearch-service-vector-database-capabilities-revisited/) – AWS Big Data Blog. An updated look at how OpenSearch supports vector search, embeddings, and hybrid search.
+ [Building cost-effective RAG applications with Amazon Bedrock Knowledge Bases and Amazon S3 Vectors](https://aws.amazon.com/blogs/machine-learning/building-cost-effective-rag-applications-with-amazon-bedrock-knowledge-bases-and-amazon-s3-vectors/) – AWS Machine Learning Blog. Using Amazon S3 Vectors as a low-cost vector store for RAG.
