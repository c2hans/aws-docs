---
source_url: https://docs.aws.amazon.com/solutions/industrial-data-fabric-with-palantir-foundry-technology-on-aws/index.html
---

---
title: 'Guidance for Industrial Data Fabric with Palantir Foundry on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/industrial-data-fabric-with-palantir-foundry-technology-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Industrial Data Fabric with Palantir Foundry on AWS

## Overview

This Guidance demonstrates how to build an Industrial Data Fabric with Palantir Foundry on AWS. Foundry is a software as a service (SaaS) product that harnesses data from various industrial data sources such as enterprise resource planning (ERP), a manufacturing execution system (MES), and data lakes. The data is rapidly integrated with fully automated pipelines and low-code tools that allow you to train and build machine learning models. You can build or customize manufacturing applications supporting everything from shop floor scheduling to a global operations center. Full-featured web applications provide you with real-time visibility, decision-making tools, and the ability to resolve operational decisions.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/industrial-data-fabric-with-palantir-foundry-technology-on-aws.pdf)

![Architecture diagram](/images/solutions/industrial-data-fabric-with-palantir-foundry-technology-on-aws/images/industrial-data-fabric-with-palantir-foundry-technology-on-aws-1.png)

1. **Step 1**: Internet of Things (IoT) data from sensors and programmable logic controllers (PLCs) is ingested using AWS IoT Greengrass and sent to AWS IoT SiteWise. You can build assets and dashboards in AWS IoT SiteWise.
1. **Step 2**: Create rules in AWS IoT Core to stream time series data to Palantir Foundry using Amazon Kinesis Data Firehose. Foundry data connectors in the AWS Cloud are used to ingest data from the operational technology (OT) data lake stored in Amazon Simple Storage Service (Amazon S3) to Foundry.
1. **Step 3**: Foundry has data connectors that can ingest data from other data sources such as enterprise resource planning (ERP), a manufacturing execution system (MES), and data lakes.
1. **Step 4**: Data from the connectors is rapidly integrated with fully automated pipelines and low-code tools.
1. **Step 5**: The Foundry Ontology harmonizes data from the semantic elements (such as objects, properties, and links), and kinetic elements (such as actions, functions, and dynamic security).
1. **Step 6**: Install the Foundry software development kit (SDK) in Amazon SageMaker Notebooks that offers fully managed Jupyter Notebooks. Configure Foundry API keys to access Foundry datasets and Ontology objects.
1. **Step 7**: Use datasets from Foundry to train and build machine learning (ML) models in Amazon SageMaker. Models hosted in AWS can be imported or invoked remotely in Foundry workflows.
1. **Step 8**: Build or customize manufacturing applications supporting everything from shop floor scheduling to a global operations center. Full-featured web applications provide you with real-time visibility, decision-making tools, and the ability to resolve operational decisions.
1. **Step 9**: Operational decisions and results can be written back to the source system, ensuring consistency across Product Lifecycle Management (PLM), ERP, MES, and other key systems.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

As your operations evolve over time, you can implement changes within this Guidance so that you can establish a continuous cycle of improvement. With Amazon CloudWatch, you have system-wide visibility into your cloud resources. Configure CloudWatch alarms so that you can collect, monitor, act, and analyze any breaches in the thresholds you set. The services in this Guidance can also be deployed across multiple Availability Zones to ensure that your applications can withstand the rare, but possible, event of a complete Availability Zone failure. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

When deploying this Guidance, all data in transit is encrypted using SSL and data at rest is encrypted using AWS Key Management Service (AWS KMS). This Guidance also uses a SAML-based authentication and authorization standard for any users. Foundry uses role-based access with auditing enabled when accessing services and machines. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

To ensure a highly available network topology, this Guidance uses Amazon S3 to store data. Any applications running on Amazon Elastic Compute Cloud (Amazon EC2) are deployed across three Availability Zones to improve availability and fault tolerance. Foundry implements logging for any customer actions and workflows so that you are notified when thresholds are crossed or significant events occur. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance scales the compute nodes that are needed to perform the task to meet the workload requirements of various traffic and data access patterns. In addition, it uses purpose-built storage services, such as Amazon S3, that reduces latency, increases throughput, and is highly scalable. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

There are various ways this Guidance was designed to reduce cost. Amazon S3 Intelligent-Tiering storage class automates storage cost savings by moving data when patterns change. And, by using Amazon EC2 Instance Savings Plans, you can take advantage of a flexible pricing model that can reduce your on-demand bill in exchange for a one- or three-year hourly spend commitment. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses AWS Auto Scaling to help monitor applications and adjust capacity so that you maintain performance with only the minimum resources required. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
