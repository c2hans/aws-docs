---
source_url: https://docs.aws.amazon.com/solutions/building-a-composable-customer-data-platform-on-aws/index.html
---

---
title: 'Guidance for Building a Composable Customer Data Platform on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-composable-customer-data-platform-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Building a Composable Customer Data Platform on AWS

## Overview

This Guidance demonstrates how to construct a composable customer data platform (CDP) on AWS, leveraging Hightouch capabilities in conjunction with an existing Snowflake data warehouse. It shows you how to collect, unify, and activate customer data to address various marketing needs effectively. By adopting this approach, you can swiftly adapt to market changes, integrating only essential components tailored to your specific requirements. This Guidance enables you to customize your CDP while maintaining robust security and scalability, ultimately driving more targeted marketing campaigns and improved customer experiences.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-a-composable-customer-data-platform-on-aws.pdf)

![Architecture diagram](/images/solutions/building-a-composable-customer-data-platform-on-aws/images/building-a-composable-customer-data-platform-on-aws-1.png)

1. **Step 1**: Batch data is ingested from various SaaS platforms using available Amazon Appflow connectors. Third party data insights are ingested using AWS Data Exchange. Ingested batch data is stored in Amazon Simple Storage Service (Amazon S3) and transformed using an Amazon S3 trigger that invokes AWS Lambda function. AWS Glue can help with data preparation and quality checks. You can also use Snowflake Marketplace to bring third party insights directly into Snowflake tables.
1. **Step 2**: Real-time data is ingested using Amazon Kinesis Data Streams or Amazon Managed Streaming for Apache Kafka (Amazon MSK). Data streams are then sent to Amazon Data Firehose which can do a Direct PUT to Snowflake in seconds.
1. **Step 3**: To resolve identities of ingested data, you can choose between AWS Entity Resolution or Hightouch Identity Resolution based on your use case. Use Guidance for Preparing and Validating Records for Entity Resolution on AWS to resolve identities of batched transformed data in Amazon S3 using AWS Entity Resolution matching workflows.
1. **Step 3a**: Transformed and resolved data is loaded from Amazon S3 into Snowflake over AWS PrivateLink.
1. **Step 4**: Stream data through Firehose to invoke a Lambda function and transform data. Additionally, invoke AWS Entity Resolution GetMatchId API to find matches for the given data record.
1. **Step 4a**: The transformed and matched data is then sent to Snowflake using Snowpipe Streaming to build Customer 360 over an Amazon private network using PrivateLink.
1. **Step 5**: Alternatively, use Hightouch Identity Resolution to stitch your data to build customer profiles directly from data in Snowflake tables. The identity graph table is stored back in Snowflake. All traffic between Hightouch and Snowflake is securely managed using PrivateLink.
1. **Step 6**: Build a Customer 360 view once you centralize all your customer data in Snowflake tables to launch personalized customer experiences across various channels.
1. **Step 7**: Marketers can use Hightouch Customer Studio to build, manage, and analyze audiences with no SQL knowledge required. All traffic between Hightouch and Snowflake goes over PrivateLink.
1. **Step 8**: Create sync pipelines using Hightouch Reverse ETL to activate your audiences to various destinations.
1. **Step 9**: For any AI/ML needs, you can train and deploy models using Amazon SageMaker AI and Snowpark ML.
1. **Step 9a**: Use Amazon QuickSight or Hightouch Campaign Intelligence to analyze data from various marketing campaigns.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Leveraging serverless offerings like Amazon S3, Kinesis, Amazon MSK, and Lambda eliminates infrastructure management burdens while enabling automatic scaling based on demand. These services provide built-in scalability, elasticity, high availability, and durability, allowing development teams to concentrate on core functionality and continuous workload improvement rather than managing underlying infrastructure components. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The Guidance implements robust data protection through server-side encryption for data at rest in S3 buckets. PrivateLink establishes private connections between Amazon Virtual Private Cloud (Amazon VPC) and AWS Partners, enhancing security by keeping traffic within AWS networks and eliminating public internet exposure. This simplified network management approach significantly reduces potential attack surfaces and strengthens the overall security posture. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 supports data version control, prevents accidental deletions, and enables cross-Region replication. The serverless architecture, incorporating Kinesis, Amazon MSK, and Lambda, delivers automatic scaling and high availability without server management overhead. Amazon S3 versioning enables preservation and restoration of object versions, facilitating recovery from unintended actions and application failures, while the serverless components handle resource scaling automatically. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance optimizes performance through serverless technologies that provision resources precisely matched to usage requirements. Automatic resource scaling helps ensure appropriate capacity without over-provisioning, while PrivateLink reduces network latency by keeping traffic within the AWS network. This approach delivers high bandwidth connectivity and improved user experience through optimized resource utilization and streamlined network pathways. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 enables cost-effective data storage through flexible storage classes and automatic scaling, eliminating upfront infrastructure costs. PrivateLink reduces data transfer costs while maintaining consistent performance compared to public internet routing. Amazon S3 lifecycle rules can automatically transition or delete data based on defined criteria, further optimizing storage costs through automated management. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3 lifecycle configurations enable intelligent data management across storage classes based on access patterns, while Lambda offers execution-based resource consumption that minimizes energy waste from idle servers. These serverless services automatically optimize resource utilization in response to demand, resulting in improved energy efficiency and reduced environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
