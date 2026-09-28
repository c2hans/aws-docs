---
source_url: https://docs.aws.amazon.com/solutions/multi-account-environments-on-amazon-quicksight/index.html
---

---
title: 'Guidance for Multi-Account Environments on Amazon QuickSight'
canonical_url: https://docs.aws.amazon.com/solutions/multi-account-environments-on-amazon-quicksight/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Multi-Account Environments on Amazon QuickSight

## Overview

This Guidance provides a unified way to build Amazon QuickSight environments spanning multiple accounts. This enables you to host assets from different development phases separately and promote them using a continuous integration and continuous delivery (CI/CD) pipeline. It allows you to host assets from different development phases separately across these accounts. This approach provides improved isolation, security, access management, and cost tracking. As a result, you can efficiently manage your service quotas, quickly identify resources used for individual workloads, and reduce the impact of an unexpected security event. There are two deployment modes for this Guidance, one uses a QuickSight template, and the other uses an asset bundle API. You can adapt either for your business needs while still adhering to AWS best practices, such as isolating production and non-production workloads for enhanced security and stability of your assets.

## How it works

### Amazon QuickSight template

There are two deployment modes for this Guidance, the first one uses an Amazon QuickSight template, the second uses an asset bundle API. This architecture diagram displays the configuration of deploying a QuickSight template. For details on the asset bundle API deployment mode, refer to the next tab.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/multi-account-environments-on-amazon-quicksight.pdf)Step 1An Amazon EventBridge rule invokes the QSAssetsCFNSynthesizer AWS Lambda function when a new dashboard version is deployed.Step 2The Lambda function describes the Amazon QuickSight assets that were created manually in the development account and generates AWS CloudFormation templates.Step 3The CloudFormation templates are uploaded to Amazon Simple Storage Service (Amazon S3). Two templates are generated: source assets which create an analysis template, and destination assets, which create an analysis from the QuickSight template and its required datasets and data sources.Step 4Amazon S3 is configured as the source stage for AWS CodePipeline and acts as the source repository for the pipeline deployments.Step 5CodePipeline is configured with two deployment stages for production and preproduction. The promotion to production is protected with a manual approval to prevent uncontrolled promotion of assets.Step 6The first stage will deploy the source assets CloudFormation template in the development account, which creates a QuickSight template in development that models the analysis to be promoted across the environments. Then the destination assets' CloudFormation template is deployed in preproduction, creating a QuickSight analysis and its dependent assets (such as DataSource and DataSets).Step 7Deployment to production will be kept on hold with a manual approval until the assets have been reviewed in preproduction.Step 8Once the assets have been reviewed and approved, the second stage will deploy the source assets template to model the QuickSight assets that were previously created in preproduction. The second stage will then deploy the destination assets to create the QuickSight analysis and its depending assets in production.### Asset Bundle API

This architecture diagram displays the asset bundle API deployment mode.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/multi-account-environments-on-amazon-quicksight.pdf)Step 1An EventBridge rule invokes the QSAssetsCFNSynthesizer Lambda function when a new dashboard version is deployed.Step 2The Lambda function uses the QuickSight advanced deployment APIs (AssetBundle) to generate a CloudFormation template that models the development analysis and all its depending assets (such as DataSource and DataSets).Step 3The CloudFormation templates are uploaded to Amazon S3. Two templates are generated: source assets, which will be empty in this case, and destination assets, which create an analysis from the CloudFormation template generated in the previous step.Step 4Amazon S3 is configured as the source stage for CodePipeline and acts as the source repository for the pipeline deployments.Step 5CodePipeline is configured with two deployment stages for production and preproduction. The promotion to production is protected with a manual approval to prevent uncontrolled promotion of assets.Step 6The first stage will deploy the source assets CloudFormation template in the development account (empty in this deployment mode) and then the destination assets CloudFormation template in preproduction, creating a QuickSight analysis and its depending assets (such as DataSource and DataSets).Step 7Deployment to production will be kept on hold with a manual approval until the assets have been reviewed in preproduction.Step 8Once the assets have been reviewed and approved, the second stage will deploy the source assets template in preproduction (empty in this deployment mode) and then the destination assets to create the QuickSight analysis and its depending assets in production.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-multi-account-environment-on-amazon-quicksight)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CodePipeline provides continuous delivery across different environments or stages without human intervention. This helps you reduce maintenance, complexity, and the introduction of errors. Additionally, you can configure a manual approval action, sent to an Amazon Simple Notification Service (Amazon SNS) topic, to prevent unwanted changes from reaching critical environments, such as production. CodePipeline uses CloudFormation to deploy assets in a repeatable, auditable, and scalable way, managing the entire asset lifecycle. For auditability, Lambda sends logs that are useful for visibility and troubleshooting. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

In this Guidance, AWS Identity and Access Management (IAM) resource policies have all been scoped down to the minimum permissions required for the resources to work properly. IAM also allows audited and authorized access to assets between accounts. For example, the Lambda function can upload data to a bucket in a different account by assuming an IAM role as an identity. Additionally, AWS Key Management Service (AWS KMS) encrypts content that is sent to the Amazon SNS topic, both in transit and at rest, until it is delivered through the selected method (such as email). [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

QuickSight, CloudFormation, and Lambda are Regional AWS managed services that are designed for reliability and fault tolerance. These services help make the solution secure, reliable, and scalable while reducing its complexity. Additionally, Lambda and CloudFormation play a key role in deploying resources across accounts, providing an extra layer of isolation (such as for different software lifecycle environments) and a disaster recovery environment. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

CloudFormation provides a simple, reliable, and repeatable way to deploy your assets across AWS accounts or AWS Regions within minutes. By using it (as a deployment provider) in conjunction with CodePipeline, you can automate the deployment of changes across all environments. Through QuickSight and the ability to implement continuous deployment of assets, you can democratize access to business intelligence tools at scale in your company, making data consumption easier. This also improves your company’s agility in experimenting and developing new functionalities or features. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda, CodePipeline, and QuickSight are serverless, so you can avoid the cost of maintaining your own servers. Additionally, they scale up and down based on demand, helping you reduce costs by only paying for the resources you use. For CodePipeline, you only pay for each pipeline that is active per month, and because CloudFormation is used as the deployment provider, there are no deployment costs. For Lambda, you pay only for the implementation time and memory that your functions use. Finally, for QuickSight, you pay for provisioned authors, and you pay when readers access the platform. However, QuickSight charges only up to a maximum price to keep costs predictable. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Due to their serverless nature, Lambda, CodePipeline, Amazon S3, and QuickSight can dynamically scale based on demand, which means that resources never run when they are not needed. This helps minimize emissions and their associated environmental impact. Additionally, this Guidance uses an Amazon S3 lifecycle feature that automatically deletes assets based on an age and version history rules, helping reduce the resources dedicated to storage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
