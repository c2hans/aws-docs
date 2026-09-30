---
source_url: https://docs.aws.amazon.com/solutions/connecting-cdps-to-data-lakes-with-aws-clean-rooms/index.html
---

---
title: 'Guidance for Connecting CDPs to Data Lakes with AWS Clean Rooms'
canonical_url: https://docs.aws.amazon.com/solutions/connecting-cdps-to-data-lakes-with-aws-clean-rooms/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Connecting CDPs to Data Lakes with AWS Clean Rooms

## Overview

This Guidance shows you how to use customer data platforms (CDPs) to set up a collaboration between first-party marketing data and third-party data from a publishing partner. By using an AWS Clean Rooms collaboration, CDPs can facilitate the connection between separate data lakes on AWS. Marketers can upload their data to the CDP application, then use the application to run reports from the compiled data, helping them activate their audiences.

## How it works

This architecture diagram shows how marketers using customer data platforms (CDPs) can set up AWS Clean Rooms collaborations with publishing partners to combine first- and third-party customer data directly.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/connecting-cdps-to-data-lakes-with-aws-clean-rooms.pdf)

![Architecture diagram](/images/solutions/connecting-cdps-to-data-lakes-with-aws-clean-rooms/images/connecting-cdps-to-data-lakes-with-aws-clean-rooms-1.png)

1. **Step 1**: The marketer uploads first-party data to the CDP's application.
1. **Step 2**: The CDP account stores the marketer's first-party data in an Amazon Simple Storage Service (Amazon S3) data lake and registers the data in its AWS Glue Data Catalog.
1. **Step 3**: The publisher's application stores ad impressions and user data in an Amazon S3 data lake in the publisher's account. It then registers the data in its Data Catalog.
1. **Step 4**: The CDP creates an AWS Clean Rooms collaboration within its account.
1. **Step 5**: The CDP invites the publisher to join the AWS Clean Rooms collaboration. The publisher accepts the invitation.
1. **Step 6**: The CDP adds the marketer's first-party data to the AWS Clean Rooms collaboration from the CDP's Amazon S3 data lake.
1. **Step 7**: The publisher adds data to the AWS Clean Rooms collaboration from the publisher's Amazon S3 data lake.
1. **Step 8**: The marketer runs a report on the CDP application.
1. **Step 9**: The CDP queries data within the AWS Clean Rooms collaboration.
1. **Step 10**: AWS Clean Rooms sends query results to a separate S3 bucket in the CDP account.
1. **Step 11**: The CDP reads query result data from Amazon S3 and returns the marketer's query results within the CDP application.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch, which continuously monitors operations and enables access to log files, is configurable so you can monitor the reliability, availability, and performance of AWS Clean Rooms. AWS CloudTrail automatically tracks event histories, enabling you to access information about who made requests to AWS Clean Rooms, the IP address from which the request was made, when it was made, and additional details. You can also configure an event trail for more details in tracking API requests. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance lets you use scoped-down AWS Identity and Access Management (IAM) policies to provide specific users and roles access. Using IAM, you can apply the principle of least privilege to restrict who can access and run queries on AWS Clean Rooms. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 stores multiple copies of data across Availability Zones, providing 99.999999999 percent durability of the data stored within S3 buckets. Additionally, AWS Glue and AWS Clean Rooms are serverless and fully managed by AWS, so the overall infrastructure is elastic, highly available, and fault tolerant, with built-in reliability and resiliency. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS Glue crawlers enable you to quickly scan and define the schemas for your data and register these schemas to your Data Catalog. You can configure these crawlers to run on a schedule or use an invocation to crawl source data. You can also configure AWS Glue to scale up or down within a specified range of AWS Glue job workers so that it only uses as much compute capacity as needed. Additionally, AWS Clean Rooms enables you to share subsets of your data quickly and securely, and it only provisions the necessary capacity to implement a query. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 provides low-cost storage for building data lakes and storing data. It also provides different storage tiers and lifecycle policies to optimize storage. For example, you can use Amazon S3 Intelligent-Tiering to provide automated data archiving based on usage or implement lifecycle policies to move data between storage tiers, helping you optimize costs. Additionally, this Guidance uses pay-as-you-go services, so you pay only for what you consume. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS Clean Rooms enables you to share only subsets of your data, reducing the need for data duplication across multiple platforms. Additionally, this Guidance reduces the need for CDPs to create custom solutions that might require additional compute resources. AWS Glue and AWS Clean Rooms are both serverless services, which means they scale seamlessly to meet compute needs, such as by provisioning only the compute resources required to run a query. This enables you to avoid unnecessary compute and waste of resources so that you use the least amount of carbon generation necessary. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
