---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html
---

# Replicate mainframe databases to AWS by using Precisely Connect
<a name="replicate-mainframe-databases-to-aws-by-using-precisely-connect"></a>

*Lucio Pereira, Sayantan Giri, and Balaji Mohan, Amazon Web Services*

## Summary
<a name="replicate-mainframe-databases-to-aws-by-using-precisely-connect-summary"></a>

This pattern outlines steps for replicating data from mainframe databases to Amazon data stores in near real time by using Precisely Connect. It implements an event-based architecture with Amazon Managed Streaming for Apache Kafka (Amazon MSK) and custom database connectors in the cloud to improve scalability, resilience, and performance.

Precisely Connect is a replication tool that captures data from legacy mainframe systems and integrates it into cloud environments. Data is replicated from mainframes to AWS through change data capture (CDC) by using near real-time message flows with low-latency and high-throughput heterogeneous data pipelines.

This pattern also covers a disaster recovery strategy for resilient data pipelines with multi-Region data replication and failover routing.

## Prerequisites and limitations
<a name="replicate-mainframe-databases-to-aws-by-using-precisely-connect-prereqs"></a>

**Prerequisites**
+ An existing mainframe database—for example, IBM DB2, IBM Information Management System (IMS), or Virtual Storage Access Method (VSAM)—that you want to replicate to the AWS Cloud
+ An active [AWS account](https://aws.amazon.com/account/)
+ [AWS Direct Connect](https://aws.amazon.com/directconnect/) or [AWS Virtual Private Network (AWS VPN](https://aws.amazon.com/vpn/)) from your corporate environment to AWS
+ A [virtual private cloud](https://aws.amazon.com/vpc/) with a subnet that is reachable by your legacy platform

## Architecture
<a name="replicate-mainframe-databases-to-aws-by-using-precisely-connect-architecture"></a>

**Source technology stack**

A mainframe environment that includes at least one of the following databases:
+ IBM IMS database
+ IBM DB2 database
+ VSAM files

**Target technology stack**
+ Amazon MSK
+ Amazon Elastic Kubernetes Service (Amazon EKS) and Amazon EKS Anywhere
+ Docker
+ An AWS relational or NoSQL database such as the following:
  + Amazon DynamoDB
  + Amazon Relational Database Service (Amazon RDS) for Oracle, Amazon RDS for PostgreSQL, or Amazon Aurora
  + Amazon ElastiCache for Redis
  + Amazon Keyspaces (for Apache Cassandra)

**Target architecture**

*Replicating mainframe data to AWS databases*

The following diagram illustrates the replication of mainframe data to an AWS database such as DynamoDB, Amazon RDS, Amazon ElastiCache, or Amazon Keyspaces. The replication occurs in near real time by using Precisely Capture and Publisher in your on-premises mainframe environment, Precisely Dispatcher on Amazon EKS Anywhere in your on-premises distributed environment, and Precisely Apply Engine and database connectors in the AWS Cloud.

![Replicating mainframe data to AWS databases](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/17ac53b7-86d5-4a8c-a55f-56b6338a1af3/images/777dd7da-48ed-4510-b8fa-9041be042671.png)

The diagram shows the following workflow:

1. Precisely Capture gets mainframe data from CDC logs and maintains the data in internal transient storage.

1. Precisely Publisher listens for changes in the internal data storage and sends CDC records to Precisely Dispatcher through a TCP/IP connection.

1. Precisely Dispatcher receives the CDC records from Publisher and sends them to Amazon MSK. Dispatcher creates Kafka keys based on the user configuration and multiple worker tasks to push data in parallel. Dispatcher sends an acknowledgment back to Publisher when records have been stored in Amazon MSK.

1. Amazon MSK holds the CDC records in the cloud environment. The partition size of topics depends on your transaction processing system (TPS) requirements for throughput. The Kafka key is mandatory for further transformation and transaction ordering.

1. The Precisely Apply Engine listens to the CDC records from Amazon MSK and transforms the data (for example, by filtering or mapping) based on target database requirements. You can add customized logic to the Precisely SQD scripts. (SQD is Precisely’s proprietary language.) The Precisely Apply Engine transforms each CDC record to Apache Avro or JSON format and distributes it to different topics based on your requirements.

1. The target Kafka topics hold CDC records in multiple topics based on the target database, and Kafka facilitates transaction ordering based on the defined Kafka key. The partition keys align with the corresponding partitions to support a sequential process.

1. Database connectors (customized Java applications) listen to the CDC records from Amazon MSK and store them in the target database.

1. You can select a target database based on your requirements. This pattern supports both NoSQL and relational databases.

*Disaster recovery*

Business continuity is key to your organization’s success. The AWS Cloud provides capabilities for high availability (HA) and disaster recovery (DR), and supports your organization’s failover and fallback plans. This pattern follows an active/passive DR strategy and provides high-level guidance for implementing a DR strategy that meets your RTO and RPO requirements.

The following diagram illustrates the DR workflow.

![Disaster recovery workflow for replicating mainframe data on AWS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/17ac53b7-86d5-4a8c-a55f-56b6338a1af3/images/9cccba7a-7a25-411e-829f-7cd5a7a20ab4.png)

The diagram shows the following:

1. A semi-automated failover is required if any failure happens in AWS Region 1. In the case of failure in Region 1, the system must initiate routing changes to connect Precisely Dispatcher to Region 2.

1. Amazon MSK replicates data through mirroring between Regions, For this reason, during failover, the Amazon MSK cluster in Region 2 has to be promoted as the primary leader.

1. The Precisely Apply Engine and database connectors are stateless applications that can work in any Region.

1. Database synchronization depends on the target database. For example, DynamoDB can use global tables, and ElastiCache can use global datastores.

*Low-latency and high-throughput processing through database connectors*

Database connectors are critical components in this pattern. Connectors follow a listener-based approach to collect data from Amazon MSK and send transactions to the database through high-throughput and low-latency processing for mission-critical applications (tiers 0 and 1). The following diagram illustrates this process.

![Using database connectors to replicate mainframe data on AWS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/17ac53b7-86d5-4a8c-a55f-56b6338a1af3/images/79479634-becb-4212-bbfc-1a3b17ae1bed.png)

This pattern supports the development of a customized application with single-threaded consumption through a multithreaded processing engine.

1. The connector main thread consumes CDC records from Amazon MSK and sends them to the thread pool for processing.

1. Threads from the thread pool process CDC records and send them to the target database.

1. If all threads are busy, the CDC records are kept on hold by the thread queue.

1. The main thread waits to get all the records cleared from the thread queue and commits offsets into Amazon MSK.

1. The child threads handle failures. If failures happen during processing, the failed messages are sent to the DLQ (dead letter queue) topic.

1. The child threads initiate conditional updates (see [Condition expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html) in the DynamoDB documentation), based on the mainframe timestamp, to avoid any duplication or out-of-order updates in the database.

For information about how to implement a Kafka consumer application with multi-threading capabilities, see the blog post [Multi-Threaded Message Consumption with the Apache Kafka Consumer](https://www.confluent.io/blog/kafka-consumer-multi-threaded-messaging/) on the Confluent website.

## Tools
<a name="replicate-mainframe-databases-to-aws-by-using-precisely-connect-tools"></a>

**AWS services**
+ [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) is a fully managed service that helps you build and run applications that use Apache Kafka to process streaming data.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without having to install or maintain your own Kubernetes control plane or nodes.
+ [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/) helps you deploy, use, and manage Kubernetes clusters that run in your own data centers.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon ElastiCache](https://docs.aws.amazon.com/elasticache/) helps you set up, manage, and scale distributed in-memory cache environments in the AWS Cloud.
+ [Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html) is a managed database service that helps you migrate, run, and scale your Cassandra workloads in the AWS Cloud.

**Other tools**
+ [Precisely Connect](https://www.precisely.com/product/precisely-connect/connect) integrates data from legacy mainframe systems such as VSAM datasets or IBM mainframe databases into next-generation cloud and data platforms.

## Best practices
<a name="replicate-mainframe-databases-to-aws-by-using-precisely-connect-best-practices"></a>
+ Find the best combination of Kafka partitions and multi-threaded connectors to balance optimal performance and cost. Multiple Precisely Capture and Dispatcher instances can increase cost because of higher MIPS (million instructions per second) consumption.
+ Avoid adding data manipulation and transformation logic to the database connectors. For this purpose, use the Precisely Apply Engine, which provides processing times in microseconds.
+ Create periodic request or health check calls to the database (*heartbeats*) in database connectors to warm up the connection frequently and reduce latency.
+ Implement thread pool validation logic to understand the pending tasks in the thread queue and wait for all threads to be completed before the next Kafka polling. This helps avoid data loss if a node, container, or process crashes.
+ Expose latency metrics through health endpoints to enhance observability capabilities through dashboards and tracing mechanisms.

## Epics
<a name="replicate-mainframe-databases-to-aws-by-using-precisely-connect-epics"></a>

### Prepare the source environment (on premises)
<a name="prepare-the-source-environment-on-premises"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the mainframe process (batch or online utility) to start the CDC process from mainframe databases. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | Mainframe engineer |
| Activate mainframe database log streams. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | Mainframe DB specialist |
| Use the Capture component to capture CDC records. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | Mainframe engineer, Precisely Connect SME |
| Configure the Publisher component to listen to the Capture component. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | Mainframe engineer, Precisely Connect SME |
| Provision Amazon EKS Anywhere in the on-premises distributed environment. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | DevOps engineer |
| Deploy and configure the Dispatcher component in the distributed environment to publish the topics in the AWS Cloud. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | DevOps engineer, Precisely Connect SME |

### Prepare the target environment (AWS)
<a name="prepare-the-target-environment-aws"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provision an Amazon EKS cluster in the designated AWS Region. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | DevOps engineer, Network administrator |
| Provision an MSK cluster and configure applicable Kafka topics. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | DevOps engineer, Network administrator |
| Configure the Apply Engine component to listen to the replicated Kafka topics.  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | Precisely Connect SME |
| Provision DB instances in the AWS Cloud. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | Data engineer, DevOps engineer |
| Configure and deploy database connectors to listen to the topics published by the Apply Engine. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | App developer, Cloud architect, Data engineer |

### Set up business continuity and disaster recovery
<a name="set-up-business-continuity-and-disaster-recovery"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Define disaster recovery goals for your business applications. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | Cloud architect, Data engineer, App owner |
| Design disaster recovery strategies based on defined RTO/RPO. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | Cloud architect, Data engineer |
| Provision disaster recovery clusters and configurations. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | DevOps engineer, Network administrator, Cloud architect |
| Test the CDC pipeline for disaster recovery.  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-mainframe-databases-to-aws-by-using-precisely-connect.html) | App owner, Data engineer, Cloud architect |

## Related resources
<a name="replicate-mainframe-databases-to-aws-by-using-precisely-connect-resources"></a>

**AWS resources**
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
+ [Condition expressions with Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html)
+ [Amazon EKS](https://docs.aws.amazon.com/eks/index.html)
+ [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/)
+ [Amazon ElasticCache](https://docs.aws.amazon.com/elasticache/index.html)
+ [Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/?icmpid=docs_homepage_databases)
+ [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html)
+ [Amazon RDS and Amazon Aurora](https://docs.aws.amazon.com/rds/index.html)
+ [Amazon VPC](https://docs.aws.amazon.com/vpc/index.html)

**Precisely Connect resources**
+ [Precisely Connect Overview](https://www.precisely.com/product/precisely-connect/connect)
+ [Change Data Capture with Precisely Connect](https://help.precisely.com/r/Connect-CDC-SQData/4.1/en-US/Connect-CDC-SQData-Installation/Connect-CDC-SQData-Architecture)

**Confluent resources**
+ [Multi-Threaded Message Consumption with the Apache Kafka Consumer](https://www.confluent.io/blog/kafka-consumer-multi-threaded-messaging/)
