---
source_url: https://docs.aws.amazon.com/solutions/predictive-segmentation-using-third-party-data-with-aws-clean-rooms/index.html
---

---
title: 'Guidance for Predictive Segmentation using Third-Party Data with AWS Clean Rooms'
canonical_url: https://docs.aws.amazon.com/solutions/predictive-segmentation-using-third-party-data-with-aws-clean-rooms/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Predictive Segmentation using Third-Party Data with AWS Clean Rooms

## Overview

This Guidance demonstrates how AWS services can help you automate the collection of customer first-party and third-party data, enabling collaboration without sharing raw data, and generate predictive segments using machine learning. Use these predictive segments to send tailored messages through various channels including mobile push, in-app, email, SMS, or custom channels to elevate the engagement between you and your customers.

## How it works

This diagram shows how first-party data is combined with third-party data to generate predictive segments in AWS Clean Rooms.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/predictive-segmentation-using-third-party-data-with-aws-clean-rooms.pdf?target=_blank)

![Architecture diagram](/images/solutions/predictive-segmentation-using-third-party-data-with-aws-clean-rooms/images/predictive-segmentation-using-third-party-data-with-aws-clean-rooms-1.png)

1. **Step 1**: Amazon Pinpoint captures the customer interaction first-party data needed for predictive segmentation. This data loads into Amazon Simple Storage Service (Amazon S3) using Amazon Kinesis Data Firehose.
1. **Step 2**: Use AWS Glue Data Catalog to catalog the first-party data stored in Amazon S3 and make it available to AWS Clean Rooms as a table.
1. **Step 3**: Clean and normalize the third-party partner data and store that data in an Amazon S3 bucket within the partner's AWS account. Use Glue Data Catalog to catalog the files and make it available to AWS Clean Rooms as a table.
1. **Step 4**: Set up an AWS Clean Rooms Collaboration with the third-party account as the data provider and the first-party account as the query runner.
1. **Step 5**: Run the data collaboration query in AWS Clean Rooms, and store the query results within the first-party data account.
1. **Step 6**: Optionally, upload the dataset to Amazon Neptune, a fully managed graph database, to visualize the data relationships (such as cross-device user data or household data).
1. **Step 7**: Optionally, use Amazon QuickSight to build dashboards, visualize your analysis, and to generate insights.
1. **Step 8**: Use Amazon SageMaker to build, train, and deploy machine learning (ML) models that generate predictive segments from the first-party and third-party data.
1. **Step 9**: Import the generated predictive segments in Amazon Pinpoint to utilize the generated segments in Amazon Pinpoint campaigns.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

With Amazon CloudWatch, you can collect and track all operational metrics, log files, and set alarms for failure. This service allows you to maintain visibility into the details of operations, such as queries run on AWS Clean Rooms. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All of the interactions between the services in this Guidance use AWS Identity and Access Management (IAM) roles with IAM policies set to provide the least privilege necessary for the services. In addition, AWS Clean Rooms enables the use of advanced cryptographic computing tools to keep data encrypted, even during query processing, to comply with the stringent data-handling policies of AWS. By using Amazon S3 for storage, you can encrypt all the data at rest by default. Amazon S3 provides the choice of having AWS or the customer manage the encryption keys. This helps you to adapt to your different security criteria. By using Amazon S3 bucket policies, you can define fine-grained access control. And by enabling server-side encryption on Kinesis Data Firehose, you can encrypt all sensitive data while transferring to services downstream. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Because this Guidance uses managed services, all of the stored data through the various services are highly available and not dependent on the rare, but possible, failure of an Availability Zone. Managed services help you avoid failures due to increased data volumes because of the underlying scalability of each service, such as Amazon S3 and Kinesis Data Firehose. Amazon S3 is a reliable and durable way to store your data, and Kinesis Data Firehose ensures easy, reliable data delivery to the destination for analysis in the downstream process. And we recommend using AWS Backup to back up all data stored in Amazon S3 buckets. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses a serverless architecture that allows for automatic scaling of the required resources through managed services. By using Amazon Pinpoint, you can manage large volumes of customers and their interactions. And with AWS Clean Rooms, you can quickly create numerous multi-party collaborations without the need to deploy any underlying infrastructure. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

When you use managed services through a serverless architecture, you can scale your applications to accommodate demand, paying for only what you use. Amazon S3 Intelligent-Tiering automates storage cost savings by moving data when access patterns change, allowing you to optimize your performance while containing costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Through the extensive use of managed services coupled with a serverless architecture, this Guidance helps you continually scale to match your workload volume while ensuring that only the minimum resources are used. We also recommend managing your objects so that they are stored effectively throughout their lifecycle by configuring Amazon S3 Lifecycle. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
