---
source_url: https://docs.aws.amazon.com/solutions/active-active-replication-on-amazon-rds-for-mysql/index.html
---

---
title: 'Guidance for Active-Active Replication on Amazon RDS for MySQL'
canonical_url: https://docs.aws.amazon.com/solutions/active-active-replication-on-amazon-rds-for-mysql/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Active-Active Replication on Amazon RDS for MySQL

## Overview

This Guidance demonstrates how to configure active-active replication with up to nine Amazon Relational Database Service (Amazon RDS) for MySQL instances using the Group Replication plugin. With the provided AWS CloudFormation stacks and scripts, you can implement a multi-primary mode topology to achieve continuous availability for your applications. Write operations are distributed across multiple database instances in an active-active cluster, maximizing availability and reducing write latency.

## How it works

This architecture diagram shows how to setup an active-active replication configuration for up to 9 Amazon RDS for MySQL instances using the Group Replication plugin. This allows for high availability and failover capabilities for your MySQL database.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/active-active-replication-on-amazon-rds-for-mysql.pdf)

![Architecture diagram](/images/solutions/active-active-replication-on-amazon-rds-for-mysql/images/active-active-replication-on-amazon-rds-for-mysql-1.png)

1. **Step 1**: An existing Amazon Relational Database Service (Amazon RDS) for MySQL instance is required to deploy this Guidance. The source application runs on Amazon Elastic Compute Cloud (Amazon EC2), Amazon Elastic Kubernetes Service (Amazon EKS), Amazon Elastic Container Service (Amazon ECS), or an environment of your choice. In this Guidance, we assume the application is deployed through Amazon EC2 instances across multiple Availability Zones (AZs). The Amazon RDS for MySQL instance can be encrypted using the default Amazon Key Management Service (AWS KMS) or a customer managed key.
1. **Step 2**: Once the prerequisites are complete, the AWS CloudFormation stacks will create resources such as RDS for MySQL instances, ProxySQL, and a Network Load Balancer. Additionally, an Amazon Simple Notification Service (Amazon SNS) topic, an AWS Lambda function, and Amazon EventBridge rules will be deployed.
1. **Step 2a**: Network Load Balancer automatically distributes your incoming traffic from your applications across multiple targets, such as ProxySQL on Amazon EC2 instances, in one or more AZs.
1. **Step 2b**: ProxySQL redirects the traffic to the active DB instance of the Group Replication cluster.
1. **Step 3**: An Amazon CloudWatch alarm is created to monitor RDS failure events (such as DB instance shutdown, restart, failover, or failure) and notify through an Amazon SNS topic.
1. **Step 4**: An Amazon EventBridge rule is configured to monitor for RDS failure events (such as DB instance shutdown, restart, or failure) and sends notifications through an Amazon SNS topic. The rule also calls a Lambda function when the event occurs.
1. **Step 5**: A Lambda function provides a framework to add any additional functionalities during the RDS failure event. Some of the functionalities that can be added, but are not limited to, are: If one of the instances in a Group Replication topology is restarted, verify that the restarted DB instance is joined back to the Group Replication topology. If one of the instances in a Group Replication topology is upgraded, the DB instance will be in read_only mode. In this case, upgrade the other DB instances in the replication topology. Perform periodic health checks using MySQL performance schema tables, and if one DB instance is in a suspended state, redirect the traffic to other DB instances in the Group Replication topology.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-active-active-replication-on-amazon-rds-for-mysql)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

RDS for MySQL, EventBridge, Amazon SNS, and AWS CloudTrail help you with tracking and reviewing logs and information for quick error review and incident responses. Specifically, RDS for MySQL allows you to set up multi-primary mode between your RDS for MySQL database instances to provide continuous availability for your applications. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Elastic Load Balancing (ELB) automatically distributes your incoming traffic across multiple targets; it monitors the health of its registered targets and routes traffic only to the healthy targets. AWS KMS is used in this Guidance to provide default encryption with the option to use custom KMS keys. The encrypted DB instances for RDS for MySQL offer an additional layer of data protection by encrypting underlying storage, backups, replicas, and snapshots. Lastly, consider protecting your resources with identity-based policies such as AWS Identity and Access Management (IAM). [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

RDS for MySQL offers high availability through data replication across multiple AZs, and the Group Replication plugin offers data resilience. For durable storage for RDS snapshots, use Amazon Simple Storage Service (Amazon S3) to secure storage for critical data. ELB automatically distributes your incoming traffic across multiple targets, such as Amazon EC2 instances, containers, and IP addresses in one or more AZs. It monitors the health of its registered targets and routes traffic only to the healthy targets, which improves application availability. ELB scales your load balancer as your incoming traffic changes over time. Lastly, CloudFormation automates resource deployment and provisions a rollback upon failures, supporting reliability in the midst of failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Use the Group Replication plugin in RDS for MySQL, along with configurations like Transaction Size and Follow Controls, to optimize your application's performance and replication throughput. Also, using ProxySQL to split read and write operations across the RDS DB instances further enhances your application's performance. Moreover, Lambda and EventBridge are scalable, customizable services that help you maintain the active-active cluster topology. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

RDS for MySQL allows you to deploy scalable MySQL servers with cost-efficient and resizable hardware capacity. And with ELB, you pay only for what you use. Finally, the broad and deep portfolio of Amazon EC2 instances, combined with Amazon EC2 Auto Scaling, helps you tailor compute resources to your business needs and scale capacity up and down based on observed demand. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The auto scaling capabilities of Amazon EC2 help align resources with application needs, minimizing waste and promoting sustainability. We recommend Graviton-based Amazon EC2 instances for RDS for MySQL to reduce your carbon footprint by using up to 60% less energy for the same performance as comparable x86-based instances. Additionally, the ability to stop and start RDS for MySQL DB instances eliminates the need for running resources for temporary testing or daily development activities. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

This blog post discusses MySQL Group Replication, its use cases, configuration, application-level considerations, and significance in modern database management.

[Read the blog](https://aws.amazon.com/blogs/database/introducing-group-replication-plugin-for-active-active-replication-on-amazon-rds-for-mysql/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
