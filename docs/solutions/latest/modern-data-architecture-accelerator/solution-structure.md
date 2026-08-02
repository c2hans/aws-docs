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
| Key Features |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |
| Ideal For |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |

#### 2. Basic Data Lake
<a name="2-basic-data-lake"></a>

| Purpose | Secure S3 data lake with coarse-grained access control |
| --- | --- |
| Key Features |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |
| Ideal For |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |

#### 3. AI/ML Platform
<a name="3-aiml-platform"></a>

| Purpose | Team-based data science platform on SageMaker Studio |
| --- | --- |
| Key Features |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |
| Best For |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |

#### 4. Lakehouse Analytics
<a name="4-lakehouse-analytics"></a>

| Purpose | End-to-end analytics lakehouse spanning ingestion through BI |
| --- | --- |
| Key Features |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |
| Best For |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |

#### 5. DataZone Governed Lakehouse
<a name="5-datazone-governed-lakehouse"></a>

| Purpose | Enterprise lakehouse with fine-grained governance via DataZone |
| --- | --- |
| Key Features |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |
| Best For |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |

#### 6. SMUS Research Environment
<a name="6-smus-research-environment"></a>

| Purpose | SageMaker Unified Studio (SMUS) for multi-team research in a single account |
| --- | --- |
| Key Features |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |
| Best For |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |

#### 7. SMUS Data Mesh
<a name="7-smus-data-mesh"></a>

| Purpose | Multi-account SageMaker Unified Studio data mesh |
| --- | --- |
| Key Features |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |
| Best For |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |

#### 8. MLOps Platform
<a name="8-mlops-platform"></a>

| Purpose | End-to-end ML lifecycle: training, deployment, and monitoring |
| --- | --- |
| Key Features |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |
| Best For |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |

#### 9. GenAI Foundation
<a name="9-genai-foundation"></a>

| Purpose | Bedrock-based Customer Support Agent with RAG and guardrails |
| --- | --- |
| Key Features |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |
| Best For |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |

#### 10. GAIA Chatbot
<a name="10-gaia-chatbot"></a>

| Purpose | Production-ready GenAI chatbot backend with authentication and streaming |
| --- | --- |
| Key Features |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |
| Best For |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/solution-structure.html)  |

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
