---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/multi-tenant-saas-storage-strategies.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# SaaS Storage Strategies
<a name="multi-tenant-saas-storage-strategies"></a>

Publication date: **May 6, 2021** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 Multitenant storage represents one of the more challenging aspects of building and delivering Software as a Service (SaaS) solutions. There are a variety of strategies that can be used to partition tenant data, each with a unique set of nuances that shape your approach to multitenancy. Adding to this complexity is the need to map each of these strategies to the different storage models offered by AWS, such as [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS), and [Amazon Redshift](https://aws.amazon.com/redshift). Although there are high-level themes you can apply universally to these technologies, each storage model has its own approach to scoping, managing, and securing data in a multitenant environment. This paper offers SaaS developers insights into a range of data partitioning options, allowing them to determine which combination of strategies and storage technologies best align with the needs of their SaaS environment.

### Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

In the [SaaS Lens](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-lens.html), we focus on best practices for architecting your software as a service (SaaS) workloads on AWS.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

### Introduction
<a name="introduction"></a>

 AWS offers Software as a Service (SaaS) developers a rich collection of storage solutions, each with its own approach to scoping, provisioning, managing, and securing data. The way that each service represents, indexes, and stores data adds a unique set of considerations to your multitenant strategy. As a SaaS developer, the diversity of these storage options represents an opportunity to align the storage needs of your SaaS solution with the storage technologies that best match your business and customer needs.

 As you weigh AWS storage options, you must also consider how the multitenant model of your SaaS solution fits with each storage technology. Just as there are multiple flavors of storage, there are also multiple flavors of multitenant partition strategies. The goal is to find the best intersection of your storage and tenant partitioning needs.

 This paper explores all the moving parts of this puzzle. It examines and classifies the models that are typically used to achieve multitenancy, and helps you weigh the pros and cons that shape your selection of a partitioning model. It also outlines how each model is realized on [Amazon RDS](https://aws.amazon.com/rds/), [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), and [Amazon Redshift](https://aws.amazon.com/redshift). As you dig into each storage technology, you’ll learn how to use the AWS constructs to scope and manage your multitenant storage.

 Although this paper gives you general guidance for selecting a multitenant partitioning strategy, it’s important to recognize that the business, technical, and operational dimensions of your environment will often introduce factors that will also shape the approach you select. In many cases, SaaS organizations adopt a hybrid of the variations described in this paper.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
