---
source_url: https://docs.aws.amazon.com/solutions/supply-chain-control-tower-visibility-on-aws/index.html
---

---
title: 'Guidance for Supply Chain Control Tower Visibility on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/supply-chain-control-tower-visibility-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Supply Chain Control Tower Visibility on AWS

## Overview

This Guidance demonstrates how AWS Supply Chain Control Tower can improve visibility into business-critical systems. Analyze a constant stream of data in near real-time to determine actionable insights and predictive recommendations for your supply chain.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/supply-chain-control-tower-visibility-on-aws.pdf)

![Architecture diagram](/images/solutions/supply-chain-control-tower-visibility-on-aws/images/supply-chain-control-tower-visibility-on-aws-1.png)

1. **Step 1**: Supply Chain Control Towers (SCCT) rely on data inputs from external systems such as logistic partners. File-based integrations are often used. Modern approaches include posting/pushing data to a secure API that is built using Amazon API Gateway and AWS Lambda
1. **Step 2**: A Consumer Packaged Goods (CPG) organization relies on critical systems that manage everything from raw materials to production capacity. A range of integration methods can be used to integrate with these systems: Amazon EventBridge to deliver events as they occur, Amazon AppFlow for turn-key integrations with systems such as SAP, and for systems that are limited to file based integrations. AWS Transfer Family can be used to manage secure file transfers such as SFTP jobs.
1. **Step 3**: Various equipment across your supply chain also has data critical to SCCT. Connected devices can transmit messages through AWS IoT Core using the MQTT protocol.
1. **Step 4**: Services such as AWS DataBrew and AWS Glue can be used to transform and normalize data before pushing to the data platform. Amazon Textract can be used to extract important data from images/paper documents (such as dock slips) for ingestion into the data-platform.
1. **Step 5**: At the heart of the SCCT is your data-platform that will be your single source of truth for your data. There are many patterns that are suitable.
1. **Step 6**: Amazon SageMaker can be used to build, train, and deploy machine learning models that are focused on specific use cases such as ETA prediction.
1. **Step 7**: Amazon QuickSight can be used with Amazon OpenSearch Service for live analytics, Amazon Athena for impromptu queries for data in your data lake, and Amazon Redshift for complex queries and views.
1. **Step 8**: QuickSight can be used to visualize the data analyzed in your data platform to create actionable insights for specific SCCT use cases (listed).
1. **Step 9**: Your SCCT can be extended with microservices for specific use cases. Example: Query transport location data from Amazon DynamoDB through Amazon Lambda for visualization with Amazon Location Services
1. **Step 10**: A scalable, secure and serverless front-end is created leveraging AWS Amplify for easy code development, Amazon Cognito for identity management, Amazon CloudFront for content distribution, Amazon Simple Storage Service (Amazon S3) for storage of static assets, and Amazon Route 53 DNS.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

By solely leveraging AWS managed services, each service emits its own set of metrics into Amazon CloudWatch, where customers can monitor for errors. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

For public facing services (such as the UI), Amazon Cognito is used to ensure secure access to the core applications and services - this includes role-based access controls. Provisioned API endpoints are also secured with appropriate access, authentication, and authorization controls to ensure use by allowed systems and users. For other AWS services, AWS Identity and Access Management (IAM) role-based access controls are leveraged to ensure least privileged access between services. The AWS managed services used in this architecture support secure communication by encrypting data in transit. Where data is stored (such as Amazon Redshift and Amazon S3), data is also encrypted at rest. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This architecture leverages managed services that are designed to be highly available by default. Some services (such as Amazon Redshift) can also be configured to be deployed over multiple availability zones. Each component in this architecture is designed to maintain availability in the event of disaster events. AWS managed services are designed to span multiple availability zones. Other services, like Amazon Redshift, can also be deployed over multiple availability zones. In the case of availability zone failure, services deployed can continue to operate. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Scalable and highly available services like Amazon S3, Amazon Kinesis, AWS Glue and Amazon Redshift are purposefully built for data analytics workloads. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This architecture follows a serverless-first approach. Where possible, serverless services scale according to load to ensure you only pay for what is used. In addition, AWS managed services are used that allow for utility billing. Data transfer is a consideration for any data-orientated architecture. In this solution, the biggest data volume is ingested from source systems which is generally uncharged in the inbound direction. Data transfer for AWS SFTP file transfers, API Gateway requests, and Amazon AppFlow data are charged as per the documented service pricing. All other data is kept within the region for processing to minimize transfer charges. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS managed services help to scale up and down according to business requirement and traffic, and are inherently more sustainable than on-premises solutions. Additionally, leveraged serverless components automate the process of infrastructure management and make it more sustainable. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
