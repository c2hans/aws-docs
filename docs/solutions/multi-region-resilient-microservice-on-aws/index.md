---
source_url: https://docs.aws.amazon.com/solutions/multi-region-resilient-microservice-on-aws/index.html
---

---
title: 'Guidance for Multi-Region Resilient Microservice on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/multi-region-resilient-microservice-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Multi-Region Resilient Microservice on AWS

Launch a failover sequence deployment across multiple AWS Regions to protect workloads

## Overview

This Guidance demonstrates how to build highly resilient web applications that can withstand disruptions, minimizing impact on revenue and application downtime. By leveraging a multi-Region architecture, automated failover orchestration, and comprehensive monitoring, this Guidance helps ensure critical web applications remain available and consistent, even in the face of significant impairments. You can reduce the blast radius of affected users, maintain data integrity, and make informed decisions on when to failover between primary and standby Regions to maximize uptime and protect business continuity.

## How it works

### Active/Active State

This architecture diagram shows the active/active state across two AWS Regions.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multi-region-resilient-microservice-on-aws.pdf?target=_blank)Step 1Amazon Route 53 failover records use Amazon Application Recovery Controller managed health checks to route requests to the active Regions.Step 2Application Load Balancers (ALBs) send requests to the user interface (UI) tasks on Amazon Elastic Container Service (Amazon ECS). Depending on the page being accessed, the UI will make a service call to the appropriate service through Amazon ECS Service Connect.Step 3As records are written to the writer instances of the Catalog and Orders Amazon Aurora global databases, they are replicated to the standby clusters.Step 4As records are written to the Carts Amazon DynamoDB global table in one Region, they are replicated to the table in the other Region.Step 5The Checkout service uses Amazon ElastiCache for Redis for temporarily caching the contents of the cart until the order is placed.Step 6The Orders service leverages Amazon MQ for RabbitMQ broker to publish order creation events for any downstream consumption purposes.Step 7Amazon CloudWatch Synthetics from each Region sends requests from the application in each Region (using the ALB's address) to the DNS name resolved through Route 53 and pushes the metrics, logs, and traces to CloudWatch.Step 8AWS Systems Manager automation runbooks automate the enabling and disabling of the Amazon Application Recovery Controller routing controls and the failing-over of the Aurora global databases.### Failover Sequence

This architecture diagram shows the failover sequence when the workload fails over to us-west-2 from us-east-1 AWS Region.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multi-region-resilient-microservice-on-aws.pdf#page=2?target=_blank)Step 1Systems Manager runbook (invoked by an operator manually) toggles the Amazon Application Recovery Controller routing control "off," which causes the managed health check for the Region to enter a "failed" state.Step 2Route 53 returns only the remaining healthy Region as a client to resolve the application's fully-qualified domain name.Step 3Systems Manager runbook executes Aurora global database managed failover, which promotes the standby Region to the primary for writes.Step 4The former primary Region is rebuilt as a secondary Region by Aurora.Step 5Systems Manager runbook recovers a copy of the old primary database from a snapshot and compares the data in the new primary database to the old, and then creates a missing transaction report.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Go to sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-multi-region-resilient-microservice-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS X-Ray traces application calls from Amazon ECS tasks, visualizing communication flows of microservices and analyzing user requests as they travel through the UI to underlying microservices. CloudWatch Synthetics generates traffic to the application, creating metrics for setting thresholds and alerting if issues arise. Systems Manager runbooks automate failover and failback processes, minimizing human error and ensuring the application meets recovery time objective (RTO) and recovery point objective (RPO) requirements. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) roles and policies secure microservices' interactions with AWS services, enforcing robust security through meticulously defined permissions. AWS Key Management Service (AWS KMS) encrypts data at rest across services, including Aurora and DynamoDB. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Elastic Load Balancing (ELB) routes traffic requests from the application's web interface to healthy Amazon ECS tasks, while Amazon ECS replaces unhealthy tasks and adds more tasks to handle increased load. Amazon Application Recovery Controller reliably enables and disables AWS Regions based on application traffic. DynamoDB global tables and Aurora global databases keep application data consistent within the RPO requirements across multiple AWS Regions. Systems Manager runbooks orchestrate components that need to be changed when shifting traffic from one AWS Region to another. Together, these services help ensure the application experiences minimal service interruptions. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

ELB distributes incoming traffic across multiple targets, preventing any single instance from becoming overwhelmed and maintaining high performance. Aurora read replicas offload read traffic from the primary database instance, distributing the workload and improving overall performance. Aurora global databases extends the benefits of read replicas across multiple Regions, enabling read scaling and improved performance for geographically distributed applications. DynamoDB global tables replicate DynamoDB tables across multiple AWS Regions, enabling low-latency data access for users worldwide. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Auto scaling automatically adjusts the number of Amazon ECS tasks based on demand, so that you only pay for the resources needed. AWS Fargate for Amazon ECS eliminates the need to provision and manage servers, allowing you to run containers without the overhead of managing Amazon Elastic Compute Cloud (Amazon EC2) instances, leading to improved efficiency and reduced costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Auto scaling and DynamoDB On-Demand add capacity when needed and scale down when not required. On-demand services minimize the environmental impact of the workload by efficiently using only the necessary resources to meet the application's demands. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
