---
source_url: https://docs.aws.amazon.com/whitepapers/latest/deploying-oracle-soa-suite-12c/deploying-oracle-soa-suite-12c.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Deploying Oracle SOA Suite 12c on AWS
<a name="deploying-oracle-soa-suite-12c"></a>

Publication date: **October 19, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 This whitepaper provides guidance for deploying [Oracle SOA Suite 12c](https://www.oracle.com/middleware/technologies/soasuite.html) applications on Amazon Web Services (AWS). This whitepaper provides a reference architecture and information about best practices for high availability, security, scalability, and performance when you deploy Oracle SOA Suite 12c-based applications on AWS.

 The target audience of this whitepaper is solutions architects, systems architects, and system administrators with a basic understanding of cloud computing, AWS, and Oracle SOA Suite 12c.

 This whitepaper assumes that you have a basic understanding of AWS. For an overview of AWS services, refer to [Overview of Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html).

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Many enterprises today rely on application and data integration to deliver new services and capabilities to their customers. Oracle SOA Suite 12c is a popular application integration and service-oriented architecture (SOA) solution that enables you to build, deploy, and manage integrations. Some of the benefits of deploying Oracle SOA Suite on AWS include:
+  **Low cost** – Resources are billed by the hour and only for the duration they are used.
+  **Eliminate the need for large capital outlays** – Replace large, upfront expenses with low variable payments that only apply to what you use.
+  **High availability** – Achieve high availability by deploying Oracle SOA Suite 12c in a Multi-AZ configuration.
+  **Flexibility** – Add compute capacity elastically to cope with demand.
+  **Testing** – Add test environments, use them for short durations, and pay only for the duration they are used.

 You can use various AWS services to deploy Oracle SOA Suite 12c-based applications on AWS in a secure, highly-available, and cost-effective manner. With automatic scaling, you can dynamically scale the compute resources required for your application, thereby keeping your costs low. You can use [Amazon Elastic File System](https://aws.amazon.com/efs) (Amazon EFS) as shared storage to store Oracle SOA Suite artifacts. Amazon EFS provides a scalable, fully-managed elastic network file system (NFS) with the ability to grow and shrink automatically as you add and remove files.

### Use cases for Oracle SOA Suite 12c on AWS
<a name="use-cases-for-oracle-soa-suite-12c-on-aws"></a>

 Oracle SOA Suite 12c customers use AWS for a variety of use cases, including:
+  Migration of existing Oracle SOA Suite production environments.
+  Implementation of new Oracle SOA Suite production environments.
+  Implementation of disaster recovery environments.
+  Running Oracle SOA Suite development, test, demonstration, proof of concept (POC), and training environments.
+  Temporary environments for migrations and testing upgrades.
+  Temporary environments for performance testing.
