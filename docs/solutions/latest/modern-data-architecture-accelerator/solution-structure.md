---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html
---

# Solution Structure
<a name="solution-structure"></a>

MDAA is a comprehensive solution built using a modular approach. Think of it as a sophisticated building kit for creating secure and scalable data infrastructure on AWS. Just as a building needs a foundation, walls, and utilities, MDAA provides all the necessary components to build your data/AI platform.

## The Module Concept
<a name="the-module-concept"></a>

Think of modules as specialized building blocks. For example:
+ If you want to deploy raw and transformation buckets for your data lake, there’s a datalake module that creates encrypted S3 buckets with proper access controls, sets up fine-grained lifecycle policies for cost optimization and configures bucket policies and cross-account access if needed
+ If you need to query data using Amazon Athena, there’s a module that sets up Athena workgroups with resource controls, configures query result locations, connects with your datalake and establishes necessary IAM permissions for query execution
+ If you want to add AWS Lake Formation settings to your tables, there’s a module that configures Lake Formation permissions and security settings, sets up database and table-level access controls, etc.

For the complete list of available modules and starter kits, along with their configuration options, see the [MDAA documentation](https://aws.github.io/modern-data-architecture-accelerator/index.html).

## How Modules Work Together
<a name="how-modules-work-together"></a>

Consider this practical scenario: You want to build a secure data lake for financial data.
+ Start with the roles module to create necessary IAM roles and policies
+ Add the datalake module to create encrypted storage
+ Add the Glue module to catalog your data
+ Implement Lake Formation module for compliance
+ Configure Athena module for analysts to query
+ Add audit modules for security

## MDAA Starter Packages
<a name="mdaa-starter-packages"></a>

### Overview
<a name="overview"></a>

Modern Data Architecture Accelerator (MDAA) provides a comprehensive set of pre-configured starter packages, each designed to accelerate your journey in building enterprise-grade secure and compliant data platforms on AWS. These packages eliminate the complexity of starting from scratch by providing production-ready configurations, security controls, and infrastructure templates.

### Available Starter Packages
<a name="available-starter-packages"></a>

#### 1. Minimal
<a name="1-minimal"></a>

| Purpose | Foundational governance layer for building custom architectures |
| --- | --- |
| Key Features |  +  IAM role generation with CDK Nag compliance <br />+  Glue Catalog KMS encryption at the account level <br />+  Lake Formation settings delegating access control to IAM at the account level <br />+  Resource tagging for cost allocation and operational governance   |
| Ideal For |  +  Starting a new MDAA project from scratch and adding modules incrementally <br />+  Establishing governance foundations before committing to a specific architecture <br />+  Learning MDAA with the simplest possible deployment   |

#### 2. Basic Data Lake
<a name="2-basic-data-lake"></a>

| Purpose | Secure S3 data lake with coarse-grained access control |
| --- | --- |
| Key Features |  +  KMS-encrypted S3 buckets with enforced SSL-only access and public access blocking <br />+  IAM-based access control with dedicated admin and user roles <br />+  Glue Data Catalog with encrypted metadata store <br />+  Athena workgroup for isolated SQL queries <br />+  Glue crawlers for automated schema discovery and Glue Data Quality rules <br />+  CloudTrail audit trail with a dedicated audit bucket <br />+  Lake Formation settings delegating access control to IAM   |
| Ideal For |  +  Centralizing data storage with appropriate security controls <br />+  Governance and compliance requirements without fine-grained column/row security <br />+  Self-service data access via Athena for authorized users   |

#### 3. AI/ML Platform
<a name="3-aiml-platform"></a>

| Purpose | Team-based data science platform on SageMaker Studio |
| --- | --- |
| Key Features |  +  All Basic Data Lake features, plus: <br />+  SageMaker Studio Domain with team-specific user profiles <br />+  Fine-grained access control via Lake Formation <br />+  Team-specific Athena workgroups for SQL-based exploration <br />+  IAM roles with separation of duties (data-admin, data-user, data-scientist, team-execution)   |
| Best For |  +  Self-service ML experimentation and model development <br />+  Team-isolated notebook environments with shared data lake access <br />+  Collaborative data science with role-based access   |

#### 4. Lakehouse Analytics
<a name="4-lakehouse-analytics"></a>

| Purpose | End-to-end analytics lakehouse spanning ingestion through BI |
| --- | --- |
| Key Features |  +  S3 data lake (raw \+ transformed), KMS-encrypted with coarse-grained access <br />+  KMS-encrypted Glue Data Catalog, Lake Formation settings, DataOps project with sample database and crawler <br />+  Glue ETL job with sample PySpark script and Glue Data Quality ruleset \+ workflow <br />+  Athena workgroup over the data lake <br />+  Redshift cluster with multi-AZ high availability and cross-region snapshot copy <br />+  QuickSight account, VPC connection, and data sources for Athena and Redshift <br />+  IAM roles (data-admin, data-user, glue-etl), S3 audit bucket, and CloudTrail audit trail   |
| Best For |  +  Teams needing ingestion, processing, quality validation, warehousing, and BI in one deploy <br />+  Consuming analytics via Athena, Redshift, and QuickSight <br />+  A validated end-to-end reference across all data foundations capabilities   |

#### 5. DataZone Governed Lakehouse
<a name="5-datazone-governed-lakehouse"></a>

| Purpose | Enterprise lakehouse with fine-grained governance via DataZone |
| --- | --- |
| Key Features |  +  All Basic Data Lake features, plus: <br />+  DataZone domain for data product management, discovery, and subscription <br />+  Fine-grained access control via Lake Formation (database and table level) <br />+  Three-zone S3 data lake (raw, transformed, curated), KMS-encrypted <br />+  Glue Data Catalog with encrypted metadata and automated schema discovery <br />+  IAM roles with separation of duties (data-admin, data-engineer, data-users, glue-etl) <br />+  Multiple DataOps projects for producer and consumer teams   |
| Best For |  +  Enterprises requiring fine-grained access control on structured data <br />+  Multi-team environments with data producers and consumers <br />+  Organizations building data product marketplaces   |

#### 6. SMUS Research Environment
<a name="6-smus-research-environment"></a>

| Purpose | SageMaker Unified Studio (SMUS) for multi-team research in a single account |
| --- | --- |
| Key Features |  +  SMUS domain (DataZone V2) with IAM Identity Center SSO integration <br />+  Project profiles for standardized team environments <br />+  Team-based access control via IAM Identity Center groups <br />+  Lake Formation governance for fine-grained data access <br />+  Glue Catalog encryption and IAM roles for domain/data administration   |
| Best For |  +  Multi-team research environments with shared governance in a single account <br />+  Self-service ML platform access via the SMUS portal <br />+  Rapid onboarding of research teams with standardized project profiles   |

#### 7. SMUS Data Mesh
<a name="7-smus-data-mesh"></a>

| Purpose | Multi-account SageMaker Unified Studio data mesh |
| --- | --- |
| Key Features |  +  Single SMUS domain associated to multiple accounts for centralized governance <br />+  Cross-account data sharing via Lake Formation and DataZone <br />+  Custom blueprints deployed across all accounts via project profiles <br />+  Three-zone data lake (raw/transformed/curated) in the enterprise account <br />+  DataOps projects with Glue catalogs, crawlers, and SMUS data sources <br />+  Domain units for organizational hierarchy <br />+  IAM Identity Center (SSO) integration for user and group management <br />+  VPC-based networking with private subnets per account   |
| Best For |  +  Medium-to-large organizations implementing a multi-account data mesh <br />+  Cross-account data sharing between business units under central governance <br />+  Team autonomy with each business unit managing its own pipelines   |

#### 8. MLOps Platform
<a name="8-mlops-platform"></a>

| Purpose | End-to-end ML lifecycle: training, deployment, and monitoring |
| --- | --- |
| Key Features |  +  Unified training and deployment CI/CD pipelines via `@aws-mdaa/sagemaker-mlops`  <br />+  SageMaker Pipeline (preprocess → train → register) with automatic execution <br />+  SageMaker Endpoint with model quality monitoring schedule <br />+  Model Package Group for versioned model registry <br />+  EventBridge-triggered deployment on model approval <br />+  KMS-encrypted S3 bucket for model artifacts <br />+  CodeCommit repositories seeded with ML scripts and MDAA configs <br />+  Optional cross-account deployment (dev → pre-prod → prod)   |
| Best For |  +  Automated ML model training pipelines with versioned model registry <br />+  Multi-stage deployment with manual approval gates <br />+  Real-time inference endpoints with model quality monitoring <br />+  Network-isolated training and inference for compliance   |

#### 9. GenAI Foundation
<a name="9-genai-foundation"></a>

| Purpose | Bedrock-based Customer Support Agent with RAG and guardrails |
| --- | --- |
| Key Features |  +  Bedrock Agents with custom action groups for customer support <br />+  Knowledge Bases with vector stores for efficient retrieval <br />+  Guardrails for content safety and appropriate responses <br />+  Multi-sync architecture for concurrent file uploads <br />+  KMS-encrypted S3 buckets for knowledge base data sources <br />+  IAM roles with least-privilege Bedrock permissions   |
| Best For |  +  Customer support agents with natural language interaction <br />+  Knowledge base search and retrieval over internal documents <br />+  Document processing with Retrieval Augmented Generation (RAG)   |

#### 10. GAIA Chatbot
<a name="10-gaia-chatbot"></a>

| Purpose | Production-ready GenAI chatbot backend with authentication and streaming |
| --- | --- |
| Key Features |  +  Cognito User Pool with email/password or enterprise SSO authentication <br />+  Bedrock Knowledge Base with OpenSearch Serverless vector store <br />+  Bedrock Guardrails for content filtering and PII protection <br />+  KMS-encrypted S3 data lake for document storage <br />+  REST API (API Gateway) for session management, feedback, and admin operations <br />+  WebSocket API (AppSync Events) for real-time chat streaming <br />+  VPC-deployed Lambda functions for serverless compute <br />+  CloudFront CDN serving `aws-exports.json` configuration <br />+  Optional WAF web application firewall   |
| Best For |  +  RAG-powered chatbot with enterprise authentication <br />+  Document Q&A over internal knowledge bases (PDF, TXT, MD, HTML, DOCX) <br />+  Real-time streaming chat with content-filtered AI responses   |

### Package Benefits
<a name="package-benefits"></a>

#### Time to Market
<a name="time-to-market"></a>
+ Reduce implementation time by 60-70%
+ Avoid common architectural pitfalls
+ Start with proven configurations

#### Cost Optimization
<a name="cost-optimization"></a>
+ Pre-configured resource optimization
+ Built-in cost control measures
+ Efficient resource utilization patterns

#### Security & Compliance
<a name="security-compliance"></a>
+ Security controls aligned with AWS best practices
+ Built-in compliance frameworks
+ Automated security monitoring

#### Scalability
<a name="scalability"></a>
+ Designed for growth
+ Flexible architecture
+ Easy module addition/removal

### Best Practices
<a name="best-practices"></a>

#### Security
<a name="security"></a>
+ Enable all recommended security features
+ Implement proper encryption
+ Regular security assessments
+ Continuous monitoring

#### Operations
<a name="operations"></a>
+ Follow GitOps practices
+ Implement proper tagging
+ Regular backup testing
+ Disaster recovery planning

#### Cost Management
<a name="cost-management"></a>
+ Enable cost allocation tags
+ Set up budget alerts
+ Regular cost reviews
+ Resource optimization

### Support and Maintenance
<a name="support-and-maintenance"></a>

#### Regular Updates
<a name="regular-updates"></a>
+ Security patches
+ Feature updates
+ Performance improvements
+ Best practice updates

**Note**
All packages are regularly updated to incorporate the latest AWS features and security best practices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
