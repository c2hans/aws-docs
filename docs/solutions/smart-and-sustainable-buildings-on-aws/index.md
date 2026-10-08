---
source_url: https://docs.aws.amazon.com/solutions/smart-and-sustainable-buildings-on-aws/index.html
---

---
title: 'Guidance for Smart and Sustainable Buildings on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/smart-and-sustainable-buildings-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Smart and Sustainable Buildings on AWS

## Overview

This Guidance demonstrates how to integrate building systems, assets, and sensors to enable real-time and historical insights for sustainable building management. Operations data from sources such as HVAC, water, electricity, and solar power are consolidated and processed with artificial intelligence and machine learning (AI/ML) capabilities. The data is stored, analyzed, and visualized to reveal where and how buildings are generating emissions across their infrastructure and operations. Customers can also deploy their own sensors, on their own networks, and quickly show which buildings are driving the greatest emissions across their global environment.

## How it works

Integrate building systems, assets, and sensors to enable real-time insights for sustainable management across your infrastructure and operations.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/smart-and-sustainable-buildings-on-aws.pdf)

![Architecture diagram](/images/solutions/smart-and-sustainable-buildings-on-aws/images/smart-and-sustainable-buildings-on-aws-1.png)

1. **Step 1**: Ingest utility bills with Amazon API Gateway and convert into machine data using Amazon Textract to normalize electric, gas, water, and waste usage (see the Guidance for Utility Bill Processing on AWS for more details). This data can be sent to the data lake for further analysis.
1. **Step 2**: Send device telemetry from legacy Building Management System (BMS) platforms to AWS IoT Core for ingestion into the Cloud. Deliver real-time telemetry data to AWS IoT SiteWise and to the data lake using Amazon Kinesis Data Firehose.
1. **Step 3**: Harvest and process device sensor data with AWS IoT SiteWise Edge deployed on AWS IoT Greengrass and send directly to AWS IoT SiteWise.
1. **Step 4**: Use Amazon AppFlow or AWS DataSync to connect to your BMS and Enterprise Resource Planning (ERP) systems. This allows you to ingest equipment attributes and your Building Information Modeling (BIM) platform for spatial building models and other attributes. Use AWS Lambda to modify equipment data to adhere to a chosen building metadata standard.
1. **Step 5**: Build a data lake using Amazon Simple Storage Service (Amazon S3) to store your data, save technical metadata in your AWS Glue Data Catalog, use AWS Step Functions to orchestrate AWS Glue jobs for extract, transform, and load (ETL), and administer fine-grained access control with AWS Lake Formation.
1. **Step 6**: Collect device measurement data in Amazon Timestream or AWS IoT SiteWise to calculate metrics and generate alarms.
1. **Step 7**: Manage your asset attributes and relationships in Amazon Neptune or create a digital twin of your sites and assets using AWS IoT TwinMaker. Compose an interactive 3D view of your environment and overlay real-time measurements directly from AWS IoT SiteWise.
1. **Step 8**: Provide structured query language (SQL) access to your data through Amazon Athena, or build embeddable, machine learning (ML) dashboards in Amazon QuickSight or Amazon Managed Grafana.
1. **Step 9**: Connect Amazon SageMaker to your data lake to train ML models for deployment back on-site in AWS IoT Greengrass for real-time inferencing. Model outputs can be used to control on-site equipment or to derive new metrics for ingestion through the standard architecture.
1. **Step 10**: Monitor overall system health and performance using Amazon CloudWatch.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-smart-and-sustainable-buildings-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudWatch provides centralized logging with metrics and alarms across all deployed services to raise alerts for operational anomalies. For example, you can create an alert to prompt for a service limit increase if you surpass a threshold of concurrent Lambda executions or active Kinesis Data Firehose partitions. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Resources are protected using AWS Identity and Access Management (IAM) policies and principles. Use least-privilege access and role-based access to grant operators permissions to modify resources, such as deploying an updated stack through AWS CloudFormation. AWS Key Management Service (AWS KMS) encrypts your data at-rest in Amazon S3 and AWS IoT SiteWise. AWS KMS encrypts your data in-transit with Lambda and Kinesis Data Firehose. The keys should be rotated on a regular schedule. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses AWS services that are serverless, enabling auto-scaling to respond to fluctuating demands. For example, AWS IoT Core, AWS IoT SiteWise, and Kinesis Data Firehose scale to match the throughput of your data with no management required. For in-flight processing, Lambda will automatically scale the number of execution environments required to handle demand. AWS services are used to provide various options for data backup and recovery. For example, Amazon S3 has object versioning, replication, and backup features to ensure Recovery Point Objectives (RPOs) can be met. If needed, AWS IoT SiteWise APIs can provide definitions of assets and models for easy backup and restoration. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Services in this Guidance were purposefully selected to handle the needs of a modernized building management system. Amazon S3 was selected for its reliable long-term storage and flexibility of consuming tools and services. AWS IoT SiteWise provides managed, scalable ingestion, and real-time calculation of streaming asset data, minimizing the need to build custom components. It integrates seamlessly with AWS IoT TwinMaker, which was chosen for digital twin creation. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance relies on serverless AWS services such as AWS IoT TwinMaker, AWS Glue, Lambda, Athena, and Kinesis Data Firehose. These services are fully managed and autoscale according to workload demand. As a result, you only pay for what you use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Data in Amazon S3 can be stored in more efficient file formats (such as Parquet) to prevent unnecessary processing and reduce the overall storage required. Amazon S3 lifecycle policies can automatically move data to more energy-efficient storage classes, enforce deletion timelines, and minimize overall storage requirements. This Guidance uses managed, serverless technologies such as AWS Glue, Lambda, Athena, and Step Functions to ensure hardware is minimally provisioned to meet demand. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Creating Sustainable, Data-Driven Buildings**: Article: This article demonstrates how to create scalable solutions to improve building energy efficiency and reduce emissions.

[Learn more](https://www.amazon.science/latest-news/creating-sustainable-data-driven-buildings)

- **Guidance for Monitoring and Optimizing Energy Usage on AWS**: Guidance: This Guidance demonstrates how to optimize the energy use of heavy equipment for workloads within a Building Management Systems (BMS).

[Learn more](https://aws.amazon.com/solutions/guidance/monitoring-and-optimizing-energy-usage-on-aws/)

- **Guidance for Utility Bill Processing on AWS**: Guidance: This Guidance shows how to derive sustainability insights from utility bills using artificial intelligence and machine learning (AI/ML).

[Learn more](https://aws.amazon.com/solutions/guidance/utility-bill-processing-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
