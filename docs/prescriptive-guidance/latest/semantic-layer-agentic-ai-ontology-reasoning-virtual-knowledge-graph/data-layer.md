---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/data-layer.html
---

# Data Layer

## Data Layer Overview
<a name="data-layer-overview.08144b15-5a4c-5f2f-a088-f696755f47d4"></a>

The **Data Layer** serves as the foundational data fabric of the architecture, encompassing both structured and unstructured data sources across AWS, hybrid, and multicloud environments. For structured data, the layer provides unified access to a broad spectrum of sources including **Amazon Athena** (with connectors for AWS, hybrid, and multicloud data sources), **Amazon Redshift**, **Amazon RDS/Aurora**, **S3 Tables with Apache Iceberg**, **Snowflake**, **Databricks**, and any JDBC-compliant data source. Access control and governance are enforced through **AWS IAM** and **AWS Lake Formation** where supported, with comprehensive data catalog and lineage capabilities provided by **Amazon SageMaker Catalog** and **AWS Glue Data Catalog**. These catalogs also enable ontology induction — the automated discovery and generation of ontology classes, properties, and relationships from existing data schemas, table structures, and column metadata. This structured data foundation enables the [Knowledge Layer'](knowledge-layer.md)s Virtual Knowledge Graph (VKG) Service to virtualize relational and data warehouse sources as RDF without data duplication, using ontology-driven R2RML mappings to translate SPARQL queries into optimized SQL.

For unstructured data — including PDFs, images, and documents — the Data Layer implements **Document Ingest Pipelines** that process, chunk, and extract semantic content from raw files. AWS services such as **Amazon Textract** (Optical Character Recognition (OCR) and document extraction), **Amazon Comprehend** (Named Entity Recognition (NER) and entity recognition), and **AWS Lambda** (orchestration) can be combined with open-source alternatives like [**unstructured.io**](https://docs.unstructured.io/welcome) for flexible document processing workflows. These pipelines prepare unstructured content for semantic indexing and knowledge extraction, generating controlled vocabularies and lightweight taxonomies that bridge the gap between raw documents and formal ontologies.

Processed documents and content are indexed using **GraphRAG** techniques — with the [**Amazon Neptune GraphRAG toolkit**](https://github.com/awslabs/graphrag-toolkit) serving as a strong implementation choice. GraphRAG creates graphs of concepts, topics, and their vector embeddings, along with associations to document chunks and source documents, stored in the **Lexical Graph Database**. The Lexical Graph Database consists of **Amazon Neptune Database** (for the concept graph and document-chunk relationships) and **Amazon OpenSearch Serverless** (for vector embeddings and semantic search), or alternatively **Amazon Neptune Analytics** which provides integrated vector storage without requiring a separate vector store. This architecture enables hybrid retrieval — combining graph traversal (finding related concepts and documents) with vector similarity search (semantic matching) — to power retrieval-augmented generation (RAG) workflows for agentic AI applications.

**Why GraphRAG over Vector-Only RAG?** Traditional vector RAG retrieves document chunks based solely on embedding similarity, effective for direct lookups but limited when queries require cross-document reasoning, multi-hop relationships, or corpus-level understanding. GraphRAG augments vector search with a knowledge graph of concepts and relationships, enabling discovery of contextually relevant information that is structurally connected but not semantically similar to the query. Benchmarks demonstrate that GraphRAG improves retrieval accuracy by 7-35% over vector-only approaches (sources: [AWS Blog](https://aws.amazon.com/blogs/machine-learning/improving-retrieval-augmented-generation-accuracy-with-graphrag/), [arXiv:2507.03608](https://arxiv.org/abs/2507.03608)). This hybrid pattern delivers the retrieval quality required for agentic AI, where incomplete retrieval cascades into incomplete context for agent decision-making.

**GraphRAG Retrieval** provides hybrid semantic search capabilities that combine vector similarity with graph traversal to deliver context-aware document and concept retrieval. When a query is submitted via REST API, the GraphRAG Service applies Amazon Bedrock Guardrails to detect and redact PII or toxic content, then generates a query embedding using Amazon Titan Embeddings. The service executes a semantic similarity search against Amazon OpenSearch Service (commonly Serverless), retrieving document chunk identifiers that meet the specified similarity threshold. Using these identifiers, the service queries the Lexical Graph Database (Neptune DB) to perform graph traversal — discovering additional related topics, concepts, and document chunks through multi-hop relationship following. Finally, the service retrieves the full content for relevant document chunks from S3 (where they were cost-effectively stored by the Document Ingest Pipeline), returning ranked results with concept metadata, document chunks, provenance links, and graph context. This hybrid retrieval approach — combining vector embeddings for semantic matching with graph structures for contextual relevance — powers retrieval-augmented generation (RAG) workflows that deliver accurate, citation-backed answers for agentic AI applications.

In parallel with GraphRAG, **Information Extraction** workflows extract structured, ontology-grounded knowledge from normalized document chunks. Using modular extraction techniques including **spaCy**, **LLM models via Amazon Bedrock**, **Amazon Comprehend**, and **Amazon Comprehend Medical**, the Information Extraction Service identifies entities and relationships guided by domain ontologies. Extracted knowledge is validated and written to the **Semantic Layer Graph Database** — a curated, ontology-aligned knowledge graph containing only validated facts — while comprehensive extraction results (including candidate entities and low-confidence extractions) are stored in the Lexical Graph Database with full provenance links to source documents. This **two-tier knowledge architecture** balances production-ready, validated knowledge with exploratory, comprehensive extraction results, enabling both semantic queries over structured domain knowledge and citation-based retrieval back to source documents.

## Document Ingest Pipeline
<a name="document-ingest-pipeline.61533075-6531-5a14-8a70-c55363232194"></a>

### Data Flow — Document Ingest Pipeline
<a name="data-flow---document-ingest-pipeline.fd325490-efca-51e2-9c52-dd029dbf17a9"></a>

**1. S3 Bucket (Raw Documents) → AWS Lambda (Ingest Orchestrator)** Unstructured documents (PDFs, images, Word documents, spreadsheets, etc.) are uploaded to a source **Amazon S3 bucket** configured as the raw document landing zone. An S3 event notification triggers an **AWS Lambda function** automatically upon object creation (PUT or POST). The Lambda function acts as the ingest orchestrator, validating the uploaded object metadata (file type, size, source path) and enforcing guardrails such as a **100 MB file size limit**. The function assigns a unique processing job ID (UUID), determines the appropriate processing workflow based on document type, and enriches the event payload with document metadata including source system, upload timestamp, and content classification tags.

**2. AWS Lambda → Amazon SQS (Enqueue Processing Job)** The Lambda function publishes a document processing message to an **Amazon SQS queue** for asynchronous, decoupled processing. The SQS message payload includes the S3 object key, bucket name, document type, processing job UUID, and metadata extracted from S3 object tags (e.g., source system, document classification, tenant ID). SQS provides durability, fault tolerance, and the ability to scale the Document Processing Service independently from the ingest rate. The queue is configured with appropriate visibility timeout (aligned with expected processing duration), message retention (up to 14 days), and dead-letter queue (DLQ) settings to handle processing failures and retries.

**3. Amazon SQS → Document Processing Service (Amazon ECS)** The **Document Processing Service**, deployed as containerized tasks on **Amazon ECS** (with **Fargate** or **EC2** instances), continuously polls the SQS queue for new document processing messages. **unstructured.io is a good choice** for implementing this service — its official Docker image provides native support for PDFs, Office file formats (DOCX, XLSX, PPTX), images (PNG, JPEG), HTML, and other document types, with built-in table extraction capabilities. Alternative implementations could use AWS-native services like **Amazon Textract** and **Amazon Comprehend**, or other open-source document processing frameworks. ECS tasks scale horizontally based on queue depth using CloudWatch metrics and Application Auto Scaling policies.

Each ECS task retrieves a batch of messages, downloads the corresponding source documents from the raw S3 bucket, and executes the document processing pipeline:
+ **Format Detection & Element Extraction** — The processing service automatically detects document format and extracts structured elements including text blocks, tables, images, headers, footers, and metadata. When using unstructured.io, these capabilities are built-in. For AWS-native implementations, **Amazon Textract** provides OCR and table extraction, while **Amazon Rekognition** handles image analysis.
+ **Plain Text Normalization** — Extracted elements are combined to create a plain text representation of the document, preserving semantic structure while removing formatting artifacts. Tables are converted to structured text representations.
+ **Text Chunking** — The plain text representation is segmented into chunks optimized for downstream embedding and retrieval. Each chunk is written as a separate file following the naming convention: `<UUID>-chunk-1.txt`, `<UUID>-chunk-2.txt`, ..., `<UUID>-chunk-n.txt`, where the UUID matches the processing job ID assigned in Step 1.
+ **Metadata Generation** — A metadata file is created with the same UUID used for the chunk filenames (e.g., `<UUID>-metadata.json`). The metadata file includes:
  + Processing job UUID
  + Source document S3 key and bucket
  + Total number of chunks generated
  + Per-chunk details: page numbers included, token count, character count, chunk sequence number
  + Document-level metadata: file type, processing timestamp, extraction confidence, detected language
  + Chunk file references/URLs (S3 keys for each chunk file)

The Document Processing Service writes all output — chunk files (`<UUID>-chunk-*.txt`) and metadata file (`<UUID>-metadata.json`) — to the **NORMALIZED S3 Bucket** designated for processed documents. Upon successful S3 write, the service deletes the original message from the SQS queue to prevent reprocessing.

**4. NORMALIZED S3 Bucket → AWS Lambda (Completion Handler)** When new normalized documents (metadata files) are written to the NORMALIZED S3 Bucket, an S3 event notification triggers an **AWS Lambda function** that acts as the completion handler. The Lambda function reads the metadata file to extract processing details and prepares the event payload for downstream subscribers.

**5. AWS Lambda → Amazon SNS (Normalized Document Processing Topic)** The completion handler Lambda function publishes a document processing completion event to the **Normalized Document Processing SNS Topic**. The SNS message payload includes:
+ Processing job UUID
+ Source document S3 key
+ Metadata file S3 key/URL
+ Chunk file S3 keys/URLs (array of references to `<UUID>-chunk-*.txt` files)
+ Number of chunks generated
+ Total token count across all chunks
+ Processing status (`SUCCESS`, `PARTIAL_SUCCESS`, `FAILED`)
+ Document metadata (file type, language, page count)

**SNS Topic with SQS Fan-out Pattern** — The Normalized Document Processing SNS Topic is configured with an **SQS fan-out pattern** for extensibility and parallel processing. Each downstream processing service subscribes to the SNS topic via its own dedicated SQS queue, enabling:
+ **Independent scaling** — Each subscriber (GraphRAG, Information Extraction, Search Indexing) scales independently based on its own queue depth
+ **Fault isolation** — Failures in one subscriber do not impact others
+ **Parallel execution** — Multiple downstream processes consume the same normalized document event simultaneously without blocking each other
+ **Replay capability** — SQS message retention allows subscribers to replay events if processing fails

Downstream subscribers include:
+ **GraphRAG Service** — Subscribes to build concept graphs and vector embeddings using the **Amazon Neptune GraphRAG toolkit** (covered in next architecture diagram). Processes chunks independently and in parallel with other subscribers.
+ **Information Extraction Service** — Extracts structured entities, relationships, and domain-specific knowledge from normalized chunks (covered in subsequent architecture diagram). Operates independently of GraphRAG ingest.
+ **Search Indexing Service** — Updates full-text and semantic search indexes in **Amazon OpenSearch Serverless**
+ **Audit & Governance Services** — Logs document processing events for compliance and lineage tracking

SNS message filtering policies can route events based on document type, classification, or processing outcome, ensuring subscribers receive only relevant events.

## Processing Capabilities by Document Type (unstructured.io)
<a name="processing-capabilities-by-document-type--unstructured.io-.1f55d620-5919-5a25-ac35-c088946c4f29"></a>

|
|
| Document Type | Direct Processing | Table Extraction | Additional AWS Services (Optional) |
| --- |--- |--- |--- |
| PDF (text-based) | ✅ Yes | ✅ Yes | Amazon Textract (enhanced table extraction) |
| PDF (scanned/image) | ✅ Yes with OCR | ✅ Yes | Amazon Textract (higher accuracy OCR) |
| DOCX, XLSX, PPTX | ✅ Yes | ✅ Yes | — |
| Images (PNG, JPG) | ✅ Yes with OCR | ❌ No | Amazon Rekognition (object detection, scene analysis) |
| HTML, Markdown | ✅ Yes | ✅ Yes | — |
| Email (EML, MSG) | ✅ Yes | ❌ No | — |

*Note: This table reflects unstructured.io capabilities. Alternative implementations using AWS-native services (Textract, Comprehend) or other frameworks will have different capability profiles.*

### Cross-Cutting Concerns
<a name="cross-cutting-concerns.06d7d316-9691-5687-a0a2-c25b3cbc5888"></a>
+ **Scalability:** S3 and SQS provide virtually unlimited throughput. ECS tasks auto-scale based on SQS queue depth. SNS with SQS fan-out enables independent scaling of downstream subscribers. Lambda functions scale automatically to handle S3 and SNS event volumes.
+ **Error Handling:** SQS visibility timeout prevents duplicate processing during retries. Dead-letter queues (DLQ) capture failed messages after maximum retry attempts. CloudWatch Alarms monitor DLQ depth and ECS task failure rates. Failed jobs are logged with detailed error context for manual remediation.
+ **Security:** S3 buckets enforce server-side encryption (SSE-S3 or SSE-KMS). IAM execution roles for Lambda and ECS tasks follow least-privilege access to S3, SQS, SNS, and Secrets Manager. VPC endpoints ensure private connectivity to AWS services without traversing the public internet.
+ **Guardrails:** 100 MB file size limit enforced at ingest (Step 1). Additional guardrails can include maximum page count, supported file types whitelist, and virus scanning (Amazon GuardDuty Malware Protection or ClamAV).
+ **Idempotency:** Document Processing Service checks for previously processed UUIDs before initiating extraction, preventing duplicate processing of SQS message retries.
+ **Observability:** OpenTelemetry traces propagate from S3 upload → Lambda → SQS → ECS processing → S3 output → Lambda → SNS → SQS fan-out, providing end-to-end visibility via **AWS X-Ray**. **Amazon CloudWatch Logs** capture chunk counts, token counts, processing latency per document type, and error details. CloudWatch Metrics track ingest rate, processing throughput, queue depth, and fan-out latency.
+ **Cost Optimization:** S3 Intelligent-Tiering automatically moves infrequently accessed normalized documents to lower-cost storage classes. ECS Fargate Spot can reduce compute costs for fault-tolerant processing workloads. SQS fan-out pattern eliminates the need for custom routing logic, reducing Lambda invocations.

This document ingest pipeline provides a **scalable, fault-tolerant, and event-driven architecture** for normalizing unstructured content at scale. The **SNS with SQS fan-out pattern** enables parallel, independent downstream processing — ensuring that GraphRAG indexing, Information Extraction, and other workflows can scale and fail independently without impacting each other.

## GraphRAG Ingest
<a name="graphrag-ingest.5ee12d63-77fd-5671-acab-f88b5985a7cd"></a>

### Data Flow — GraphRAG Ingest
<a name="data-flow---graphrag-ingest.b37f4181-a19e-5b09-98de-035a7e412134"></a>

**1. Amazon SNS → Amazon SQS (Normalized Document Processing Event)** The **Normalized Document Processing SNS Topic** (from the Document Ingest Pipeline) publishes document completion events to an **Amazon SQS queue** dedicated to the GraphRAG Service. This implements the SQS fan-out pattern, allowing the GraphRAG service to scale independently from other downstream subscribers (Information Extraction, Search Indexing, etc.). The SQS message contains the processing job UUID, metadata file S3 key/URL, chunk file S3 keys/URLs, and document metadata from the normalization pipeline.

**2. Amazon SQS → AWS Lambda (GraphRAG Orchestrator)** An **AWS Lambda function** polls the SQS queue and is triggered when new messages arrive. The Lambda function acts as the GraphRAG orchestration layer, deserializing the SQS message payload, validating the event structure, and coordinating the GraphRAG ingest workflow (concept extraction, graph construction, and vector embedding indexing). The Lambda function prepares the invocation payload for the GraphRAG Service, including references to the normalized document chunks and metadata in S3. For high-volume scenarios, the Lambda can batch multiple document events together to optimize ECS task utilization.

**3. AWS Lambda → GraphRAG Service (Amazon ECS)** The Lambda function invokes the **GraphRAG Service** deployed as containerized tasks on **Amazon ECS** (with **Fargate** or **EC2** instances). The **Amazon Neptune GraphRAG toolkit is a good choice** for implementing this service — it provides a framework for automating the construction of a graph with vector embeddings from unstructured data, and composing question-answering strategies that query this graph to retrieve structurally relevant information when answering user questions. The toolkit includes purpose-built capabilities for concept extraction, graph construction, and vector embedding generation optimized for Neptune. Alternative implementations could use other graph construction frameworks or custom LLM-based extraction pipelines. The ECS service scales horizontally based on queue depth or direct Lambda invocations, enabling parallel processing of multiple documents simultaneously.

**4. GraphRAG Service → S3 Bucket (Retrieve Normalized Chunks)** The GraphRAG Service retrieves the normalized document chunks and metadata file from the **NORMALIZED S3 Bucket** using the S3 keys provided in the event payload. The service reads:
+ Chunk text files (`<UUID>-chunk-1.txt`, `<UUID>-chunk-2.txt`, etc.)
+ Metadata file (`<UUID>-metadata.json`) containing token counts, page references, chunk sequence numbers, and document structure

The service processes each chunk through the GraphRAG ingest pipeline:
+ **Concept & Topic Extraction** — Uses Amazon Bedrock foundation models or other LLMs to extract key concepts, topics, entities, and themes from each chunk. Concepts are identified with semantic labels and definitions.
+ **Relationship Detection** — Identifies semantic relationships between extracted concepts (e.g., "relates to", "is a type of", "mentioned in context with", "co-occurs with").
+ **Vector Embedding Generation** — Generates dense vector embeddings for each concept/topic and chunk using Amazon Bedrock embeddings models (e.g., Amazon Titan Embeddings, Cohere Embed).
+ **Graph Construction** — Builds an RDF graph structure connecting concepts to each other, to their source document chunks, and to parent documents.

**5. GraphRAG Service → Neptune DB (Lexical Graph Database)** The GraphRAG Service writes the constructed concept graph to **Amazon Neptune DB** within the **Lexical Graph Database**. The graph includes:
+ **Concept/Topic nodes** — Each extracted concept as an RDF resource with properties (`rdfs:label`, `skos:definition`, concept type, extraction confidence)
+ **Document chunk nodes** — References to the source chunks from which concepts were extracted, with metadata (page numbers, token counts, chunk sequence)
+ **Document nodes** — Top-level document metadata and references to source files in S3
+ **Concept-to-concept relationships** — Semantic associations discovered between concepts (stored as RDF triples)
+ **Concept-to-chunk relationships** — Links from concepts to the specific document chunks where they appear, enabling provenance and citation
+ **Chunk-to-document relationships** — Links from chunks to their parent documents

Neptune's native RDF and SPARQL support enables efficient graph traversal and querying across the lexical graph. The service uses Neptune's bulk load API or SPARQL INSERT queries to persist the graph data. Named graphs can be used to organize concepts by document, domain, or processing batch for easier management and querying.

**6. GraphRAG Service → OpenSearch (Vector Embeddings)** In parallel with writing to Neptune (Step 5), the GraphRAG Service indexes the vector embeddings into **Amazon OpenSearch Serverless** (also part of the **Lexical Graph Database**). OpenSearch stores:
+ **Concept/Topic embeddings** — Dense vectors representing the semantic meaning of each concept
+ **Chunk embeddings** — Dense vectors representing the semantic content of each document chunk
+ **Metadata** — Concept labels, chunk IDs, document IDs, and references back to Neptune graph nodes (via concept IRI or chunk ID)

OpenSearch's k-NN (k-nearest neighbors) plugin enables fast semantic similarity search across concepts and chunks. Each embedding document in OpenSearch includes a reference to the corresponding Neptune graph node, enabling hybrid retrieval that combines:
+ **Vector similarity search** in OpenSearch (semantic matching based on embeddings)
+ **Graph traversal** in Neptune (relationship following, multi-hop reasoning, and context expansion)

**Alternative: Amazon Neptune Analytics** — Instead of using separate Neptune DB and OpenSearch services, **Amazon Neptune Analytics** can serve as the unified Lexical Graph Database, providing integrated vector storage without requiring a separate vector store. Neptune Analytics supports both graph queries and vector similarity search natively, simplifying the architecture.

## GraphRAG Output — Lexical Graph Structure
<a name="graphrag-output---lexical-graph-structure.c64c5dfb-dd52-5019-990d-33fab61592b9"></a>

|
|
| Graph Component | Description | Storage |
| --- |--- |--- |
| **Concept/Topic Nodes** | Extracted topics, themes, entities with labels and definitions | Neptune (RDF resources) |
| **Concept Embeddings** | Vector representations of concepts for semantic search | OpenSearch (k-NN vectors) or Neptune Analytics |
| **Document Chunk Nodes** | Normalized text chunks with metadata (page, tokens, sequence) | Neptune (RDF resources) |
| **Chunk Embeddings** | Vector representations of chunk content | OpenSearch (k-NN vectors) or Neptune Analytics |
| **Document Nodes** | Top-level document metadata and source references | Neptune (RDF resources) |
| **Concept-Concept Edges** | Semantic relationships between concepts (co-occurrence, similarity) | Neptune (RDF triples) |
| **Concept-Chunk Edges** | Links from concepts to chunks where they appear | Neptune (RDF triples) |
| **Chunk-Document Edges** | Links from chunks to parent documents | Neptune (RDF triples) |

### Cross-Cutting Concerns
<a name="cross-cutting-concerns.aea2ea6a-9f0c-52ab-ab15-b422064a3a40"></a>
+ **Scalability:** SQS and Lambda enable elastic scaling of GraphRAG ingest pipleine. ECS tasks auto-scale based on queue depth or processing load. Neptune supports read replicas for query scalability. OpenSearch Serverless automatically scales compute and storage based on workload.
+ **Error Handling:** SQS visibility timeout and retry policies handle transient failures. Dead-letter queue (DLQ) captures failed GraphRAG ingest jobs after maximum retry attempts. CloudWatch Alarms monitor DLQ depth and ECS task failures.
+ **Security:** Lambda execution roles grant least-privilege access to SQS, S3, ECS, Neptune, OpenSearch, and Bedrock. Neptune and OpenSearch are VPC-native with private subnet access. S3 buckets enforce encryption at rest (SSE-KMS). VPC endpoints ensure private connectivity to AWS services.
+ **Idempotency:** GraphRAG Service checks for previously processed document UUIDs in Neptune before initiating extraction, preventing duplicate graph construction from SQS message retries.
+ **Observability:** OpenTelemetry traces propagate from SNS → SQS → Lambda → ECS → Neptune/OpenSearch writes, providing end-to-end visibility via **AWS X-Ray**. CloudWatch Logs capture concept extraction results, embedding generation latency, graph write statistics, and processing errors. CloudWatch Metrics track processing throughput, concept count per document, vector indexing latency, and queue depth.
+ **Cost Optimization:** ECS Fargate Spot reduces compute costs for GraphRAG ingest. S3 Intelligent-Tiering optimizes storage costs for normalized chunks. OpenSearch Serverless charges only for actual usage. Neptune's serverless option (if using Neptune Analytics) eliminates idle capacity costs. Bedrock foundation models are invoked on-demand with pay-per-token pricing.
+ **Hybrid Retrieval Pattern:** The combination of Neptune (graph) and OpenSearch (vector) enables advanced RAG workflows:

  1. Start with vector similarity search in OpenSearch to find semantically related concepts/chunks

  1. Expand results via graph traversal in Neptune to discover related concepts and additional context

  1. Return enriched results with both semantic relevance (vector similarity) and structural context (graph relationships)

This GraphRAG architecture enables **semantic understanding of unstructured documents at scale**, building a queryable graph of concepts, topics, and their relationships that powers advanced retrieval-augmented generation (RAG) for agentic AI applications. The Lexical Graph Database serves as the semantic index layer between raw documents and agent reasoning workflows, enabling both semantic search and graph-based reasoning over document content.

## GraphRAG Retrieval
<a name="graphrag-retrieval.0bc027c0-19c8-52b4-83d5-967959072085"></a>

### Data Flow — GraphRAG Retrieval
<a name="data-flow---graphrag-retrieval.08a80d5a-2ad9-5b89-a2b7-c99b02868c87"></a>

**1. REST API → GraphRAG Service (Amazon ECS)** A client initiates a retrieval request via a **REST API** endpoint, invoking the **GraphRAG Service** deployed as containerized tasks on **Amazon ECS** (with Fargate or EC2 instances) within the VPC. The API request includes:
+ **Query input** — Natural language question or search query
+ **Similarity threshold** — Minimum cosine similarity score for vector search results (e.g., 0.7)
+ **Directives/hints** — Optional parameters such as document type filters, date ranges, ontology scope, result limit (`top_k`), or traversal depth

The request is authenticated via JWT/OIDC bearer tokens propagated by the AgentCore Gateway. The GraphRAG Service acts as the orchestration layer for hybrid retrieval, coordinating vector similarity search and graph traversal to retrieve relevant document chunks and concepts.

**2. GraphRAG Service → Amazon Bedrock (Guardrails & Embedding Generation)** The GraphRAG Service applies **guardrails to enforce policy** before processing the query. AWS provides **Amazon Bedrock Guardrails** as a guardrail capability, which may satisfy policy requirements such as:
+ **Detecting and redacting PII** — Identifying and removing personally identifiable information from the query
+ **Removing toxic content** — Filtering offensive, harmful, or inappropriate language
+ **Blocking sensitive topics** — Preventing queries related to restricted domains

After applying guardrails, the service **creates a vector embedding of the query** using an embedding model. One option is **Amazon Titan Embeddings** (via Amazon Bedrock), which generates dense vector representations of the query text. The embedding model used must match the model used during GraphRAG indexing (Document Ingest Pipeline) to ensure semantic consistency.

**3. GraphRAG Service → Amazon OpenSearch Service (Vector Similarity Search)** The GraphRAG Service **submits the vector embedding of the query** and executes a **semantic similarity search** against **Amazon OpenSearch Service** (commonly **OpenSearch Serverless** for auto-scaling and cost efficiency). The service performs a k-NN (k-nearest neighbors) search against the indexed vector embeddings of concepts, topics, and document chunks. OpenSearch returns:
+ **Document chunk identifiers** that are semantically similar (cosine similarity **greater than or equal to the threshold**)
+ **The most similar results** based on a limit (`top_k`)
+ **Similarity scores** for each result
+ **Metadata** including concept labels, chunk text snippets, and references to Neptune graph nodes (concept IRIs, chunk IDs)

This vector search provides the initial set of semantically relevant results based on embedding similarity.

**4. GraphRAG Service → Lexical Graph Database (Neptune DB) — Graph Traversal** The GraphRAG Service **issues a query to the Lexical Graph Database (Neptune DB)** with a **graph traversal based on the identifiers of the returned document chunks** from Step 3. The service executes SPARQL queries to:
+ Retrieve full concept/topic nodes with properties (`rdfs:label`, `skos:definition`, extraction confidence, provenance)
+ **Traverse the extracted topics and concepts** to find additional topics/concepts that are related to the documents
+ Follow concept-to-concept relationships (co-occurrence, semantic similarity, domain relationships)
+ Follow concept-to-chunk relationships to discover additional document chunks that mention related concepts
+ Retrieve document chunk metadata (page numbers, token counts, chunk sequence, source document references)
+ Expand context by following multi-hop relationships (e.g., "retrieve all concepts related to the matched concept within 2 hops")

**Neptune returns the graph of topics/concepts, document chunks, and documents**, providing structural context that enriches the vector search results. This graph traversal **discovers additional document chunks** that may not have been semantically similar to the query but are contextually relevant through their relationships to matched concepts.

**5. GraphRAG Service → S3 Bucket (Document Chunk Content Retrieval)** For the relevant document chunks identified through Steps 3-4, the GraphRAG Service **retrieves the content for document chunks and documents** that are **stored cost-effectively in S3** (where they were processed by the Document Ingest Pipeline). Using the S3 keys stored in Neptune's chunk metadata, the service fetches:
+ **Chunk text files** (`<UUID>-chunk-1.txt`, `<UUID>-chunk-2.txt`, etc.) containing the normalized text content
+ **Associated metadata files** (`<UUID>-metadata.json`) with page numbers, token counts, and source document references

This step ensures that the service can return the actual text content to the user or agent, not just chunk IDs or references. The retrieved chunks include the original normalized text, enabling citation with exact passages and page numbers.

**6. GraphRAG Service → REST API Response** The GraphRAG Service aggregates and ranks the results from vector search (Step 3), graph traversal (Step 4), and chunk retrieval (Step 5), then returns a unified response to the REST API client:
+ **Ranked results** — Concepts and document chunks ordered by relevance (combining vector similarity scores and graph-based relevance metrics)
+ **Concept metadata** — Labels, definitions, related concepts, extraction confidence, provenance
+ **Document chunks** — Full text content with page numbers, chunk sequence, and source document references
+ **Provenance** — Links from concepts to source chunks and documents, enabling citation and traceability
+ **Graph context** — Related concepts and relationships discovered through graph traversal

The response enables downstream consumers (Q&A Agent, chatbots, user interfaces) to present semantically grounded, citation-backed answers with full context.

## Hybrid Retrieval — Combining Vector Search and Graph Traversal
<a name="hybrid-retrieval---combining-vector-search-and-graph-traversal.3da303a9-c576-50be-9615-27251782e80c"></a>

The power of GraphRAG retrieval lies in combining:

1. **Vector similarity search (OpenSearch)** — Fast, semantic matching based on embeddings to find relevant concepts and chunks

1. **Graph traversal (Neptune)** — Structural context, relationship following, and multi-hop reasoning to discover related concepts and supporting evidence that may not be semantically similar but are contextually relevant

This hybrid approach outperforms vector-only or graph-only retrieval by balancing semantic relevance with structural context, enabling more comprehensive and accurate question answering.

### Cross-Cutting Concerns
<a name="cross-cutting-concerns.8476d095-9321-508b-91e1-6c0fc5b23d7c"></a>
+ **Guardrails Integration** — Amazon Bedrock Guardrails are applied at the query entry point to enforce policy before processing, ensuring that sensitive or inappropriate queries are filtered before consuming downstream resources.
+ **Embedding Consistency** — The embedding model used for query vectorization (e.g., Amazon Titan Embeddings) must match the model used during GraphRAG indexing to ensure semantic consistency and accurate similarity scoring.
+ **Performance** — Vector search in OpenSearch is highly parallelizable and returns results in milliseconds. Graph traversal in Neptune adds latency proportional to traversal depth but is optimized using SPARQL query planning and Neptune's graph-native storage.
+ **Scalability** — ECS auto-scales based on query volume. OpenSearch Serverless scales compute and storage automatically. Neptune supports read replicas for query scaling.
+ **Observability** — OpenTelemetry traces propagate from REST API → GraphRAG Service → Bedrock (guardrails/embeddings) → OpenSearch query → Neptune query → S3 retrieval, providing end-to-end visibility via AWS X-Ray. CloudWatch Metrics track vector search latency, graph traversal depth, guardrail invocations, and result quality.
+ **Cost Optimization** — OpenSearch Serverless charges only for actual usage. S3 Intelligent-Tiering optimizes storage costs for infrequently accessed chunks. Bedrock Guardrails and Titan Embeddings are pay-per-use, minimizing idle capacity costs.

This GraphRAG Retrieval architecture enables **semantic, context-aware document and concept retrieval** that powers RAG workflows for agentic AI applications, combining the strengths of vector embeddings, guardrails, and knowledge graphs to deliver accurate, explainable, and citation-backed answers.

## Information Extraction
<a name="information-extraction.56b26184-b141-55f0-844c-6b8a05ab8078"></a>

### Data Flow — Information Extraction Processing
<a name="data-flow---information-extraction-processing.4d639cce-6cb9-5eb7-a6c8-57a5f982c113"></a>

**1. Amazon SNS → Amazon SQS (Normalized Document Processing Event)** The **Normalized Document Processing SNS Topic** (from the Document Ingest Pipeline) publishes document completion events to an **Amazon SQS queue** dedicated to the Information Extraction Service. This implements the SQS fan-out pattern, allowing the Information Extraction processor to scale independently from other downstream subscribers (GraphRAG, Search Indexing, etc.). The SQS message contains the processing job UUID, metadata file S3 key/URL, chunk file S3 keys/URLs, and document metadata from the normalization pipeline. This queue operates in parallel with the GraphRAG ingest queue, enabling simultaneous, independent processing of the same normalized documents.

**2. Amazon SQS → AWS Lambda (Information Extraction Orchestrator)** An **AWS Lambda function** polls the SQS queue and is triggered when new messages arrive. The Lambda function acts as the Information Extraction orchestration layer, deserializing the SQS message payload, validating the event structure, and determining the appropriate extraction workflow based on document type and metadata. The Lambda function prepares the invocation payload for the Information Extraction Service, including references to the normalized document chunks and metadata in S3. For high-volume scenarios, the Lambda can batch multiple document events together to optimize ECS task utilization.

**3. AWS Lambda → Information Extraction Service (Amazon ECS)** The Lambda function invokes the **Information Extraction Service** deployed as containerized tasks on **Amazon ECS** (with **Fargate** or **EC2** instances). The service implements a **modular architecture** that allows for different extraction techniques, including **spaCy** (rule-based and statistical NLP), **LLM models** via Amazon Bedrock, **Amazon Comprehend** (for general entity recognition), and **Amazon Comprehend Medical** (for healthcare-specific extraction). The ECS service scales horizontally based on queue depth or direct Lambda invocations, enabling parallel processing of multiple documents simultaneously.

**4. Information Extraction Service → S3 Bucket (Retrieve Normalized Chunks)** The Information Extraction Service retrieves the normalized document chunks and metadata file from the **NORMALIZED S3 Bucket** (same bucket used by GraphRAG ingest) using the S3 keys provided in the event payload. The service reads:
+ Chunk text files (`<UUID>-chunk-1.txt`, `<UUID>-chunk-2.txt`, etc.)
+ Metadata file (`<UUID>-metadata.json`) containing token counts, page references, chunk sequence numbers, and document structure

The service processes each chunk through the information extraction pipeline:
+ **Ontology-Guided Entity Recognition** — Extracts entities using the provided ontologies to guide the types of information to extract. The ontology defines target entity classes (e.g., `Person`, `Organization`, `Claim`, `Diagnosis`, `Procedure`) and their expected properties. Extraction techniques (spaCy, LLM models, Amazon Comprehend) are applied based on entity type and document domain.
+ **Ontology-Guided Relationship Extraction** — Identifies semantic relationships between extracted entities using ontology-defined object properties (e.g., `employedBy`, `diagnoses`, `submittedBy`, `covers`). The ontology provides relationship constraints (domain, range) to guide extraction and validation.
+ **Codification & Normalization** — Extracted entities and relationships are codified according to the ontology vocabulary, ensuring consistency with the Knowledge Layer's T-Box. Entity identifiers are normalized (e.g., standardizing organization names, mapping codes to ontology classes).
+ **Validation & Reasoning** — Additional validation and reasoning may be performed to ensure consistency and quality of extracted entities and relationships. This includes:
  + **SHACL validation** against ontology constraints (e.g., cardinality, datatype, value ranges)
  + **Consistency checking** to detect conflicting facts or constraint violations
  + **Inference** to derive implied relationships based on ontology axioms
  + **Confidence scoring** to flag low-confidence extractions for review
+ **Provenance Tracking** — Records the source chunks, extraction technique used (LLM model, spaCy, Amazon Comprehend), confidence scores, and extraction timestamps for each extracted fact. Entities and relationships are annotated with properties indicating the extraction method.

**5. Information Extraction Service → Neptune DB (Semantic Layer Graph Database)** The Information Extraction Service writes the **ontology-based, grounded** extracted knowledge to **Amazon Neptune DB** within the **Semantic Layer Graph Database (SLGD)**. This is the curated, domain-specific knowledge graph that represents validated facts about the business domain. The extracted data includes:
+ **Entity instances** — Individuals conforming to ontology classes (e.g., `ex:Person/JohnDoe`, `ex:Organization/AcmeCorp`, `ex:Claim/CLM123456`) with typed properties
+ **Relationships** — RDF triples connecting entities via ontology-defined object properties (e.g., `ex:Claim/CLM123456 ex:submittedBy ex:Person/JohnDoe`)
+ **Attributes** — Datatype properties on entities (e.g., claim amount, submission date, diagnosis code)
+ **Provenance metadata** — Links from extracted facts back to source document chunks in the Lexical Graph Database, extraction confidence scores, extraction timestamps, and extraction methods
+ **Validation status** — Flags indicating whether facts passed SHACL validation and reasoning checks

The Semantic Layer Graph Database is **more curated** than the Lexical Graph Database — it contains only validated, ontology-aligned knowledge that has passed quality checks. Named graphs can be used to organize extracted knowledge by confidence level (e.g., high-confidence vs. candidate extractions requiring validation), source document, or extraction batch.

**6. Information Extraction Service → Neptune DB (Lexical Graph Database) — Provenance & Enrichment** In parallel with writing to the Semantic Layer Graph Database (Step 5), the Information Extraction Service writes **provenance links and enrichment metadata** to the **Lexical Graph Database (LGD)** (Neptune DB instance used by GraphRAG). The Lexical Graph Database will have **more entities and relationships** than the Semantic Layer Graph Database, as it includes:
+ **All extracted entities and relationships** — Including low-confidence extractions, candidate facts, and entities that did not pass validation for the Semantic Layer
+ **Extraction technique annotations** — Properties on entities and relationships indicating the extraction method (e.g., `ex:extractedBy "LLM Model"`, `ex:extractedBy "spaCy"`, `ex:extractedBy "Amazon Comprehend"`)
+ **Document chunk associations** — Links from extracted entities to the specific chunks in the Lexical Graph where they were mentioned, enabling provenance and citation
+ **Bidirectional references** — Enriches Lexical Graph chunk nodes with references to the structured entities extracted from them, connecting unstructured content to structured knowledge

This creates a **two-tier knowledge architecture**:
+ **Lexical Graph Database (LGD)** — Comprehensive, document-centric, includes all extractions regardless of confidence or validation status
+ **Semantic Layer Graph Database (SLGD)** — Curated, domain-centric, ontology-aligned, contains only validated knowledge

The integration between the two databases enables powerful hybrid queries:
+ **Semantic queries** — "Find all claims submitted by organization X" (queries SLGD)
+ **Provenance queries** — "Show me the document chunks where this claim appears" (traverses to LGD)
+ **Exploratory queries** — "What candidate entities were extracted but not validated?" (queries LGD for entities not in SLGD)

## Information Extraction Output — Two-Tier Knowledge Graph
<a name="information-extraction-output---two-tier-knowledge-graph.2935a2bc-2ce6-5d5b-b45b-6f7acd0dcee6"></a>

|
|
| Graph Component | Lexical Graph Database (LGD) | Semantic Layer Graph Database (SLGD) |
| --- |--- |--- |
| **Entity Instances** | All extracted entities (validated \+ candidates) | Only validated, ontology-aligned entities |
| **Relationships** | All extracted relationships | Only validated, ontology-defined relationships |
| **Extraction Metadata** | Technique, confidence, timestamp for all extractions | Validation status, reasoning results |
| **Provenance Links** | Links to source chunks and documents | Links to source chunks via LGD |
| **Curation Level** | Comprehensive, exploratory | Curated, production-ready |
| **Use Cases** | Document retrieval, exploratory analysis, debugging | Semantic queries, reasoning, agent workflows |

### Cross-Cutting Concerns
<a name="cross-cutting-concerns.00823196-3700-5cfb-82c0-2d221938b292"></a>
+ **Scalability:** SQS and Lambda enable elastic scaling of information extraction processing. ECS tasks auto-scale based on queue depth or processing load. Neptune supports read replicas for query scalability across both Graph Databases.
+ **Error Handling:** SQS visibility timeout and retry policies handle transient failures. Dead-letter queue (DLQ) captures failed extraction jobs after maximum retry attempts. CloudWatch Alarms monitor DLQ depth and ECS task failures. Failed extractions can be flagged for manual review or sent to human-in-the-loop validation workflows.
+ **Security:** Lambda execution roles grant least-privilege access to SQS, S3, ECS, Neptune (both instances), and Bedrock. Neptune instances are VPC-native with private subnet access. S3 buckets enforce encryption at rest (SSE-KMS). VPC endpoints ensure private connectivity to AWS services.
+ **Idempotency:** Information Extraction Service checks for previously processed document UUIDs in Neptune before initiating extraction, preventing duplicate entity creation from SQS message retries. Extracted entities are assigned deterministic IRIs based on source document and extracted identifiers to enable safe re-processing.
+ **Data Quality & Validation:** Extracted facts are validated against SHACL constraints defined in the ontology before being committed to the Semantic Layer Graph Database. Low-confidence extractions remain in the Lexical Graph Database for exploratory analysis.
+ **Observability:** OpenTelemetry traces propagate from SNS → SQS → Lambda → ECS → Neptune writes (both databases), providing end-to-end visibility via **AWS X-Ray**. CloudWatch Logs capture entity extraction results, relationship counts, confidence scores, validation outcomes, and processing errors. CloudWatch Metrics track processing throughput, entity count per document, extraction latency, validation pass rate, and queue depth.
+ **Cost Optimization:** ECS Fargate Spot reduces compute costs for information extraction processing. Bedrock foundation models are invoked on-demand with pay-per-token pricing. Neptune's serverless option eliminates idle capacity costs. Modular extraction architecture allows cost-effective technique selection (e.g., spaCy for simple entities, LLMs for complex relationships).
+ **Modular Extraction Architecture:** The service supports pluggable extraction techniques:
  + **spaCy** — Fast, rule-based extraction for well-defined entity types (names, dates, identifiers)
  + **LLM Models (Bedrock)** — Flexible, context-aware extraction for complex entities and relationships
  + **Amazon Comprehend** — General-purpose entity recognition and sentiment analysis
  + **Amazon Comprehend Medical** — Healthcare-specific entity extraction (diagnoses, procedures, medications, anatomy)
  + **Custom Models** — Fine-tuned models for domain-specific extraction tasks

This Information Extraction processing architecture enables **structured, ontology-grounded knowledge extraction from unstructured documents at scale**, building a curated, queryable knowledge graph (SLGD) that powers semantic queries, reasoning workflows, and agent-based question answering — while maintaining comprehensive provenance and exploratory capabilities in the Lexical Graph Database (LGD). The two-tier architecture balances production-ready, validated knowledge with exploratory, comprehensive extraction results.
