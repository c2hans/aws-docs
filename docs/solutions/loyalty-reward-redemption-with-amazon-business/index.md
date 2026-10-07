---
source_url: https://docs.aws.amazon.com/solutions/loyalty-reward-redemption-with-amazon-business/index.html
---

---
title: 'Guidance for Loyalty Reward Redemption with Amazon Business'
canonical_url: https://docs.aws.amazon.com/solutions/loyalty-reward-redemption-with-amazon-business/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Loyalty Reward Redemption with Amazon Business

## Overview

This Guidance helps you set up a loyalty reward redemption lifecycle for your customers that includes catalogs, orders, custom payment methods, initiative launches, and fulfillment. Loyalty reward redemption improves customer satisfaction and re-share behaviors while increasing revenue. However, building a loyalty program can be complex and costly, as these programs require in-depth expertise of inventory selection, purchasing negotiation, and customer portal management. This Guidance uses AWS services and Amazon Business to enable the redemption and fulfillment of the loyalty program, leveraging the Amazon Prime Delivery experience. Loyalty customers will have access to a customized member portal and SMS notifications about shipment confirmation and delivery, while you will have access to a data lake that consolidates customer order information and preferences.

## How it works

### Loyalty User Experience

This architecture diagram shows how loyalty users can access the portal as defined by the catalog manager to redeem products using points and money. Amazon Business then delivers these products directly to users.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/loyalty-reward-redemption-with-amazon-business.pdf#page=1)Step 1With a web browser or mobile application, the loyalty user browses the products catalog hosted on AWS Amplify, authenticating with Amazon Cognito.Step 2The loyalty user chooses a product and uses points earned through the loyalty program. Amazon Aurora stores points, and Amazon API Gateway and AWS Lambda retrieve points.Step 3Invoke the Loyalty Engine AWS Step Functions workflow if the loyalty user chooses to pay an optional fee to redeem points. Authorize the payment using Amazon Elastic Container Service (Amazon ECS) and third-party payment services such as Amazon Pay.Step 4The loyalty user orders the product using Amazon ECS and Amazon Business direct ordering APIs. The loyalty user then waits for the order and shipment confirmation from Amazon Business through the Amazon ECS Order Status. Generate an invoice for payment calling Invoicing Lambda.Step 5Invoke Amazon Simple Notification Service (Amazon SNS) through Shipment Notification Lambda to notify the loyalty user about shipment status.Step 6Store order information into Amazon Aurora using Order Information Lambda.Step 7Receive the invoice from Amazon Business through Amazon Simple Email Service (Amazon SES), and extract relevant data to store in Enterprise Resource Planning (ERP) software using Amazon Textract.### Catalog Manager and Business Operator Experience

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/loyalty-reward-redemption-with-amazon-business.pdf#page=2)Step 1Access the catalog manager application hosted on Amplify to configure the loyalty experience, authenticating with Amazon Cognito.Step 2Configure the loyalty experience using API Gateway and Lambda. Store all configuration information on Amazon Aurora, including price and points conversion factor, customer brand (such as colors and logo), integration with external payment and integration systems (such as API endpoints and ERP), tiers of users, and marketing campaigns.Step 3Store loyalty orders on Aurora to run analytics workloads.Step 4Perform analytics using data exported to Amazon Simple Storage Service (Amazon S3) through one or more AWS Glue jobs.Step 5Load Amazon Redshift tables from Amazon S3.Step 6Perform personalization of products displayed in the loyalty portal using Amazon Personalize. Forecast loyalty inventory with a custom forecast model on Amazon SageMaker and determine trends in product popularity, intercepting potential out-of-stock issues.Step 7Report loyalty performance in Amazon QuickSight to business users allowing them to know more about their customer base, most loved products, seasonality trends, and more.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch stores all logs and metrics from all the services used in this architecture. CloudWatch can also ingest information from customer code running in Amazon ECS. This Guidance is designed to provide the information necessary to understand its internal state (for example, metrics, logs, events, and traces) across all components for observability. It also captures changes in state, user activity, and access privileges to monitor the health of the workload, identify when outcomes are at risk, and enable effective responses. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) policies control services interactions. Policies and roles are granted the least amount of permissions required for the application to operate. IAM policies and roles limit unauthorized access to services so that a malicious actor, misconfiguration, or bug cannot expose user data or impact application operations. AWS WAF blocks malicious actors from accessing the authentication layer hosted on Amazon Cognito. It protects the web application from a known list of offending IP addresses. AWS Key Management Service (AWS KMS) keys encrypt Aurora and Amazon Redshift data in transit using TLS 1.2 or higher so that malicious actors cannot read confidential information. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS Amplify allows a modern application (integrated into a development pipeline) to work reliably and at scale because it embeds a content delivery network (CDN). This Guidance describes an application that may be accessed simultaneously by thousands of users. In case of load spikes or technical issues on edge nodes or the origin, Amplify redirects traffic, scales its capacity, and caches original content, allowing the application to serve traffic steadily at all hours of the day. While Amplify reliably serves static content, API Gateway serves dynamic content to users, using caching and throttling to not overwhelm the backend. Additionally, Aurora replicates data across different Availability Zones and supports automated failover for minimal service interruption. Aurora also provides automated backups that you can use to restore application functionality in case of human errors or malfunctions. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Aurora delivers significant PostgreSQL performance by tightly integrating the database engine with an SSD-based virtualized storage layer purpose-built for database workloads, reducing writes to the storage system, minimizing lock contention, and eliminating delays created by the database process thread. Aurora features a storage system that delivers high performance, availability, and performance, and this storage can be increased for up to 15 low-latency read replicas. Additionally, Amplify CDN can improve performance for remote users by distributing and caching requests. API Gateway scales automatically to support traffic spikes and can cache requests to accelerate the requests and reduce load on the database. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

There are no minimum fees or upfront commitments for using Amplify, API Gateway, Step Functions, or Amazon ECS. Amazon ECS can run containers without having to provision or manage Amazon Elastic Compute Cloud (Amazon EC2) instances. Amazon ECS supports auto scaling and can also use Amazon EC2 Spot Instances to achieve a significant cost reduction without sacrificing performance. Aurora offers an I/O optimized configuration that can be useful if the database is under a sustained heavy I/O load, as it offers zero charges for read and write I/O operations. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon ECS allows customer to fine tune container requirements, avoiding provisioning for peak times. Amazon ECS and Aurora also support AWS Graviton processors for the underlying clusters. AWS Graviton processors offer the best price performance per watt of energy, and latest generations of AWS Graviton processors use up to 60% less energy for the same performance. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
