---
source_url: https://docs.aws.amazon.com/solutions/edge-computing-in-retail-on-aws/index.html
---

---
title: 'Guidance for Edge Computing in Retail on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/edge-computing-in-retail-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Edge Computing in Retail on AWS

## Overview

This Guidance demonstrates how to enhance customer experience and operational efficiency in retail by combining AWS edge computing services with on-premises retail facilities. IoT sensors, cameras, and point-of-sale systems collect in-store data that's processed locally through AWS IoT Greengrass and edge components for immediate analysis. The system enables real-time customer journey optimization through Amazon Bedrock Agents and Amazon Personalize while maintaining security with Amazon GuardDuty. You can streamline operations, deliver personalized shopping experiences, and make data-driven decisions faster without compromising on security or performance

## Benefits

### Maintain critical retail operations

Ensure essential store functions like point-of-sale and security systems operate reliably, even during network interruptions. Local processing capabilities keep your business running while automatically synchronizing with the cloud when connectivity returns.

### Deliver real-time personalized experiences

Process customer data instantly at store locations to provide timely, personalized recommendations and experiences. Combine edge analytics with cloud-based AI to optimize customer journeys and increase engagement.

### Reduce operating costs

Reduce data transfer and infrastructure costs by processing store data locally and sending only relevant information to the cloud. Maximize existing hardware investments through containerized applications.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/edge-computing-in-retail-on-aws.pdf)

![Architecture diagram](/images/solutions/edge-computing-in-retail-on-aws/images/edge-computing-in-retail-on-aws-1.png)

1. **Step 1**: IoT sensors, IP cameras, point-of-sale systems, mobile clients, and appliances collect raw data in-store
1. **Step 2**: AWS IoT Greengrass streams data via Device Gateway and Stream Manager
1. **Step 3**: Data is initially processed by edge components using Lambda function and AI/ML Inference for quick analysis
1. **Step 4**: Amazon EKS Hybrid Node/Amazon ECS Anywhere runs Applications & Databases that support Point of Sale and Retail Applications
1. **Step 5**: Amazon GuardDuty provides threat detection at the edge
1. **Step 6**: App data, logs, and metrics are sent to Amazon Kinesis, Amazon EventBridge, or IoT Topic via MQTT, HTTP, or WebRTC protocols
1. **Step 7**: Data is stored in Amazon Kinesis, Amazon S3 or managed database where transformation is conducted with AWS Glue or AWS Lambda. Store Analytics surfaced using Amazon Athena.
1. **Step 8**: Machine Learning is conducted and edge models optimized using Amazon SageMaker AI
1. **Step 9**: Amazon Bedrock Agents & Amazon Personalize optimize customer journeys and personalized recommendations
1. **Step 10**: Amazon Location Service kicks off business logic when customer enters/exits store Geofence
1. **Step 11**: Content is updated and distributed globally with Amazon Cloudfront to closest Edge location. Lambda@Edge allows auth logic to be added & AWS WAF provides protection from exploits
## Related content

- **Consolidate, modernize, transform: Edge computing for modern retail**: Learn how retailers can leverage AWS edge computing solutions to consolidate infrastructure, establish unified cloud-edge architecture, and enable next-generation store applications while maximizing existing investments and reducing operational costs.

[Go to blog](https://aws.amazon.com/blogs/industries/consolidate-modernize-transform-edge-computing-for-modern-retail/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
