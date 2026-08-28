---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/best-practices-for-deploying-sas-server.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Best Practices for Deploying SAS Server on AWS
<a name="best-practices-for-deploying-sas-server"></a>

Publication date: **February 1, 2020** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

Many SAS customers are moving their SAS applications from on-premises data centers to the AWS Cloud. In order to migrate, customers must be aware of all the layers of their SAS infrastructure. Customers should understand how their SAS applications run, and how to optimize their Amazon Web Services (AWS) architecture.

 This whitepaper addresses performance considerations and best practices for SAS®9 (SAS® Foundation and SAS Grid Manager) and SAS® Viya® when hosted on AWS. The content is written for IT professionals familiar with SAS and AWS.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 SAS is an analytics software that provides organizations a suite of capabilities that enable users to draw insights from data and make intelligent decisions. The SAS platform includes software platforms that underpin SAS product offerings in analytics, data management, and visualization. SAS 9.4 provides simplified architecture and deployment options for running SAS on a cloud infrastructure. SAS Viya is a cloud- enabled, in-memory analytics engine that provides quick, accurate and reliable analytical insights.

 SAS 9.4 provides the following features:

1.  Data Management

1.  Visual Analytics

1.  Governance and Security

1.  Forecasting and Text Mining

1.  Statistical Analysis

1.  Environment Management

 SAS is also a 4GL programming language used by data scientists for more than 80,000 customers globally. SAS 9 does not leverage the benefits of the cloud in terms of managed hosting, elasticity, and scalability. SAS Viya, on the other hand, is a cloud-enabled, in-memory analytics engine with features such as elasticity, scalability, and fault tolerance. In this whitepaper, SAS customers can learn about the best practices for running their SAS 9 workloads on AWS and evaluate how to modernize their architecture of SAS Viya.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
