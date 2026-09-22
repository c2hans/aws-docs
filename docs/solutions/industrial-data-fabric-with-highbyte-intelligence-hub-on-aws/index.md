---
source_url: https://docs.aws.amazon.com/solutions/industrial-data-fabric-with-highbyte-intelligence-hub-on-aws/index.html
---

---
title: 'Guidance for Industrial Data Fabric with HighByte Intelligence Hub on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/industrial-data-fabric-with-highbyte-intelligence-hub-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Industrial Data Fabric with HighByte Intelligence Hub on AWS

## Overview

This Guidance combines AWS IoT SiteWise with HighByte Intelligence Hub to facilitate the transformation of manufacturing and industrial operations through a proven, governed, data-driven approach. HighByte Intelligence Hub serves as an edge-native DataOps solution, bridging the gap between operational technology (OT) and IT by integrating industrial information across diverse systems. With this Guidance, you can achieve a Unified Namespace (UNS) that helps ensure seamless data access and integration throughout the manufacturing enterprise's lifecycle. This Guidance facilitates the establishment and upkeep of an enterprise-governed asset model across remote sites with central and remote HighByte Intelligence Hubs. The central Intelligence Hub enables the creation and maintenance of an enterprise-governed asset hierarchy and model across remote sites, while remote Intelligence Hubs at the site level aid in ingesting data from different industrial edge data sources. This provides an effortless publishing process to AWS IoT SiteWise, a purpose-built AWS industrial Internet of Things (IoT) service. **Note:** See Disclaimer below

## How it works

### Delivering Industrial DataOps (IDO) on Industrial Data Fabric (IDF)

This high-level architecture diagram is a reference that helps you create an enterprise governed model, ingest near real-time and historical data at scale from edge data sources into an IDF on AWS, and interface with applications using REST APIs.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/industrial-data-fabric-with-highbyte-intelligence-hub-on-aws.pdf?target=_blank)Step 1Define a governed data model in a central location. The centralized model can be populated with metadata from corporate systems such as enterprise resource planning (ERP), piping and instrumentation diagram (P&ID), and computerized maintenance management system (CMMS).

Step 2Bring the governed model into an edge application, where additional metadata from systems, such as a manufacturing execution system (MES), can be added. Data streams can then be mapped to the imported model. Asset Hierarchy can also be moved to AWS IoT SiteWise.Step 3Ingest data depending on the source. Stream data feeds from a variety of sources using AWS DataSync for file share, Amazon Kinesis, Amazon Managed Streaming for Apache Kafka (Amazon MSK), AWS IoT Core, AWS IoT SiteWise, or AWS Transfer Family for SFTP.Step 4Optimize data storage for the workload, which can include Amazon DynamoDB key value and document data structures, Amazon Simple Storage Service (Amazon S3) for object storage, Amazon Neptune for graph use cases, Amazon Redshift for data warehousing, Amazon Timestream for time series data, and AWS IoT SiteWise to organize industrial equipment data. Data from AWS IoT SiteWise can be integrated with AWS IoT TwinMaker.Step 5Use AWS artificial intelligence and machine learning (AI/ML) services such as Amazon SageMaker to build, train, and deploy ML models.Step 6Use AWS analytics services such as Amazon OpenSearch Service, Amazon Managed Service for Apache Flink, Amazon Athena, Amazon EMR, and AWS Glue for data processing.Step 7AWS WAF provides protection from web exploits while Amazon API Gateway provides REST method support. Amazon Cognito provides user authentication and AWS token support.Step 8Egress data from the Industrial Data Fabric (IDF) with connectors directly to AWS services or through API Gateway to supported AWS services. For services that are not supported by API Gateway, an OAuth 2.0 pattern with Amazon Cognito is used to generate AWS temporary tokens.### IDF Governed Data Model with HighByte Intelligence Hub

This architecture diagram helps you create an enterprise governed data model, ingest real-time and historical data at scale from edge data sources, and visualize this data using Amazon Managed Grafana. AWS IoT SiteWise provides a contextualized timeseries data store and AWS IoT TwinMaker allows for digital twin scenes.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/industrial-data-fabric-with-highbyte-intelligence-hub-on-aws.pdf#page=2?target=_blank)Step 1Define a governed data model in HighByte Central Hub running as a Docker image in Amazon Elastic Container Service (Amazon ECS). Publish the Enterprise Hierarchy from HighByte to AWS IoT SiteWise, including model information. Sync asset models from the central hub to the remote hubs.Step 2Connect to data sources with the HighByte remote hubs using models from the central hub. Insert data into AWS IoT SiteWise in the appropriate portion of the hierarchy model. Data can be inserted in near real-time using AWS IoT SiteWise or delayed using buffered ingestion.Step 3Use buffered ingestion through Amazon S3 to reduce AWS IoT SiteWise ingestion costs. The AWS IoT SiteWise Open Database Connectivity (ODBC) driver provides direct integration to AWS IoT SiteWise for business intelligence (BI) client tools.Step 4Train models in Amazon Lookout for Equipment for anomaly detection and prediction maintenance using data from AWS IoT SiteWise. Native AWS IoT SiteWise integration through Amazon S3 allows data exchange between services. Use AWS AI/ML services such as SageMaker to build, train, and deploy custom ML models.Step 5Access AWS IoT SiteWise data through API Gateway and AWS Lambda with Amazon Cognito for authenticated REST method support.Step 6Visualize AWS IoT SiteWise data and AWS IoT TwinMaker scenes using Amazon Managed Grafana.### HighByte Intelligence Hub Industrial DataOps on AWS

This architecture diagram demonstrates how HighByte Intelligence Hub integrates OT with IT to combine industrial information across multiple systems, enabling OT teams to model, transform, and share plant floor data with IT systems.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/industrial-data-fabric-with-highbyte-intelligence-hub-on-aws.pdf#page=3?target=_blank)Step 1HighByte Intelligence Hub consumes both real-time and asset model data from a myriad of edge data sources, including relational databases and AWS IoT Greengrass, by using standard industrial protocol input connectors. This includes data ingestion from industrial historians, such as Inductive Automation's Ignition Server and Aveva's PI System.Step 2Intelligence Hub enables customers to standardize, organize, and merge your industrial data into a single equipment model. Then, using flows, you can route the asset models to multiple output connectors, each with a different frequency. HighByte can be deployed on the edge using an AWS container option, including IoT Greengrass, Amazon Elastic Kubernetes Service (Amazon EKS) Anywhere, and Amazon ECS Anywhere. Intelligence Hub provides a variety of output connectors that support many of standard industrial protocols, including a native AWS IoT SiteWise connector.Step 3Bring in asset models and timeseries based sensor data into Amazon S3. AWS Lake Formation helps you collect and catalog data from databases and object storage, move the data into Amazon S3, and clean and classify data using ML algorithms. Data is accessed through AWS Glue Data Catalog.Step 4Build asset models within the HighByte editor and deploy the model directly to AWS IoT SiteWise along with the streaming data. Calculate and visualize metrics from telemetry data using AWS IoT SiteWise Monitor.Step 5Intelligence Hub can connect directly to AWS IoT Core through its native Message Queuing Telemetry Transport (MQTT) service or use IoT Greengrass locally. Intelligence Hub also enables bi-directional communication with AWS IoT Core and IoT Greengrass.Step 6Intelligence Hub can connect directly to Amazon Kinesis Data Streams for massively scalable and durable near real-time data streaming. Streaming data can be transformed and analyzed in near real-time using Amazon Managed Service for Apache Flink, and sent to Amazon Data Firehose. Time series data can also be sent to Timestream from Amazon Managed Service for Apache Flink.Step 7Telemetry data is published in near real-time to Data Firehose by either an AWS IoT Core rule, Kinesis Data Streams, or a HighByte and Data Firehose connector. This loads the streaming data reliably into an Amazon S3 data lake.Step 8Use Amazon Redshift to store structured data sets and analytics results in a data warehouse. Data into Amazon Redshift can be ingested either through AWS Glue from Amazon S3 or directly through the Intelligence Hub Redshift connector.Step 9Create BI reports and visualize data from Amazon Redshift and Amazon S3 with Amazon QuickSight and Athena.Step 10When real-time and historical data is available in Amazon S3, Lookout for Equipment uses the data to detect abnormal equipment behavior so that potential machine failures are detected before failures occur and unplanned downtime is avoided. Computed metrics can be written back into Amazon S3 for storage and consumption. Custom ML models can be developed with SageMaker.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The majority of AWS services used by this Guidance, such as Amazon S3 and API Gateway, are serverless, lowering the operational overhead of maintaining the Guidance. This also allows you to evolve the design pattern in a continuous cycle of improvement over time. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance leverages AWS Security Token Service (AWS STS) and Amazon Cognito. These services allow you to take advantage of cloud technologies to protect data, systems, and assets in a way that can improve your security posture. Security Best Practices for Manufacturing OT describes how to design, deploy, and secure distributed manufacturing workloads and resources at the industrial edge. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses many of the AWS managed services to allow for a highly available network topology. Availability and reliability are managed on your behalf by AWS service teams (for example, Amazon S3, AWS IoT SiteWise, and Amazon Cognito). [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses purpose-built storage services, such as Amazon S3, that can reduce latency and increase throughput. You can use cross-region replication (CRR) to provide lower-latency data access to different geographic Regions. This Guidance provides multiple data-driven approaches to meet your workload requirements of scaling, traffic, and data access patterns. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses purpose-built storage services, such as Amazon S3, that can reduce latency and increase throughput. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance utilizes scalable services, such as Amazon S3, to align the services to your needs. Its functionalities are implemented by using a serverless architecture (including Amazon Cognito and API Gateway). Your resources are available only when needed and do not run constantly. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Partner Solution**: Start by building your own platform the focuses on liberating plant data from EDGE  to cloud with context

[HighByte Intelligence Hub](https://aws.amazon.com/marketplace/pp/prodview-xgrwamplfankq?sr=0-1&ref_=beagle&applicationId=AWSMPContessa)

[Read usage guidelines](/solutions/guidance-disclaimers/)
