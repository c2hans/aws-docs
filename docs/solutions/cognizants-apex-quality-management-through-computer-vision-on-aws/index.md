---
source_url: https://docs.aws.amazon.com/solutions/cognizants-apex-quality-management-through-computer-vision-on-aws/index.html
---

---
title: 'Guidance for Cognizant''s APEx Quality Management through Computer Vision on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/cognizants-apex-quality-management-through-computer-vision-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Cognizant's APEx Quality Management through Computer Vision on AWS

## Overview

This Guidance helps you reduce the time required to set up an in-plant computer vision (CV) quality detection system. It provides workflows and interfaces that enable quality subject matter experts to train CV models so that you don’t have to procure expensive data scientists. The architecture includes a series of interfaces for one-touch gateway onboarding, which eliminates the need for specialized personnel to set up, deploy, and manage the gateways and CV models. The architecture also uses edge technology, machine learning (ML), and user interfaces to initiate quality inference, orchestrate gateway deployments, calculate key performance indicators (KPIs), and visualize data through dashboards.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/cognizants-apex-quality-management-through-computer-vision-on-aws.pdf)

![Architecture diagram](/images/solutions/cognizants-apex-quality-management-through-computer-vision-on-aws/images/cognizants-apex-quality-management-through-computer-vision-on-aws-1.png)

1. **Step 1**: An industrial camera is used to capture product images which are stored on the edge device for the CV use case.
1. **Step 2**: The captured images are routed through the Dispatcher to the appropriate Compiled Quality Model for inference.
1. **Step 3**: The result of the inference is stored on the gateway with AWS IoT Greengrass Stream Manager and combined with other near real-time data and calculations to generate overall equipment effectiveness (OEE) and other operational metrics and identify quality issues. This is available to view in the factory through the Visualization layer.
1. **Step 4**: Near real-time data is collected from the machinery, typically from an Industrial Programable Logic Controller (PLC), using built-in connectors, like AWS IoT SiteWise Edge Data Collection Pack, or custom Protocol Adapters, and stored on the gateway.
1. **Step 5**: Operational metrics, as configured in the cloud interface, are calculated based on near real-time data, inferences, and results from the Advanced Aggregation function in the AWS IoT SiteWise Edge Data Processing Pack.
1. **Step 6**: Additional Advanced Aggregations are calculated based on Operational Technology (OT) system configurations and shift schedules and stored on the edge device. The PostgreSQL Container will manage this data on the edge.
1. **Step 7**: Data and aggregations, as configured, are transferred from the edge device to AWS IoT SiteWise for enterprise-level views and additional data analysis. AWS IoT Core handles data requiring immediate actions. Advanced calculations, advanced alarming, and other backend services are deployed as containers in Amazon Elastic Kubernetes Services (Amazon EKS). Amazon Relational Database Service (Amazon RDS) stores event, operational, and configuration data.
1. **Step 8**: The container-based business logic and configuration data can be replicated to the edge environment and orchestrated through AWS IoT Greengrass to provide the same functionality while reducing undifferentiated heavy lifting in maintaining multiple code bases. Supporting features include: a) S3 Component Sync to synchronize data between the edge device and cloud, including stored images when model re-training is requested, b) Health Monitor to surface issues on the gateway, such as connectivity and downloaded modules, c) Command Module to orchestrate actions between the cloud and edge device, such as requests to send stored images to the cloud, and d) Secret and Shadow Manager and Amazon SageMaker Edge Manager, which are AWS-provided components.
1. **Step 9**: Even if cloud connectivity is lost, users can view the operational data, quality results, and custom dashboard on the edge through features such as Asset Nav, an Operational Dashboard, and KPIs and Models.
1. **Step 10**: The simplified user interface (UI) helps train ML models, manage gateway deployments and enterprise operational performance, and reduce the complexity and personas required to provision a gateway in the factory. Plant managers can use the UI to monitor KPIs in their own plants or enable an organization-wide view of metrics. Process managers can explore quality KPIs and issues on a per-line basis and examine the results of a particular part. IT engineers can train models and associate the models to particular manufacturing lines or gateways. Amazon SageMaker Edge Manager facilitates the model deployment to the specific gateway.
1. **Step 11**: Process or quality engineers train new models by requesting images from the edge device through the S3 Component Sync (custom AWS IoT Greengrass component), and storing the images in Amazon Simple Storage Service (Amazon S3). An intuitive interface, powered by Amazon SageMaker Ground Truth, is used to identify good or bad part images and annotate defects.
1. **Step 12**: Amazon EventBridge, AWS Lambda, and Amazon Simple Queue Service (Amazon SQS) orchestrate a series of processes executed in Amazon EKS to automatically train the CV model with Amazon SageMaker and compile and package the model for the edge with Amazon SageMaker Neo. The model is version-controlled and available for deployment to the gateway. Based on the customer use case, Amazon Lookout for Vision can be used for model training.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

KPI and summary dashboards are a feature of this Guidance. The dashboard displays metrics such as OEE and the number of good and bad parts from the images. You can use this dashboard to examine your manufacturing operations and determine whether you are achieving expected outcomes. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The edge-to-cloud communications use security mechanisms provided by AWS, including X.509 certificates for mutual transport layer security (mTLS) and bi-directional encryption of traffic. AWS Identity and Access Management (IAM) roles are used for deployment, and interservice communications are configured following the principle of least privilege access. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses managed services, which are highly available by design. The in-plant gateway is not highly available, but the Gateway Management feature provides one-touch gateway onboarding, enabling a low recovery time objective (RTO). You can configure what data to back up and where to store that data. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Services in this Guidance were selected to reduce the undifferentiated heavy lifting for the end user while operating the solution. For example, AWS IoT SiteWise is used to collect, store, and process incoming data in near real time. This allows you to focus on KPIs important to your business rather than the underlying technology of ingesting data. AWS IoT SiteWise Edge enables the same business logic that operates in the cloud to be deployed to the edge device. This reduces efforts to maintain multiple disparate systems. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

When choosing services for this Guidance, we considered the overall costs of maintaining the architecture, not just the costs for operating a service. For example, although AWS IoT SiteWise Edge has a significant monthly cost, this service will help you save on costs related to customer development, support, and maintenance. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses a combination of managed services and services that elastically scale based on demand. As managed services, AWS IoT Core, AWS IoT SiteWise, and Amazon S3 provide compute and storage on demand. Amazon EKS is configured to scale up and down based on usage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
