---
source_url: https://docs.aws.amazon.com/solutions/cross-chain-analytics-using-bitcoin-and-ethereum-open-data-on-aws/index.html
---

---
title: 'Guidance for Cross-Chain Analytics using Bitcoin and Ethereum Open Data on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/cross-chain-analytics-using-bitcoin-and-ethereum-open-data-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Cross-Chain Analytics using Bitcoin and Ethereum Open Data on AWS

## Overview

This Guidance helps you extract, transform, and load (ETL) blockchain data into a column-oriented storage format that allows for easy access and expedited analysis. It consists of an open-source architecture for running cross-chain analytics on public blockchain data in addition to Bitcoin and Ethereum public datasets available through [Open Data on AWS](https://aws.amazon.com/opendata/) . This Guidance pulls data from the public Bitcoin and Ethereum blockchains and normalizes it into tabular data structures for blocks, transactions, and additional tables for data inside a block.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/cross-chain-analytics-using-bitcoin-and-ethereum-open-data-on-aws.pdf)

![Architecture diagram](/images/solutions/cross-chain-analytics-using-bitcoin-and-ethereum-open-data-on-aws/images/cross-chain-analytics-using-bitcoin-and-ethereum-open-data-on-aws-1.png)

1. **Step 1**: To consume the data for Ethereum and Bitcoin, use Amazon Managed Blockchain for Ethereum and self-hosted Bitcoin Core through Amazon Elastic Container Registry (Amazon ECR), Amazon Elastic File System (Amazon EFS), Amazon DynamoDB, and Erigon Ethereum nodes.
1. **Step 2**: Deploy the Bitcoin feed and worker services through AWS Copilot on AWS Fargate and Amazon Elastic Container Store (Amazon ECS), and subscribe to the Bitcoin Core node to fetch historical and live data.
1. **Step 3**: Deploy the Ethereum feed and worker services through AWS Copilot on Fargate and Amazon ECS. Subscribe to the Managed Blockchain for Ethereum and Erigon Ethereum node to fetch historical and live data.
1. **Step 4**: Amazon Simple Storage Service (Amazon S3) stores data from the feeds as Parquet files. Amazon S3 ingests new data immediately after the creation of a new block.
1. **Step 5**: AWS Glue aggregates everyday and intraday Parquet files.
1. **Step 6**: With catalog data in AWS Glue Data Catalog, Amazon Athena and Amazon Redshift can query historical and live data.
1. **Step 7**: Amazon QuickSight visualizes data for business analysts.
1. **Step 8**: Researchers and data scientists use Amazon SageMaker to run cross chain analytics in Jupyter Notebooks.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-digital-assets-on-aws/tree/main/analytics)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

With Managed Blockchain, you can complete the deployment of Ethereum full node(s) to connect to public testnets and the Ethereum mainnet in a matter of minutes. This is in contrast to the slow deploy and sync times of self-hosted Ethereum nodes that can take 24-36 hours. We have built observability into the architecture with process-level metrics, logs, and dashboards. Extend these mechanisms to your needs, and create alarms in Amazon CloudWatch to inform your on-call team of any issues. Finally, you can automate the deployment of this Guidance with infrastructure as code frameworks such as AWS Cloud Development Kit (CDK) or AWS CloudFormation. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses role-based access with AWS Identity and Access Management (IAM). The Amazon S3 bucket has encryption enabled, is private, and blocks public access. All roles are defined with least-privilege access, and all communications between services stay within the customer account. Administrators can control access to the Jupyter notebook, SageMaker, Amazon Redshift, Athena, and QuickSight through IAM roles. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Various components in the architecture are deployed across multiple Availability Zones, such as the Managed Blockchain Ethereum nodes. By nature, all the serverless components, such as Fargate, are highly available and automatically scale to accommodate demand. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses serverless technologies, which provide built-in fault tolerance and continuous scaling. Serverless services also allow for comparative testing against varying load levels and minimizes undifferentiated tasks like capacity provisioning and patching, so you can focus on business needs rather than server management. Further, you can enable auto scaling for AWS Glue, which will automatically remove workers from the cluster depending on the parallelism at each stage of the job run. Similarly, Amazon S3 automatically scales to meet high request rates. There are no limits to the number of prefixes in a bucket, and you can increase read or write performance through parallelization. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using the AWS Glue serverless computing platform for ETL and Athena for serverless query, you pay only for the resources you use. To further optimize cost, you can use the Amazon S3 Intelligent-Tiering storage class, which automatically selects the ideal cost-effective storage tier for your content depending on its access patterns, such as frequency of access. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using managed services such as Fargate and AWS Glue, we minimize the environmental impact of the backend services. Furthermore, public Ethereum blockchain shifted from the proof-of-work to the proof-of-stake consensus mechanism in late 2022, reducing Ethereum’s energy consumption by ~99.5 percent.* *The Merge, Ethereum, April 19, 2023. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Access Bitcoin and Ethereum open datasets for cross-chain analytics**: This post shares an open-source solution for running cross-chain analytics on public blockchain data along with public datasets for Bitcoin and Ethereum available through AWS Open Data.

[Learn more](https://aws.amazon.com/blogs/database/access-bitcoin-and-ethereum-open-datasets-for-cross-chain-analytics/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
