---
source_url: https://docs.aws.amazon.com/solutions/identifying-diagnosis-codes-from-clinical-notes-on-aws/index.html
---

---
title: 'Guidance for Identifying Diagnosis Codes from Clinical Notes on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/identifying-diagnosis-codes-from-clinical-notes-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Identifying Diagnosis Codes from Clinical Notes on AWS

## Overview

This Guidance shows how to use generative artificial intelligence (generative AI) to summarize patient histories and identify likely medical conditions and diagnosis codes. Patient-provider interactions capture multiple types of documentary details, such as patient profile, clinical notes, and laboratory work. By juxtaposing this data with historical diagnosis knowledge bases and analyzing it with generative AI foundation models, you can generate summaries of likely medical conditions. You can then recommend these summaries and relevant International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) codes to providers, helping then improve patient care.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/identifying-diagnosis-codes-from-clinical-notes-on-aws.pdf)

![Architecture diagram](/images/solutions/identifying-diagnosis-codes-from-clinical-notes-on-aws/images/identifying-diagnosis-codes-from-clinical-notes-on-aws-1.png)

1. **Step 1**: Source data can come in many different forms, such as the Fast Healthcare Interoperability Resources (FHIR) format. If it is already in FHIR format—for example, if it is coming from an electronic health record (EHR)—it can be directly sent to AWS HealthLake through synchronous FHIR APIs or through asynchronous bulk imports.
1. **Step 2**: Patient-provider interactions can be summarized using AWS HealthScribe and stored in Amazon Simple Storage Service (Amazon S3).
1. **Step 3**: Results can also be enriched using Amazon Comprehend Medical, which supports ICD-10-CM diagnosis codes.
1. **Step 4**: An AWS Lambda function acts in response to Amazon S3 events to invoke Amazon Bedrock.
1. **Step 5**: Using prompt engineering with an Amazon Bedrock Converse API, you can identify your patient's medical conditions and store the results in an Amazon S3 bucket.
1. **Step 6**: Use an Amazon OpenSearch Service vector database to store your organization's specific guidelines on how to detect nuances of medical conditions.
1. **Step 7**: You can use AWS Lake Formation to govern permissions.
1. **Step 8**: You can use Amazon Athena to analyze the data stored in AWS Glue Data Catalog tables.
1. **Step 9**: You can present insightful dashboards and visualizations to end users using Amazon QuickSight.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-identifying-diagnosis-codes-from-clinical-notes-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch collects and tracks metrics for AWS resources like Lambda, Amazon Bedrock, and Amazon Comprehend Medical in real time. Using CloudWatch logs, you can monitor your systems and applications, identify concerns early, and proactively troubleshoot and remediate issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) provides fine-grained access control to AWS services and resources under conditions you specify, supporting the principle of least privilege. Lake Formation helps you centrally govern and secure data and globally share it for analytics and machine learning. It also delivers fine-grained data access control, down to the row and column level, so you can provide users with specific data access. Additionally, AWS CloudTrail lets you record API calls made within your AWS account and provides an audit trail that you can use for compliance. Finally, Amazon Comprehend Medical detects protected health information in clinical text, supporting privacy protection. This Guidance uses managed services with high built-in reliability, such as Athena, HealthLake, Amazon Bedrock, Amazon Comprehend Medical, and AWS HealthScribe. As another example, Amazon S3 is designed to provide 99.999999999 percent durability and 99.99 percent availability of objects. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Performance Efficiency

This Guidance provides high performance, helping you deliver impactful patient care. For example, serverless services like HealthLake, Amazon Comprehend Medical, and AWS HealthScribe provide managed scaling that doesn’t rely on any custom engineering in your code. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance optimizes costs by using serverless services like Athena and Amazon Bedrock. Serverless services charge only for the resources used, so you don’t have to pay for idle server capacity. And because they automatically scale to handle varying loads, they reduce costs during low-traffic periods and support efficient resource use during peak times. These services also offer various cost optimization mechanisms. For example, Amazon S3 Lifecycle policies and Amazon S3 Intelligent-Tiering provide lower-cost storage options. Finally, serverless services shift operational responsibilities to AWS, lowering your total cost of ownership by empowering developers to focus on code rather than infrastructure maintenance. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance’s use of cloud-native serverless services—like Lambda, Athena, and Amazon Bedrock—can reduce a workload’s carbon footprint by 88 percent. This empowers you to pursue your environmental, social, and governance goals. Additionally, Amazon S3 enables data archival, and Lake Formation enables data classification so that you can define how long health records are retained. As a result, you can more easily achieve regulatory compliance while optimizing energy expenditures related to storage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
