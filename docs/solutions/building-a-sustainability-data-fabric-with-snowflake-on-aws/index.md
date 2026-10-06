---
source_url: https://docs.aws.amazon.com/solutions/building-a-sustainability-data-fabric-with-snowflake-on-aws/index.html
---

---
title: 'Guidance for Building a Sustainability Data Fabric with Snowflake on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-sustainability-data-fabric-with-snowflake-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Building a Sustainability Data Fabric with Snowflake on AWS

## Overview

This Guidance shows you how to build a sustainability data fabric on AWS using the best of Snowflake and AWS offerings. This combination offers a scalable platform that’s flexible and extensible for ingesting, organizing, and analyzing both structured and unstructured sustainability data, providing a unified solution for comprehensive data management and insights. You can then use advanced analytics with artificial intelligence and machine learning (AI/ML) models to generate key environmental, social, and governance (ESG) metrics and insights.

## How it works

### Overview

This architecture diagram illustrates how to use Snowflake for integrating, processing, and analyzing sustainability data, with the unified platform encompassing carbon accounting, energy optimization, and supply chain transparency. The subsequent tabs depict data ingestion and data management processes.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-a-sustainability-data-fabric-with-snowflake-on-aws.pdf)Step 1Sustainability data can originate from sources external to Snowflake and AWS. This data can represent physical data objects, such as utility bills, or digital assets, such as emissions database tables. AWS services can be used to ingest both structured and unstructured data into AWS and Snowflake.Step 2The Snowflake AI Data Cloud is used to create and run sustainability workloads to gain and share insights across your organization. Snowflake also provides connectors to adopt services outside of the Snowflake AI Data Cloud. Third-party resources, such as weather data and emission factors, can be supplemented through Snowflake Marketplace, AWS Marketplace, and AWS Data Exchange.Step 3Data consumers can request access to data assets from the data owner. Data owners can grant the request and apply rules on how the data is used to facilitate external collaboration.### Data sources and ingestion

This architecture diagram illustrates the ingest, preparation, and storage of unstructured sustainability data using AWS services.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-a-sustainability-data-fabric-with-snowflake-on-aws.pdf)Step 1Sustainability data can take many forms, such as near real-time streaming data from industrial processes or CSV files. This information is organized and collected from data providers.Step 2Organizations ingesting data from streaming sources, such as sensors and industrial machinery, can use services like Amazon Kinesis Data Streams and AWS IoT Core to bring data into AWS. AWS Transfer Family helps automate data transfer processing steps, such as copying, tagging, scanning, filtering, compression, and encryption. AWS Glue is a managed service to perform extract, transform, and load (ETL) operations on the data.Step 3Amazon API Gateway helps you build secure HTTP, REST, and WebSocket endpoints to process thousands of API calls. Amazon AppFlow is an application integration service to securely transfer data between software as a service (SaaS) applications and AWS services.Step 4For data existing on AWS, such as Amazon Simple Storage Service (Amazon S3) objects, AWS DataSync can be used to synchronize data automatically with the Snowflake AI Data Cloud Sustainability Workflow.Step 5Both internal and external data is collected in Snowflake data stores.### Snowflake AI Data Cloud sustainability workflow

This architecture diagram shows how you can manage sustainability workloads across your organization by applying data governance best practices, integrating workflows with third-party data, and using compute instances to extract additional insights.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-a-sustainability-data-fabric-with-snowflake-on-aws.pdf)Step 1Snowflake offers data storage capabilities that allow for the collection of raw and unstructured data into a unified and scalable data management platform, providing a single access point to initiate a sustainability workflow.Step 2Snowflake Marketplace, AWS Marketplace and AWS Data Exchange provide you with access to a wide range of sustainability-related datasets, such as emission factors and weather data.Step 3Data products on Snowflake perform ETL operations with data quality checks.Step 4Assets created by Snowflake data products are registered in the data catalog using Snowflake Horizons. You can orchestrate asset registration with AWS Step Functions.Step 5With machine learning (ML) technology, data analytics workflow products on Snowflake help you automate sustainability workloads, such as carbon accounting and environmental, social, and governance (ESG) information.Step 6You can use Amazon Bedrock to map environmental impact factors at scale, as outlined in Guidance for Environmental Impact Factor Mapping on AWS. Additionally, you can use Amazon SageMaker AI to optimize energy consumption as described in Guidance for Monitoring and Optimizing Energy on AWS.Step 7The Snowflake External Access service provides secure access between the Snowflake AI Data Cloud and external data consumers.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon Bedrock and AWS Lambda provide generative AI compute capabilities without the need to upgrade or patch virtual machine images or operating system versions. Furthermore, Amazon Elastic Compute Cloud (Amazon EC2), with its extensive selection of over 750 instance types, helps you to meet your specific requirements for processor, storage, networking, operating system, and workload needs. This comprehensive approach helps you to achieve optimal price-performance ratios to support your diverse computing workloads, including high-performance computing (HPC), ML, and Windows-based applications. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) integrates with all AWS services, including Lambda and Amazon EC2. This enables application code running in Lambda to authenticate with other services, such as Amazon Bedrock and API Gateway, without needing to store long-lived credentials. Furthermore, IAM identity-based policies can be used to define and manage access permissions, determining whether a user can create, access, or delete Amazon Kendra resources. For instance, a user within your AWS account can be denied access to query a specific Amazon Kendra index through the application of an IAM policy. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses fully managed serverless offerings like Amazon Bedrock, Lambda, Amazon EC2, and Amazon S3 that are all deployed across multiple Availability Zones (AZs) by default. These services do not involve long-running compute or database resources that require maintenance, leading to fewer points of failure within the overall architecture. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Bedrock is a fully managed generative AI service that offers a choice of foundation models (FMs) through a single API. You can quickly experiment with a variety of FMs and use a single API for inference regardless of the models you choose, giving you the flexibility to use FMs from different providers and keep current with the latest model versions with minimal code changes. Additionally, Amazon AppFlow is a fully managed integration service that helps you securely transfer data between SaaS applications, such as Salesforce, SAP, Google Analytics, and various AWS services. Amazon AppFlow is used here as an entry point to connect to various Snowflake services. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda and Amazon Bedrock automatically scale and allocate resources based on demand. These fully managed services also reduce the operational burden on DevOps team, lowering the costs associated with infrastructure management and maintenance. Additionally, Lambda and Amazon Bedrock offer a pay-as-you-go pricing model so that you’re only charged when these services are actively processing requests. For example, Amazon Bedrock has an on-demand and batch mode that lets you use FMs on a pay-as-you-go basis without having to make any time-based term commitments. Amazon S3 is also used here to provide you with the flexibility to choose storage tiers based on your workload and data retention requirements. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda, Amazon Bedrock, and Amazon Kinesis enable more efficient operations by shifting the responsibility of maintaining your hardware infrastructure to AWS. Learn more about Amazon and AWS Sustainability efforts. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
