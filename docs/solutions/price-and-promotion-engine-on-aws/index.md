---
source_url: https://docs.aws.amazon.com/solutions/price-and-promotion-engine-on-aws/index.html
---

---
title: 'Guidance for Price and Promotion Engine on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/price-and-promotion-engine-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Price and Promotion Engine on AWS

## Overview

This Guidance helps you simplify the complexity of promotions, including stacked promotions, coupons, free shipping, loyalty discounts, buy-one-get-one, flash sales, and many others. In their search for the best deal, consumers compare promotions across many stores. However, marketers are often limited to the few promotion types supported by their website or point of sale, preventing them from maximizing marketing investments. This Guidance takes transaction context (such as a customer’s loyalty tier, time of day, and a list of possible promotions) and determines how to best apply promotions to a cart of products. With this Guidance, marketing teams can provide consumers with more targeted promotions for maximized discounts to increase sales and brand loyalty.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/price-and-promotion-engine-on-aws.pdf)

![Architecture diagram](/images/solutions/price-and-promotion-engine-on-aws/images/price-and-promotion-engine-on-aws-1.png)

1. **Step 1**: The pricing engine relies on primary data from systems such as SAP, Product Information Management System (PIMS), or Master Data Management (MDM). Amazon AppFlow is used for turn-key integrations with systems such as SAP and systems that are limited to file-based integrations. AWS Transfer Family manages secure file transfers, such as secure file transfer protocol (SFTP) jobs.
1. **Step 2**: Primary data from Amazon Simple Storage Service (Amazon S3) is batch-ingested into a relational database management system (RDBMS) and hosted in Amazon Aurora using AWS Lambda.
1. **Step 3**: The Marketing team uses Web App to create promotions and deals that are stored in Aurora. Web App is a scalable, secure, and serverless front-end application, created with AWS Amplify for easy code development, Amazon Cognito for identity management, and Amazon CloudFront for content distribution.
1. **Step 4**: AWS Batch and AWS Fargate serverless runtime processes complex promotions, deals, and dynamic pricing data at a given scheduled time, such as the end of the day. These services store eligible records in Amazon DynamoDB.
1. **Step 5**: A customer facing commerce system, such as e-Commerce or point of sale, requests the Price Engine API through an Amazon API Gateway private endpoint on every "Add to cart" event to re-calculate the price based on configured promotions and deals.
1. **Step 6**: Lambda calculates the price of respective products from the cart, based on rule records defined in DynamoDB. Amazon DynamoDB Accelerator (DAX) in-memory cache reduces read latency from DynamoDB, which also helps reduce overall API response time to less than a second.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS managed services emit their own set of metrics into Amazon CloudWatch, where you can monitor services for errors and set up CloudWatch alarm notifications. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

For public facing services (such as the Web App UI), Amazon Cognito secures access to the core applications and services. This includes role-based access controls. Provisioned API endpoints are also secured with private Amazon Virtual Private Cloud (Amazon VPC) endpoints for secure communication from a customer’s on-premises systems or within the AWS Cloud. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS managed services are designed to span multiple Availability Zones. Other services, such as Aurora and Amazon DAX, can also be deployed over multiple Availability Zones. In case of failure in one Availability Zone, you can deploy services to another Availability Zone to continue operations. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This architecture follows a serverless-first approach and uses managed services. Serverless services and managed services are scalable and highly available. For example, recalculating the price on each 'Add to cart' event is critical to the performance of the Price Engine API. Lambda handles this task, which allows you to run code without provisioning or managing servers or containers. You simply upload your code, and Lambda manages running and scaling your code. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This architecture ingests data from source systems, and data moving in the inbound direction is generally uncharged. Data transfer for AWS Transfer for SFTP file transfers, API Gateway requests, and Amazon AppFlow data is charged as per publicly documented service pricing. To minimize transfer charges, all other data is kept within the AWS Region for processing. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS managed services scale up and down according to business requirements and traffic, making them more sustainable than on-premises architectures that do not offer on-demand scalability. Additionally, serverless components of this architecture automate the process of infrastructure management. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
