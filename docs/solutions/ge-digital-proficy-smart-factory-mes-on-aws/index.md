---
source_url: https://docs.aws.amazon.com/solutions/ge-digital-proficy-smart-factory-mes-on-aws/index.html
---

---
title: 'Guidance for GE Digital Proficy Smart Factory MES on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/ge-digital-proficy-smart-factory-mes-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for GE Digital Proficy Smart Factory MES on AWS

## Overview

This Guidance shows how you can drive value by using GE Digital’s [Proficy Smart Factory](https://aws.amazon.com/marketplace/pp/prodview-jru3jqjxt2pom/) manufacturing execution system (MES) with AWS services. GE Digital Proficy Smart Factory is a Software-as-a-Service (SaaS) offering from General Electric (GE) and is available on the AWS Marketplace. Proficy Smart Factory is a powerful operation management offering built to handle multiple uses, such as efficiency, quality, and production management. It also supports batch analysis, scheduling, digital operations, and industrial data management. Proficy Smart Factory spans on-premises, cloud-based MES capabilities and, when used in conjunction with other AWS services, can help you can gain more insights from manufacturing data through machine learning (ML) and predictive analytics.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/ge-digital-proficy-smart-factory-mes-on-aws.pdf)

![Architecture diagram](/images/solutions/ge-digital-proficy-smart-factory-mes-on-aws/images/ge-digital-proficy-smart-factory-mes-on-aws-1.png)

1. **Step 1**: GE Digital Proficy Smart Factory is a Software-as-a-Service (SaaS) offering from General Electric (GE). It is available on the AWS Marketplace. Proficy Smart Factory is a powerful operation management offering built to handle multiple use cases, such as 1/ Efficiency Management 2/ Quality Management 3/ Production Management 4/ Batch Analysis 5/ Scheduling 6/ Digital Operations and 7/ Industrial Data Management. Plant and enterprise users can access the SaaS software through web based user interface. GE Proficy Smart Factory offering provides access to Proficy Suite of Software including GE Proficy Plant Applications, GE Proficy Historian and GE Proficy Operations Hub.
1. **Step 2**: GE Proficy Historian Collectors running on-premises can collect data from a myriad of industrial data sources, such as Programmable Logic Controllers (PLCs), and Internet of Things (IoT) devices. Industrial data sources can include OPC DA/HDA, OPCUA, GE iFIX SCADA software, Proficy Historian, AVEVA PI Historian, MQTT, ODBC, or AWS IoT Core.
1. **Step 3**: GE Proficy Smart Factory can connect to other enterprise systems such, as Enterprise Resource Planning (ERP), Product Lifecycle Management (PLM), Warehouse Management System (WMS) and a Laboratory Information Management System (LIMS) through the GE Proficy Plant Applications.
1. **Step 4**: Establish a centralized data repository on AWS to facilitate enterprise-wide analytics. Use Proficy Smart Factory to provide contextualized data to GE Proficy Manufacturing Data Cloud (Proficy MDC). Use Proficy Historian's Parquet export feature to directly ingest data from Proficy Historian into a data lake powered by AWS Lake Formation, AWS Glue Data Catalog and Amazon Simple Storage Service (Amazon S3).
1. **Step 5**: Use AWS artificial intelligence and machine learning (AI/ML) services such as Amazon Lookout for Equipment, and Amazon SageMaker to build, train, and deploy ML models.
1. **Step 6**: Use AWS analytics services such as Amazon EMR, Amazon Athena, and Amazon Redshift, along with Amazon QuickSight and Amazon Managed Grafana for data processing and visualization.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch can be configured with this Guidance to enhance your operational excellence. GE uses CloudWatch to collect and centralize logs, metrics, and application performance data. The GE Proficy Smart Factory application is managed by GE Digital, and these tools provide the capability to monitor and manage the application and the underlying infrastructure. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Proficy Smart Factory MES authenticates and authorizes application users using a user account and authorization (UAA) service, an open-source identity server project, operated by the Cloud Foundry Foundation. You can integrate your on-premises active directories with this service. This Guidance also encrypts data in transit using TLS for user interfaces, API access, and data collector agents, and it uses AWS Key Management Service (AWS KMS) to encrypt all critical and sensitive data at rest. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

In this Guidance, GE Digital manages the availability and reliability of the SaaS application for a highly available network topology. We do recommend using a reliable and redundant internet connection to maintain access to the application. Finally, resiliency is a shared responsibility between AWS and you. AWS is responsible for the resiliency of the infrastructure running the services in the AWS Cloud. Your responsibility is determined by the AWS Cloud services you configure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

In this Guidance, GE Digital chooses AWS services for use in the SaaS to deliver a well-performing application. For data and analytics integration, you can use an Amazon S3 data lake along with purpose-built industrial AI/ML services. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Proficy Smart Factory is priced on a per line basis, so you pay only for each physical line you bring to the MES system. The data repository cost depends on the amount of data ingested from the MES and scales with the size of the manufacturing line. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

In this Guidance, GE Digital manages the resources for the SaaS application to achieve optimum usage. This Guidance also uses Amazon S3 data lakes, which scale based on data volume. You should use serverless versions of the analytics services when possible so that you will use only the minimum resources required. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
