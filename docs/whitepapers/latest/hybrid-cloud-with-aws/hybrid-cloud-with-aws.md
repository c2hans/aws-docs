---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-with-aws/hybrid-cloud-with-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid Cloud with AWS
<a name="hybrid-cloud-with-aws"></a>

Publication date: **November 5, 2020** ([Document history](document-revisions.md))

 Businesses and organizations often have a mix of cloud, on-premises, and edge computing infrastructure. A hybrid cloud with Amazon Web Services (AWS) delivers IT resources like compute, storage, databases, and more, through an integration of AWS Cloud services with on-premises and edge infrastructure. Hybrid cloud architectures help organizations integrate their on-premises and cloud operations to support a broad spectrum of hybrid cloud use cases, often using a common set of services, tools, and interfaces. This whitepaper outlines major use cases, defines hybrid architectural tenets, describes an implementation framework, and provides AWS solutions to guide you in creating a hybrid cloud strategy, and to design and implement a hybrid cloud environment with AWS.

## Introduction
<a name="introduction"></a>

 Many businesses and organizations now adopt cloud computing as a key aspect of their technology strategy. They are moving their workloads to the AWS Cloud for greater agility, cost savings, performance, availability, resiliency, and scalability. While most applications can be easily migrated, some applications need to be re-architected or modernized before they can be moved to the cloud. There are a subset of applications that must remain on-premises due to low-latency, local data processing, high data transfer costs, or data residency requirements. This leads many organizations to seek [hybrid cloud](https://en.wikipedia.org/wiki/Cloud_computing#Hybrid_cloud) architectures to integrate their on-premises and cloud operations to support a broad spectrum of use cases.

 Considerations for building a [hybrid cloud with AWS](https://aws.amazon.com/hybrid/) include:
+  **Creating a hybrid cloud strategy**: A hybrid cloud strategy provides guidelines that govern consumption of cloud and on-premises resources to support your business objectives. This whitepaper describes common use cases for building a hybrid cloud, such as ongoing migration to the cloud, ensuring business continuity during disasters, extending cloud infrastructure on-premises to support low-latency applications, or expanding international footprint on AWS. These use cases help you identify and define your business objectives for building a hybrid cloud, and provide guidelines for workload placements on the hybrid cloud.
+  **Creating a technical strategy**: A technical strategy for the hybrid cloud identifies the guiding tenets of the hybrid cloud architecture, and defines an implementation framework. This whitepaper outlines common tenets of a hybrid cloud architecture to help you define guiding principles for a planned hybrid cloud implementation. An example tenet is having a consistent set of interfaces for resource provisioning and management across the hybrid cloud infrastructure.

   The operations and management framework described in this whitepaper helps architects and systems integrators to identify the building blocks, best practices, and AWS services needed to create a technical strategy to implement a hybrid cloud with AWS.

 Dropbox has built a hybrid cloud with AWS with a strategy to leverage the scale, agility, innovation, and global footprint provided by AWS. They have built a consistent set of tools and interfaces for provisioning and managing the hybrid infrastructure to ensure developer productivity. Dropbox’s hybrid cloud with AWS powers the infrastructure that serves more than 500 million worldwide customers. Similarly, a large US-based insurance company has experienced higher business agility from adopting a cloud-first strategy. They consume Software-as-a-Service (SaaS) solutions first, then leverage AWS Managed Services and infrastructure to deliver cloud-native solutions, and only consume on-premises solutions when they have hybrid cloud use cases such as low-latency processing of data.

 When you build a hybrid cloud strategy that best meets your business needs, consider tradeoffs such as the possibility of added operational overhead or reduced agility with on-premises infrastructure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
