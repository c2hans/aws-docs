---
source_url: https://docs.aws.amazon.com/solutions/data-anonymization-on-aws/index.html
---

---
title: 'Guidance for Data Anonymization on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/data-anonymization-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Data Anonymization on AWS

## Overview

This Guidance provides a data anonymization capability that enables you to discover and protect sensitive data as it is stored and processed. For example, you can use this capability to anonymize national ID numbers, trade data, and healthcare information.

## How it works

This architecture diagram shows how to integrate AWS services to anonymize data, protecting sensitive information while facilitating secure and compliant data usage in a reliable, secure, and scalable cloud environment.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/data-anonymization-on-aws.pdf)

![Architecture diagram](/images/solutions/data-anonymization-on-aws/images/data-anonymization-on-aws-1.png)

1. **Step 1**: Within AWS Organizations, enable Amazon GuardDuty, AWS Security Hub, Amazon Macie, and AWS Key Management Service (AWS KMS) for your home and operational AWS Regions.
1. **Step 2**: Configure GuardDuty and Security Hub in your home and operational Regions to provide comprehensive threat monitoring, centralize security incident management, and help achieve compliance with AWS security best practices and industry standards.
1. **Step 3**: Set up Macie in your home and operational Regions to identify sensitive data in your specific accounts or in Amazon Simple Storage Service (Amazon S3) buckets.
1. **Step 4**: Use AWS KMS to create and control cryptographic keys, facilitating secure data encryption across your AWS services.
1. **Step 5**: Use AWS Identity and Access Management (IAM) Identity Center to securely manage access to AWS resources by making sure that only authorized personnel and services can perform anonymization tasks and access anonymized data.
1. **Step 6**: Send relevant logs to a centralized log storage bucket for compliance retention and analysis.
1. **Step 7**: Use AWS Glue to orchestrate extract, transform, and load (ETL) workflows that prepare and transform data for anonymization, using its built-in personally identifiable information detection feature to automatically identify and redact sensitive information.
1. **Step 8**: Optionally, if you have your own scripts, use AWS Lambda to implement them and AWS Step Functions to orchestrate the workflows to seamlessly implement tasks and coordinate processes.
1. **Step 9**: Use Amazon S3 as a data lake for storing both raw and anonymized data.
1. **Step 10**: Use Amazon Redshift to store and manage structured, anonymized data in a data warehouse, enabling efficient querying and analysis while integrating with your data lake.
[Read usage guidelines](/solutions/guidance-disclaimers/)
