---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-agents.html
---

# Capability 3. Providing secure access to data and systems for generative AI
<a name="gen-ai-agents"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

[Retrieval Augmented Generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/) is a foundational pattern that enhances large language model (LLM) responses by retrieving information from external knowledge bases before generating answers. This approach addresses a core limitation of foundation models (FMs): They are trained on data with a fixed knowledge cutoff and lack access to current enterprise data such as customer records, product catalogs, internal documentation, and business systems.

RAG enables the LLM to provide up-to-date, context-specific responses by dynamically pulling relevant information from enterprise data sources. However, this integration introduces critical security challenges. Securing RAG implementations requires extending defense-in-depth principles from Capability 1 and Capability 2 to address how LLMs securely use data from external sources. The following diagram illustrates recommended AWS services for the Generative AI account RAG capability.

![Recommended services for the Generative AI account RAG capability.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/79ec66a6-987a-4982-842f-c5e2062b5bea.jpeg)

The Generative AI account includes services for storing embeddings in a vector database, storing conversations for users, and maintaining a prompt store. The account includes security services to implement security guardrails and centralized security governance. Create Amazon Simple Storage Service (Amazon S3) gateway endpoints for the model invocation logs, prompt store, and knowledge base data source buckets in Amazon S3 that the VPC environment accesses. Create an Amazon CloudWatch Logs gateway endpoint for the CloudWatch logs that the VPC environment accesses.

## Rationale
<a name="agents-rationale"></a>

RAG enhances FM responses by retrieving information from external, authoritative knowledge bases before generating answers. This approach overcomes FM limitations by providing access to up-to-date, context-specific data, improving the accuracy and relevance of generated responses.

RAG can be implemented across Scopes 2-5 of the [Generative AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/). Scope 2 applications represent scenarios where organizations use third-party AI services (like Salesforce Einstein or ChatGPT) where the service provider controls both the FM and the application layer. You control only the prompts and customer data you provide to the service. You can enhance responses from third-party enterprise applications by implementing RAG to extract information from internal data, which augments queries processed by the third-party application. In Scope 2, you implement RAG either by connecting to your organization's data sources or by uploading and referencing custom documents.

In Scope 3, you build a generative AI application using a pre-trained FM such as those offered on Amazon Bedrock. You control your application and any customer data your application uses. The FM provider controls the pre-trained model and its training data.

RAG systems face the following unique security risks:
+ Data exfiltration of RAG data sources by threat actors
+ Poisoning of RAG data sources with prompt injections or malware
+ Unauthorized access to sensitive information through inadequate access controls
+ Sensitive information disclosure through uncontrolled model outputs
+ Lack of data provenance leading to compliance and auditability challenges

**Design considerations**

Avoid customizing an FM with sensitive data (for more information, see Capability 2). Instead, use the RAG technique to interact with sensitive information. RAG provides the following advantages:
+ **Tighter control and visibility** – Keep sensitive data separate from the model. You can edit, update, or remove data without retraining the model, ensuring data governance and compliance with regulatory requirements.
+ **Reduced sensitive information disclosure** – RAG controls interactions with sensitive data during model invocation. This reduces the risk of unintended disclosure that occurs when you incorporate data directly into the model's parameters.
+ **Flexibility and adaptability** – Update or modify sensitive information as data requirements or regulations change without retraining or rebuilding the language model.
+ **Enhanced security posture** – Implement multiple security layers including metadata filtering, access controls, and data redaction at different stages of the RAG pipeline.

### Multi-layered security strategy
<a name="multi-layered-security-strategy.996c819c-3b60-5da6-918a-40bd04a7abf1"></a>

Implement a defense-in-depth approach with security controls at the following stages:
+ **Ingestion time** – Filter and validate data before it enters the knowledge base.
+ **Storage level** – Encrypt data at rest and implement access controls.
+ **Retrieval time** – Apply metadata filtering and role-based access controls.
+ **Inference time** – Use guardrails to filter model outputs and detect sensitive information.

### Amazon Bedrock Knowledge Bases
<a name="9999999999999999br--knowledge-bases.d10de160-614f-5a8f-ac38-f4fc08ca44b0"></a>

[Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) provides a fully managed solution for building RAG applications by securely connecting FMs to your organization's data. This service uses vector stores (such as Amazon OpenSearch Serverless) to retrieve relevant information efficiently. The FM uses this information to generate responses. Amazon Bedrock synchronizes your data from Amazon S3 to the knowledge base and generates [embeddings](https://aws.amazon.com/what-is/embeddings-in-machine-learning/) for efficient retrieval.

Key features of Amazon Bedrock Knowledge Bases include the following:
+ **Source attribution** – Knowledge bases include source attribution for all retrieved information to improve transparency and minimize hallucinations. This provenance tracking enables you to:
  + Verify the accuracy of generated responses.
  + Maintain audit trails for compliance.
  + Build user trust in AI-generated content.
  + Support troubleshooting and investigations during security events.
+ **Automated vector store management** – Amazon Bedrock automatically creates and manages vector stores in OpenSearch Serverless, synchronizing data from Amazon S3 and generating embeddings for efficient retrieval.
+ **Metadata filtering** – Knowledge bases support metadata filtering capabilities that enable access control by pre-filtering the vector store based on document metadata before searching for relevant documents. This filtering reduces noise, improves retrieval accuracy, and enforces data access policies.
+ **Multimodal support** – Knowledge bases process documents with visual resources, extracting and retrieving images in responses to queries, which supports comprehensive document understanding.

For each vector database option, configure the following:
+ Field mappings for vector embeddings, text chunks, and metadata
+ [Customer managed AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) for encrypting secrets and data
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) secrets for authentication credentials
+ Network connectivity through [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) where supported

## Security considerations
<a name="agents-security"></a>

Generative AI RAG workloads face unique risks, including data exfiltration of RAG data sources. Another risk is indirect prompt injection attacks where threat actors insert malicious documents into the knowledge base to manipulate model outputs.

Amazon Bedrock knowledge bases provide security controls for data protection, access control, network security, logging and monitoring, and metadata filtering for secure retrieval. These controls address data exfiltration and unauthorized access risks. To mitigate indirect prompt injection attacks, implement input validation and content filtering on documents before ingestion.

## Remediations
<a name="agents-remediations"></a>

This section reviews the AWS services and features that address the risks that are specific to this capability.

### Data protection
<a name="data-protection.1163c219-90e5-5d63-b6cf-2235d8d1169f"></a>

Encrypt your knowledge base data in transit and at rest using an AWS Key Management Service (AWS KMS) customer managed key. When you configure a data ingestion job for your knowledge base, encrypt the job with a customer managed key. If you let Amazon Bedrock create a vector store in Amazon OpenSearch Service for your knowledge base, Amazon Bedrock passes an AWS KMS key of your choice to OpenSearch Service for encryption.

You can encrypt sessions in which you generate responses from querying a knowledge base with an AWS KMS key. You store the data sources for your knowledge base in your Amazon S3 bucket. If you encrypt your data sources in Amazon S3 with a customer managed key, attach the required policies to your [knowledge base service role](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html).

If you configure vector stores with AWS Secrets Manager secrets, encrypt the secrets with customer managed keys and attach decryption permissions to the knowledge base service role. Ensure all data in transit uses TLS 1.2 or higher with secure cipher suites.

For more information and the policies to use, see [Encryption of knowledge base resources](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-kb.html) in the Amazon Bedrock documentation.

### Data classification and handling
<a name="data-classification-and-handling.b2be39cb-6c71-5060-8383-ce9460a244dc"></a>

Implement data classification schemes to categorize data based on sensitivity and criticality. Establish clear classification tiers (for example, Public, Internal, Confidential, and Restricted) with specific handling requirements for each level.

Classify data at the point of ingestion. Use automated tools like Amazon Macie to detect and classify sensitive data in Amazon S3 buckets that contain knowledge base data sources.

Use AWS resource tags to categorize sensitive data and monitor compliance with protection requirements. [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) tag policies enforce tagging standards across accounts.

Maintain a data catalog that maps data in your organization, its location, sensitivity level, and the controls in place to protect it. [AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html) supports metadata storage and management.

### Data lineage and provenance tracking
<a name="data-lineage-and-provenance-tracking.9426e1cc-5d18-56ad-8f8f-94b89bf9d33a"></a>

Implement comprehensive data provenance tracking to record the history of data as it progresses through your RAG workload.

Data lineage provides the following benefits:
+ **Regulatory compliance** – Demonstrates data handling practices for audits and certifications
+ **Troubleshooting** – Enables root cause analysis when data quality issues arise
+ **Security investigations** – Provides audit trails during security incidents
+ **Data quality** – Ensures confidence in data origin, transformations, and ownership
+ **Impact analysis** – Identifies downstream effects of data changes

Implementation approaches for data provenance tracking include the following:
+ **AWS Glue Data Catalog** – Store metadata and track lineage across data processing pipelines.
+ **Amazon SageMaker ML Lineage Tracking** – Track model training data, hyperparameters, and deployment artifacts.
+ **AWS CloudTrail** – Capture API activities across AI services for audit trails.
+ **Amazon CloudWatch** – Monitor data quality, usage, and model drift with generative AI-driven debugging and root cause analysis.
+ **Third-party integration** – Support open telemetry with integration to third-party observability tools.

### Identity and access management
<a name="identity-and-access-management.6c85598b-3d09-58f6-a756-ba573721d12d"></a>

Create a custom service role for knowledge bases for Amazon Bedrock following the principle of least privilege. Create a [trust relationship](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-permissions.html#agents-permissions-trust) that allows Amazon Bedrock to assume this role, and create and manage knowledge bases.

Attach identity policies to the custom knowledge base service role that grant permissions to access Amazon Bedrock models, data sources in Amazon S3, vector databases, and encryption keys. For the complete list of required permissions, see [Create a service role for Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html) in the Amazon Bedrock documentation.

Knowledge bases support security configurations to set up data access policies for your knowledge base and network access policies for your private Amazon OpenSearch Serverless knowledge base. For more information, see [Create a knowledge base by connecting to a data source in Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html) in the Amazon Bedrock documentation.

### Metadata filtering for secure retrieval
<a name="metadata-filtering-for-secure-retrieval.458f5ff2-32d1-599f-bfe5-fd842714370e"></a>

Amazon Bedrock Knowledge Bases supports [metadata filtering](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-metadata-filtering-to-improve-retrieval-accuracy/) to refine and secure contextual retrieval from vector stores. For every document added, you can supply metadata files (up to 10KB each) with attributes such as tags, dates, project IDs, and business units.

Metadata filtering enables fine-grained access control for RAG systems. By attaching metadata as key-value pairs to each vector during ingestion, you can do the following:
+ **Filter queries** – Filter queries based on user attributes such as department, role, or clearance level. For example, metadata can include `{"department": "finance", "classification": "confidential"}` to restrict access to financial data.
+ **Enforce data classification policies** – Tag vectors with sensitivity levels (public, internal, confidential, and restricted) and filter based on user permissions.
+ **Support multi-tenant architectures** – Use metadata to isolate data between different tenants or business units, ensuring data segregation in shared infrastructure.
+ **Enable temporal access controls** – Include timestamp metadata to implement time-based access restrictions or data retention policies.

It's up to the application or agent to add the correct metadata to each API call with Amazon Bedrock to filter results based on required key-value pairs.

### Input and output validation
<a name="input-and-output-validation.e2a82e65-f35a-5759-a217-87106e6c34bf"></a>

Input validation protects Amazon Bedrock knowledge bases from malicious content. Use malware protection in Amazon S3 to scan files for malicious content before uploading them to a data source. For an example implementation, see [Integrating Malware Scanning into Your Data Ingestion Pipeline with Antivirus for Amazon S3](https://aws.amazon.com/blogs/apn/integrating-malware-scanning-into-your-data-ingestion-pipeline-with-antivirus-for-amazon-s3/) (AWS Blog post).

Use Amazon Comprehend to detect and redact sensitive information in documents before indexing them in your RAG knowledge base. For an example implementation, see [Protect sensitive data in RAG applications with ](https://aws.amazon.com/blogs/machine-learning/protect-sensitive-data-in-rag-applications-with-amazon-bedrock/)Amazon Bedrock (AWS blog post). For more information, see [Detecting PII](https://docs.aws.amazon.com/comprehend/latest/dg/how-pii.html) entities in the Amazon Comprehend documentation.

Use Amazon Macie to detect and generate alerts on potential sensitive data in Amazon S3 data sources to enhance security and compliance.

## Recommended AWS services
<a name="agents-services"></a>

This section discusses the AWS services that are recommended to build this capability securely. In addition to the services in this section, use Amazon CloudWatch and AWS CloudTrail as explained in Capability 2.

### Amazon OpenSearch Serverless
<a name="amazon-9999999999999999opensearch--serverless.a96a447e-84c6-590b-9196-d65f8bda13e3"></a>

[Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.html) is an on-demand, auto-scaling configuration for Amazon OpenSearch Service. An OpenSearch Serverless collection is an OpenSearch cluster that scales compute capacity based on your application's needs. Amazon Bedrock knowledge bases use OpenSearchServerless for [embeddings](https://aws.amazon.com/what-is/embeddings-in-machine-learning/) and Amazon S3 for the [data sources](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html) that [sync](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ingest.html) with the OpenSearch Serverless [vector index](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html).

Implement [authentication and authorization](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-serverless.html) for your OpenSearch Serverless vector store following the principle of least privilege. With [data access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) in OpenSearch Serverless, you can allow users to access collections and indexes regardless of their access mechanisms or network sources. Access permissions are done at the generative AI application layer.

OpenSearch Serverless supports [server-side encryption](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html) with AWS KMS to protect data at rest. Use a customer managed key to encrypt that data. To allow the creation of an AWS KMS key for transient data storage during data ingestion, [attach a policy](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html#kb-permissions-kms-ingestion) to your knowledge bases for the Amazon Bedrock service role.

[Private access](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html) can apply to OpenSearch Serverless-managed VPC endpoints, supported AWS services such as Amazon Bedrock, or both. Use [AWS PrivateLink](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html) to create a private connection between your VPC and OpenSearch Serverless endpoint services. Use [network policy rules](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html#serverless-network-policies) to specify Amazon Bedrock access.

Monitor OpenSearch Serverless using [Amazon CloudWatch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-cloudwatch.html), which collects raw data and processes it into readable, near real-time metrics. OpenSearch Serverless integrates with [AWS CloudTrail](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/logging-using-cloudtrail.html), which captures API calls for OpenSearch Serverless as events. OpenSearch Service integrates with [Amazon EventBridge](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-monitoring-events.html) to notify you of events that affect your domains.

### Amazon S3
<a name="9999999999999999s3-.179f840f-c937-56b9-ae23-799403d5e6c4"></a>

Store your [data sources](https://docs.aws.amazon.com/bedrock/latest/userguide/s3-data-source-connector.html) for your knowledge base in an Amazon S3 bucket. If you encrypted your data sources in Amazon S3 using a custom AWS KMS key (recommended), [attach a policy](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-kb.html#encryption-kb-ds) to your knowledge base service role.

Use [malware protection](https://aws.amazon.com/blogs/apn/integrating-malware-scanning-into-your-data-ingestion-pipeline-with-antivirus-for-amazon-s3/) in Amazon S3 to scan files for malicious content before uploading them to a data source. Host your [model invocation logs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html#setup-s3-destination) and commonly used prompts as a prompt store in Amazon S3. Encrypt all buckets with a customer managed key.

For additional network security hardening, create a [gateway endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) for the S3 buckets that the VPC environment accesses. Log and monitor all access. Enable versioning if you have a business need to retain the history of Amazon S3 objects. Apply object-level immutability with [Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html). Use resource-based policies to control access to your Amazon S3 files.

### Amazon Comprehend
<a name="9999999999999999cmplong-.33aff879-5106-5b93-882e-bcd4249dece1"></a>

[Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) uses natural language processing (NLP) to extract insights from document content. You can use Amazon Comprehend to detect and redact [PII entities](https://docs.aws.amazon.com/comprehend/latest/dg/pii.html) in English or Spanish text documents.

Integrate Amazon Comprehend into your [data ingestion pipeline](https://aws.amazon.com/blogs/machine-learning/detecting-and-redacting-pii-using-amazon-comprehend/) to automatically detect and redact PII entities from documents before you index them in your RAG knowledge base. This approach helps to ensure compliance and protects user privacy. Depending on the document types, you can use Amazon Textract to [extract and send text to Amazon Comprehend](https://docs.aws.amazon.com/textract/latest/dg/textract-to-comprehend.html) for analysis and redaction.

With Amazon S3, you can encrypt your input documents when creating a text analysis, topic modeling, or custom Amazon Comprehend job. Amazon Comprehend integrates with [AWS KMS to encrypt the data](https://docs.aws.amazon.com/comprehend/latest/dg/kms-in-comprehend.html) in the storage volume for `Start*` and `Create*` jobs. Amazon Comprehend encrypts the output results of `Start*` jobs by using a customer managed key.

Use the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in [resource policies](https://docs.aws.amazon.com/comprehend/latest/dg/cross-service-confused-deputy-prevention.html) to limit the permissions that Amazon Comprehend gives another service to the resource. Use [AWS PrivateLink](https://docs.aws.amazon.com/comprehend/latest/dg/vpc-interface-endpoints.html) to create a private connection between your virtual private cloud (VPC) and Amazon Comprehend endpoint services. Implement identity-based policies for Amazon Comprehend with the [principle of least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).

Amazon Comprehend integrates with AWS CloudTrail, which captures API calls for Amazon Comprehend as events.

### Amazon Macie
<a name="9999999999999999mcelong-.7c05d260-aee8-5937-9abb-4909e91beb1a"></a>

Macie identifies [sensitive data](https://docs.aws.amazon.com/macie/latest/user/data-classification.html) in your knowledge bases that is stored as data sources, model invocation logs, and prompt stores in Amazon S3 buckets. For Macie security best practices, see the *Amazon Macie* section in Capability 2.

### AWS KMS
<a name="9999999999999999kms-.de4df8c1-9763-520f-907c-0d46b39e6e4c"></a>

Use AWS Key Management Service (AWS KMS) customer managed keys to encrypt the following:
+ [Data ingestion jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-kb.html#encryption-kb-ingestion) for your knowledge base
+ Amazon OpenSearch Service [vector database](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-kb.html#encryption-kb-oss)
+ [Sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-kb.html#encryption-kb-runtime) in which you generate responses from querying a knowledge base
+ [Model invocation logs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html#setup-s3-destination) in Amazon S3
+ Amazon S3 bucket that hosts the [data sources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
