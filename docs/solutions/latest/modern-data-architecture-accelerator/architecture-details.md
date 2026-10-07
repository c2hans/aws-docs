---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up MDAA, and how they work together.

## Architecture and Design
<a name="architecture-and-design"></a>

The first step in building a data, analytics, or AI platform with MDAA is to decide on an initial architecture. MDAA is highly flexible and can be adapted to most common data platform architectures on AWS. These include basic data lakes and data warehouses, Lake House, complex Data Mesh architectures, and generative AI development environments. The initial architecture does not need to be the target end-state architecture for the platform, as these architectures often build on each other. An MDAA configuration and deployment can be adapted iteratively from one architectural state to another.

## AWS Reference Architectures
<a name="aws-reference-architectures"></a>

### Modern Data Architecture (Lake House)
<a name="modern-data-architecture"></a>

The AWS reference architecture for data platforms is the Modern Data Architecture, sometimes referred to as Lake House. This architecture provides a flexible, scalable foundation on which virtually any data problem — using analytics, data science, or AI/ML — can be solved on AWS. The architecture is also fully open and interoperable with data capabilities both inside and outside of AWS.

At the core of the Modern Data Architecture is a scalable, Amazon S3-based data lake. This data lake is wrapped with a unified data governance layer and a DataOps layer that facilitates seamless data movement between the core data lake and purpose-built analytics services on the perimeter. The selection of purpose-built analytics services in a Modern Data Architecture is typically tailored to the specific use cases to be solved on the platform.

MDAA has the flexibility to support virtually any derivative form of the AWS Modern Data Architecture, including the core S3 data lake, the unified governance layer (AWS Glue and AWS Lake Formation), the seamless data movement and DataOps layer, and a wide variety of purpose-built analytical services supporting analytics, discovery, data science, and AI/ML.

### Data Mesh
<a name="data-mesh"></a>

Data Mesh is a sophisticated, fully-distributed data platform architecture which is intended to provide maximum autonomy to business units in the activities of data product development. Each business participating in the mesh is furnished with its own data mesh node, which is itself typically an implementation of an individual Lake House. Within a data mesh node, each business unit has autonomy to produce data products, which can be exchanged with other nodes/business units via producer/consumer relationships. While the data mesh platform itself is distributed, it is critical for each node in the data mesh to still conform to a robust, unified governance framework in order to facilitate seamless, governed exchange of data between producers and consumers.

MDAA supports configuration and deployment of complex Data Mesh architectures, distributed across arbitrary numbers of business units and AWS accounts. These deployments can occur centrally, from within a single deployment account across a multi-account landscape, or can be entirely distributed, with each data mesh node being deployed by individual business units using their own MDAA configurations. Hybrid models are also supported, using services such as Service Catalog, where a centralized team can define platform component templates (Service Catalog 'Products'), but delegate authority to individual business units for their final configuration and deployment.

### Hub and Spoke
<a name="hub-and-spoke"></a>

Hub and Spoke is a hybrid model between a fully centralized Lake House and a fully decentralized Data Mesh. In a Hub and Spoke architecture, there is a greater concentration of enterprise data assets and governance within the Hub, but within each Spoke, individual business units are still afforded autonomy in data product development. While in a full-blown Data Mesh there may be pairwise exchange of data products between any two participating nodes, in Hub and Spoke, exchange would only occur between the hub and spoke nodes. A Hub and Spoke architecture is often more suitable for organizations with a less mature and robust organizational data governance framework, but can also be a stepping stone for these organizations to move to a full Data Mesh architecture as their institutional data maturity increases.

## Detailed Architecture
<a name="detailed-architecture"></a>

MDAA is designed to be able to implement the following detailed reference architecture (or any derivative/subset of), which is a practical implementation of the AWS Modern Data Architecture (Lake House). The key platform functions and capabilities represented are:

### Data Ingest
<a name="data-ingest"></a>

All of the capabilities required to ingest data into the platform, including from structured, unstructured, batch, and streaming data sources.
+ Structured and unstructured data sources
+ Batch and streaming data ingestion patterns
+ Integration with AWS-native and third-party data sources
+ Automated landing zone configuration for incoming data

### S3 Data Lake/Persistence
<a name="s3-data-lake"></a>

Provides secure, scalable storage at the core of the architecture, able to accommodate data of virtually any volume and variety.
+ Centralized storage for raw, curated, and enriched data
+ Server-side encryption with KMS key management
+ Lifecycle policies for cost optimization across storage tiers
+ Integration with the governance layer for cataloging and access control
+ Support for multi-domain and multi-environment deployments

### Governance
<a name="governance"></a>

Provides the governance functions of the platform, such as cataloging and fine-grained access control.
+ Data cataloging via AWS Glue Data Catalog
+ Fine-grained access control via AWS Lake Formation
+ Tag-Based Access Control (TBAC) for scalable permissions management
+ Unified governance framework across distributed architectures
+ Data quality and compliance enforcement

### Processing/Curation (DataOps)
<a name="processing-curation"></a>

Provides the seamless movement of data throughout the platform, as well as capabilities required for data curation, data quality, and enrichment.
+ Data transformation and curation capabilities
+ Data quality management
+ Data enrichment workflows
+ Integration between platform components
+ Support for ETL/ELT patterns

### Analytics, Query, and Consumption
<a name="analytics-query-consumption"></a>

Provides capabilities to analyze, query, and consume data from the platform into a wide variety of tools for the purpose of data product development.
+ Query engines including Amazon Athena and Amazon Redshift
+ Data visualization and reporting capabilities
+ Self-service analytics for business users
+ Support for data product development and sharing

### Data Science, AI/ML
<a name="data-science-ai-ml"></a>

Provides capabilities to support sophisticated exploratory analytics, data science, machine learning, and artificial intelligence.
+ Amazon SageMaker Unified Studio for integrated data and AI development
+ Managed notebook environments for data exploration
+ Integration with the data lake and governance layers
+ Support for generative AI workloads via Amazon Bedrock and Agentcore Runtime

## SageMaker Unified Studio
<a name="sagemaker-unified-studio"></a>

Amazon SageMaker Unified Studio provides a single environment where data teams can work with data, analytics, and AI tools through a unified experience. Within the MDAA architecture, the SageMaker Unified Studio module sits at the intersection of the Governance, Analytics, and Data Science/AI/ML layers, providing a collaborative workspace that is fully integrated with the platform’s governed data assets.

SageMaker Unified Studio brings together capabilities that traditionally required switching between multiple AWS services. Data engineers, analysts, and data scientists can discover governed data from the platform’s Glue Data Catalog and Lake Formation layer, run SQL analytics, build and train ML models, and develop generative AI applications — all from a single interface. This tight integration with the platform’s governance layer ensures that all activities within the studio respect the fine-grained access controls and Tag-Based Access Control (TBAC) policies defined at the platform level.

MDAA’s SageMaker Unified Studio module deploys and configures the following:
+ SageMaker Unified Studio domains with domain units and authorization units
+ Support for managed and custom blueprints, project profiles, and projects
+ Integration with the platform’s Lake Formation governance layer for fine-grained data access
+ Connection to the S3 data lake for seamless access to raw, curated, and enriched datasets
+ IAM roles with least-privilege permissions aligned to the platform’s role model
+ Support for SQL analytics, data preparation, ML model development, and generative AI workflows
+ Collaboration features enabling data teams to share notebooks, queries, and models within governed boundaries

By deploying SageMaker Unified Studio as part of the broader MDAA platform, organizations gain a governed, self-service environment where data teams can move from data discovery through to AI/ML model deployment without leaving the platform’s security and governance perimeter.

## Generative AI
<a name="genai"></a>

MDAA provides comprehensive support for building and deploying generative AI applications through Amazon Bedrock and Bedrock Agentcore Runtime. These modules extend the Data Science, AI/ML layer of the platform, enabling organizations to build, deploy, and operate generative AI solutions that use the governed data assets in the platform’s data lake.

### Bedrock
<a name="bedrock"></a>

Amazon Bedrock helps you build and scale generative AI applications with foundation models. The Bedrock Builder CDK application helps you configure and deploy secure Bedrock Agents, Knowledge Bases, and associated resources with just a few lines of configuration. Because the Bedrock module integrates with the platform’s S3 data lake and governance layer, Knowledge Bases can be populated from governed datasets, and Agents can access platform data through the same fine-grained access controls that govern all other consumers on the platform.

### Agentcore Runtime
<a name="agentcore-runtime"></a>

Bedrock Agentcore Runtime provides a managed runtime environment for deploying and operating agentic AI applications at scale. Within the MDAA architecture, the Agentcore Runtime module enables organizations to deploy secure, production-grade agentic applications that integrate with the platform’s governed data and infrastructure.

MDAA’s Agentcore Runtime module deploys and configures the following:
+ Agentcore Runtime gateway endpoints for hosting agentic applications
+ Integration with the platform’s VPC and networking layer for secure connectivity
+ IAM roles and policies aligned to the platform’s least-privilege security model
+ Support for custom agent runtimes with configurable compute and scaling
+ Integration with the platform’s governance and observability layers

### Bedrock Agent Configuration
<a name="bedrock-agent-configuration"></a>

When you deploy a Bedrock Agent using this CDK application, you get a complete setup that includes:
+ A fully configured Amazon Bedrock Agent that automates your workflows using foundation models
+ A comprehensive execution policy that manages access to your Knowledge Base, Foundation Model, and Bedrock Guardrails
+ An Agent Execution Role with Bedrock Service as a Trusted Principal
+ A dedicated KMS key for encrypting Agent resources

### Lambda Integration Capabilities
<a name="lambda-integration-capabilities"></a>

The CDK application offers flexible Lambda function integration options:

#### Lambda Layers and Functions
<a name="lambda-layers-and-functions"></a>
+ Create custom Lambda layers for code reuse across functions
+ Deploy specific Lambda functions for Agent Action Groups
+ Maintain consistent functionality across your agent operations
+ Enable CloudWatch observability features for comprehensive monitoring and debugging

#### VPC Configuration
<a name="vpc-configuration"></a>
+ Configure VPC settings with custom subnet parameters
+ Choose between existing security groups or create new ones
+ Implement secure networking with configurable egress rules

### Action Groups and Security Controls
<a name="action-groups-and-security-controls"></a>

You can enhance your agent’s capabilities through:
+ Action Group Configuration: Create custom action groups by either using existing Lambda functions or deploying new ones
+ Guardrail Implementation: Add optional Bedrock Guardrails to strengthen security
+ Automated Policy Management: The system automatically updates execution policies to include necessary guardrail permissions

### Best Practices and Recommendations
<a name="best-practices-and-recommendations"></a>

To make the most of your Bedrock Builder deployment:
+ Review and plan your security configurations before deployment
+ Document your guardrail settings for future reference
+ Use meaningful names for your Lambda functions and layers
+ Regularly review and update your execution policies
+ Enable CloudWatch observability for Lambda functions to monitor performance and troubleshoot issues

The Bedrock Builder CDK application simplifies the deployment and management of secure Bedrock Agents. By automating the configuration process and providing flexible integration options, you can focus on building generative AI solutions that use your platform’s governed data assets rather than managing infrastructure.

### GenAI Chatbot v2
<a name="genai-chatbot-v2"></a>

The GenAI Chatbot v2 (`@aws-mdaa/gaia-v2`) module deploys an authenticated GenAI chatbot backend. It replaces GAIA v1 (`@aws-mdaa/gaia` and `@aws-mdaa/gaia-l3-construct`), which was removed from the MDAA repository in v1.9.0. GAIA v2 introduces:
+ AppSync Events API for real-time bidirectional streaming, fronted by a Cognito User Pool with optional external OIDC (for example, Microsoft Entra ID)
+ Pluggable data source model — exactly one of Bedrock Knowledge Base RAG, direct Bedrock model invocation with streaming, or a customer-provided Lambda
+ Optional client and admin CloudFront UIs with custom-domain and ACM certificate support
+ Chat history, feedback, and service-interruption banner backed by KMS-encrypted DynamoDB tables
+ WAF protection (regional and global), VPC-attached Lambda execution, and synth-time validation of misconfigurations

The previously published `@aws-mdaa/gaia@1.8.1` and `@aws-mdaa/gaia-l3-construct@1.8.1` packages remain available on the npm registry, marked deprecated, so existing deployments can continue to build while migrating; new features land in v2 only. See [Migrating from GAIA v1 to GAIA v2](troubleshooting.md#gaia-v1-to-v2-migration) for migration guidance.

### Data Protection on AgentCore Runtime
<a name="data-protection-on-agentcore-runtime"></a>

MDAA’s Bedrock AgentCore Runtime module applies built-in data protection to service-created runtime log groups on every deployment. Customer-managed KMS encryption and a CloudWatch Data Protection policy with a comprehensive PII identifier baseline (email addresses, credit card numbers, SSNs, names, addresses, US phone numbers, IP addresses) are always applied. The baseline can be extended via `dataProtection.additionalIdentifiers` but cannot be narrowed. The module also supports:
+ Optional `allowedModelArns` to scope execution role Bedrock permissions to specific model ARNs
+ Optional `enforceVpcOnly` to deny invocation from outside the VPC for every caller type — IAM/SigV4 as well as JWT/OAuth — through explicit deny statements in an auto-generated resource-based policy that covers all `bedrock-agentcore:InvokeAgentRuntime*` variants
+ Optional `networkConfiguration.vpcEndpoint` to create the AgentCore interface VPC endpoint with Private DNS, an app-security-group-scoped security group, and an invoke-only endpoint policy; `enforceVpcOnly` requires this endpoint to be satisfiable
+ Optional `logRetentionDays` for CloudWatch Logs retention on runtime log groups (defaults to 30 days)
+ Typed `CfnRuntime`/`CfnRuntimeEndpoint` constructs for compile-time validation

## Module-Level Configuration
<a name="module-level-configuration"></a>

MDAA ships a broad and growing catalog of deployable modules spanning the ingest, storage, governance, DataOps, analytics, data science, and generative AI layers described above. Each module is configuration-driven and documented in the MDAA documentation site, which is the authoritative reference for each module’s configuration schema, defaults, and behavior.

For the current list of modules and starter kits and their per-module configuration details, refer to:
+ The [MDAA module and starter kit documentation](https://aws.github.io/modern-data-architecture-accelerator/index.html).
+ The [MDAA release notes](https://github.com/aws/modern-data-architecture-accelerator/releases/) for modules and capabilities added or changed in each release.
+ The JSON schemas and module documentation generated under `.mdaa/<version>/` when you scaffold or enhance a project with `mdaa init` (see [Scaffold a project with `mdaa init`](scaffold-a-project-with-mdaa-init.md)).
