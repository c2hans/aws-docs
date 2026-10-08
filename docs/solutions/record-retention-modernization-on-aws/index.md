---
source_url: https://docs.aws.amazon.com/solutions/record-retention-modernization-on-aws/index.html
---

---
title: 'Guidance for Record Retention Modernization on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/record-retention-modernization-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Record Retention Modernization on AWS

## Overview

This Guidance helps you modernize your record retention to extract value from your data, while staying compliant with record-keeping rules from the U.S. Securities and Exchange Commission (SEC), Commodity Futures Trading Commission (CFTC), and the Financial Industry Regulatory Authority (FINRA). Financial service institutions (FSIs) are expected to have compliant record retention. FSIs often satisfy record retention requirements by using on-premises legacy storage solutions which do not scale, require constant hardware and software refreshes, and do not allow end-customers to easily access the data. With this Guidance, you can use cloud-native services for storing, processing, and monitoring access to data, so analysts, data scientists, and other stakeholders can work with the data while staying in compliance with regulators.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/record-retention-modernization-on-aws.pdf)

![Architecture diagram](/images/solutions/record-retention-modernization-on-aws/images/record-retention-modernization-on-aws-1.png)

1. **Step 1**: Transaction data is created in the line of business applications.
1. **Step 2**: AWS DataSync, AWS Transfer Family, or AWS Snowball transfer data to an AWS Region.
1. **Step 3**: Amazon Simple Storage Service (Amazon S3) stores data in its raw form.
1. **Step 4**: AWS Glue crawlers discover and catalog the raw data.
1. **Step 5**: Customers can process the raw data using AWS Glue Studio jobs or Amazon EMR.
1. **Step 6**: Amazon DynamoDB stores job details, results, and other metadata for auditing purposes.
1. **Step 7**: AWS Glue Data Catalog stores processed data schema and partition information.
1. **Step 8**: S3 buckets store processed data for retention, configured with S3 Object Lock in Compliance Mode, with a default retention period that matches compliance requirements.
1. **Step 9**: AWS Lake Formation provides access control and governance, which enables granular access control on a database-, table-, or column-level.
1. **Step 10**: End users, such as the record management team, data science teams, auditors, and designated third-parties (D3P), access the data through services such as Amazon Athena, Amazon Redshift Spectrum, and Amazon SageMaker.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses fully managed services, such as Amazon S3, DataSync, Transfer Family, AWS Glue, Lake Formation, and Athena. These services eliminate the need to administer data processing, data storage, and data warehousing systems, so you can focus on building your applications. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

End users use AWS Identity and Access Management (IAM) single-sign on, which authorizes access to QuickSight dashboards and the Athena user interface in addition to the Amazon Redshift Query user interface (UI) for ad-hoc queries and SageMaker for machine learning (ML) projects. DataSync uses HTTPS for encryption in-transit. Transfer Family uses secure file transfer protocol (SFTP) and file transfer protocol (FTPS), which are secured by the underlying protocols based on secure shell (SSH) and transport layer security (TLS) cryptographic algorithms. Snowball supports server-side encryption at rest. Amazon S3 supports server-side and client-side encryption. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Serverless capabilities such as Athena, AWS Glue, Lake Formation, DynamoDB, Amazon Redshift Serverless, and Amazon EMR Serverless scale with demand. Transfer Family supports up to three Availability Zones to minimize network latency. Amazon EMR supports multi-master deployments in the same Availability Zone, while Amazon Redshift uses a relocation capability that allows you to move a cluster to another Availability Zone with minimal changes to your application. DataSync recovers from network path failures and uses integrity checks and full checksums to ensure correct transfer of data. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

With serverless services, you can use automatic scaling and recover resources, while using the minimum amount of services required for a task. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

In this Guidance, we use serverless services that scale automatically with demand so that you pay only for the amount of resources you use. For example, AWS Glue and Amazon EMR Serverless only consume resources when jobs are running. Users pay only for the Athena queries they run, and Amazon Redshift Serverless scales with demand. Additionally, DataSync efficiently transfers data to AWS to minimize costs. Amazon EMR can make use of transient clusters and Amazon Elastic Cloud Compute (Amazon EC2) Spot instances, which provide up to a 90% discount compared to on-demand prices. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By extensively using serverless services and dynamic scaling, resources are only consumed when needed. You do not need to maintain peak capacity to avoid costly application failures when scaling resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **How financial institutions modernize record retention on AWS**: This post explores how financial institutions can use a range of AWS services to build a secure, scalable, and cost-effective record retention solution to assist them in pursuing their regulatory objectives.

[Learn more](https://aws.amazon.com/blogs/industries/how-financial-services-institutions-modernize-record-retention-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
