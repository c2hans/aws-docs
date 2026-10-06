---
source_url: https://docs.aws.amazon.com/solutions/disaster-recovery-using-amazon-aurora/index.html
---

---
title: 'Guidance for Disaster Recovery Using Amazon Aurora'
canonical_url: https://docs.aws.amazon.com/solutions/disaster-recovery-using-amazon-aurora/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Disaster Recovery Using Amazon Aurora

## Overview

This Guidance shows how to deploy a comprehensive disaster recovery (DR) solution for Amazon Aurora. Different business requirements necessitate different ways of achieving your DR objectives, and finding the best option to meet your recovery point objective (RPO) and recovery time objective (RTO) can be overwhelming. This Guidance evaluates the most common routes to take when developing the database portion of your DR plan. By spanning your database resources to a secondary AWS Region and using AWS Backup or Aurora global databases, you can restore your data more easily in the event of a disaster, minimizing interruptions to your business.

## How it works

### Replicate data

This architecture diagram shows how to implement an Aurora Global database to replicate data to a secondary Region.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/disaster-recovery-using-amazon-aurora.pdf)Step 1Prerequisites: This Guidance requires an existing Amazon Aurora Regional cluster. The application can run on Amazon Elastic Compute Cloud (Amazon EC2), Amazon Elastic Kubernetes Service (Amazon EKS), Amazon Elastic Container Service (Amazon ECS), or another service of your choice. This Guidance assumes you have used Amazon EC2 instances in virtual private clouds (VPCs) across multiple Availability Zones (AZs). You can encrypt an Aurora cluster using the default AWS Key Management Service (AWS KMS) or using a customer-managed key (CMK).Step 2AWS CloudFormation creates resources, including an Aurora read replica in the primary AWS Region if one does not exist already and an Aurora global database with a reader instance in the secondary Region. An Amazon CloudWatch dashboard, an Amazon Simple Notification Service (Amazon SNS) topic, an AWS Lambda function, and Amazon EventBridge rules are deployed in both Regions.Step 3The CloudWatch dashboard is configured in the primary and secondary Regions to monitor key metrics related to Aurora, along with the replication status.Step 4A CloudWatch alarm is created in both Regions to generate alarms for AuroraGlobalDBReplicationLag metrics and notifications through the Amazon SNS topic.Step 5An EventBridge rule is configured for planned switchovers and unplanned failovers. When an event occurs, it sends notifications using Amazon SNS and calls the Lambda functions in both Regions.Step 6The Lambda function provides a framework to add any additional functionalities during the failover event. For example: You can configure the application to use an Amazon Route 53 in a newly promoted Region during a failover event so that no application configuration is required during the event. You can configure the application to restart an Amazon EC2 instance or the application deployment pods in the Amazon EKS cluster after the database failover event.### Backup data

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/disaster-recovery-using-amazon-aurora.pdf#page=2)Step 1A preexisting organizational structure within AWS Organizations is necessary to establish cross-account AWS Backup between two accounts: Account A, which serves as the production or source account, and Account B, which is the central backup or target account. Notably, this Guidance provides the flexibility to include multiple target accounts.Step 2An existing Aurora cluster in the source account is encrypted using a CMK that is shared across the source and target accounts. The cluster should also be tagged appropriately so that the solution can identify the desired resources for backup.Step 3CloudFormation is used to deploy the solution resources in your source and target AWS accounts and Regions. The required CloudFormation stacks are provided as part of this solution.Step 4The Aurora cluster in Region A of the production account is backed by AWS Backup according to the schedule you provided while deploying the solution. The backups are stored in an AWS Backup vault encrypted with an AWS KMS CMK.Step 5AWS Backup copies the backups to the cross-account (that is, the target account) and stores it in the backup vault in Account B Region A. The backup vault is encrypted using a CMK created by CloudFormation.Step 6Once the cross-account backup copy is complete, an EventBridge rule in the source account forwards a backup copy complete notification to the target account event bus (Account B Region A).Step 7An EventBridge rule in the target account in Region A identifies the notification as an incoming event.Step 8Once the event is received in the target account, the EventBridge rule invokes a Lambda function to finally copy the backup to the desired destination (Account B Region B) and store it in the AWS Backup vault in Region B.Step 9The backup of your Aurora cluster is now available in the target account in Region B and is stored in the AWS Backup vault of Region B. The backup vault is encrypted with an AWS KMS CMK. This backup can be used to restore the Aurora database.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment.

[Open implementation guide](https://aws-solutions-library-samples.github.io/ai-ml/disaster-recovery-using-amazon-aurora.html)

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-disaster-recovery-using-amazon-aurora)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Aurora enables you to customize DR solutions based on your RPO and RTO needs to uphold operational continuity during disaster events. CloudWatch and AWS CloudTrail aid in tracking and reviewing logs and information. By contributing to operational visibility, these services enable quick and effective error review and incident response. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses AWS Identity and Access Management (IAM) to enforce the least-privilege model, limiting access to resources. Private resources, protected by IAM identity-based policies, offer heightened security. Additionally, it uses AWS-managed roles in CloudFormation to control access. AWS KMS provides default encryption and the option to use custom keys to safeguard data. Encrypted DB clusters in Aurora offer an additional layer of data protection by encrypting underlying storage, backups, replicas, and snapshots, helping you meet compliance requirements. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Aurora supports data resilience by using replication across multiple AZs to maintain high availability. Amazon Simple Storage Service (Amazon S3) offers durable storage for critical data, like Aurora snapshots and AWS Backup data. CloudFormation automates resource deployment, as well as rollbacks upon failures. CloudWatch dashboards and Amazon SNS notifications enable monitoring and alerts, and AWS Backup facilitates backup and restore operations for Aurora databases, all contributing to a highly reliable architecture. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses services selected to enhance performance. Aurora offers low-latency, storage-based replication, and Aurora global databases provide cross-Region replication, helping you minimize the impact on workload performance while maintaining data availability in the event of a failure. Additionally, CloudFormation enables you to customize values to meet service-level agreements and RPO and RTO requirements. Finally, AWS Backup uses Lambda and EventBridge for scalable backup frequency that you can optimize based on your business requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Aurora global databases and AWS Backup offer a pay-as-you-go model that helps you avoid maintenance overhead. You can also choose a headless configuration for Aurora global databases, reducing costs to storage and replicated I/O. Additionally, AWS Backup lets you adjust configurations, such as for retention periods, to optimize costs based on your recovery objectives. As a result of using these services, you can reduce unnecessary expenses while maintaining data integrity and availability. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The services in this Guidance contribute to sustainability by scaling resources based on workload demands. Aurora enables dynamic resizing of storage space to achieve optimal resource utilization and minimize unnecessary consumption. Aurora global databases replicate these dynamic changes across Regions to maintain consistency. Additionally, AWS Backup offers incremental and continuous backups, reducing data redundancy and optimizing backup efficiency. By using this Guidance with Aurora serverless v2 clusters, you can enhance capacity adjustments, aligning resources with application needs and minimizing waste. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
