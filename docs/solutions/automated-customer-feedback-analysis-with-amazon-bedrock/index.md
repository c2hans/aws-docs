---
source_url: https://docs.aws.amazon.com/solutions/automated-customer-feedback-analysis-with-amazon-bedrock/index.html
---

---
title: 'Guidance for Automated Customer Feedback Analysis with Amazon Bedrock'
canonical_url: https://docs.aws.amazon.com/solutions/automated-customer-feedback-analysis-with-amazon-bedrock/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Automated Customer Feedback Analysis with Amazon Bedrock

## Overview

This Guidance demonstrates how to streamline the process of extracting insights from customer feedback, enabling businesses to make data-driven decisions and enhance the overall customer experience. Manually analyzing large volumes of unstructured data like reviews and comments is time-consuming, prone to inconsistencies, and challenging to scale. Large language models (LLMs) available on Amazon Bedrock can efficiently categorize customer feedback, extract specific aspects, and determine associated sentiments, providing valuable insights into customer satisfaction levels and areas for improvement.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automated-customer-feedback-analysis-with-amazon-bedrock.pdf)

![Architecture diagram](/images/solutions/automated-customer-feedback-analysis-with-amazon-bedrock/images/automated-customer-feedback-analysis-with-amazon-bedrock-1.png)

1. **Step 1**: Upload user feedback (for example, a CSV or JSON file) to Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 2**: The Amazon S3 data event of the uploaded files triggers the AWS Step Functions through Amazon EventBridge.
1. **Step 3**: An AWS Lambda function validates the uploaded file at the beginning of Step Functions workflow.
1. **Step 4**: Step Functions uses a map state to invoke Lambda functions for parallel LLM processing with Amazon Bedrock, saving results to encrypted Amazon Relational Database Service (Amazon RDS) databases using AWS Key Management Service (Amazon KMS).
1. **Step 5**: Amazon Bedrock takes the user-defined instruction prompt as a task, a feedback record as input, and generates expected insight analysis.
1. **Step 6**: A Lambda function performs post-processing on the insight results, for example, summarizing the statistics of input feedback and optionally suggesting new categories.
1. **Step 7**: Step Functions publishes the results to an Amazon Simple Notification Service (Amazon SNS) topic, which sends an email with the results to business users.
1. **Step 8**: Configure Amazon QuickSight to visualize the results in the Amazon RDS database.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-automated-insight-extraction-framework-for-customer-feedback-analysis-with-amazon-bedrock)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses Step Functions for efficient workflow orchestration, automating extract, transform, load (ETL) operations for customer feedback data. It employs modular Lambda functions, enabling easy maintenance. The end-to-end automation significantly reduces manual intervention, such as manually analyzing and categorizing large volumes of unstructured data, to minimize errors and improve consistency in feedback analysis. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The Guidance addresses security concerns when dealing with customer feedback data by implementing robust measures. It uses AWS KMS for encryption, Amazon S3 for secure data storage with fine-grained access controls, and a virtual private cloud (VPC) for network isolation. For LLM-powered insight extraction, it leverages Amazon Bedrock, which provides enterprise-grade security and privacy controls. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3, Lambda, Amazon RDS, QuickSight, and Amazon Bedrock significantly reduce operational overhead and improve system reliability by offloading infrastructure management to AWS. The Step Functions workflow includes comprehensive error handling and reliable state management, ensuring fault tolerance and process integrity. This Guidance also uses LLMs through Amazon Bedrock to consistently extract nuanced insights from unstructured data. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Serverless components like Lambda and Step Functions enable automatic scaling to handle varying workloads. Step Functions has a map state processing mode for large-scale parallel workloads, allowing for efficient processing of extensive datasets. For data analytics and visualization, this Guidance integrates QuickSight, which uses its in-memory computation engine (SPICE) to provide fast query performance on large datasets. The integration of LLMs through Amazon Bedrock significantly boosts natural language processing capabilities, leading to more accurate insight extraction. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The serverless architecture, through services like Lambda and Step Functions, help ensure that costs are directly tied to actual usage, preventing overprovisioning and unnecessary expenses. Storage costs are optimized through the use of Amazon S3 for cost-effective storage of input files and processed data. Efficiently processing and categorizing feedback also contributes to cost savings by reducing the need for manual analysis and enabling more targeted use of human resources. For data visualization, QuickSight allows you to optimize costs based on your usage patterns, as you pay only for the amount of resources used. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Serverless scaling minimizes energy consumption. Amazon S3 and Amazon RDS optimize resource utilization, and the integration of Amazon Bedrock reduces the need for energy-intensive model training. You can further enhance sustainability by monitoring resource usage, implementing data lifecycle policies, and optimizing Lambda functions and Step Functions workflows. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Build an automated insight extraction framework for customer feedback analysis with Amazon Bedrock and Amazon QuickSight**: This blog demonstrates how to integrate LLMs into enterprise applications to harness their generative capabilities.

[Build an automated insight extraction framework for customer feedback analysis with Amazon Bedrock and Amazon QuickSight](https://aws.amazon.com/blogs/machine-learning/build-an-automated-insight-extraction-framework-for-customer-feedback-analysis-with-amazon-bedrock-and-amazon-quicksight/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
