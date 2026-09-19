---
source_url: https://docs.aws.amazon.com/solutions/scalable-analytics-using-apache-druid-on-aws/index.html
---

---
title: 'Guidance for Scalable Analytics Using Apache Druid on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/scalable-analytics-using-apache-druid-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Scalable Analytics Using Apache Druid on AWS

## Overview

This Guidance demonstrates how to build a robust, scalable, real-time analytics solution for massive data volumes, leveraging Apache Druid and AWS services. It shows how to deploy Druid on AWS infrastructure in a cost-effective and highly available manner, taking advantage of AWS elasticity and flexible pricing models. The resulting fault-tolerant data environment efficiently scales with growing business demands while maintaining high performance. This Guidance enables you to process and analyze large datasets in real-time, enabling faster and more informed decision-making across your organization.

## Benefits

### Accelerate time-to-insight with scalable analytics

Deploy a production-ready Apache Druid environment that automatically scales to match your analytics workload. Focus on deriving insights while AWS manages the underlying infrastructure complexity.

### Strengthen security and compliance

Protect your analytics platform with defense-in-depth security including network isolation, encryption, and access controls. Meet compliance requirements through comprehensive audit logging and monitoring.

### Optimize analytics costs

Reduce operational costs through automatic resource scaling and workload-optimized instance selection. Pay only for the resources you need with demand-based scaling across compute tiers.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/scalable-analytics-using-apache-druid-on-aws.pdf)

![Architecture diagram](/images/solutions/scalable-analytics-using-apache-druid-on-aws/images/scalable-analytics-using-apache-druid-on-aws-1.png)

1. **Step 1**: AWS WAF protects the Druid web console and Druid API endpoints against common web exploits and bots that may affect availability, compromise security, or consume excessive resources. AWS WAF is only provisioned and deployed for internet facing clusters.
1. **Step 2**: A security hardened Linux server (Bastion host) manages access to the Druid servers running in a private network separate from an external network. It can also be used to access the Druid web console through SSH tunneling, where a private Application Load Balancer (ALB) is deployed.
1. **Step 3**: ALB serves as the single point of contact for clients. The load balancer distributes incoming application traffic from identity providers—such as object identifiers (OIDS) and lightweight directory access protocol (LDAP)—across multiple query servers in multiple Availability Zones.
1. **Step 4**: The private subnet consists of the following:
1. **Step 4a**: The Druid Master Auto Scaling group contains a collection of Druid master servers. A master server manages data ingestion and availability and is responsible for starting new ingestion jobs and coordinating availability of data on the data servers. Within a master server, functionality is split between two processes: the Coordinator and Overlord.
1. **Step 4b**: The Druid Data Auto scaling group contains a collection of Druid data servers. A data server runs ingestion jobs and stores queryable data. Within a data server, functionality is split between two processes: the Historical and MiddleManager.
1. **Step 4c**: The Druid Query Auto scaling group contains a collection of Druid query servers. A query server provides the endpoints that users and client applications interact with, routing queries to data servers or other query servers. Within a query server, functionality is split between two processes; the Broker and Router.
1. **Step 4d**: The ZooKeeper Auto Scaling group contains a collection of ZooKeeper servers. Apache Druid uses Apache ZooKeeper for management of current cluster state.
1. **Step 5**: An Amazon Simple Storage Service (Amazon S3) bucket provides deep storage for the Apache Druid cluster. Deep storage is the location where the segments are stored.
1. **Step 6**: AWS Secrets Manager stores the secrets used by Apache Druid, including the Amazon Relational Database Service (Amazon RDS) secret and the administrator user secret. It also stores the credentials for the system account the Druid components use to authenticate with each other.
1. **Step 7**: Amazon CloudWatch supports logs, metrics, and dashboards.
1. **Step 8**: An Amazon Aurora PostgreSQL database provides the metadata storage for the Apache Druid cluster. Druid uses the metadata store to house only metadata about the system and does not store the actual data.
1. **Step 9**: The notification system, powered by Amazon Simple Notification Service (Amazon SNS), delivers alerts or alarms promptly when system events occur. This helps ensure immediate awareness and action when needed.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](/solutions/latest/scalable-analytics-using-apache-druid-on-aws/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions/scalable-analytics-using-apache-druid-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
