---
source_url: https://docs.aws.amazon.com/whitepapers/latest/demand-forecasting/demand-forecasting.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Demand Forecasting
<a name="demand-forecasting"></a>

Publication date: **September 23, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 Amazon Web Services (AWS) customers look for easier, faster, more accurate, and more cost-effective ways to forecast the demand for their products, services, and materials. This whitepaper provides best practices, architectural patterns, technologies, and recommendations about demand forecasting on AWS. This paper addresses a wide array of readers, including technical professionals, non-technical professionals, and organizations with or without science teams.

 We discuss general trends and AWS services, and architectures for wide variety of needs. You can use this paper to find the best solutions, next steps, and best practices specific to your business. The content is based on findings about industrials, manufacturing, Consumer Packaged Goods (CPG), retail, and utilities; but it is applicable to other industries.

### Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 In the [Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html), we focus on how to design, deploy, and architect your machine learning workloads in the AWS Cloud. This lens adds to the best practices described in the Well-Architected Framework.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

### Introduction
<a name="introduction"></a>

 This document provides ways to build automations and data pipelines, and recommends AWS solutions and partner support to fit your business needs. It provides guidance on data sources and utilization of statistical and machine learning (ML)-based demand forecasting using managed AWS technologies. It also addresses artificial intelligence/machine learning (AI/ML) technologies which do not require data scientists to be involved. The document also contains example architectures building custom solutions.

 The first part of this document provides high-level information and background, such as common practices of demand forecasting in the industries. Next it introduces industry pain points to help you to identify your own business pain points.

 In the second part, we provide solutions to address your business environments, skillsets, data residency, and business needs. The following section explores technical aspects of the solutions, including various reference architectures and patterns.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
