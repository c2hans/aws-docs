---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/introduction.html
---

# Migrating to Amazon OpenSearch Service
<a name="introduction"></a>

*Muhammad Ali, Prashant Agrawal (SSA), Kevin Fallis, Vivek Gautam, Aneri Modi, Bharav Patel, and Brian Presley, Amazon Web Services*

For many customers, migrating self-managed Elasticsearch or OpenSearch deployments to [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) is challenging. The common challenges are of workload assessment, capacity planning, and architectural optimization. There are also questions concerning how to meet all requirements of operational analytics applications from on-premises data centers in the Amazon Web Services (AWS) Cloud. This guide covers the overall journey of a migration to Amazon OpenSearch Service, and provides best practices that AWS experts have accumulated over time. The step-by-step instructions can help you conduct your migrations in an effective and efficient approach. This guide mainly covers Amazon OpenSearch Service provisioned domains and not Amazon OpenSearch Serverless collections.

## Overview
<a name="overview"></a>

[OpenSearch](https://opensearch.org/) is a distributed, open-source search and analytics suite used for a broad set of operational analytics use cases such as real-time application monitoring, log analytics, data observability, and application and product catalog search. OpenSearch provides low-latency search response. It also offers fast access to large volumes of data with an integrated open-source data visualization tool called *OpenSearch Dashboards*.

Amazon OpenSearch Service supports performing interactive log analytics, real-time application monitoring, website search, and more. Amazon OpenSearch Service offers the latest versions of OpenSearch and support for 19 versions of Elasticsearch (versions 1.5–7.10). It also provides visualization capabilities powered by OpenSearch Dashboards and Kibana (versions 1.5–7.10). Amazon OpenSearch Service currently has tens of thousands of active customers with hundreds of thousands of clusters processing hundreds of trillions of requests per month.

Managing OpenSearch or Elasticsearch clusters on premises or on cloud infrastructure is highly complex, expensive, and tedious work. To run these clusters, you must provision and maintain the infrastructure. The efforts include the following:
+ Hardware procurement and setup
+ Software installation
+ Configuration, patching, and upgrading
+ Reliability and availability considerations
+ Performance and scalability considerations
+ Security and compliance considerations, such as network isolation, fine-grained access control, encryptions, and compliance programs such as the following:
  + Federal Risk and Authorization Management Program(FedRAMP)
  + General Data Protection Regulation (GDPR)
  + Health Insurance Portability and Accountability Act (HIPAA)
  + International Organization for Standardization (ISO)
  + Payment Card Industry Data Security Standard (PCI DSS)
  + System and Organization Controls (SOC).

By comparison, Amazon OpenSearch Service manages these tasks for you. In this guide, you will learn approaches and best practices for migrating on-premises or self-managed Elasticsearch or OpenSearch to the fully managed Amazon OpenSearch Service.
