---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/data-and-retrieval.html
---

# Data and retrieval

Retrieval-augmented generation (RAG) brings enterprise information into a model's context before it answers. A policy assistant, for example, searches approved documents and cites the passages behind its response. Protecting that information requires controls for source storage, ingestion, indexes, and any copies retained in conversation history.

This section of the guide explains those controls alongside the [model inference guidance](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/). The application team controls how the application retrieves information, and data owners determine who can read it and how long to retain it. [Tool access](https://dp8l2mfblnx2f.cloudfront.net/connects/tool-access/) covers applications that also query live systems.

## Security considerations
<a name="security-considerations"></a>
+ A shared retrieval identity can expose documents that the requesting user cannot read.
+ Untrusted documents can introduce unauthorized instructions or affect the accuracy of later responses.
+ Copies in indexes, caches, and memory can remain accessible after source access changes.
+ Broad ingestion permissions can admit protected or unreviewed content into a knowledge base.

## Infrastructure security
<a name="infrastructure-security"></a>

### Knowledge bases and vector storage
<a name="knowledge-bases-and-vector-storage"></a>

[Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) retrieves enterprise content and can include citations in generated responses. For a design using [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) and a customer-managed vector store, keep source documents in a protected S3 bucket and limit ingestion to an approved pipeline. Give the knowledge base service role access to that source, the selected embedding model, and its vector index. Other knowledge base types and connectors need permissions for their own data sources.

[Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html) provides a vector-store option with separate encryption, network, and data access policies. Together, these policies govern how data is encrypted, how clients connect, and which operations they can perform. Configure all three, with index writes restricted to approved ingestion identities and reads restricted to the retrieval service. Private connectivity alone does not authorize a reader. Review overlapping policies and alternate search endpoints that could bypass application authorization.

Grant the required [AWS Identity and Access Management (IAM) data-plane permissions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) as well; a data access policy alone is insufficient.

Keep unreviewed uploads in a staging bucket, separate from the [S3 source bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) available for ingestion. Enable [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) on both buckets and permit promotion only through the ingestion pipeline. Use [Amazon GuardDuty Malware Protection for S3](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malware-protection-s3.html) to scan uploads, and promote only the object version whose scan completed with `NO_THREATS_FOUND`. Keep pending, failed, unsupported, and threat-positive objects out of the ingestion source. When using [scan-result tags](https://docs.aws.amazon.com/guardduty/latest/ug/tag-based-access-s3-malware-protection.html) to control access, prevent other principals from setting or changing the GuardDuty result tag.

Validate document type, source, and permitted use before promotion; a malware scan does not validate those properties. Quarantine rejected files. Isolate document-processing compute from unrelated workloads and limit its outbound destinations and storage access.

## Identity and data security
<a name="identity-and-data-security"></a>

### Authorization and classification
<a name="authorization-and-classification"></a>

Establish a user's document permissions before the application searches the knowledge base. The [Knowledge Bases retrieval filter](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_KnowledgeBaseVectorSearchConfiguration.html) is optional in the API. When using metadata for authorization, require trusted backend code to construct the filter from verified identity and protect the metadata it evaluates. Restrict direct retrieval access so that callers cannot omit or replace this filter. Don't use a model-generated relevance filter to establish access rights. Reject requests with missing authorization context; see the [retrieval scope example](https://dp8l2mfblnx2f.cloudfront.net/bedrock-integration/#enforce-retrieval-scope-in-the-backend). Test document access through search, citations, caches, and source links, including cross-tenant queries and recently revoked permissions. Where [combining sources can reveal protected information](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/smbdb-knowledge-worker-co-pilot.html#llm-specific-security-risks), have data owners define permitted combinations and test them before release.

Ingestion credentials can read documents that an individual end user cannot. Ingestion permission does not establish retrieval entitlement. For example, the [customer-managed Confluence connector](https://docs.aws.amazon.com/bedrock/latest/userguide/confluence-data-source-connector.html) does not preserve source access restrictions for callers with retrieval permission. Apply the backend authorization above to existing deployments using that connector.

Check each connector's documented behavior. The [Salesforce connector for Amazon Bedrock Managed Knowledge Base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-ds-salesforce-acl.html) can synchronize document access control lists (ACLs) and check access at query time. The application must authenticate users and supply verified identity context. This filtering is not a security boundary and does not enforce Salesforce field-level security. Validate the selected connector's permissions and revocation behavior before relying on it.

Give ingestion and retrieval separate IAM roles scoped to their required resources. Use [AWS KMS](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-kb.html) customer managed keys where the selected knowledge base resources require customer control of encryption. Coordinate key policies with Amazon S3 and vector-store permissions. Require Transport Layer Security (TLS) on each data path. Classify chunks, embeddings, exports, and stored prompts according to the information they contain.

Apply the [shared data classification controls](https://dp8l2mfblnx2f.cloudfront.net/architecture/#apply-shared-network-and-identity-controls) before corpus admission. For scanned documents, [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) extracts text for review. Restrict access to extraction outputs and validate redaction quality before indexing. The data owner must approve the permitted use of the resulting content.

### Provenance, memory, and deletion
<a name="provenance-memory-and-deletion"></a>

Correcting or removing a source document can require changes to its derived chunks and indexes. The application needs lineage records linking source versions to those transformations so that the team can identify affected content. [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) can help organize source datasets, while the application records the RAG transformations beyond the catalog. Restrict catalog changes to data owners and approved pipelines, and assign owners to approve additions, corrections, and removal of poisoned or obsolete content.

[Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) retains conversation events and extracted context when the application needs continuity. Authorize access to actor, session, and namespace identifiers using trusted user context. Define retention for events and long-term records separately, and include memory in deletion handling when it contains retrieved data.

Reconcile source updates and deletions with ingestion completion and subsequent retrieval tests. [Deleting a Knowledge Bases data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-ds-delete.html) follows its configured deletion policy and does not delete the vector store itself. Account for failed deletion, retained Amazon S3 object versions, caches, citations, logs, and backups. Document legal retention exceptions and prevent removed content from reappearing through later ingestion.

## AI application security
<a name="ai-application-security"></a>

In the [Amazon Bedrock Knowledge Bases retrieval-and-generation flow](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html), [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) evaluates the input and generated response, **not the retrieved references**. Enforce retrieval authorization before generation and separately validate content admitted to the index. A response filter cannot repair an unauthorized retrieval.

Include custom ingestion, retrieval, and caching code in the [application code review workflow](https://dp8l2mfblnx2f.cloudfront.net/answers/ai-applications/#review-custom-application-code-with-aws-continuum). Review the code that parses documents, constructs access filters, and assigns cache entries to users or tenants. Test proposed fixes with users who have different document permissions, including revoked access, and verify that citations cannot expose restricted source content.

### Protect retrieved context and observe data access
<a name="protect-retrieved-context-and-observe-data-access"></a>

Retrieved text, metadata, and extracted document content can contain instructions intended to redirect the model. Treat them as untrusted input, preserve source attribution, and separate the content from application instructions. Apply Guardrails to selected content paths after checking inspection coverage. Evaluate poisoned documents, misleading citations, and unsupported answers alongside retrieval quality.

Collect [ingestion logs](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html) and application retrieval metrics in [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), and configure alarms for failures. Correlate these with [AWS CloudTrail](https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html) records. Enable Knowledge Bases data events for `Retrieve` and `RetrieveAndGenerate`, and S3 data events for access to the source documents that require auditing. Keep query text and retrieved content out of routine logs unless investigation requirements justify retaining them. Apply the [shared detection controls](https://dp8l2mfblnx2f.cloudfront.net/architecture/#detect-threats-in-ai-workloads) to the source storage and processing resources, and record coverage gaps.

## Design considerations
<a name="design-considerations"></a>

Choose whether tenants [share a knowledge base and vector index or use separate knowledge bases](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/kg-per-tenant-kb.html), based on data sensitivity and contractual or regulatory requirements. Enforce each user's document permissions on each retrieval path. Define acceptable ingestion lag and revocation delay. Test access denial and deletion under partial failures, and retain provenance metadata, such as source document identifiers and versions, to identify affected answers without copying the corpus into logs.
