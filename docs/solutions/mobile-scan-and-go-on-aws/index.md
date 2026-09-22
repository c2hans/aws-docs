---
source_url: https://docs.aws.amazon.com/solutions/mobile-scan-and-go-on-aws/index.html
---

---
title: 'Guidance for Mobile Scan & Go on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/mobile-scan-and-go-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Mobile Scan & Go on AWS

Building a Smart Store experience for frictionless shopping, using AWS native services

## Overview

This Guidance demonstrates how you can set up scan and go technology using AWS services. It can help you move the scan and checkout process to your own application with the help of AWS AppSync, which creates GraphQL APIs and offers a single endpoint for your data. This Guidance also shows how you can configure various other AWS services to provide personalized recommendations, stream the data to a centralized data lake, and authenticate users. The authenticated users will scan any barcode, either 1D or 2D, where they can read about the product, check the price, and more, then move the product to their cart to complete the self-checkout process. Finally, by leveraging machine learning capabilities, the application incorporates features such as fraud detection, and near real-time redemption of loyalty points.

## How it works

This architecture diagram demonstrates how you can build and use scan and go technology on AWS. Configuring this Guidance helps you to streamline in-store experiences, efficiently handle transactions, and offer tailored product suggestions to elevate your customer’s journey.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/mobile-scan-go-on-aws.pdf)

![Architecture diagram](/images/solutions/mobile-scan-and-go-on-aws/images/mobile-scan-and-go-on-aws-1.png)

1. **Step 1**: Users start with an application built by AWS Amplify and that is authenticated with Amazon Cognito for barcode scanning or visual searches.
1. **Step 2**: After successful authentication, users are directed to relevant screens. AWS AppSync handles all queries received by the system.
1. **Step 3**: [optional] Amazon Location Services requests permissions from the user and then provides the user's location to the application to push the relevant product catalog for the store.
1. **Step 4**: Depending on specific needs, AWS AppSync requests data from the store's relevant database. Amazon OpenSearch Service, using search microservice, retrieves and returns this information to the user. The Product Information Management (PIM) system can also serve as a product catalog.
1. **Step 5**: Amazon Personalize, powering recommendations microservice, provides recommendations for items, generates personalized promotions or coupons, guides the customers in the store, personalizes the search results based on past behaviors, and reminds of abandoned carts.
1. **Step 6**: Amazon API Gateway invokes AWS Lambda to validate point of sale (POS) transactions. Lambda performs tasks, like database checks and updates, then relays responses back to POS.
1. **Step 7**: All operations and data from the search engine and store inventory are streamed into a centralized data lake. This data undergoes cleaning and normalization using AWS Glue, ensuring it is prepared and optimized for querying purposes.
1. **Step 8**: The reportable data can be consumed on demand through Amazon Athena, or loaded into Amazon Redshift. This allows different users, tools, and resources to efficiently access and utilize the data as needed. Amazon QuickSight is available for visual analysis.
1. **Step 9**: The AWS Amplify-built application integrates with other microservices within the retail stack, such as a scanning service, payment gateway API, and a QR code generator which follow customer journey.
1. **Step 10**: Leveraging machine learning capabilities with Amazon SageMaker, the application incorporates features such as fraud detection, and near real-time redemption of loyalty points.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS AppSync, Lambda, API Gateway, OpenSearch, Amazon Redshift, and QuickSight are configured in this Guidance so that you can run and monitor your systems effectively while gaining insights into your operations. AWS AppSync enables near real-time data synchronization across users and devices, vital for a seamless scan and go experience. Lambda and API Gateway, particularly crucial for handling POS transactions, automate functionalities and secure interactions to reduce the need for extensive server management. OpenSearch supports near real-time data analysis and visualization, which are necessary for understanding system performance. Finally, Amazon Redshift and QuickSight transform operational data into accessible, understandable formats for analysis and reporting, thereby supporting data-driven decision-making. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Cognito, AWS Identity and Access Management (IAM), API Gateway, and Lambda help secure your workloads. Cognito provides robust user sign-up, sign-in, and access control—enhancing the security of user data and interactions. IAM facilitates secure control access to AWS resources. It enables the management of users, security credentials such as access keys, and permissions that control which AWS resources users can access. API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management, authorization, and access control. Additionally, the automatic scaling behavior for Lambda is designed to maintain optimal security and performance at the lowest operational cost. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Configure Lambda, API Gateway, AWS AppSync, and OpenSearch to enhance the reliability of your workloads. These services are resilient, scalable, and helps ensure your data consistency—essential for reliability. Lambda and API Gateway handle traffic efficiently and ensure the smooth running of operations. AWS AppSync offers strong data synchronization capabilities, enabling consistent user experiences across various devices and platforms. And OpenSearch provides the ability to analyze and visualize system data, helping identify potential issues early and make informed decisions. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda and API Gateway are designed for low-latency, high-throughput performance, making them ideal for handling POS transactions in the scan and go system. Also, AWS AppSync offers a highly scalable data synchronization solution that can handle a large number of concurrent users, ensuring a seamless user experience, even during peak usage periods. Finally, Amazon Personalize allows for near real-time personalization and recommendations, which improves user engagement and the overall application performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda is a serverless computing service that allows you to run code without provisioning or managing servers, which reduces operational overhead and costs. With OpenSearch, it provides cost-effective and scalable search capabilities, helping you to optimize costs by tailoring our cluster to the required workload. Furthermore, Amazon Personalize also operates on a pay-as-you-go model, so you only pay for what you use, and it can provide cost-effective personalization and recommendations. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda enables the application configured through this Guidance to be more efficient by reducing the amount of unused computing resources. Amazon Simple Storage Service (Amazon S3) provides storage services that include features like Amazon S3 Intelligent-Tiering storage class. This feature automatically moves data to the most cost-effective access tier, without performance impact or operational overhead. This storage optimization feature reduces resource usage and cost. Moreover, SageMaker provides a fully managed service that enables users to quickly and easily build, train, and deploy machine learning models. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
