---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a high-level overview of how MDAA enables flexible deployment of data platforms on AWS. MDAA supports multiple architectural patterns that can evolve as your organization’s needs change.

## Architecture diagram
<a name="architecture-diagram"></a>

The first step of building an analytics platform with MDAA is to decide on an initial architecture. MDAA is extremely flexible, able to be adapted to most common analytics platform architectures on AWS. These include basic Data Lakes and Data Warehouses, Lake House, and complex Data Mesh architectures. Note that the initial architecture does not need to be the target end-state architecture for the platform, as these architectures often build on each other, and a MDAA configuration/deployment can be adapted through iteration from one architectural state to another.

As an example, the following is the architecture for the Basic Datalake.

![basic datalake](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/basic_datalake.png)

**Basic Datalake on AWS architecture**

1. You use AWS CloudFormation to install MDAA into your environment. Your environment must meet prerequisites before deploying the solution. (See [PREDEPLOYMENT](https://github.com/aws/modern-data-architecture-accelerator/blob/main/PREDEPLOYMENT.md).) The provided CloudFormation template deploys an AWS CodePipeline that contains the MDAA installation engine for building analytics platforms.

1. The Modern Data Architecture (Lake House) framework functions as the core architecture pattern. This way, you can establish a flexible, scalable foundation for solving virtually any data problem—using analytics, data science, or AI/ML—on AWS. The architecture remains fully open and interoperable with data capabilities both inside and outside of AWS.

1. An S3-based data lake serves as the core component, wrapped with a unified data governance layer. The solution deploys AWS Glue and AWS Lake Formation to provide comprehensive data cataloging and access controls. Additionally, the solution implements a DataOps layer to facilitate seamless data movement between the core data lake and purpose-built analytics services on the perimeter.

1. The solution deploys purpose-built analytics services that you can select based on specific use cases. These services support various analytical workloads including traditional BI, data science, and machine learning. The solution maintains flexibility to add or modify analytics services as requirements evolve.

1. For organizations requiring distributed data architecture, MDAA supports deployment of Data Mesh patterns. Each business unit can operate an autonomous data mesh node, typically implementing an individual Lake House architecture. The solution enables producer/consumer relationships between nodes while maintaining unified governance.

Supported Architecture Patterns
+ Modern Data Architecture (Lake House) - The AWS reference architecture centered around an S3-based data lake with unified governance and analytics capabilities
+ Data Mesh - A distributed architecture pattern providing autonomy to business units while maintaining centralized governance
+ Hub and Spoke - A hybrid model combining centralized enterprise data assets with distributed business unit capabilities

 **Core Platform Functions**

MDAA implements these key platform capabilities:
+ Data Ingest
+ S3 Data Lake/Persistence
+ Governance
+ Processing/Curation (DataOps)
+ Analytics, Query, and Consumption
+ Data Science, AI/ML
+ Visualization

 **Additional notes**

Initial deployment establishes the core data lake, governance framework, and basic analytics capabilities. Additional components can be added iteratively based on specific requirements and use cases.

The solution maintains flexibility to evolve from basic data lake architectures to more sophisticated patterns like Data Mesh. The unified governance model ensures consistent controls even as the architecture grows in complexity. When implementing Data Mesh patterns, each node maintains autonomy while adhering to organization-wide governance standards.

We provide guidance on selecting appropriate architecture patterns based on organizational maturity, use cases, and compliance requirements. The solution documentation includes detailed deployment procedures for each supported pattern.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
