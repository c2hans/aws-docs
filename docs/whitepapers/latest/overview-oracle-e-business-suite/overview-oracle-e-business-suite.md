---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/overview-oracle-e-business-suite.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Overview of Oracle E-Business Suite on AWS
<a name="overview-oracle-e-business-suite"></a>

Publication date: **July 6, 2023** ([Document history](document-revisions.md))

 [Oracle E-Business Suite](https://www.oracle.com/applications/ebusiness/) is a popular suite of integrated business applications for automating enterprise-wide processes like customer relationship management, financial management, and supply chain management. This is the first whitepaper in a series focused on Oracle E-Business Suite on Amazon Web Services (AWS). It provides an architectural overview for running Oracle E-Business Suite 12.2 on AWS.

 The whitepaper series is intended for customers and partners who want to learn about the benefits and options for running Oracle E-Business Suite on AWS. Subsequent whitepapers in this series will discuss advanced topics and outline best practices for high availability, security, scalability, performance, migration, disaster recovery, and management of Oracle E-Business Suite systems on AWS.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Almost all large enterprises use enterprise resource planning (ERP) systems for managing and optimizing enterprise-wide business processes. Cloud adoption among enterprises is growing rapidly, with many adopting a cloud-first strategy for new projects and migrating their existing systems from on-premises to AWS. ERP systems such as Oracle E-Business Suite are mission critical for most enterprises and figure prominently in considerations for planning an enterprise cloud migration.

 This whitepaper provides a brief overview of Oracle E-Business Suite and a reference architecture for deploying Oracle E-Business Suite on AWS. It also discusses the benefits of running Oracle E-Business suite on AWS, and various use cases.
