---
source_url: https://docs.aws.amazon.com/solutions/serverless-reservation-system-for-lodging-on-aws/index.html
---

---
title: 'Guidance for Serverless Reservation System for Lodging on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/serverless-reservation-system-for-lodging-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Serverless Reservation System for Lodging on AWS

## Overview

This Guidance demonstrates how to build a highly available lodging reservation system using multiple serverless compute and database services, each tailored for specific functionalities. It showcases the services employed to support the back-end of an administration portal, inventory management, and the search and book functionalities for booking engines, mobile apps, and third-party systems. With this Guidance, you can develop a consistent, low-latency inventory and booking service capable of handling any scale.

## How it works

This architecture diagram shows how to build a serverless, microservice-based, and central reservation system.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/serverless-reservation-system-for-lodging-on-aws.pdf?target=_blank)

![Architecture diagram](/images/solutions/serverless-reservation-system-for-lodging-on-aws/images/serverless-reservation-system-for-lodging-on-aws-1.png)

1. **Step 1**: The property administrator access for the administrator portal is stored in an Amazon Simple Storage Service (Amazon S3) bucket and served by Amazon CloudFront. The property administrator creates business objects such as room types, rates, shopping and booking rules, taxes, and more through Amazon API Gateway, which calls Amazon Cognito to validate credentials in the requests.
1. **Step 2**: AWS Lambda processes the configuration requests and stores them in Amazon S3 and Amazon DynamoDB. Configuration changes invoke Amazon EventBridge events for processing by other parts of the application.
1. **Step 3**: New configuration events from EventBridge invoke a Lambda function, which reads the published configuration from Amazon S3 and updates the inventory data in an Amazon Aurora serverless relational database.
1. **Step 4**: Client applications pass the searched destination to the geolocation service hosted in AWS Fargate. The geolocation service calls Amazon Location Service to determine the GeoHash. Amazon ElastiCache caches results to improve performance and reduce cost.
1. **Step 5**: Client applications use the GeoHash to call the shopping API using API Gateway and Lambda to search for properties in the location. The service retrieves the Geohash mapping from DynamoDB, a NoSQL database, and retrieves properties from the Inventory API and the dynamic pricing microservice.
1. **Step 6**: The pricing microservice provides dynamic hotel prices to the shopping service. It reads the published hotel configuration from Amazon S3.
1. **Step 7**: The booking microservice uses API Gateway, Lambda, and Amazon S3 to process client booking requests. It creates booking records in Amazon Quantum Ledger Database (Amazon QLDB). It then publishes bookings to Amazon Kinesis for consumption by the dynamic pricing microservice and other analytical or third-party applications.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

EventBridge allows you to respond to events in real-time, automating responses based on changes in your AWS environment. Amazon CloudWatch monitors AWS resources and applications, providing insights into performance, operational health, and overall status so you can take proactive measures to maintain operational excellence. These services enable the building and operation of reliable, scalable, and efficient systems aligned with business objectives. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) manages access to AWS resources, defining and enforcing least privilege access and supporting multi-factor authentication (MFA) for enhanced security. Amazon Cognito simplifies user authentication and authorization, enabling secure application access while protecting user data. AWS CloudTrail provides visibility into account activity, auditing, monitoring, and compliance with security policies. EventBridge automates responses to security events, such as rotating access keys or disabling compromised resources, fortifying the overall security posture. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

EventBridge simplifies event management and routing, enabling reliable event-driven architectures. Aurora Serverless automatically scales database capacity based on demand for high availability and fault tolerance. Additionally, Fargate delivers a reliable and scalable infrastructure for containerized applications without managing servers or clusters. Location Service provides reliable and accurate location data, contributing to overall application reliability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

CloudFront efficiently delivers content by caching at edge locations, reducing latency, and improving the user experience. DynamoDB offers fast and scalable NoSQL database performance, delivering single-digit millisecond response times at any scale, making it suitable for applications with intense read/write traffic and high-performance requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 provides cost-effective storage and content delivery—you pay only for the storage you use. Lambda provides serverless computing, reducing infrastructure expenses. Further, Lambda enables running code without provisioning or managing servers so that you only pay for consumed compute time. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda and Fargate, serverless compute services, contribute to sustainability efforts by automatically provisioning and scaling resources based on actual workload demands. These services minimize waste, reduce energy consumption, and lower carbon emissions by optimizing resource utilization and eliminating idle resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
