---
source_url: https://docs.aws.amazon.com/solutions/deploying-smart-machines-on-aws/index.html
---

---
title: 'Guidance for Deploying Smart Machines on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-smart-machines-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Deploying Smart Machines on AWS

## Overview

This Guidance demonstrates how to deploy, manage, and monitor smart industrial products with AWS services. You can remotely manage these products at scale and build a robust industrial data management layer and an industrial data lake, collectively referred to as the “industrial data foundation.” This data foundation enables remote monitoring and notifications for maintenance personnel. Additionally, it drives artificial intelligence and machine learning (AI/ML) models, business intelligence dashboards and reports, AI assistants, APIs, and provides contextual product information for contact center agents.

## How it works

### Connect and Manage Machines

This architecture diagram shows the process of connecting smart machines, remotely managing them, and constructing an industrial data management layer. The following slides show further details on building a data foundation and managing the device lifecycle.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-smart-machines-on-aws.pdf#page=1)Step 1A smart machine connects to AWS IoT Core using a Message Queuing Telemetry Transport (MQTT) client, AWS IoT Device SDK, or the edge runtime provided by AWS IoT Greengrass. The telemetry data is then ingested into AWS IoT SiteWise directly through AWS IoT SiteWise Edge or through AWS IoT Core.Step 2If the machine lacks direct internet connectivity, use an edge gateway as a cloud connectivity layer. The edge gateway collects data from the machines, data historians, applications, then processes, stores, and forwards it to the AWS Cloud. Run custom applications and ML inferences at the edge.Step 3Facilitate scalable two-way communication between machines or edge gateways and the AWS Cloud, without the need to manage infrastructure, using AWS IoT Core.Step 4Remotely provision, monitor, update, and troubleshoot machines or edge gateways by leveraging AWS IoT Device Management. Build a custom fleet management console using AWS Amplify to visualize your fleet, and search across it to view machine state and health data.Step 5Audit your fleet for compliance with security best practices and continuously monitor it using AWS IoT Device Defender. Any security findings are sent to AWS Security Hub for a centralized view of all security issues from various AWS services.Step 6Ingest and contextualize operational data from your machines using AWS IoT SiteWise data streams and modeling capabilities. Additionally, compute performance metrics, store timeseries data, create alarm definitions, and provide flexible data access to external applications.### Build an Industrial Data Foundation

This architecture diagram demonstrates how the industrial data foundation can enable operations monitoring, alarm notifications, AI/ML models, business intelligence dashboards and reports, AI assistants, APIs, lifecycle management— empowering contact center agents with contextual machine information.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-smart-machines-on-aws.pdf#page=2)Step 7Build an industrial data lake using the contextual data from AWS IoT SiteWise. Govern, secure, and share data using AWS Lake Formation for advanced analytics. Catalog and analyze data with services like AWS Glue and Amazon Athena.Step 8Remotely monitor machines using AWS IoT SiteWise Monitor or with Amazon Managed Grafana for rich, contextual dashboards. Build digital twins powered by AWS IoT TwinMaker to improve equipment performance.Step 9Notify operational personnel about the health of machines using AWS IoT Events and Amazon Simple Notification Service (Amazon SNS). Create state machines and event monitoring applications with AWS IoT Events.Step 10Develop AI/ML solutions for predictive maintenance with Amazon SageMaker and build generative AI solutions using Amazon Bedrock.Step 11Amazon QuickSight enables data-driven decisions. With the Amazon Q add-on, business users can ask natural language queries for quick insights. Empower employees with enterprise information using Amazon Q Business.Step 12Provide historical and real-time machine data to customers by building serverless APIs using Amazon API Gateway and AWS AppSync that can scale to millions of users.Step 13Use Amazon DynamoDB for storing machine configuration, AWS CodePipeline for automating continuous integration and continuous delivery (CI/CD), Amazon Simple Storage Service (Amazon S3) for storing artifacts, and AWS IoT Greengrass for managing edge devices.Step 14Leverage Amazon Connect Customer to meet customer service needs and empower agents with contextual machine information.### DevOps Lifecycle Management

This architecture diagram illustrates the process of enhancing machine capabilities and resolving issues through over-the-air (OTA) updates, leveraging an automated CI/CD pipeline that involves various stages of development, including build, test and deployment. This DevOps lifecycle helps close the loop to quickly respond to customer needs in the market.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-smart-machines-on-aws.pdf#page=3)Step 1The machine builder gathers requirements through Voice of Customer feedback and product usage analysis in an effort to enhance machine capabilities or resolve ongoing issues.Step 2Software developers and embedded developers make changes to the source code hosted by source control services such as GitHub, GitLab, and Bitbucket.Step 3Leverage AWS CodeBuild with cross-build tools to create artifacts for devices and emulators. DynamoDB provides the necessary machine-specific configuration. CodePipeline automates the CI/CD process by orchestrating various stages of development.Step 4Store the artifacts meant for testing and production release securely in Amazon S3.Step 5Test the artifacts by deploying them to emulated environment and a test group of physical devices. Emulated environments can be created using emulators such as Quick Emulator (QEMU) and Arm Virtual Hardware (AVH) on Amazon Elastic Compute Cloud (Amazon EC2). Use thing groups from AWS IoT Core to organize the test devices for testing.Step 6Devices receive over-the-air (OTA) updates from AWS IoT Core and securely download the necessary artifacts from Amazon S3 using pre-signed URLs or MQTT file streams. They then update the firmware or software and report the status back to AWS IoT Core. The machine builder verifies the update for improved security, usability, reliability, and functionality and then approves it.Step 7Deploy approved artifacts to all devices with configurable rollout rates and schedules, and monitor continuously during and after deployment.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The AWS IoT suite of services provides comprehensive capabilities for securely managing smart industrial products. AWS IoT Device Management enables just-in-time provisioning and orchestration of over-the-air software updates. The component-based AWS IoT Greengrass allows seamless extension and customization of edge applications, with device health monitored through local diagnostics and Amazon CloudWatch. The AWS IoT SiteWise service enables monitoring of data collection, processing, and storage, offering bulk operations to adapt information models at scale. Additionally, AWS IoT Core integrates with CloudWatch to monitor device health and provides automated responses to address operational issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS IoT Core secures device communication with authentication, encryption, and granular permissions. AWS IoT SiteWise and Amazon Simple Notification Service (Amazon S3) encrypt data at rest. AWS IoT Device Defender continuously monitors devices for anomalies and vulnerabilities. Lastly, Security Hub aggregates and prioritizes alerts from across services, providing a holistic view of your security posture. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The suite of services for AWS IoT Core are designed for reliability, with features to handle intermittent connectivity and data resiliency. For example, AWS IoT Greengrass allows processing at the edge even without cloud access, while AWS IoT SiteWise provides throttling to maintain service availability. AWS IoT SiteWise enables backup of asset data to Amazon S3, and AWS IoT Core replicates device information across Availability Zones. AWS IoT Device Management offers capabilities for reliable over-the-air updates. Underpinning the platform, Amazon S3 provides 99.9999999% (11 nines) availability, with cross-Region replication for enhanced data protection. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services used in this Guidance offer flexible options for ingesting and storing industrial telemetry data. Specifically, AWS IoT SiteWise offers hot, warm, and cold storage tiers to optimize performance and cost, while the AWS IoT SiteWise Edge capability enables low-latency local processing. Amazon S3 storage classes can be selected to match specific performance needs, with multipart uploads improving transfer speeds for large datasets. SageMaker allows configurable inference scheduling to optimize prediction performance based on asset criticality and service level agreements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS IoT Core provides cost optimization capabilities across its suite of services. For example, AWS IoT SiteWise offers differentiated storage tiers and edge processing to reduce data transfer needs, while AWS IoT Greengrass filters and aggregates data locally before cloud ingestion. The pay-as-you-go AWS IoT Core pricing, along with its Basic Ingest feature, further lowers messaging costs. Amazon S3 helps optimize storage expenses through tiered classes and intelligent tiering based on access patterns. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS IoT SiteWise offers an Edge component to filter incoming data locally and a retention period setting to automatically remove older data from hot or warm storage tiers no longer needed. The scalable AWS IoT Core service can support billions of assets and trillions of messages. This allows you to scale your Internet of Things (IoT) products up or down based on demand. Furthermore, IoT rules enable filtering and transformation to reduce storage and processing requirements. Amazon S3 provides lifecycle configuration to transition objects between storage classes and delete expired data, while Amazon Redshift Spectrum allows querying Amazon S3 data directly without the need to load it. Additionally, the inference recommender in SageMaker helps optimize resources used for model inferencing, reducing overall consumption. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Building Smart Industrial Machines with AWS: A Comprehensive Guide**: This blog demonstrates how AWS IoT managed services can accelerate your transformation into a smart industrial leader.

[Read the blog](https://aws.amazon.com/blogs/iot/building-smart-industrial-machines-with-aws-iot-a-comprehensive-guide/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
