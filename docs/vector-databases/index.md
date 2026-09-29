---
source_url: https://docs.aws.amazon.com/vector-databases/index.html
---

---
title: 'Choosing a database for your generative AI applications'
canonical_url: https://docs.aws.amazon.com/vector-databases/
source: aws-documentation
generated_on: 2026-09-29
---

# Choosing a database for your generative AI applications

This page helps you choose AWS vector databases and vector search options for your generative AI applications. The internal databases, data lakes, or unstructured data or document stores that you use contain a wealth of domain-specific data (such as financial or health records, or supply chain information). These data stores are generically called knowledge bases. For generative AI, you can encode your data as a set of elements, each expressed internally as a vector. Vector databases enable Retrieval Augmented Generation (RAG), the process for retrieving facts from knowledge bases to fortify large language models (LLMs) with up-to-date and accurate data.

- [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html): Amazon OpenSearch Service is a fully-managed service for running OpenSearch, an open source search engine and analytics suite. OpenSearch supports vector search through its vector engine for both managed clusters and serverless collections. OpenSearch also supports vector search with its Amazon OpenSearch Serverless deployment option. If your database type is a search engine, OpenSearch is an ideal choice for use cases where your vector indexes must scale horizontally, letting you handle more throughput for storing embeddings and performing similarity searches.
- [Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html): Amazon Aurora PostgreSQL-Compatible Edition and Amazon Relational Database Service (Amazon RDS) for PostgreSQL are fully managed relational databases with the pgvector open source vector search extension. Aurora PostgreSQL also supports vector search with its Amazon Aurora Serverless v2 deployment. These are ideal options if you are already invested in relational databases, particularly PostgreSQL.
- [Amazon MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-overview.html): Vector search for Amazon MemoryDB is an in-memory database providing the fastest vector search performance at the highest recall rates among popular vector databases on Amazon Web Services. MemoryDB offers single-digit millisecond vector search and update latencies at even the highest levels of recall. MemoryDB is ideal for in-memory database workloads requiring single-digit millisecond latencies at the highest levels of recall, or if you are already familiar with the MemoryDB, Valkey, or OSS Redis APIs.
- [Amazon Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html): Amazon Neptune Analytics is an analytics graph database engine with graph algorithms and vector search for combining graphs with RAG, such as GraphRAG. Neptune Analytics is ideal for GraphRAG use cases, and queries that require a higher-level understanding of large data sets.
- [Amazon DocumentDB (with MongoDB compatibility)](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html): Vector search for Amazon DocumentDB (with MongoDB compatibility) is available with Amazon DocumentDB 5.0 instance-based clusters. DocumentDB (with MongoDB compatibility) is ideal for document database applications, existing MongoDB users, or users who need to store JSON-style documents together with embeddings.
- [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/VectorSearch.html): Amazon DynamoDB is a serverless, NoSQL, fully managed database with native vector search through vector indexes. Vector indexes let you store vector embeddings alongside your operational data and run similarity searches with the SearchVectors API, with no separate vector database or data replication pipeline to manage. DynamoDB is ideal for RAG and AI agent memory workloads where your operational data already lives in DynamoDB. DynamoDB also offers zero-ETL integration with Amazon OpenSearch Service when you want full-text search alongside vector search.

---

## Related Links

- [Decision Guides](https://aws.amazon.com/getting-started/decision-guides/)
- [Getting Started with AWS](https://aws.amazon.com/documentation/gettingstarted/)
- [SDKs & Tools](https://aws.amazon.com/tools/)
- [AWS General Reference](http://docs.aws.amazon.com/general/latest/gr/Welcome.html)
- [AWS Training](https://aws.amazon.com/training/)
- [AWS Case Studies](https://aws.amazon.com/solutions/case-studies/)
- [AWS Whitepapers](https://aws.amazon.com/whitepapers/)
