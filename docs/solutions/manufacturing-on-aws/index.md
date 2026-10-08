---
source_url: https://docs.aws.amazon.com//solutions/manufacturing-on-aws//index.html
---

---
title: 'Guidance for Manufacturing on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/manufacturing-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Manufacturing on AWS

## Overview

This Guidance demonstrates how to unify fragmented industrial data from operational technology (OT) and information technology (IT) environments through a modern data fabric on AWS, enabling organizations to accelerate digital transformation initiatives. Organizations can connect edge devices and on-premises equipment to AWS cloud services using pre-built connectors and industrial protocols, streaming real-time data securely for processing and analysis. Amazon SageMaker AI Unified Studio provides a single environment to discover data assets, build machine learning models, and deploy AI agents that optimize manufacturing operations and supply chain performance. The approach includes integrated data quality management, semantic search capabilities, and governance controls that maintain security while enabling collaboration across teams. You can reduce operational costs, improve manufacturing efficiency, and establish a scalable foundation for AI-driven insights and intelligent automation across your industrial operations.

## Benefits

### Unify your factory data pipeline

Connect edge devices, industrial historians, and IT systems to AWS cloud services through a single, integrated architecture. Reduce data silos by streaming, transforming, and storing operational and information technology data in one governed environment.

### Accelerate AI-driven manufacturing decisions

Deploy machine learning models at the edge for real-time defect detection and run generative AI agents in the cloud to optimize supply chain, maintenance, and engineering workflows. Shorten the time from raw sensor data to actionable insight using Amazon SageMaker AI AI and Amazon Bedrock.

### Scale manufacturing intelligence securely

Govern cross-domain data sharing, enforce access policies, and track data lineage across your organization using Amazon SageMaker AI Unified Studio and AWS Lake Formation. Extend the same cloud capabilities to your plant floor with AWS Outposts, helping you meet data residency and latency requirements without sacrificing visibility.

## How it works

### Overview

This architecture diagram illustrates how to effectively support manufacturing use cases on AWS. It shows the key components and their interactions, providing an overview of the architecture's structure and functionality.

[Download the architecture diagram](downloads/smart-manufacturing-on-aws.pdf)Step 1Identify information related to industrial activities from on-premises equipment.

Step 2Collect real-time data from edge devices and transmit data streams securely to AWS IoT SiteWise in the cloud. Leveraging partners like Litmus, Domatica's EasyEdge, and Belden accelerate your integration with AWS IoT SiteWise Edge.

Step 3Connect edge devices through AWS Shop Floor Connectivity Framework using industrial protocols. Stream data securely to AWS cloud services. Deploy cloud-developed machine learning models at the edge using AWS IoT Greengrass for defect detection and anomaly inference.

Step 4Leverage Siemens Industrial Edge, a centrally managed solution to connect data from assets and IT systems to AWS IoT SiteWise, AWS IoT Core, and Amazon Simple Storage Service. Deploy ML models and industrial applications.

Step 5Connect edge devices and IT systems using AWS partner solutions like HighByte. Contextualize and stream data to AWS storage and analytics services including AWS IoT SiteWise, Amazon Simple Storage Service, Amazon S3 Tables, Amazon Timestream for InfluxDB, Amazon Redshift, Amazon RDS, AWS IoT Core, Amazon Kinesis, Amazon Kinesis Data Firehose, and Amazon Managed Service for Apache Flink.

Step 6Connect your on-premises applications to Amazon Simple Storage Service through AWS Storage Gateway using NFS and SMB file shares.

Step 7Extend AWS infrastructure and services to your premises with AWS Outposts, a fully managed service. Run your manufacturing-specialized applications on AWS services locally at your plant and integrate with AWS cloud infrastructure.

Step 8Ingest diverse data through AWS services. Stream real-time data via AWS IoT SiteWise, AWS IoT Core, Amazon Kinesis, and Amazon MSK. Transfer structured data using AWS Database Migration Service and AWS Glue. Process unstructured and semi-structured data with Amazon Simple Storage Service. Extract, create, and update ERP data with Amazon AppFlow.

Step 9Access AWS Analytics and AI/ML services through Amazon SageMaker AI Unified Studio. Find and query data and AI assets across your organization. Collaborate on projects to build analytics and AI artifacts. Share data, models, and generative AI applications securely. Amazon SageMaker AI Unified Studio is integrated with Amazon Q Developer, which provides AI-powered assistance for code development, data analysis, and ML workflows.

Step 10Process OT and IT data through AWS analytics services via Amazon SageMaker AI Unified Studio Portal. Catalog data with AWS Glue Data Catalog, transform through Visual ETL, and analyze using Amazon Athena. Process streaming data with Amazon Managed Service for Apache Flink and generate insights using Amazon EMR.

Step 11Unify data across Amazon Simple Storage Service data lakes, including Amazon S3 Tables, and Amazon Redshift data warehouses with Amazon SageMaker AI Lakehouse. Build analytics and AI/ML applications on a single data copy using Apache Iceberg–compatible tools and engines.

Step 12Organize assets, users, and projects within Amazon SageMaker AI Unified Studio domains. Create multiple domains to match enterprise structure. Collaborate in projects to manage data assets, analyze data, develop ML models, and build generative AI applications.

Step 13Enrich technical catalog metadata with business context using Amazon SageMaker AI Catalog. Discover and access approved data and models through generative AI semantic search. Monitor data quality, track lineage, and enforce access policies in Amazon SageMaker AI Unified Studio.

Step 14Build, train, and deploy machine learning models and generative AI capabilities using Amazon SageMaker AI AI and Amazon Bedrock. Leverage Agentic AI to improve manufacturing, optimize supply chain, get digital twins agents for Engineering and Design, all impacting your sustainability.

Step 15Integrate with cloud-hosted ERP, Supply Chain, Maintenance, and WMS/TMS manufacturing solutions, including MCP servers for industrial knowledge. Exchange data with enterprise platforms like Snowflake and Databricks to enhance manufacturing analytics.

Step 16Visualize data with Amazon Managed Grafana from Amazon Redshift or Amazon Simple Storage Service via Amazon Athena. Build dashboards using Amazon QuickSight and Amazon Managed Grafana.

### Edge Services

This architecture diagram illustrates how to effectively collect data from the factory and send to AWS services in the cloud.

[Download the architecture diagram](downloads/smart-manufacturing-on-aws.pdf)Step 1Identify information related to industrial activities from on-premises equipment.

Step 2Deploy and run your cloud-developed machine learning models at the edge through AWS IoT Greengrass for defect detection and anomaly inference.

Step 3Collect real-time data from edge devices and transmit data streams securely to AWS IoT SiteWise Edge in the cloud. Leveraging partners like Litmus, Domatica's EasyEdge, Siemens Industrial Edge, and Belden CloudRail accelerate your integration with AWS IoT SiteWise Edge.

Step 4Connect edge devices through AWS Shop Floor Connectivity Framework and partner solutions like HighByte. Stream and contextualize data securely to AWS IoT SiteWise, Amazon Simple Storage Service, AWS IoT Core, Amazon Kinesis, and Amazon MSK using industrial protocols.

Step 5Connect your on-premises applications to Amazon Simple Storage Service through AWS Storage Gateway using NFS and SMB file shares.

Step 6Extend AWS infrastructure to plant premises with AWS Outposts. Run manufacturing applications locally using AWS services and integrate with AWS cloud infrastructure.

### Cloud Services

This architecture diagram illustrates how data collected from the factory can be used with AWS cloud services.

[Download the architecture diagram](downloads/smart-manufacturing-on-aws.pdf)Step 1Process diverse data types through AWS services. Stream real-time data through AWS IoT SiteWise, AWS IoT Core, Amazon Kinesis, and Amazon MSK. Transfer structured data using AWS DMS and AWS Glue. Process unstructured data with Amazon Simple Storage Service. Extract and update ERP data using Amazon AppFlow.

Step 2Access AWS Analytics and AI/ML services through Amazon SageMaker AI Unified Studio. Find and query data and AI assets organization-wide. Collaborate on projects to build analytics and AI artifacts. Share data, models, and generative AI applications securely. Amazon SageMaker AI Unified Studio is integrated with Amazon Q Developer, which provides AI-powered assistance for code development, data analysis, and ML workflows.

Step 3Process OT and IT data through AWS analytics services via Amazon SageMaker AI Unified Studio. Catalog data using AWS Glue Data Catalog, transform with AWS Glue Visual ETL, and analyze with Amazon Athena. Process streams with Amazon Managed Service for Apache Flink and generate insights using Amazon EMR.

Step 4Unify data across Amazon Simple Storage Service data lakes, including S3 Tables, and Amazon Redshift data warehouses with Amazon SageMaker AI Lakehouse. Build powerful analytics and AI/ML applications on a single copy of data using all Apache Iceberg–compatible tools and engines.

Step 5Deploy and operate AI agents at scale on Amazon Bedrock AgentCore. Run agent logic on AgentCore Runtime. Route tool calls through AgentCore Gateway. Access production documentation through Amazon Bedrock Knowledge Bases.

### Cloud Services with Partners and Agentic AI

This architecture diagram illustrates how data collected from the factory can be used with AWS cloud services, partner integrations, and Agentic AI.

[Download the architecture diagram](downloads/smart-manufacturing-on-aws.pdf)Step 1Access analytics and AI/ML tools through Amazon SageMaker AI Unified Studio's single environment — run queries in Amazon Athena and Amazon Redshift Query Editor, build notebooks in Amazon EMR and AWS Glue Notebook, collaborate on data, models, and generative AI applications organization-wide. Ask natural-language questions from the plant floor through Amazon QuickSight. Traverse cross-domain relationships in Amazon Neptune to give agents semantic context for reasoning.

Step 2Leverage Amazon Bedrock and Agentic AI to improve manufacturing and optimize supply chain. Use Amazon Bedrock AgentCore, a comprehensive set of enterprise-grade services that help securely deploy and operate AI agents at scale, with components like AgentCore Runtime for low-latency serverless environments. Access production documentation and policies using Retrieval Augmented Generation (RAG), through managed Amazon Bedrock Knowledge Bases. Connect to Model Context Protocol (MCP) servers to allow agents to connect to systems where data lives.

Step 3Integrate with cloud-hosted manufacturing solutions, including MCP servers. Exchange data with enterprise platforms using Iceberg REST Catalog. Build ETL pipelines with Amazon SageMaker AI Zero-ETL for Amazon Simple Storage Service, Amazon S3 Tables, and Amazon Redshift. Query data using Amazon Athena.

[Read usage guidelines](/solutions/guidance-disclaimers/)
