---
source_url: https://docs.aws.amazon.com/solutions/carbon-accounting-on-aws/index.html
---

# Guidance for Carbon Accounting on AWS

## Overview

This Guidance helps customers calculate their carbon footprints, track their Greenhouse gas (GHG) emitting activities, and identify carbon hotspots. The [Guidance for Sustainability Insights Framework on AWS](/solutions/sustainability-insights-framework-on-aws/) provides the software building blocks to help accelerate the design, implementation, or expansion of applications to automate carbon footprint tracking.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/carbon-accounting-on-aws.pdf)

![Architecture diagram](/images/solutions/carbon-accounting-on-aws/images/carbon-accounting-on-aws-1.png)

1. **Step 1**: Sustainability subject matter experts (SMEs) and operations personnel submit their respective data sources through a web application built on top of the Sustainability Insights Framework (SIF) on AWS.
1. **Step 2**: Amazon Route 53, the Domain Name System (DNS) service, enables front-end clients to resolve the website hostname to Amazon CloudFront, the AWS content delivery network. CloudFront routes the web requests to the origin servers and caches the static content and assets served from Amazon Simple Storage Service (Amazon S3) and origin servers. It secures the application traffic using AWS WAF (a web application firewall) to protect the application against common exploits and bots. This web app exposes the access patterns shown in steps 4-9.
1. **Step 3**: An administrator uses the SIF Access Management module to configure roles such as sustainability experts, auditors, executives, and operations managers. For example, an auditor could have read-only access to all calculation logs, and an operations manager could have access to submit new activity information (step 7). The SIF Access Management module controls fine-grained permissions to resources in other SIF modules.
1. **Step 4**: The sustainability SME selects the emission factors that are most representative of their business activities and loads them into the SIF Impacts module. Emission factors in this module can be applied in the carbon footprint calculations of a pipeline.
1. **Step 5**: A user can define reference data (called "mappings") in the SIF Reference Datasets module. This data can then be used in calculations. For example: mapping a location's US postal code to the corresponding electrical grid region when calculating a carbon footprint.
1. **Step 6**: The sustainability SME defines the calculations based on the methodology required for reporting. The SIF Calculations module allows users to define reusable formulas for carbon accounting of scopes 1, 2, and 3 business activities (such as the fuel consumption of vehicles).
1. **Step 7**: Users create pipelines that specify the data source formats and the calculations to run on those data sources in the SIF Pipelines module. For example, the sustainability SME defines a pipeline to calculate the carbon footprint of fuel consumption from truck transportation using a standardized form that operations managers complete.
1. **Step 8**: Data from business operations is uploaded and transformed into carbon footprint data using the SIF Pipelines Processors module. Once the data has been processed through the pipelines, dashboards or reports can be configured for carbon emissions tracking and operations monitoring.
1. **Step 9**: The user can configure dashboards or reports to track scopes 1, 2, and 3 such as emissions and other metrics required for climate disclosures. The user can also use the dashboards to identify carbon hotspots, review progress towards climate targets, and draw insights for decarbonization planning.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Monitor your organization's operational health and notify operators of faults with Amazon CloudWatch, where you can customize metrics, alarms, and dashboards. For more on how to gain insights into your operations, see the Guidance for Sustainability Insights Framework on AWS. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Resources deployed by this Guidance are protected by AWS Identity and Access Management (IAM) policies and principles. CloudFront allows customers to enable TLS to secure data in transit and also makes use of AWS WAF for additional protection. User authentication is managed through Amazon Cognito, and all APIs use a Cognito authorizer. Data is protected through access controls implemented by IAM and Amazon S3 bucket policies. The Guidance for Sustainability Insights Framework on AWS provides in-depth, best-practices for architecting secure workloads on AWS. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

To help your workloads perform their intended function correctly and consistently, this Guidance uses a serverless web application that scales automatically and is automatically deployed across multiple Availability Zones. The architecture is managed through an AWS Cloud Development Kit (AWS CDK). Implementing reliable workloads for carbon footprint tracking is detailed further in the Guidance for Sustainability Insights Framework on AWS. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

CloudFront, a serverless application that caches content, decreases latency to the end user. The Guidance for Sustainability Insights Framework on AWShas more on the efficient use of computing resources. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

With the serverless web application this Guidance uses, you only pay for what you use. Caching through CloudFront reduces data transfer and access costs for Amazon S3. For the cost implications of the Sustainability Insights Framework of this Guidance, please refer to theGuidance for Sustainability Insights Framework on AWS. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

All computing resources in this Guidance run through AWS Lambda that does not require any hardware provisioning when not in use. Reducing your total resources is further detailed in the Guidance for Sustainability Insights Framework on AWS. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
