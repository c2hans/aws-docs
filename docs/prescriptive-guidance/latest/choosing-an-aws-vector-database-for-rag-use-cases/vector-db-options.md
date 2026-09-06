---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/vector-db-options.html
---

# Vector database options
<a name="vector-db-options"></a>

AWS offers a diverse range of vector database solutions to support different use cases and requirements in generative AI applications. These options can be broadly categorized into individual database services and managed service offerings, each with distinct characteristics and advantages. Understanding these options is crucial for organizations looking to implement vector search capabilities effectively while maintaining optimal performance, scalability, and cost efficiency.

For more information about vector database solutions, see the following sections:
+ [Individual vector database options](#individual-dbs)
+ [Managed service option](#managed-db)
+ [Choosing the right vector database](#choosing-database)

## Individual vector database options
<a name="individual-dbs"></a>

The individual vector database options on AWS include [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html), [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html), [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) with pgvector, [Amazon MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html), [Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html), [Amazon Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html), and [Amazon S3 Vector](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors.html). (An open-source extension, pgvector adds the ability to store and search ML-generated vector embeddings.) These solutions offer different approaches to vector search, allowing organizations to choose based on their existing infrastructure, technical requirements, and specific [use cases](use-cases.md).

### Amazon Kendra
<a name="9999999999999999ken-.ea853400-f7b3-5125-90e3-70fe4d864a1e"></a>

Amazon Kendra is an enterprise-grade intelligent search service that uses natural language processing and advanced machine learning algorithms to return specific answers to search questions from your data. Amazon Kendra simplifies the implementation of search functionality, making it an effective backend solution for generative AI applications.

Other key features of Amazon Kendra include the following:
+ Native connections to over [40 data sources](https://aws.amazon.com/kendra/connectors/)
+ Built-in data preparation capabilities
+ Quick setup that doesn't require deep technical expertise

Benefits of Amazon Kendra include the following
+ Automated data processing (chunking, ingestion, retrieval)
+ Powerful customization options:
  + [Facet search](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html)
  + [Search analytics](https://docs.aws.amazon.com/kendra/latest/dg/search-analytics.html)
  + [Tuning search relevance](https://docs.aws.amazon.com/kendra/latest/dg/tuning.html)
+ Simple programmatic access through the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/kendra/latest/dg/gs-python.html)

For more information, see [Benefits of Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html#what-is-benefits) in the Amazon Kendra documentation.

### Amazon OpenSearch Service
<a name="9999999999999999eslong-.6b13dbbb-8078-5151-9a47-7b05986a5d7b"></a>

Amazon OpenSearch Service is a managed service that helps you deploy, operate, and scale OpenSearch Service clusters in the AWS Cloud.

Core capabilities of OpenSearch Service include the following:
+ Open-source search and analytics engine
+ Distributed architecture
+ Real-time data processing

Some advantages of using OpenSearch Service include the following:
+ Horizontal scalability
+ RESTful API support
+ Handles structured and unstructured data
+ Real-time data analysis
+ Suitable for various deployment sizes

For more information, see [Features of Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html#what-is-features) in the OpenSearch Service documentation.

### Amazon RDS for PostgreSQL with pgvector
<a name="9999999999999999rdslongpostgres--with-pgvector.591f2e39-134b-5627-a90f-dc94ae0846ac"></a>

Amazon RDS for PostgreSQL with [pgvector](https://github.com/pgvector/pgvector) combines the AWS managed relational database service with PostgreSQL's vector processing extension. This combination enables organizations to store and query high-dimensional vectors while maintaining Amazon RDS. The solution is particularly suitable for generative AI applications that require real-time vector operations without the overhead of managing database infrastructure.

Key benefits of Amazon RDS for PostgreSQL with pgvector include the following:
+ High availability
+ Automatic failover
+ Cost-effective (pay-per-use)
+ Built-in monitoring
+ Real-time vector data integration

For more information, see [Advantages of Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) in the Amazon RDS documentation.

### Amazon DocumentDB
<a name="9999999999999999docdb-.8c35ef65-83c2-56b3-ac49-73e904140de9"></a>

Amazon DocumentDB (with MongoDB compatibility) is a document database that offers native vector search capabilities in version 5.0 and later. It combines the flexibility of JSON-based document storage with vector search, supporting both hierarchical navigable small world (HNSW) and Inverted File Flat (IVFFlat) indexing methods.

Core capabilities of Amazon DocumentDB include the following:
+ Store and index vectors up to 2,000 dimensions (up to 16,000 dimensions without indexing)
+ Millisecond response times for vector similarity searches
+ Support for euclidean, cosine, and dot product distance metrics
+ Seamless integration with existing MongoDB-compatible applications

Use Amazon DocumentDB in the following situations:
+ For applications that are already using MongoDB APIs and that need vector search capabilities
+ For use cases that require flexible document data structures combined with semantic search
+ For scenarios that need both traditional document queries and vector similarity searches
+ For applications that provide product recommendations, personalization, chat assistants, and fraud detection

For more information, see [Vector search for Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/vector-search.html) in the Amazon DocumentDB documentation.

### Amazon MemoryDB
<a name="9999999999999999mdblong-.0052412e-da55-5fcb-a64b-3d084afbf556"></a>

Amazon MemoryDB is a Redis-compatible, in-memory database that delivers the fastest vector search performance among popular vector databases on AWS. It provides sub-millisecond query latencies with multi-Availability Zone durability.

Core capabilities of MemoryDB include the following:
+ Store application data and millions of vectors in a single database
+ Single-digit millisecond query and update response times
+ Highest recall rates at the fastest performance on AWS
+ Support for up to 32,768 dimensions per vector
+ Real-time semantic search and caching capabilities

Use MemoryDB in the following situations:
+ For real-time applications that require ultra-low latency (sub-10ms)
+ For high-throughput workloads with millions of requests per day
+ For use cases such as real-time recommendation engines, semantic caching, and anomaly detection
+ For applications that need both in-memory data store and vector search capabilities

For more information, see [Vector search](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search.html) in the MemoryDB documentation.

### Amazon Neptune Analytics
<a name="9999999999999999neptunelong--analytics.7b6eabeb-e71e-5a6e-a2b4-b74ba9c506bc"></a>

Amazon Neptune Analytics is a graph analytics engine that offers native vector search capabilities, making it ideal for Graph Retrieval Augmented Generation (GraphRAG) use cases. It combines vector similarity search with graph traversals and algorithms.

Core capabilities of Neptune Analytics include the following:
+ Analyze tens of billions of relationships within seconds
+ Combine vector search with graph algorithms (path finding, community detection, centrality)
+ Support for GraphRAG applications with topological knowledge
+ Up to 80 times faster than existing graph analytical solutions
+ Integration with Amazon Bedrock for fully managed GraphRAG

Use Neptune Analytics in the following situations:
+ For GraphRAG applications that require knowledge graphs with vector embeddings
+ For use cases that require traversing complex relationships alongside vector similarity
+ For applications that require explainable AI responses with relationship context
+ For scenarios such as customer 360 views, fraud detection networks, and knowledge discovery

For more information, see the [Amazon Neptune Analytics documentation](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html).

### Amazon S3 Vectors
<a name="9999999999999999s3--vectors.5983ade3-0746-5d8c-88b4-6335894e0adb"></a>

Amazon S3 Vectors is the first cloud object store in AWS with native vector storage and query capabilities. It provides purpose-built, cost-optimized vector storage for AI applications that require massive scale.

Core capabilities of Amazon S3 Vectors include the following:
+ Storage for up to 2 billion vectors per index with support for up to 10,000 indexes per vector bucket
+ Sub-100 ms query latency that is optimized for long-term storage and infrequent access patterns
+ Up to 90% cost reduction for vector operations compared to specialized vector databases
+ Serverless architecture with automatic scaling and 99.999999999% (11 9s) durability

Use Amazon S3 Vectors in the following situations:
+ For applications that require storage of billions of vectors at minimal cost
+ For workloads that tolerate sub-second query latency (100 ms or more) rather than sub-10 ms
+ For long-term vector retention and archival use cases
+ For RAG applications with infrequent retrieval patterns
+ For organizations that prioritize storage economics over ultra-low latency

Amazon S3 Vectors integrates natively with Amazon Bedrock Knowledge Bases and works well in tiered architectures with Amazon OpenSearch Service. You can use Amazon S3 Vectors for cold storage and use OpenSearch Service for hot queries.

For more information, see [Working with S3 Vectors and vector buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors.html) in the Amazon S3 documentation.

## Managed service option
<a name="managed-db"></a>

Amazon Bedrock Knowledge Bases represents the AWS fully managed approach to vector database implementation. The service's flexibility in storage options, combined with its automated management features, makes it particularly valuable for organizations seeking to implement RAG without managing complex infrastructure.

With Amazon Bedrock Knowledge Bases, you can create, maintain, and query knowledge bases that enhance your foundation models using RAG. This service simplifies the complex process of implementing RAG by managing the entire data ingestion, vectorization, and retrieval pipeline.

Key benefits of Amazon Bedrock Knowledge Bases include the following:
+ Simplified data processing
  + Automatic data ingestion and chunking
  + Built-in text extraction from multiple file formats
  + Managed vector embeddings generation
  + Automatic metadata extraction and indexing
+ Streamlined RAG implementation
  + Pre-configured retrieval strategies
  + Automatic context window optimization
  + Built-in relevancy tuning
  + Semantic search capabilities out of the box
+ Security and governance
  + Integrated AWS Identity and Access Management (IAM) controls
  + Data encryption at rest and in transit
  + VPC support
  + Audit logging with AWS CloudTrail

Amazon Bedrock Knowledge Bases supports multiple [vector store options](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html), including:
+ Amazon Aurora PostgreSQL with pgvector
+ Amazon Neptune Analytics
+ Amazon EMR Serverless
+ Amazon S3 Vectors
+ Pinecone
+ Redis Enterprise Cloud

This managed service handles automated data ingestion, vectorization, and retrieval. This simplifies RAG implementations.

For detailed information about each supported vector store, see the [Amazon Bedrock Knowledge Bases documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html).

## Choosing the right vector database
<a name="choosing-database"></a>

Select your vector database based on these key decision factors:
+ **If you need MongoDB-compatible document database with vector search** – Choose Amazon DocumentDB. This is ideal when your application uses MongoDB APIs and you want to add semantic search capabilities without managing separate vector infrastructure.
+ **If you need ultra-low latency for real-time applications** – Choose Amazon MemoryDB. This provides the fastest vector search performance on AWS with sub-millisecond response times. It's ideal for real-time recommendation engines and high-throughput applications.
+ **If you need graph-based knowledge representations with vector search** – Choose Amazon Neptune Analytics. This is best for GraphRAG applications that need to traverse complex relationships and perform graph-based queries alongside vector searches, providing explainable AI responses.
+ **If you need to combine relational queries with vector search** – Choose Amazon Aurora PostgreSQL with pgvector. This option is ideal when your application requires both traditional SQL operations and vector similarity searches within the same database.
+ **If you require high-throughput queries with sub-10 ms latency** – Choose Amazon OpenSearch Service. It excels at handling high-frequency queries and real-time applications and includes recent GPU acceleration improvements.
+ **If you need to store billions of vectors cost-effectively** – Choose Amazon S3 Vectors. This option provides up to 90% cost savings and is ideal for applications with infrequent retrieval patterns (minutes to hours between queries) that can tolerate sub-100 ms latency.
+ **If you need full-text search alongside vector search** – Choose Amazon OpenSearch Service. This option combines powerful full-text search capabilities with vector search in a single platform.
