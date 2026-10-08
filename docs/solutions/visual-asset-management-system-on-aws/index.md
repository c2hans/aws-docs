---
source_url: https://docs.aws.amazon.com/solutions/visual-asset-management-system-on-aws/index.html
---

---
title: 'Guidance for Visual Asset Management System on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/visual-asset-management-system-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Visual Asset Management System on AWS

## Overview

This Guidance helps you centralize and automate the process of storing, converting, optimizing, and distributing 3D and 2D assets using serverless technologies. Visual Asset Management System (VAMS) with Amazon stores and manages visual assets in the cloud, which empowers any user with a web browser to upload, manage, visualize, transform, and retrieve visual assets. Organizations that previously had to visualize, transform, interface with, and deliver these assets on local systems can now do so from a web-based cloud dashboard. The VAMS API helps you build custom applications and automation.

## How it works

This architecture diagram shows the standard system architecture for a VAMS deployment. AWS Cloud Development Kit (AWS CDK) is used to deploy a React-based web app for asset management and a serverless backend for storing and processing spatial data.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/visual-asset-management-system-on-aws.pdf)

![Architecture diagram](/images/solutions/visual-asset-management-system-on-aws/images/visual-asset-management-system-on-aws-1.png)

1. **Step 1**: Amazon Cognito user pools handle user authentication, and AWS Amplify interfaces with the VAMS API.
1. **Step 2**: Using the React.js-based content management system, upload assets to Amazon Simple Storage Service (Amazon S3), apply metadata to the assets, process the assets using custom workflows and pipelines that the user creates, and generate download links for the assets.
1. **Step 3**: The VAMS API uses the Amplify JavaScript library to handle client-side requests and results and route asset uploads and downloads from Amazon S3.
1. **Step 4**: Amazon API Gateway routes server-side payloads and results, interfacing with AWS Lambda functions for handling assets, metadata, pipelines, and workflows.
1. **Step 5**: The Lambda asset function delivers assets to Amazon S3, which stores and versions the data and stores asset data in Amazon DynamoDB.
1. **Step 6**: Lambda data functions store asset metadata in a metadata DynamoDB table, allowing for extensible and customizable schema management.
1. **Step 7**: Lambda functions deliver data to Amazon SageMaker, which creates containerized asset processing pipelines. Amazon Elastic Container Registry (Amazon ECR) stores the containerized pipelines while DynamoDB stores the pipeline data. Schedule pipelines into workflows using the React.js content management interface.
1. **Step 8**: Lambda workflow functions direct workflow data to AWS Step Functions to orchestrate workflows and store them in DynamoDB. Step Functions automate the complex chaining of pipeline workloads by allowing the user to compose custom-ordered steps within the web app from their previously-defined pipelines. For example, a user could have a pipeline for file-type conversion, another for level of detail (LOD) generation, and a third for asset decimation, which they could order together into a single workflow.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch logs enable you to monitor Step Functions and Lambda as they travel through the API Gateway APIs to the underlying services. Visualizing and analyzing these components using CloudWatch helps you identify performance bottlenecks and troubleshoot requests. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito user pools authenticate and authorize users in VAMS. By using Amazon Cognito user pools, admins have greater control and security over who can access which parts of VAMS. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 and API Gateway are both fully managed services that allow VAMS to scale up or down as needed. Using loosely-coupled and microservices allow VAMS to remain working even when one component may be unavailable. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS Cloud Development Kit (AWS CDK) allows users to provision the cloud infrastructure needed to create a custom content management system (CMS). VAMS is open source and easily deployable through AWS CDK, allowing for rapid deployment, iteration, and experimentation within any new or existing AWS account. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 allows youto select a retention policy for your data. Lambda is used to run code only when that code is needed, and DynamoDB is used to store asset metadata and other necessary information. Using these managed and serverless services will help ensure that users are only charged for the resources that they actually use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

SageMaker is used to create pipelines through Jupyter notebooks. When the pipeline is not in use, you are not charged for SageMaker, meaning these resources are not unnecessarily running. VAMS shuts down any notebook after 1 hour of idle time, which reduces the number of resources being used. This reduction in the number of resources minimizes the workload’s environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Visual Asset Management System (VAMS) Workshop**: This workshop explains how to install VAMS to your AWS Account, create VAMS assets, pipelines and workflows, and use VAMS assets in your application

[Learn more](https://catalog.us-east-1.prod.workshops.aws/workshops/ab24ff8d-090a-4287-88dd-a04d03a440c1/en-US)

- **Visual Asset Management System (VAMS) Sample Code**: This sample code demonstrates how to deploy VAMS - a purpose-built, AWS native solution for the management and distribution of specialized visual assets used in spatial computing.

[Learn more](https://github.com/awslabs/visual-asset-management-system)

[Read usage guidelines](/solutions/guidance-disclaimers/)
