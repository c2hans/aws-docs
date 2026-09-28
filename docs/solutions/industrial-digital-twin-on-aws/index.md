---
source_url: https://docs.aws.amazon.com/solutions/industrial-digital-twin-on-aws/index.html
---

---
title: 'Guidance for Industrial Digital Twin on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/industrial-digital-twin-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Industrial Digital Twin on AWS

## Overview

This Guidance provides a set of artifacts that will guide customers in building a production monitoring architecture with AWS IoT TwinMaker and supporting services. The artifacts in this Guidance provide sample demo projects, data simulators, and articles that offer support for using various feature sets within AWS IoT TwinMaker and AWS IoT SiteWise. With AWS IoT TwinMaker, customers can get a 3D model of their plant operations derived from computer-aided design (CAD) or reality capture models, such as Matterport. Using AWS IoT TwinMaker’s Knowledge Graph, customers can view relationships between industrial assets and operations.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/industrial-digital-twin-on-aws.pdf)

![Architecture diagram](/images/solutions/industrial-digital-twin-on-aws/images/industrial-digital-twin-on-aws-1.png)

1. **Step 1**: AWS IoT SiteWise deploys a gateway to the edge. An Open Platform Communications Unified Architecture (OPC UA) endpoint is configured on this gateway to stream telemetry data to AWS IoT SiteWise.
1. **Step 2**: Industrial Programmable Logic Controllers (PLC), supervisory control and data acquisition (SCADA), historian, or input/output (I/O) servers can provide access to near-real-time data through the standard OPC UA protocol. AWS IoT SiteWise can subscribe to or poll these endpoints to collect data.
1. **Step 3**: Data simulation or cloud-hosted business systems can publish data through AWS IoT SiteWise APIs for storage.
1. **Step 4**: AWS IoT SiteWise contains template asset models, asset instances of those models, properties, and an asset hierarchy. A timeseries data store managed within the service can serve at enterprise-level.
1. **Step 5**: AWS IoT TwinMaker provides an immersive 3D view of your systems and operations to optimize efficiency, increase production, and improve performance. AWS IoT TwinMaker supports the use of data connectors to access information trapped in silos and provides a managed digital twin graph.
1. **Step 6**: AWS IoT TwinMaker Asset Synchronization enables built-in sync with AWS IoT SiteWise. Any changes to your assets are automatically updated within your digital twin.
1. **Step 7**: You can access your digital twin from Amazon Managed Grafana or a self-managed installation. With IoT App Kit, AWS IoT TwinMaker also supports React applications and third-party AWS Partner solutions.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-industrial-digital-twin-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS CloudFormation enables end users to automate and standardize infrastructure deployment, helping ensure consistent AWS resource provisioning for AWS IoT SiteWise, AWS IoT TwinMaker, and other supporting services. This helps you minimize manual errors and operational drift for simulation and brewery demonstration environments. GitHub streamlines code changes and responses to events with features like GitHub Actions and near-real-time notifications. Together, CloudFormation and GitHub bolster operational excellence by automating workflows, swiftly reacting to system events, and maintaining standardized operations. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) allows precise control over user and service permissions to permit only authorized access to resources and to maintain data confidentiality and integrity. IAM roles allow access from Grafana on the AWS IoT TwinMaker Workspace that are in line with the AWS IoT TwinMaker service documentation. Amazon Elastic Compute Cloud (Amazon EC2) instances for simulation are assigned an IAM instance role with access to AWS Systems Manager to support up-to-date patching. Systems Manager provides tools for consistent configuration management, patching, and auditing of resources, enhancing system and data protection. IAM and Systems Manager bolster security by offering granular access controls and a suite of management tools to detect and respond to security events. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

With AWS IoT SiteWise and AWS IoT TwinMaker, throttling limits are in place for data ingress and egress to assure continued operation. With the Managed Grafana console, you’ll have access to a workspace to visualize and analyze metrics, logs, and traces without having to build, package, or deploy any hardware or infrastructure. Managed Grafana automatically provisions, configures, and manages the operations of the workspace with automatic version upgrades. The service auto scales to meet dynamic usage demands. This is critical for handling peak usage during site operations or the start of a shift for industrial operations. As part of this Guidance, a self-managed Grafana instance is used for testing purposes. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This architecture enables organizations to scale the deployment of their industrial digital twins across multiple sites within throttling limits. AWS Regions are configurable in the CloudFormation templates, supporting global deployments where data sovereignty requirements exist. As the number of connected assets grow, the architecture can help assure that it will scale with this growth and remain performant. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS IoT SiteWise and AWS IoT TwinMaker are cost-optimized, managed services that provide customers with digital twin capabilities at the lowest possible price point. AWS IoT SiteWise and AWS IoT TwinMaker pricing is pay-as-you-go, which means you are charged only for the data that is ingested, stored, and queried. AWS IoT SiteWise contains optimized storage settings that can be configured to move data from a hot tier to cold tier in Amazon Simple Storage Service (Amazon S3). For the simulation, the scripts have been optimized to enable them to run on a t2.micro instance. This is available on the AWS Free Tier so you can explore the Guidance prior to connecting real sensor data streams. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

With AWS IoT SiteWise, you can apply a deadband to your OPC-UA source property groups to filter out and discard certain data instead of sending it to the AWS Cloud. A deadband specifies a window of expected fluctuations in the incoming data values from your OPC-UA source. If the values fall within this window, your OPC-UA server won't send it to the AWS Cloud. You can use deadband filtering to reduce the amount of data you're processing and sending to the AWS Cloud. In addition, the AWS IoT SiteWise cold tier uses Apache Parquet format in Amazon S3. It is an open source, column-oriented data file format designed for efficient data storage and retrieval. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
