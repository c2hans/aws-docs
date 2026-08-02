---
source_url: https://docs.aws.amazon.com/solutions/real-time-casino-player-analytics-on-aws/index.html
---

# Guidance for Real-Time Casino Player Analytics on AWS

## Overview

This Guidance shows how your developers can build a real-time analytics pipeline that uses AI to deliver effective marketing offers during game sessions. By using gaming-machine and shuffler data to update machine learning (ML) models in real time, this pipeline predicts the best offers for individual customers. The analytics pipeline then returns these findings to your gaming machines and applications so that you can promote offers based on each user’s customer profile.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/real-time-casino-player-analytics-on-aws.pdf)

![Architecture diagram](/images/solutions/real-time-casino-player-analytics-on-aws/images/real-time-casino-player-analytics-on-aws-1.png)

1. **Step 1**: Casino slot machine data, as well as shuffler data integrated with AWS IoT Greengrass, are streamed from the casino floor through a private network into Amazon API Gateway and AWS IoT Core, respectively. AWS X-Ray can be used to help analyze any issues.
1. **Step 2**: Data is then streamed into Amazon Kinesis Data Streams.
1. **Step 3**: Slot data from Kinesis Data Streams is processed by AWS Lambda to calculate the customer rating and store a raw copy in Amazon Simple Storage Service (Amazon S3) for ML training.
1. **Step 4**: Raw data from slot machines and shufflers is transformed to identify unique records through AWS Glue data transformation.
1. **Step 5**: The refined data after transformation is stored in an Amazon S3 bucket.
1. **Step 6**: The customer profile, ratings, and offers are updated in Amazon DynamoDB for fast retrieval by slot machines or a customer rating application.
1. **Step 7**: Refined shuffler data is stored for aggregation and retrieval in Amazon Aurora.
1. **Step 8**: Refined slot data is used to train and update the ML model on Amazon SageMaker, which then predicts the best offers for the individual customer. Refined shuffler data is used to extract metrics to feed an ML model to predict failures.
1. **Step 9**: The customer profile, ratings, and offers are made available to be consumed by games and applications to promote within the game or session.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch enhances observability through metrics and helps you visualize data through personalized dashboards and logs. Additionally, X-Ray helps you analyze user requests as they travel through your API Gateway APIs to the underlying services. Together, CloudWatch and X-Ray can help you identify performance bottlenecks and troubleshoot requests. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

In this Guidance, devices use X.509 certificates for authentication and AWS IoT policies for authorization so that they can securely connect with each other, AWS IoT Core, and IoT Greengrass. Additionally, all AWS Identity and Access Management (IAM) policies have been scoped down to the minimum permissions required for the services to function properly, helping you limit unauthorized access to resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

API Gateway and Lambda operate in multiple Availability Zones (AZs) in each AWS Region, using this redundancy to maintain availability even in the case of infrastructure failure. API Gateway automatically recovers from the failure of an AZ. Additionally, Kinesis Data Streams provides a default 24-hour retention period, enabling you to select a specific timestamp from which to start processing records. This helps you reliably resume processing at a later time without data loss. Finally, DynamoDB provides on-demand backup capability, point-in-time recovery, and global tables that sync across Regions to help support your data resiliency and backup needs. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Kinesis Data Streams enables multiple applications to consume data from the same stream. As a result, multiple actions, like archiving and processing, can take place concurrently and independently, providing higher throughput. CloudWatch provides actionable insights that help you optimize application performance, manage resource utilization, and understand system-wide operational health. Finally, Amazon DynamoDB Accelerator (DAX) helps you increase performance by providing quicker response times through in-memory reads. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The DynamoDB automatic scaling feature manages throughput based on your application traffic and your target utilization metric. This helps you make sure your tables have the required capacity required for your application and helps you avoid the cost of overprovisioning. Amazon S3 also provides automatic scalability, helping you increase your agility. Together, these services lower the total cost of ownership for storing and retrieving data. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda allows you to run code without provisioning or managing servers, and its functions automatically scale to meet the demand. It also reuses implementation environments, improving your resource utilization. These capabilities help you optimize the resource usage of your application, minimizing the energy consumption of your workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
