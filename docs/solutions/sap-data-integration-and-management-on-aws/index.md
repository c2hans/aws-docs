---
source_url: https://docs.aws.amazon.com/solutions/sap-data-integration-and-management-on-aws/index.html
---

---
title: 'Guidance for SAP Data Integration and Management on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/sap-data-integration-and-management-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for SAP Data Integration and Management on AWS

## Overview

This Guidance provides the essential data foundation for empowering customers to build data and analytics solutions. It shows how to integrate data from SAP ERP source systems and AWS in real-time or batch mode, with change data capture, using AWS services, SAP products, and AWS Partner Solutions. This Guidance includes an overview reference architecture showing how to ingest SAP systems to AWS in addition to five detailed architectural patterns that complement SAP-supported mechanisms (such as OData, ODP, SLT, and BTP) using AWS services, SAP products, and AWS Partner Solutions.

## How it works

### Overview of Architecture Patterns

This reference architecture shows various options for ingesting data from SAP systems to AWS. These architecture patterns complement SAP supported mechanisms using AWS Services, SAP Products, and AWS Partner Solutions. For detailed architecture patterns, open the other tabs.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/sap-data-integration-and-management-on-aws-v2.pdf#page=1)Step 1SAP Data hosted in SAP RISE, HANA Cloud, on-AWS or on-premises systems can be extracted in real-time or batch, full or incremental mode from SAP NetWeaver systems such as SAP ECC, SAP S/4HANA, SAP BW, etc. or SAP HANA Database using following options:
A. AWS Managed Services
B. AWS Partner Solutions with dedicated instance
C. AWS Partner Solution embedded in SAP NetWeaverOption AAWS Glue, a serverless data integration service, offers database-level and application-level data extraction.Option B1AWS Partner Solutions such BryteFlow SAP Data Lake Builder, Theobald Xtract Universal, and Qlik Replicate offer instance-based solutions for comprehensive data ingestion scenarios.Option B2Using SAP native integration, SAP Datasphere, or SAP Data Services sends data to Amazon Simple Storage Service (Amazon S3) or Amazon Redshift.Option B3SAP SLT replication engine supports replicating data to Amazon Relational Database Service (Amazon RDS) using a database connection. AWS Partner Solutions such as Syntax CxLink support streaming data to Amazon S3 and Amazon Kinesis using the ABAP add-on for SLT.Option CAWS Partner Solutions embedded in SAP NetWeaver, such as SNP Glue, offer point-to-point data replication from SAP NetWeaver-based source systems to the AWS Cloud.### AWS Managed Services

This architecture diagram shows how to ingest SAP data to AWS using AWS glue. For the other architecture patterns, open the other tabs.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/sap-data-integration-and-management-on-aws-v2.pdf#page=3)Step 2Data extracted from SAP can land in AWS Services such as Amazon S3, Amazon Redshift, Amazon Kinesis or Amazon RDS, combined with non-SAP data, further processed and analyzed using AWS analytics and GenAI services.### AWS Partner Solution - Theobald Xtract Universal

This architecture diagram shows how to ingest SAP data to AWS using the Partner Solution Theobald Software Xtract Universal.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/sap-data-integration-and-management-on-aws-v2.pdf#page=4)Step 1AWS Glue offers both application and database-level data extraction.
Use following AWS Managed Services options to extract data from SAP:Step 1AConfigure the SAP OData connector using application credentials. Use no-code Zero-ETL to replicate SAP OData services based on CDS views and BW extractors using change data capture. Glue visual ETL can be used for subsequent data transformations.Step 1BSAP OData connector can be used in visual ETL for additional capabilities such as full load, source data filtering, selection of data formats, data processing units, etc. Generated script can be modified for programmatic control.Step 1CUsing database-level extraction, establish a SAP HANA connection in AWS Glue Data catalog using properties such as SAP HANA JDBC URL, VPC, Subnet and Security Group. The AWS Glue ETL job extracts data from a single HANA table or view in a specific schema or by using a custom query from multiple tables, found in one or more schemas. This connector requires a custom design for change data capture. AWS Glue SAP HANA Connector requires a SAP HANA license that allows database-level access. It does not support SAP HANA databases with only runtime licenses or RISE installations.Step 2Once data is available in the landing zone, AWS Glue can perform additional data transformation such as join, union, aggregate, filter, renaming fields, dropping fields, adding timestamps, or custom transform.Step 3AWS Secrets Manager stores credentials. Use AWS Identity and Access Management (AWS IAM) for access management and role configurations.### AWS Partner Solution - Qlik Replicate

This architecture diagram shows SAP ERP connectivity and data integration with Qlik Replicate.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/sap-data-integration-and-management-on-aws-v2.pdf#page=5)Step 1The AWS Partner Solution Xtract Universal (XU), certified by SAP, provides application-level data extraction with change data capture (CDC) to the AWS services. As a pre-requisite install SAP transport of programs THEO_READ_TABLE and THEO_CDC_ECC or THEO_CDC_S4 required for CDC capability.Step 2Theobald Software Xtract Universal (XU) is available as a pre-configured Amazon machine image (AMI) on AWS Marketplace. Follow instructions to configure AMI on an Amazon Elastic Compute Cloud (Amazon EC2) instance.Step 3aFor application-level data extraction via SAP RFC, configure SAP RFC based extraction (10 different SAP source objects).Step 3bFor application-level data extraction via ODP, configure SAP ODP over OData based extraction (5 different SAP source objects). XU supports both OData V2 and V4.Step 4Initial and incremental data is updated in Amazon S3 (append only) or Amazon Redshift/Amazon RDS (upsert). Amazon S3 upsert operations require additional efforts and services, such as Amazon Elastic MapReduce (Amazon EMR) and Amazon Elastic Block Store (Amazon EBS). Data catalog and portioning of the schema is configured.Step 5Theobald Software XU supports AWS IAM, AWS Glue or Apache Airflow (Job scheduling), Amazon CloudWatch, and Amazon Simple Notification Service (Amazon SNS) for security, monitoring and alerts.### AWS Partner Solution - BryteFlow Ingest

This architecture diagram shows how to ingest SAP data to AWS using the AWS Partner Solution BryteFlow SAP Data Lake Builder.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/sap-data-integration-and-management-on-aws-v2.pdf#page=6)Step 1The AWS Partner Solution Qlik Replicate, certified by SAP, provides application and database-level replication with change data capture. Install the R4SAP package on source SAP system as a prerequisite for application-level data extraction. Install Qlik Replicate on an Amazon EC2 instance using the Amazon Machine Image (AMI) from AWS Marketplace.Step 1aQlik Replicate supports application-level data extraction with SAP OData services for BW extractors, CDS views, Info views, and iDocs.Step 1bQlik Replicate supports data extraction directly from SAP ECC and S/4HANA Tables, BAPI, and extractors.Step 1cDatabase-level data extraction (requires a SAP license that allows database access) uses an ODBC connector and a trigger-based mechanism (SAP HANA database) or log-based mechanism (Oracle, SQL, DB2) to replicate data.Step 2Key features include near real-time data replication, broad connectivity, support for schema evolution, replication type (one to one, one to many, many to many, and bidirectional), zero downtime operation, data transformation, and high availability.Step 3For CDC performed on a SAP Application, initial and incremental data ingestion occurs to Amazon S3 (append only) and fast copy to Amazon Redshift/Amazon RDS (insert, update, delete).Step 4Qlik Replicate uses AWS IAM for authentication and access. Configure Amazon CloudWatch for logging, monitoring and alerts.### Using SAP BDC Datasphere, Data Services

This architecture diagram shows how to ingest SAP data to AWS using SAP Datasphere or SAP Data Services.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/sap-data-integration-and-management-on-aws-v2.pdf#page=7)Step 1aFor Application-level data extraction, configure SAP OData Services based on CDS Views, BW Extractors, BW InfoProviders, or HANA information views for data extraction.Step 1bDatabase-level data extraction (requires SAP license that allows database access) uses a trigger-based (SAP HANA database) or log-based mechanism (Oracle, SQL, DB2) to replicate data.Step 2AWS Partner Solution BryteFlow SAP Data Lake Builder provides application and database level SAP data extraction with change data capture to AWS Cloud.
BryteFlow SAP Data Lake Builder is available as pre-configured AMI on AWS Marketplace. Follow instructions to configure the AMI in the EC2 instance.Step 3BryteFlow SAP Data Lake Builder software running on Amazon EC2 instance ingests the captured initial and changed data and delivers to AWS Analytics Services.
Append and upserts to Amazon S3, Amazon Redshift and Amazon RDS are supported. Amazon S3 upsert operations need additional Services (Amazon EMR and Amazon EBS). Data catalog and portioning of the schema is configured.Step 4BryteFlow SAP Data Lake Builder uses AWS IAM, AWS KMS, AWS CloudWatch, and Amazon SNS for security, monitoring, and alerts.### Using SLT

This architecture diagram shows how to ingest SAP data to AWS using SAP SLT.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/sap-data-integration-and-management-on-aws-v2.pdf#page=8)Step 1Extract data from SAP ERP hosted in RISE, on AWS, or on-premises using:
A. SAP Datasphere
B. SAP Data ServicesStep 2aSAP BDC Datasphere offers various connection types such as SAP ABAP Connections, SAP ECC Connections, and SAP S/4HANA Cloud Connections supporting RFC and ODP protocols. Refer to SAP Datasphere documentation to choose the most appropriate connectivity to extract SAP data.Step 2bUsing premium outbound integration for Amazon Simple Storage Connection, configure the SAP Datasphere replication flow to ingest data to Amazon S3.Step 3aInstall SAP Data Services on an Amazon EC2 instance or on-premises.Step 3bSAP Data Services offers various connections to extract data from SAP ECC data. Refer to SAP Data Services documentation to choose the most appropriate connectivity.Step 3cSAP Data Services offers Amazon Redshift Datastore and Amazon S3 datastore to ingest data to AWS.Step 3dSAP Data Services offers options for Amazon S3 file location protocol such as encryption type, compression type, batch size, number of threads, Amazon S3 storage class, etc.### SNP GLUE, an SAP NetWeaver Add-On Solution by SNP

This architecture diagram shows how to use SAP NetWeaver add-on solution SNP Glue to extract data from SAP to AWS.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/sap-data-integration-and-management-on-aws-v2.pdf#page=9)Step 1Configure RFC destination in SAP SLT to source SAP ERP system.Step 2Configure SAP SLT database connection to the destination Amazon RDS server using host name, username and password. Configure the SAP SLT mass transfer ID to replicate tables (initial and incremental data) in real-time or scheduled frequency to Amazon RDS.Step 3Perform insert, update, and delete operations to Amazon RDS, which can operate as a landing zone for subsequent data loads to Amazon S3 or Amazon Redshift.Step 4For data replication to Amazon S3 or Amazon Kinesis, install an AWS Partner Solution ABAP add-on such as Syntax CxLink Data Lakes on the SAP SLT Server.Step 5Syntax CxLink Data Lakes replicates data in real-time or scheduled frequencies to Amazon S3 or Amazon Kinesis. Incremental data is appended to existing data.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS CloudFormation automates the deployment process, while CloudWatch provides observability, tracking, and tracing capabilities. The entire solution can be deployed using CloudFormation, which helps automate deployments across development, quality assurance, and production accounts. This automation can be integrated into your development pipeline, enabling iterative development and consistent deployments across your SAP landscape. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM secures AWS Glue and Amazon AppFlow through permission controls and authentication. These managed services access only specified data. Amazon AppFlow facilitates access to SAP workloads. Data is encrypted in transit and at rest. AWS CloudTrail logs API calls for auditing. S3 buckets and cross-region replication can store data. For enhanced security, run Amazon AppFlow over AWS PrivateLink with Elastic Load Balancing and SSL termination using AWS Certificate Manager. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon AppFlow and AWS Glue can reliably move large volumes of data without breaking it down into batches. Amazon S3 provides industry-leading scalability, data availability, security, and performance for SAP data export and import. PrivateLink is a regional service, and as part of the Amazon AppFlow setup using PrivateLink, you will set up at least 50 percent of Availability Zones in the Region (minimum two Availability Zones per Region), providing an additional level of redundancy for ELB. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The SAP operational data provisioning framework captures changed data. Parallelization features in Amazon AppFlow and AWS Partner Solutions like BryteFlow and SNP enable customers to choose the number of parallel processes to run in the background, parallelizing large data volumes. Amazon S3 offers improved throughput with multi-part uploads through supported data integration mechanisms. The parallelization capabilities and seamless integration with Amazon S3 allow for efficient and scalable data ingestion from SAP systems into AWS. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using serverless technologies like Amazon AppFlow or AWS Glue and Amazon EC2 auto scaling, you only pay for the resources you consume. To optimize costs further, extract only the required business data groups by leveraging semantic data models (for example, BW extractors or CDS views). Minimize the number of flows based on your reporting granularity needs. Implement housekeeping by setting up data tiering or deletion in Amazon S3 for old or unwanted data. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Data extraction workloads can be scheduled or invoked in real-time, eliminating the need for underlying infrastructure to run continuously. Using serverless and auto-scaling services is a sustainable approach for data extraction workloads, as these components activate only when needed. By leveraging managed services and dynamic scaling, you minimize the environmental impact of backend services. Adopt new options for Amazon AppFlow as they become available to optimize the volume and frequency of extraction. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Replicate SAP to AWS in Real-Time with Business Logic Intact Using BryteFlow**: This blog post demonstrates how to extract and integrate SAP data on AWS for use cases like analytics, reporting, artificial intelligence (AI), machine learning (ML), and Internet of Things (IoT) in real-time, using the BryteFlow SAP Data Lake Builder on AWS.

[Learn more](https://aws.amazon.com/blogs/apn/replicate-sap-to-aws-in-real-time-with-business-logic-intact-using-bryteflow/)

- **Scaling RISE with SAP data and AWS Glue**: AWS Glue is a serverless data integration service that makes it easier to discover, prepare, move, and integrate data from multiple sources for analytics, machine learning (ML), and application development.

[Learn more](https://aws.amazon.com/blogs/big-data/scaling-rise-with-sap-data-and-aws-glue/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
