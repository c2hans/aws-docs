---
source_url: https://docs.aws.amazon.com/solutions/product-traceability-on-aws/index.html
---

# Guidance for Product Traceability on AWS

## Overview

This Guidance helps to provide transparency and traceability of the supply chain network for a product. The architecture allows vendors and stakeholders to easily upload the supply chain certificates as well as ingest relevant data from systems such as enterprise resource planning (ERP), product lifecycle management (PLM), SharePoint. It then extracts, processes, cross-checks, and validates these documents in an automated, serverless AWS workflow. This Guidance includes both an overview architecture and a detailed architecture with sample code.

## How it works

### Overview

This overview architecture shows a process flow for adding traceability and transparency to a product supply chain.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/product-traceability-on-aws.pdf)Step 1External data sources are ingested for extraction validation.Step 2Suppliers upload certificates through a secure web application.Step 3The certificate upload triggers an extraction Step Function, and certificates are eventually archived.Step 4Data is extracted from the certificate.Step 5Extracted addresses are mapped to GPS coordinates.Step 6Extracted data is matched with and crosschecked against third-party data.Step 7Relevant parties consume data.### Detailed Architecture

This detailed architecture shows a process flow for adding traceability and transparency to a product supply chain.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/product-traceability-on-aws.pdf)Step 1AWS Glue ingests, cleans, and processes third-party data, such as shipping and invoice information.Step 2Users upload supply chain certificates through a serverless portal powered by Amazon Route 53, Amazon Cognito, Amazon CloudFront, and Amazon Simple Storage Service (Amazon S3).Step 3Lifecycle rules automatically move certificates from Amazon S3 to Amazon S3 Glacier.Step 4Amazon EventBridge initiates a data extraction process, orchestrated by AWS Step Functions. Amazon Textract facilitates the extraction of key information, such as expiration date and certificate number, using plain language queries and built-in optical character recognition (OCR) functionalities.Step 5Amazon Location Service maps extracted supplier addresses to GPS coordinates, allowing for location visualization.Step 6Data extracted from the supply chain certificates is optionally matched with and crosschecked against third-party data. This data can be used as a form of extraction validation or certificate validity checking.Step 7You can access final data through Amazon Athena or Amazon Redshift and visualize it in Amazon QuickSight or in a third-party app of choice.Step 8Amazon CloudWatch and AWS CloudTrail monitor all services. AWS Key Management Service (AWS KMS) stores and manages encryption keys.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-product-traceability-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance is deployed using AWS Cloud Development Kit (AWS CDK). Changes to the main branch of your repository of choice are propagated to the Guidance infrastructure through AWS CodePipeline. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses AWS WAF, Amazon Cognito, and AWS Certificate Manager (ACM) to secure access to its hosted upload portal, restricting access to services and protecting them from attacks. All data is encrypted at rest using AWS KMS keys. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The load balancer will ensure the health of the hosted upload portal alongside built-in autoscaling for services. It is critical that the extraction be done within a Step Function that includes a retry mechanism. Otherwise, you may encounter a bottleneck in Amazon Textract due to account-level concurrency limits that can only be increased by contacting AWS support. It is possible for the extraction Lambda function to fail if too many certificates are uploaded at once. As such, the Step Function should include a fail-retry check to address failures that occur as result of Textract throttling. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

We selected the services in this Guidance to create a serverless architecture. The Guidance uses automation to minimize infrastructure management and user intervention. The architecture is also decoupled so that different functions can run independently from one another. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

All data is stored in Amazon S3, with lifecycle policies that automatically archive old certificates. This allows for cost optimization while still adhering to data retention regulations. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

All components of this Guidance are serverless and scale automatically. This approach ensures minimal energy consumption while maintaining high availability. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
