---
source_url: https://docs.aws.amazon.com/solutions/near-real-time-data-migration-from-apache-cassandra-to-amazon-keyspaces/index.html
---

---
title: 'Guidance for Near Real-Time Data Migration from Apache Cassandra to Amazon Keyspaces'
canonical_url: https://docs.aws.amazon.com/solutions/near-real-time-data-migration-from-apache-cassandra-to-amazon-keyspaces/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Near Real-Time Data Migration from Apache Cassandra to Amazon Keyspaces

## Overview

This Guidance shows how to migrate self-managed Apache Cassandra clusters to the fully-managed Amazon Keyspaces service using the open-source CQLReplicator tool developed by AWS Solutions Architects. The CQLReplicator tool enables near real-time data migration by initiating two AWS Glue jobs—a Discovery job and a Replicator job. The Discovery job collects and stores the latest primary keys from the Cassandra source. The Replicator job scans the Amazon Keyspaces ledger, queries the Cassandra source, and inserts the latest data into the Amazon Keyspaces table. By using this tool, you can reduce your operational overhead by offloading your Cassandra clusters to AWS, achieve centralized monitoring through the integration with Amazon CloudWatch, and simplify the migration experience due to the automations provided by the CQLReplicator.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/near-real-time-data-migration-from-apache-cassandra-to-amazon-keyspaces.pdf)

![Architecture diagram](/images/solutions/near-real-time-data-migration-from-apache-cassandra-to-amazon-keyspaces/images/near-real-time-data-migration-from-apache-cassandra-to-amazon-keyspaces-1.png)

1. **Step 1**: Initiate the CQLReplicator in AWS CloudShell, which creates two AWS Glue jobs called Discovery and Replicator.
1. **Step 2**: The AWS Glue Discovery job connects to the Apache Cassandra source cluster and collects all the primary keys with the latest timestamp.
1. **Step 3**: The Discovery job then persists the primary keys in an Amazon Simple Storage Service (Amazon S3) bucket. If the Discovery job has been executed previously, it compares the old and new primary keys to determine the latest changes. It then stores the changes in Amazon S3 and records the location of the bucket key in a ledger table stored in Amazon Keyspaces.
1. **Step 4**: The Replicator job scans the ledger table in Amazon Keyspaces for new change sets.
1. **Step 5**: When the Replicator job finds a change set, it reads the keys and queries the Apache Cassandra source cluster for the latest row data.
1. **Step 6**: The destination Amazon Keyspaces table will receive the data, including the complete primary key and the most recent row values.
1. **Step 7**: The AWS Glue jobs push all the logs to Amazon CloudWatch.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-near-real-time-data-migration-from-apache-cassandra-to-amazon-keyspaces?target=_blank)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS Glue automates your extract, transform, and load (ETL) processes, reducing the need for manual setup and management, while Amazon Keyspaces offloads database administration tasks, allowing your users to focus on application development. Integrated logging and monitoring capabilities in both services support efficient troubleshooting and issue resolution, enhancing operational excellence by streamlining operations and improving reliability. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Glue uses AWS Key Management Service (AWS KMS) to encrypt data at rest and TLS to secure data in transit. AWS Identity and Access Management (IAM) policies enable granular access control, allowing only authorized users access. AWS CloudTrail and CloudWatch provide logging and monitoring for comprehensive visibility into activities and resource usage, aiding in compliance and auditing. These features collectively support robust security for your ETL processes. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon Keyspaces is a fully managed and highly available NoSQL database service. It eliminates the need for manual infrastructure management, cross-Region replication, and provides built-in security features such as encryption and continuous backups. These features allow for seamless and secure operations for your users without the complexity of managing Apache Cassandra. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Keyspaces delivers low-latency, single-digit millisecond response times with tunable consistency levels and optimized Cassandra Query Language (CQL) capabilities. AWS Glue automates data preparation and integration tasks, dynamically scales resources for ETL jobs, and offers a serverless architecture with a built-in data catalog for expedited dataset discovery. Collectively, these services streamline data workflows for efficient, high-performing operations without the need for extensive manual intervention. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The use of Amazon S3 and Amazon Keyspaces services adheres to a pay-as-you-go pricing model so you only incur costs for the storage and throughput consumed. The tiered storage classes of Amazon S3 automatically transition data to lower-cost storage based on access patterns, thereby reducing expenses for infrequently accessed data. Furthermore, the serverless architecture of Amazon Keyspaces eliminates the need for provisioning and managing servers, further lowering operational costs. Collectively, these services provide a cost-effective approach for scalable storage and efficient data management without the overhead of maintaining hardware infrastructure. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS Lambda functions are architected upon a serverless model, thereby optimizing resource allocation and reducing the need to maintain physical hardware infrastructure. Furthermore, Lambda is only triggered in response to changes in the data of the base table, minimizing the compute resource run times. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
