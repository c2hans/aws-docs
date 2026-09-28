---
source_url: https://docs.aws.amazon.com/solutions/building-a-sap-cloud-data-warehouse-on-aws/index.html
---

---
title: 'Guidance for Building a SAP Cloud Data Warehouse on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-sap-cloud-data-warehouse-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Building a SAP Cloud Data Warehouse on AWS

## Overview

This Guidance shows how to extract data and business logic from SAP systems to build a data warehouse that integrates the business context and logic embedded within the SAP system. Users can select functional areas such as Order-to-Cash (including customers, sales orders, customer deliveries, and invoices) and Procure-to-Pay (including vendors, purchase orders, good receipts, and vendor invoices). Included are AWS CloudFormation templates that deploy the required data models, translating the technical data architecture into business-friendly terms and relationships. Additionally, this Guidance provides near real-time, simple, and adaptable data pipelines, with incremental change data capture (CDC) processes, conversion rules, and automatic inclusion of custom fields. This comprehensive approach delivers high-quality, contextual data to enable the creation of reports and the performance of advanced analytics with SAP and non-SAP data at speed, supporting data-driven decision making.

## How it works

### Overview

This architecture diagram shows how to build a cloud data warehouse on AWS by extracting data from SAP using the OData protocol. You can use the data warehouse to model and combine SAP data with that of other sources loaded into the data warehouse. The next two tabs show metadata replication and data marts, respectively.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-a-sap-cloud-data-warehouse-on-aws.pdf#page=1)Step 1Configure operational data provisioning (ODP) for extraction in the SAP Gateway of your SAP system.Step 2Create the OData system connection from Amazon AppFlow to your SAP source system. This is through AWS PrivateLink for SAP on AWS. You can connect with AWS through a virtual private network (VPN), AWS Direct Connect, or over the internet.Step 3In Amazon AppFlow, create the flow using the SAP source created in step 2. Run the flow to extract data from SAP and save it to an Amazon Simple Storage Service (Amazon S3) bucket.Step 4Use an AWS Glue crawler to create a data catalog entry with metadata for the extracted SAP data in an Amazon S3 bucket.Step 5Load data into Amazon Redshift through simple 'COPY' commands. Model the data with other non-SAP sources in your data warehouse.Step 6Create the dataset in Amazon QuickSight with Amazon Redshift as the data source.Step 7Create a dashboard to visualize the business data according to user requirements. Use inbuilt machine learning (ML) and insight features to help enable speed to insight.Step 8Deploy AWS Step Functions for overall orchestration and alerting of your data pipelines and processes.Step 9The generative BI capabilities of Amazon Q within Amazon QuickSight offer insights from the data.### SAP metadata replication

This architecture uses Amazon Lambda and SAP OData to replicate metadata and create Amazon Redshift Data Definition Language (DDL) tables. A Python script with PyOdata queries SAP OData sources and generates DDL to create tables in Amazon Redshift and the AWS Glue Data Catalog.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-a-sap-cloud-data-warehouse-on-aws.pdf#page=2)Step 1Configure ODP for extraction in the SAP Gateway of your SAP system.Step 2Configure and run the SAP Metadata Replication AWS Lambda function.Step 3Lambda retrieves the SAP credentials from AWS Secrets Manager.Step 4Lambda reads the config file from Amazon S3.Step 5Lambda creates Data Definition Language (DDL) statements and runs them in Amazon Redshift.Step 6Lambda creates AWS Glue tables in the AWS Glue Data Catalog.### Amazon Redshift data marts

This architecture diagram illustrates how the Redshift data mart layers are used. With the Slowly Changing Dimension Type 2 (SCD2) data modeling technique, you have the full history of your data movements that you can query.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-a-sap-cloud-data-warehouse-on-aws.pdf#page=3)Step 1The corporate memory layer contains all SAP extracted data in Amazon S3.Step 2The operational data store layer is used to temporarily hold the data until the data is loaded into the Data Mart (DM) and the architected data mart (ARCHDM) layers.Step 3The propagation layer includes the Slowly Changing Dimension Type 2 (SCD2) tables or tables that will contain the entire history of changes.Step 4The virtual data mart layer provides the presentation layer through the use of materialized views in Amazon Redshift.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-sap-order-to-cash-data-analytics-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Observability is derived from the managed services used for data processing, with process-level metrics, logs, and dashboards available through Amazon CloudWatch. These services provide valuable insights into your operations, enabling the continuous improvement of your underlying processes and procedures. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The managed services used in this Guidance are granted access only to the specified data, with access to the SAP workload facilitated through Amazon AppFlow, which supports PrivateLink to create private data flows between AWS services. Data is encrypted both in transit and at rest, and data stored in Amazon S3 is secured from unauthorized access through the use of encryption features and access management tools. Moreover, the Amazon Redshift data warehouse cluster is isolated within your virtual private cloud (VPC). These services support robust security measures, as the serverless components within the architecture are protected through AWS Identity and Access Management (IAM)-based authentication for secure validation of user identities. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon AppFlow is capable of handling large data volumes without the need to break them down into multiple batches, thereby enhancing the overall reliability of the data transfer process. Furthermore, Amazon Redshift offers several features, such as multi-Availability Zone (AZ) deployment, that serve to bolster the reliability of the data warehouse cluster. Amazon Redshift also continuously monitors the health of your system, automatically replicating data from failed drives and replacing nodes as necessary for fault tolerance. Lastly, all the serverless components in this Guidance are designed to be highly available, while the non-SAP components allow for automatic scaling. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

By using Amazon S3 for the corporate data memory, the storage capabilities of this Guidance are optimized. The processing of the data is then performed within the Amazon Redshift environment. Additionally, to enhance performance and agility, multiple flows are configured in Amazon AppFlow for the different groups of business data. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using serverless technologies, you pay only for the resources you use. To further optimize cost, extract only the business data group you need and minimize the number of flows being run based on the granularity of your reporting needs. Notably, the Amazon S3 Lifecycle configuration policies allow you to manage the objects so that they're stored cost-effectively throughout their lifecycle. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

With managed services and dynamic scaling, you minimize the environmental impact of the backend services. As new features or capabilities become available for Amazon AppFlow, consider adopting those updates so that the data warehouse can continuously improve its efficiency and performance and meet your evolving business needs over time. Lastly, reducing the quantity and frequency of extraction improves sustainability, helps reduce cost, and improves the overall performance of your workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Build an SAP Data Lake and Deliver New Business Insights**: This workshop demonstrates how to solve common business problems using native AWS services in conjunction with SAP applications.

[Learn more](https://catalog.us-east-1.prod.workshops.aws/workshops/6069af4b-2628-49ed-b297-e7f0f94958ee/en-US)

- **Extend RISE with SAP on AWS with Analytics Fabric for SAP Accelerators**: This blog post demonstrates how all SAP on AWS customers can turn SAP data into actionable insights within hours by using the AWS Analytics Fabric for SAP solution, and eliminate the burden of identifying AWS services and reduce build efforts by up to 90%.

[Learn more](https://global.staging.iad.prod.content-server.marketing.aws.dev/blogs/awsforsap/extend-rise-with-sap-on-aws-with-analytics-fabric-for-sap-accelerators/)

- **Modernize your SAP Accounts Payable reporting with an AWS Data Lake and AI/ML services**: This workshop demonstrates how to leverage AWS Generative AI service to use generative AI based queries to ask questions to find and solve problemes, and auto create reports.

[Learn more](https://catalog.us-east-1.prod.workshops.aws/workshops/56e3509f-70d9-43f7-a0b6-b74295b606f7/en-US)

- **Unlock procure-to-pay insights in SAP data with generative AI from AWS**: This video explains how to use generative AI services from AWS to accelerate decision-making across Procure-to-Pay and other key financial and supply chain processes running in SAP.

[Learn more](https://youtu.be/Kpn-SXKuDa4)

[Read usage guidelines](/solutions/guidance-disclaimers/)
