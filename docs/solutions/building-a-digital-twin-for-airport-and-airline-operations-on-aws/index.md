---
source_url: https://docs.aws.amazon.com/solutions/building-a-digital-twin-for-airport-and-airline-operations-on-aws/index.html
---

---
title: 'Guidance for Building a Digital Twin for Airport & Airline Operations on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-digital-twin-for-airport-and-airline-operations-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Building a Digital Twin for Airport & Airline Operations on AWS

## Overview

This Guidance shows how historical and current operational data, which has been captured with internet of Things (IoT) devices and camera streams, can be viewed simultaneously by constructing a digital twin. It supports multiple layers of data visualization, each tailored to the specific needs of airline operations. Passenger flow management, baggage handling, predictive maintenance for equipment, tracking movable assets, aircraft turnaround management, and a Building Management System (BMS) can all be integrated for optimal operations.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-a-digital-twin-for-airport-airline-operations-on-aws.pdf)

![Architecture diagram](/images/solutions/building-a-digital-twin-for-airport-and-airline-operations-on-aws/images/building-a-digital-twin-for-airport-and-airline-operations-on-aws-1.png)

1. **Step 1**: Extract historical and predictive data from your airport data platform, which uses AWS Database Migration Service (AWS DMS), AWS Data Exchange, Amazon Kinesis Data Streams, and Amazon Simple Storage Service (Amazon S3).
1. **Step 2**: Query Amazon Redshift from the digital twin view for historical data.
1. **Step 3**: Query Amazon SageMaker from the digital twin view for predictive and "what-if" analysis.
1. **Step 4**: Query data from your airport Ops360 datastore in Amazon DynamoDB by exposing an Amazon API Gateway endpoint through an AWS Lambda integration.
1. **Step 5**: Capture Internet of Things (IoT) sensor data from building management systems, baggage handling, passenger-flow trackers, and more. Aggregate the data and transmit it to the cloud on a schedule using AWS IoT Greengrass.
1. **Step 6**: Run inferences on your camera streams at the edge using AWS Panorama.
1. **Step 7**: Centralize all IoT data ingested into the cloud using AWS IoT Core to verify authentication and authorization standards. Use AWS IoT SiteWise to build the IoT data model for the digital twin to consume.
1. **Step 8**: Make your live video feeds available for consumption through the digital twin by using Amazon Kinesis Video Streams.
1. **Step 9**: Use AWS IoT TwinMaker to build your scenes and overlay data on your 3D models. Publish the scenes on Amazon Managed Grafana or on a custom front end built using AWS IoT Application Kit and hosted on AWS Amplify.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance lets you use an Amazon CloudFormation template or an AWS Cloud Development Kit (AWS CDK) for scripts, so you can quickly and safely deploy changes and updates to your workloads. By using infrastructure-as-code tools, you can automate deployment and security checks for all infrastructure and software updates. For observability, you can use Amazon CloudWatch, which provides level metrics and personalized dashboards and logs. You can then set up dashboards and alarms to notify you when your environment is not operating as expected. You can even set up automatic workflows to remediate certain states. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses AWS IoT Core to securely connect all IoT devices to AWS. The service encrypts all communication and requires all its clients (connected devices, server applications, mobile applications, or human users) to use strong authentication (including X.509 certificates, AWS Identity and Access Management (IAM) credentials, or third-party authentication through Amazon Cognito). AWS IoT Core also offers fine-grained authorization to isolate and secure communication among authenticated clients. This Guidance also uses Amazon Managed Grafana, which lets you control and restrict incoming traffic that can reach your workspace. It also encrypts data at rest without special configuration or third-party tools and encrypts data in transit using SSL. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses AWS Panorama so that devices can run machine learning (ML) models locally while also sending data to the cloud for further processing. This edge ML deployment reduces your dependency on cloud connectivity, improving reliability and reducing downtime risks. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses AWS IoT SiteWise, which efficiently processes a large volume of machine data at scale to help you derive insights faster. Additionally, AWS IoT TwinMaker improves efficiency by accelerating digital twin creation through prebuilt components, templates, and automation. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance helps you optimize data storage costs by using Amazon S3, which provides features like life cycle policies and S3 Intelligent-Tiering to automatically move data to the most cost-effective tiers, such as S3 Standard-Infrequent Access (S3 Standard-IA) and S3 Glacier Flexible Retrieval. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance reduces the need to connect to the cloud continuously by using AWS IoT Greengrass, which deploys ML models and logic to devices to facilitate autonomous operations locally. This lets devices perform compute, messaging, data caching, syncing, and ML inferencing at the edge, helping you minimize your power usage and reduce your carbon footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Guidance for Airport Data Management on AWS**: This Guidance helps you build data management systems that can both monitor airport operations and enhance the traveler experience.

[Learn more](/solutions/airport-data-management-on-aws/)

- **How digital twins can optimize Travel and Hospitality operations**: This blog post explores how travel and hospitality companies can use digital twins to monitor and optimize operations.

[Learn more](https://aws.amazon.com/blogs/industries/how-digital-twins-can-optimize-travel-and-hospitality-operations/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
