---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html
---

# AWS Fault Isolation Boundaries
<a name="abstract-and-introduction"></a>

Publication date: **November 16, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 Amazon Web Services (AWS) provides different isolation boundaries, such as Availability Zones (AZ), Regions, control planes, and data planes. This paper details how AWS uses these boundaries to create zonal, Regional, and global services. It also includes prescriptive guidance on how to consider dependencies on these different services and how to improve the resilience of workloads you build using them.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 AWS operates a global infrastructure to provide cloud services that help customers deploy workloads in a flexible, secure, scalable, and highly available way. The AWS infrastructure uses multiple fault isolation constructs to help customers achieve their resilience objectives. These fault isolation boundaries enable customers to design their workloads to take advantage of the predictable scope of impact containment they provide. It's also important to understand how AWS services are designed using these boundaries so that you can make intentional choices about the dependencies you select for your workload.

 This paper will first summarize AWS global infrastructure and the fault isolation boundaries it provides, as well as some of the patterns used to design our services. Using this baseline of understanding, the paper will next outline the different scopes of services AWS provides: zonal, Regional, and global. It will also present best practices for building architectures that use these isolation boundaries and different service scopes to improve the resilience of the workloads you run on AWS. In particular, it provides prescriptive guidance on how to take dependencies on global services while minimizing single points of failure. This will help you make informed choices about your AWS dependencies and how you design your workload for high availability (HA) and disaster recovery (DR).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
