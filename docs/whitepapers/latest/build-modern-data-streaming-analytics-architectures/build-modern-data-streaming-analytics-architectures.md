---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-modern-data-streaming-analytics-architectures/build-modern-data-streaming-analytics-architectures.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Build Modern Data Streaming Architectures on AWS
<a name="build-modern-data-streaming-analytics-architectures"></a>

Publication date: **May 17, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 Modern data architecture is about using the right tool for the job. It acknowledges that a “one size fits all” approach leads to compromise, and a solution that is not optimized for anyone. With modern data architecture, customers can integrate a data lake, data warehouses, and purpose-built data services, with a unified governance layer, to create a system without boundaries that enables data-driven decisions.

 When building a modern data architecture, sometimes there is a need for data to flow with low latency between components to power real-time decisions. This whitepaper helps cloud architects, data scientists, and developers to design and building modern data streaming architectures that can quickly generate insights using Amazon Web Services (AWS) streaming services such [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/), [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/), [Amazon Managed Service for Apache Flink](https://aws.amazon.com/kinesis/data-analytics/), and [Amazon Managed Streaming for Apache Kafka](https://aws.amazon.com/msk/) (Amazon MSK).

## Are you Well-Architected?
<a name="are-you-well-archietected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected) (sign-in required), you can review your workloads against these best practices by answering a set of questions for each pillar.

 In the [Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.pdf#analytics-lens), we focus on how to design, deploy, and architect your data analytics workloads in the AWS Cloud. This lens adds to the best practices described in the Well-Architected Framework.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Traditional on-premises data analytics approaches can’t handle exponential data volumes because they don’t scale well enough and are too expensive. Organizations need to easily access and analyze all types of data, such as structured, semi-structured, unstructured, and real-time streaming data to perform comprehensive and efficient analytics. They also need to easily break down data silos to gain new insights and build better experiences. With a modern data architecture, organizations can collect, store, organize, and process valuable data, make it available in a secure way, and enable applications to derive low-latency, near real-time insights.

 This whitepaper presents how you can implement a [modern data architecture on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/data-lake-house/) and realize the benefits of low latency insights with streaming technologies. This modern data architecture enables you to collect, manage, process, and analyze all your real-time streaming data in a simple and integrated fashion. A modern data streaming architecture also allows you to use all your data for a variety of use cases, such as streaming logs and event data to build live dashboards, delivering streaming data into data lakes and data warehouses, and building real-time analytics and event driven applications.

 We first discuss the concept of the modern data architecture approach, modern data streaming architecture, then present three modern data architecture data movement patterns to derive insights from your near real-time streaming data, using AWS purpose-built analytics services.
