---
source_url: https://docs.aws.amazon.com/solutions/customer-data-platform-on-aws/index.html
---

---
title: 'Guidance for Customer Data Platform on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/customer-data-platform-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Customer Data Platform on AWS

## Overview

This Guidance shows how you can build a well-architected customer data platform with data from a broad range of sources, including contact centers, email, web and mobile entries, point of sale (POS) transactions, and customer relationship management (CRM) systems. It explores each stage of building the platform, starting with the extraction of batched and real-time data streams. Next, this Guidance shows how to cleanse, enrich, and process the data to create a unified customer record across all data sources. Finally, the processed data is ready for analysis and collaboration, all in a restricted, secure environment where you set the controls. The data can be used to build more personalized customer experiences and to enhance the monetization of your marketing campaigns.

## How it works

This Guidance shows how to build a customer data platform with a full, 360 degree profile view of customer data. It explores each stage of building the platform, including data ingestion, identity resolution, segmentation, analysis, and activation.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/customer-data-platform-on-aws.pdf)

![Architecture diagram](/images/solutions/customer-data-platform-on-aws/images/customer-data-platform-on-aws-1.png)

1. **Step 1**: Build a Customer 360 profile from data sources including website, mobile application, advertising, and social media events, as well as transactional data from multiple systems of records and external data sets. This data is available for consumption in multiple formats and protocols: SaaS platform API for pull, real-time event push, batch files, Cloud Data Shares, Databases and Data Market Places.
1. **Step 2**: Achieve near real-time data ingestion through Amazon Kinesis Data Streams, Amazon Simple Queue Service (Amazon SQS) and API Gateway. Batch data ingestion uses AWS Transfer Family, AWS Database Migration Service (AWS DMS) and Amazon AppFlow. Use the Amazon AppFlow Connector SDK to build custom connectors to pull data from System of Record APIs. AWS Data Exchange (AWS ADX) subscriptions provide access to external data in multiple modes. Use Zero ETL capability where available to move data from AWS transactional datastores.
1. **Step 3**: In near real-time data collection, ingestion services collect data, apply real-time data transformations, resolution and store the data in Amazon Connect Customer Customer Profiles. Use Generative AI-based data mapping to identify where to store the incoming data. Use a combination of Customer Profile attributes (Master Data) and Profile objects (Transactional Data) to resolve and store required information. Use calculated attributes feature to generate actionable KPIs that support use cases like customer lifetime spend and other customer insights. For high volume data like clickstream, use Customer Profile as a pass-through and store the most recent information essential for activating real time personalization use cases like current items in cart, last viewed item, content, etc. Use the near real-time data export feature to send data to Analytical storage.
1. **Step 4**: In Batch Data Processing, the ingestion services collect and store raw data in Amazon Simple Storage Service (Amazon S3).
1. **Step 5**: For batch sources, use AWS Step Functions to orchestrate AWS Glue ETL jobs to clean and prepare the data. This data passes to AWS Entity Resolution service to match and link records. The resolved records persist in Amazon S3 and loaded into Amazon Connect Customer Customer Profiles. Use this common pattern for initial bulk load and/or batch sources.
1. **Step 6**: Data processing and identity resolution workflow transient data storage occur in the logical Clean Zone created using Amazon S3 Tables. The logical Curated Zone in Amazon S3 Tables store the final output of data processing for consumption.
1. **Step 7**: Use the unified customer profile stored in Amazon S3 Tables for segmentation. Use Amazon SageMaker Unified Studio to provision the ideal analytical compute features to data engineers, analysts and scientists. Use Amazon SageMaker AI to create Propensity, Churn, and other probabilistic segmentation attributes. Use Amazon Personalize recipes to generate product recommendations for upsell and cross-sell, next best action, or offer recommendations to improve other business KPIs. Use the Amazon S3 import feature to send relevant segmentation attributes to Amazon Connect Customer Profiles and use them in real-time/event-driven customer engagements. Use the Amazon Bedrock Prompt Management feature to store Generative AI prompts that allow the creation of hyper-personalized email, SMS, and push notification content. Use Amazon Bedrock Guardrails to store organizational policies and validate the generated contents before activating them. Use Amazon Bedrock Knowledge Bases to store and generate contextually relevant, personalized content.
1. **Step 8**: Use Amazon Connect Customer Outbound Campaigns that access data in Amazon Connect Customer Customer Profiles and create proactive multi-channel customer engagements. Amazon Connect Customer uses the unified customer profile to enhance the customer experience in call centers. AWS Glue software-as-a-service (SaaS) applications integrations allow uploading data to advertising platforms.
1. **Step 9**: Use AWS Clean Rooms for privacy-enhanced data collaborations with partners to support media planning, audience activation and measurement use cases. AWS Lambda and Amazon API Gateway enable API access to Customer 360 profiles.
1. **Step 10**: Store clean, modeled data in Amazon Redshift for fast and repeated queries. Make all other data in the analytical platform available for business intelligence use cases through the Amazon SageMaker Unified Studio SQL analytics feature. Amazon QuickSight offers large-scale data analysis and visualization.
1. **Step 11**: Upload Customer 360 profile data to paid media Ad Platforms such as Amazon Marketing Cloud (AMC) and Amazon Ads Demand-Side Platform (Amazon Ads DSP) for online media targeting. Marketing Platforms and other SaaS Applications use the Customer 360 profile data for marketing and data monetization use cases. Owned Media platforms use Customer 360 profile for Website and Mobile App personalization.
1. **Step 12**: Use Amazon SageMaker Catalog to create a technical and business data catalog for data discovery and data product sharing. Use Amazon SageMaker LakeHouse for fine-grained access controls on all cataloged data. Use an Apache Iceberg-compatible REST catalog to allow easy access of customer profile data to third-party tools. AWS Identity and Access Management (AWS IAM) securely manages identities and access to AWS services and resources.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance has observability built-in, with every AWS service publishing metrics to Amazon CloudWatch where dashboards and alarms can be configured, enhancing operational excellence to support a well-architected framework. And by using CloudWatch alarms, or Amazon Simple Notification Service (Amazon SNS), you are notified and can respond appropriately to incidents. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM policies are created using the least privilege access principle, and include restrictions to the specific resource and operation, supporting a secure framework for people and machine access. To further protect resources in this Guidance, secrets and configuration items are centrally managed and secured using AWS Key Management Service (AWS KMS). And to protect data, the Amazon S3 bucket is encrypted using the AWS KMS keys for data at rest. The data in transit is encrypted and transferred over HTTPS. Additionally, all of the Amazon S3 buckets are blocked from public access, and access to DynamoDB is only required within a virtual private cloud (VPC). Thus, we are using a VPC endpoint to limit access from only the required VPC. Doing this prevents that traffic from traversing the open internet and being subject to that environment. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

By deploying this Guidance, you also implement a highly available network topology in multiple ways. First, every service and technology chosen for each architecture layer is serverless and fully managed by AWS, making the overall architecture elastic, highly available, and fault-tolerant. Second, DynamoDB has a point-in-time recovery feature that provides continuous backups of your tables and enables you to restore your table data to any point-in-time in the preceding 35 days. Third, Amazon S3 offers industry-leading durability, availability, performance, security, and virtually unlimited scalability at very low costs. Finally, AWS serverless services, including Lambda, are fault-tolerant and designed to handle failures. If a service invokes a Lambda function and there is a service disruption, Lambda invokes the function in a different Availability Zone. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services selected for this Guidance are designed to enhance your workload performance. For example, by using serverless technologies, you only provision the exact resources you use. The serverless architecture reduces the amount of underlying infrastructure you need to manage, allowing you to focus on solving your business needs. You can also use automated deployments to deploy the different components of this Guidance into any AWS Region quickly, providing data residence and reduced latency. Also, all components of this Guidance are collocated in a specific Region and use a serverless stack, which avoids the need for you to make location decisions about your infrastructure apart from the Region choice. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using serverless technologies and managed services, you only pay for the resources you consume, helping you control costs. Another way this Guidance can help optimize costs is by helping you plan for data transfer charges. To do this, we recommend you identify data egress points and evaluate the use of network services like AWS PrivateLink and AWS Direct Connect to reduce data transfer costs. To further optimize compute costs for this Guidance, scoping of near real-time data ingestion allows you to leverage Amazon Kinesis Data Streams with a provisioned capacity mode. Provisioned capacity mode is best suited for predictable application traffic or for applications where the traffic is consistent, increases gradually, or where you can forecast capacity requirements to control costs. Similarly, for DynamoDB, use provisioned capacity mode for predictable workloads to reign in costs. Also, when AWS Glue is performing data transformations, you only pay for the infrastructure while the processing is occurring. In addition, through a tenant isolation model and resource tagging, you can automate cost usage alerts and measure costs specific to each tenant, application module, and service. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance scales to continually match the needs of your workloads with only the minimum resources required through the extensive use of serverless services. The efficient use of these resources also reduces the overall energy required to operate your workloads. And, this Guidance uses purpose-built data stores for specific workloads, which minimizes the resources provisioned. For example, Amazon S3 is used for data lake storage, and DynamoDB is used to support low latency queries. Finally, all of the services used in this Guidance are managed services that allocate hardware according to the workload demand. We recommend using the provisioned capacity options (as mentioned previously) in the services when available, and when the workload is predictable, to reduce cost. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **A modern approach to implementing the serverless Customer Data Platform**: This post explores how to use serverless technologies for the Customer Data Platform (CDP).

[Learn more](https://aws.amazon.com/blogs/architecture/a-modern-approach-to-implementing-the-serverless-customer-data-platform-cdp/)

- **An overview and architecture of building a Customer Data Platform on AWS**: This post examines the logical architecture of the CDP to provide guidance to help reduce complexity, increase agility, improve operational excellence, and optimize cost.

[Learn more](https://aws.amazon.com/blogs/architecture/overview-and-architecture-building-customer-data-platform-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
