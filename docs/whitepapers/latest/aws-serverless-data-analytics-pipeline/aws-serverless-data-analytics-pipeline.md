---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-serverless-data-analytics-pipeline/aws-serverless-data-analytics-pipeline.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Serverless Data Analytics Pipeline
<a name="aws-serverless-data-analytics-pipeline"></a>

Publication date: **April 7, 2021** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 This whitepaper discusses a layered, component-oriented, and logical architecture of modern analytics platforms. It also includes a reference architecture for building a serverless data platform that includes a data lake, data processing pipelines, and a consumption layer that enables several ways to analyze the data in the data lake without moving it, including business intelligence (BI) dashboarding, exploratory interactive SQL, big data processing, predictive analytics, and machine learning (ML).

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected) (sign-in required), you can review your workloads against these best practices by answering a set of questions for each pillar.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Onboarding new data or building new analytics pipelines in traditional analytics architectures usually require extensive coordination across multiple teams such as, business, data engineering, and data science and analytics. Before starting, these teams must first negotiate requirements, schema, infrastructure capacity needs, and workload management.

 It is becoming increasingly difficult and inefficient to pre-define constantly changing schemas, time consuming to negotiate capacity slots on a shared infrastructure. For these reasons, business users, data scientists, and analysts want easy, frictionless, and self-service options to build end-to-end data pipelines. The exploratory nature of ML and many analytics tasks means you need to rapidly ingest new datasets and clean, normalize, and feature engineer them without worrying about operational overhead when you must think about the infrastructure that runs data pipelines.

 A serverless data lake architecture enables agile and self-service data onboarding and analytics for all data consumer roles across a company. By using [AWS serverless technologies](https://aws.amazon.com/serverless/) as building blocks, you can rapidly and interactively build data lakes and data processing pipelines to ingest, store, transform, and analyze petabytes of structured and unstructured data from batch and streaming sources, without needing to manage any storage or compute infrastructure.

 In this whitepaper, we discuss a layered, component-oriented logical architecture of modern analytics platforms and present a reference architecture for building a serverless data platform. This architecture includes a data lake, data processing pipelines, and a consumption layer that enables several ways to analyze the data in the data lake without moving it, including business intelligence (BI) dashboarding, exploratory interactive SQL, big data processing, predictive analytics, and ML.
