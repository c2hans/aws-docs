---
source_url: https://docs.aws.amazon.com/solutions/autonomous-driving-data-framework-on-aws/index.html
---

---
title: 'Guidance for Autonomous Driving Data Framework on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/autonomous-driving-data-framework-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Autonomous Driving Data Framework on AWS

## Overview

This Guidance demonstrates how customers can process and search high-accuracy, scenario-based data with the Autonomous Driving Data Framework (ADDF). Automotive teams who want to implement common tasks for autonomous vehicles (AV) and advanced driver-assistance systems (ADAS) can share, modify, or create fully customizable modules that reduce the amount of effort required to create and deploy this Guidance.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/autonomous-driving-data-framework-on-aws.pdf)

![Architecture diagram](/images/solutions/autonomous-driving-data-framework-on-aws/images/autonomous-driving-data-framework-on-aws-1.png)

1. **Step 1**: Near real-time ingestion of sensor data, data modeling, indexing, and enrichment through AWS IoT FleetWise and data stored in Amazon Simple Storage Service (Amazon S3).
1. **Step 2**: Near real-time fleet monitoring and alerting with Amazon Redshift, Amazon Managed Grafana, and Amazon Simple Notification Service (Amazon SNS).
1. **Step 3**: Bulk upload of recording data from copy stations through AWS Direct Connect, ingestion validation and registry with Amazon API Gateway, and a raw recording staging bucket with Amazon S3.
1. **Step 4**: Initial data quality checks and data extraction with containers running on AWS Batch. Processed data is stored in Amazon S3.
1. **Step 5**: Images are annotated with machine learning models to detect objects and road lanes. Low confidence predictions are set aside for manual annotation. Bounding boxes are used for blurring faces and license plates. Amazon SageMaker Ground Truth is used for labeling.
1. **Step 6**: Use Amazon EMR in combination with Amazon S3 and AWS Batch to enrich sensor data with localized weather and map matching info. It also combines image annotations, and sensor data to detect various scenes like traffic intersections or people and objects in the street.
1. **Step 7**: AWS analytics toolchain manages parquet datasets and schema evolution with Apache Iceberg, AWS Glue Data Catalog, querying tools such as Amazon Athena, Amazon Redshift, and OpenSearch.
1. **Step 8**: Data pipeline orchestration with Amazon Managed Workflows for Apache Airflow (Amazon MWAA) observability of distributed workloads with Amazon Managed Grafana, Amazon CloudWatch, and AWS X-Ray. Amazon Neptune is used for data lineage.
1. **Step 9**: Build, test, and deploy using GitOps on AWS CodePipeline and AWS CodeBuild.
1. **Step 10**: Host high-performance, on-demand visualization applications on Amazon Elastic Kubernetes Service (Amazon EKS) for engineers. Developer instances use Amazon Elastic Compute Cloud (Amazon EC2) and Amazon DCV to stage and share files with Amazon FSx for Lustre or Amazon S3. Use AWS Step Functions for instance orchestration.
1. **Step 11**: User-facing tools like Python and Spark Notebook infrastructure use Amazon EMR and SageMaker. Custom dashboards can be configured with Grafana, and web applications are built and hosted on AWS Amplify and Amazon CloudFront.
1. **Step 12**: Scalable simulation and KPI calculation modules use Amazon EKS or AWS Batch. Amazon QuickSight is used to analyze KPIs and simulation results.
1. **Step 13**: Drive and file-level metadata can be stored and queried with Amazon DynamoDB at scale for pipeline traceability and to store metadata, manifests, markers, and tags.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/awslabs/autonomous-driving-data-framework)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance offers a secure-by-default setup to allow users to safely operate and respond to incidents and events. If you decide to move into a production-like environment, the ADDF security and operations guide outlines best practices for securely deploying and operating ADDF in the AWS Cloud. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

ADDF was built with security in mind. Before release to the public, AWS performed an initial, internal security review of ADDF and resolved any identified security issues. Both AWS and the open-source community contribute to ongoing security reviews of the framework. Interfaces to the public internet are not exposed by the core modules. Services are only reachable as an authenticated user in the context of an AWS account. Various built-in security features in ADDF are designed to help you set up a secure framework and help your organization meet common enterprise security requirements. AWS defined an ADDF shared responsibility model, as well as a secure setup and operation guide, to help you on your ADDF journey from a secure start through to production. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

To implement a reliable architecture, each individual module is designed to cover module-specific throttling and limit-issues based on current experience. The default deployment options offer the end-user a sensible working baseline with common account limits. If the end-user decides to scale out, that user is responsible for considering any newly hit constraints or limits. ADDF is an open-source project. The ADDF community constantly improves features based on customer or community input. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

ADDF provides best-practice patterns that have been proven in challenging enterprise environments with customers. All selected services reflect the learnings from real-life customer use-cases. Amazon EKS hosts high-performance, on-demand visualization applications for engineers. For developer instances, Amazon EC2 and Amazon DCV stage and share files using FSx for Lustre. Both patterns have proven to work at scale in enterprise environments. The default deployment options offer the end-user a sensible working baseline. The user is free to change the default configuration of modules to scale up or down based on the use case. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses resources based on workload data and resource characteristics to keep up with demand. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

In this Guidance, the ADDF modules describe patterns for running ADAS and AV workloads at an enterprise scale, containing common best-practices for scaling traffic and data access patterns. Any compute intensive workload should have a default value that balances between a high baseline utilization and end-user usability. The ADDF modules provide a reference implementation, and all deployed resources are set to the minimum resources needed to support the ADDF models. This ensures a high baseline utilization. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
