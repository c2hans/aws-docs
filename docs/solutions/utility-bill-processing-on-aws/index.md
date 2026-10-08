---
source_url: https://docs.aws.amazon.com/solutions/utility-bill-processing-on-aws/index.html
---

---
title: 'Guidance for Utility Bill Processing on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/utility-bill-processing-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Utility Bill Processing on AWS

Unlock sustainability insights by converting public utility invoices into machine data

## Overview

This Guidance demonstrates how organizations can derive sustainability insights by converting utility invoices into machine-readable data using an automated pipeline and generative AI technology. By automating the extraction of key data points from any utility invoice, organizations can normalize the data and gain insights into their emissions usage. This addresses the challenge businesses face in emissions footprint reporting and insights based on their real estate portfolio, given the lack of programmatic access to invoice data.

## How it works

This architectural diagram illustrates a scalable approach to processing utility invoices into machine-readable data from binary image sources. This framework can be used to automate the extraction process, apply custom data transformations, and generate insights for sustainability reporting purposes.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/utility-bill-processing-on-aws.pdf)

![Architecture diagram](/images/solutions/utility-bill-processing-on-aws/images/utility-bill-processing-on-aws-1.png)

1. **Step 1**: Any ingestion mechanism can be used to move invoice documents into Amazon Simple Storage Service (Amazon S3) for processing, such as Amazon API Gateway, Amazon Simple Email Service (Amazon SES), or the AWS SDKs.
1. **Step 2**: Invoice documents arrive in an Amazon S3 bucket, trigger event notifications in Amazon EventBridge, and start a processing workflow in AWS Step Functions.
1. **Step 3**: AWS Lambda converts the PDF document into images and saves them to Amazon S3.
1. **Step 4**: The images are combined with a text-based prompt. The full prompt is saved to Amazon S3.
1. **Step 5**: Amazon Bedrock is called directly from Step Functions using an optimized integration. The prompt instructs the foundation model to interpret the image and generate a standard structured JSON output.
1. **Step 6**: Standardized utility invoice data is stored in an output Amazon S3 bucket to integrate with downstream analytics capabilities such as Amazon QuickSight or with Data Lakes on AWS.
1. **Step 7**: An event is published through EventBridge. This event can be used to notify end users or other systems that processing has completed.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-utility-bill-processing-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses standard service metrics to monitor the health of individual pipeline components, such as Lambda function concurrency or error rate. In addition, Amazon CloudWatch metrics, alarms, and dashboards can be customized to monitor the operational health of this Guidance and notify operators of any faults. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The resources deployed through this Guidance are safeguarded through the policies and principles of AWS Identity and Access Management (IAM). Least-privilege access and role-based access controls should be used to grant operators the necessary permissions to modify resources, such as deploying an updated stack through AWS CloudFormation. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses infrastructure-as-code in an AWS Cloud Development Kit (CDK). These CDK stacks are deployed through CloudFormation for resilient change management that will automatically rollback if a fault is detected during deployment. In addition, by using loosely coupled dependencies like EventBridge rules, this Guidance can handle ingestion events from Amazon S3 and implement retries on downstream quota limits. These services enhance reliability through a decoupled, scalable, and serverless architecture, allowing for automatic scaling, reliable event processing, reduced operational overhead, and consistent, repeatable deployments through infrastructure-as-code. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance is designed to scale in order to meet the processing requirements for utility invoices. It employs a queueing mechanism to regulate the rate at which invoices are processed. For customers with large, consistent inference workloads, they can request an increase to the Lambda concurrency limit and use the provisioned throughput model of Amazon Bedrock so that the application's performance needs are adequately addressed. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The selection of serverless technologies that can be configured with this Guidance reduces costs that are directly correlated to the number of invoices processed. For the storage of binary invoice documents, this Guidance uses the Amazon Simple Storage Service Intelligent-Tiering storage class or Amazon S3 Lifecycle configuration policies. These policies can lower the long-term storage costs or eliminate the long-term storage of documents entirely. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses Amazon S3 to store invoices, which represent the largest data type within the application. AWS customers have the ability to make minor adjustments to achieve their ideal data storage configuration by using Amazon S3 Intelligent Tiering or Amazon S3 Lifecycle policies, as outlined in the Cost Optimization section. Amazon S3 enables the optimization of data storage through energy-efficient tiers while also reducing the carbon footprint through the shared infrastructure and renewable energy usage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
