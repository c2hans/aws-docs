---
source_url: https://docs.aws.amazon.com/solutions/designing-resilient-applications-with-amazon-aurora-and-amazon-rds-proxy/index.html
---

---
title: 'Guidance for Designing Resilient Applications with Amazon Aurora and Amazon RDS Proxy'
canonical_url: https://docs.aws.amazon.com/solutions/designing-resilient-applications-with-amazon-aurora-and-amazon-rds-proxy/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Designing Resilient Applications with Amazon Aurora and Amazon RDS Proxy

## Overview

This Guidance helps you achieve near-zero recovery point objective (RPO) for your applications, minimizing data loss during potential Amazon Aurora failovers. You can improve data durability by using a persistent message queue that temporarily stores application data until it can safely be committed to the database. With this Guidance, you can design highly resilient databases for applications, helping to ensure minimal data loss and maintain data integrity.

## How it works

This architecture diagram shows how to achieve near-zero RPO using Amazon Aurora and Relational Database Service (Amazon RDS) Proxy.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/designing-resilient-applications-with-amazon-aurora-and-amazon-rds-proxy.pdf?target=_blank)

![Architecture diagram](/images/solutions/designing-resilient-applications-with-amazon-aurora-and-amazon-rds-proxy/images/designing-resilient-applications-with-amazon-aurora-and-amazon-rds-proxy-1.png)

1. **Step 1**: A user generates a request to write to the Amazon Aurora database. This request is evaluated by the AWS WAF configured with standard rules to protect against common web exploits.
1. **Step 2**: If the request complies with the enacted AWS WAF policies, the request is routed to an Amazon API Gateway.
1. **Step 3**: API Gateway forwards HTTPS requests to an Amazon Simple Queue Service (Amazon SQS) queue.
1. **Step 4**: In the background, an event source mapping in AWS Lambda continuously polls the Amazon SQS queue for new messages. Amazon SQS is set to attempt message processing 25 times. If a message fails all attempts, it's sent to an Amazon SQS dead-letter queue (DLQ).
1. **Step 5**: Upon receiving a new message, Lambda retrieves the database credentials stored in AWS Secrets Manager to connect to the Aurora database.
1. **Step 6**: The message retrieved from Amazon SQS is written by Lambda to the primary Aurora instance in Availability Zone 1. This instance serves as the writer instance, with a reader instance deployed to Availability Zone 2.
1. **Step 7**: In the event of a primary instance failure, Aurora automatically promotes a secondary instance to become the new primary, a process known as failover. Throughout this failover process, Lambda continues writing data to the Aurora cluster.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-designing-resilient-applications-with-amazon-aurora-and-amazon-rds-proxy)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance helps ensure business continuity through failover to a secondary Availability Zone, achieving near-zero RPO. Amazon CloudWatch captures comprehensive metrics from all the services employed in the Guidance. Customizable CloudWatch dashboards provide a unified view for monitoring resources, enabling proactive identification and resolution of potential issues. The Guidance is designed to automatically respond to Availability Zone failures, eliminating the need for manual interventions. CloudWatch offers insights into critical metrics pertaining to services and application dependencies, facilitating informed decision-making and enhancing operational resilience. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS WAF and Amazon CloudFront safeguard the application against vulnerabilities, such as controlling malicious bot traffic and blocking common attack patterns, including SQL injection or cross-site scripting (XSS). AWS WAF monitors HTTP(S) requests to your protected web application resources, enabling granular control over access to your content. Amazon Cognito authenticates user interface (UI) and API calls to the application, simplifying the implementation of customer identity and access management (CIAM) and establishing a strong identity foundation. Additionally, Secrets Manager securely stores database credentials. This service streamlines the management, retrieval, and rotation of database credentials, API keys, and other sensitive information throughout their lifecycles, enabling tight access control and auditing of secrets. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance incorporates Amazon SQS, a message queuing service, to help ensure data integrity and prevent packet loss during failover events when the Amazon Relational Database Service (Amazon RDS) Proxy re-establishes a connection to the standby Aurora database instance. Amazon SQS enables reliable and scalable message delivery, allowing software components to send, store, and receive messages at any volume—without the risk of message loss or dependencies on the availability of other services. This resilient messaging infrastructure allows for seamless communication and data consistency, even in the face of transient failures or component restarts. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

In this Guidance, Aurora seamlessly scales the database capacity to accommodate growing data volumes within the cluster volume for optimal performance and effective resource utilization. As a managed service, Aurora dynamically scales resources based on demand, providing the necessary elasticity to handle fluctuating workloads. Specifically, Aurora storage capacity automatically increases to accommodate growing data within the cluster volume, eliminating the need for manual intervention or capacity planning. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

API Gateway and Lambda are serverless managed services that eliminate the need for provisioned compute resources. These cloud-native services adopt a pay-per-use billing model, avoiding redundant costs associated with maintaining infrastructure when the application is not in active use. Through API Gateway and Lambda, resources are dynamically allocated and charged based on actual usage, optimizing operational expenses and enabling efficient resource utilization. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

To help ensure efficient resource utilization and minimize environmental impact, this Guidance uses the Amazon SQS DLQ. If a request fails to be processed after 25 attempts, it is automatically redirected to the DLQ, avoiding infinite processing loops. Analyzing the DLQ requests enables the identification and rectification of potential issues in the data source, preventing the recurrence of the same errors and wasted processing power in the future. The DLQ limits the number of re-processing attempts per packet so that Lambda resources are not indefinitely spun up to process requests that are unlikely to succeed. This minimizes the environmental impact of the Guidance by reducing unnecessary compute operations. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
