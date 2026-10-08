---
source_url: https://docs.aws.amazon.com/solutions/data-federation-between-sap-and-aws/index.html
---

---
title: 'Guidance for Data Federation between SAP and AWS'
canonical_url: https://docs.aws.amazon.com/solutions/data-federation-between-sap-and-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Data Federation between SAP and AWS

## Overview

This Guidance outlines the process of federating data between SAP and AWS cloud analytics services, enabling you to establish a data mesh architecture. SAP provides enterprise software for running business processes, from enterprise resource planning to customer relationship management. By connecting SAP with AWS, you can easily transform and visualize your data in a scalable, secure, and cost-effective way, helping you inform your decision-making.

## How it works

This architecture diagram shows how to federate data between SAP and AWS cloud analytics services, enabling you to establish a data mesh architecture

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/data-federation-between-sap-and-aws.pdf)

![Architecture diagram](/images/solutions/data-federation-between-sap-and-aws/images/data-federation-between-sap-and-aws-1.png)

1. **Step 1**: Data from SAP S/4HANA, SAP SuccessFactors, SAP Digital Manufacturing Cloud (DMC), and other SAP systems are replicated or virtualized into SAP Datasphere. A business semantic layer is created in SAP Datasphere.
1. **Step 2**: Data from commercial off-the-shelf applications, like Salesforce and Adobe Marketing Cloud, or full-stack applications and Internet of Things (IoT) devices is extracted, loaded into Amazon Simple Storage Service (Amazon S3), and transformed through Amazon Athena as tables and views.
1. **Step 3**: Data in Athena is accessed from SAP Datasphere through data federation from SAP Datasphere connections. Your users can also access SAP Datasphere tables and views from Athena by querying SAP HANA using an Athena Federated Query.
1. **Step 4**: Data from Athena can be federated to the SAP HANA Cloud by configuring Athena as a remote source using the Smart Data Access - Athena adapter. The Athena Federated Query connection can also be used to read data from a stand-alone SAP HANA Cloud environment.
1. **Step 5**: Data federation from Amazon Redshift into SAP Datasphere is possible with SAP HANA Smart Data Integration (SDI) or the SAP Data Provisioning Agent. Install and configure this agent to federate Amazon Redshift data into SAP Datasphere. Amazon Redshift data can also be federated through the Athena Federated Query data source connector.
1. **Step 6**: Your users can access the storyboards in SAP Analytics Cloud using SAP and non-SAP data from SAP Datasphere. Similarly, you can use Amazon Q in QuickSight to visualize SAP and non-SAP data using data federation.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch monitors the AWS Lambda functions for Athena Federated Queries as they pull data from SAP HANA in real time. AWS CloudTrail then logs all the API requests when SAP Datasphere pulls data from Athena. Together, these services provide visibility so that you can review any errors and appropriately respond to incidents. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Secrets Manager stores SAP HANA Cloud and SAP Datasphere access credentials for Athena. SAP Datasphere uses AWS Identity and Access Management (IAM) permission controls and programmatic access to federate data from Athena into SAP Datasphere. Additionally, SAP Datasphere uses Java Database Connectivity to access Amazon Redshift. Working together, these services use key rotation, minimum-permission policies, and other security guardrails to maintain fine-grained access control to critical business data. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses serverless components, which maintain high availability to help you support your business-critical analytics applications. For example, Athena implements queries using compute resources across multiple facilities and automatically reroutes queries in the case of failure. Additionally, Amazon S3 provides 99.999999999 percent durability, and you can enhance availability for this Guidance through Amazon Redshift Reliability and by deploying it across multiple Availability Zones. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Athena provides a number of performance optimization techniques, including query optimizations and data partitioning. It also lets you use a variety of file formats (such as Apache Parquet or Apache Optimized Row Columnar) for optimum access. Additionally, Amazon Redshift provides performance tuning options such as massively parallel processing, data compression, query optimization, and data compression. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses serverless services such as Athena, Amazon S3, and Amazon Redshift, which bill for only the resources you use. Serverless services automatically scale up and down based on demand, so you can avoid the cost of overprovisioning resources to support peak demand. Additionally, SAP HANA Cloud provides high price performance by using AWS Graviton processors. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using managed services and dynamic scaling through services like Athena and Amazon S3, you can minimize the environmental impact of the backend service. Serverless infrastructure automatically scales up and down to match demand, so you can avoid the energy expenditure of overprovisioning hardware. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Accessing data in Amazon S3 from SAP Datasphere**: This SAP Mission demonstrates the necessary information and steps of how to access data living in Amazon S3 from SAP Datasphere.

[Learn more](https://discovery-center.cloud.sap/missiondetail/3403/3443/)

- **Data Federation from Amazon Redshift through SAP Datasphere**: This SAP Mission demonstrates how integrating SAP Datasphere and Amazon Redshift though data federation can augment the non-SAP data in Amazon Redshift with SAP data in SAP Datasphere and build unified data models.

[Learn more](https://discovery-center.cloud.sap/missiondetail/3406/3446/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
