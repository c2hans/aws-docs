---
source_url: https://docs.aws.amazon.com/solutions/advanced-cloud-observability-with-cloud-intelligence-dashboards-on-aws/index.html
---

---
title: 'Cloud Intelligence Dashboards on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/advanced-cloud-observability-with-cloud-intelligence-dashboards-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Cloud Intelligence Dashboards on AWS

## Overview

This solution demonstrates how to deploy Cloud Intelligence Dashboards in your AWS environment using AWS CloudFormation templates or command line tools. These pre-built dashboards enable you to drive financial accountability, optimize costs, and track usage goals across their AWS infrastructure. The solution also implements governance best practices and supports operational excellence through automated deployment, secure data handling, and efficient serverless architecture. By providing comprehensive visibility into cost and usage patterns, these dashboards can help you make informed decisions about your AWS resources while maintaining security and performance standards. These pre-built dashboards help customers drive financial accountability, optimize cost, track usage goals, implement best-practices for governance, and achieve operational excellence across all Well Architected pillars.

## How it works

### Foundational dashboards: deployment

This architecture diagram shows how to set up the foundation for cloud observability with Cloud Intelligence Dashboards.

[Download the architecture diagram PDF](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/advanced-cloud-observability-with-cloud-intelligence-dashboards-on-aws.pdf)Step 1Deploy the AWS CloudFormation stack for AWS Data Exports to the Data Collection AWS account.Step 2Deploy the AWS Data Exports CloudFormation stack to the Management (Payer) AWS accounts.Step 3Deploy the Cloud Intelligence Dashboards CloudFormation stack to the Data Collection AWS account.### Foundational dashboards: architecture

This architecture diagram shows the connection flow for foundational Cloud Intelligence Dashboards.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/advanced-cloud-observability-with-cloud-intelligence-dashboards-on-aws.pdf)Step 1AWS Data Exports delivers the AWS Cost & Usage Report (AWS CUR)—specifically CUR 2.0—daily to an Amazon Simple Storage Service (Amazon S3) bucket in the Management (Payer) Account.

Step 2An Amazon S3 replication rule copies export data from the S3 bucket in a Management (Payer) Account to the S3 bucket in the dedicated Data Collection Account automatically.Step 3Amazon Athena allows querying data directly from the aggregated S3 bucket using an AWS Glue table schema definition.Step 4Amazon QuickSight creates datasets from Athena, refreshes daily, and caches them in SPICE (Superfast, Parallel, In-memory Calculation Engine) for QuickSight.Step 5User teams (such as executives, FinOps, and engineers) can access Cloud Intelligence Dashboards in QuickSight. Access is secured through AWS Identity and Access Management (IAM), AWS IAM Identity Center, and optional row-level security.### Advanced dashboards: deployment

This architecture diagram shows the setup for the foundational and advanced Cloud Intelligence Dashboards.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/advanced-cloud-observability-with-cloud-intelligence-dashboards-on-aws.pdf)Step 1Deploy the CloudFormation stack for AWS Data Exports to the Data Collection AWS account.Step 2Deploy the AWS Data Exports CloudFormation stack to the Management (Payer) AWS account(s).Step 3Deploy the Cloud Intelligence Dashboards CloudFormation stack to the Data Collection AWS account.Step 4Deploy the Advanced Data Collection Permissions CloudFormation stack to the Management (Payer) AWS account(s).Step 5The Permissions CloudFormation stack in the Management (Payer) Account also deploys Permissions stacks to each of Linked accounts using StackSets.Step 6Deploy the Data Collection Stack to the Data Collection AWS account.Step 7Deploy the Advanced Dashboards using the Dashboard Plugin CloudFormation stack to the Data Collection AWS Account.### Advanced dashboards: architecture

This architecture diagram shows the connection flow for the foundational and advanced Cloud Intelligence Dashboards.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/advanced-cloud-observability-with-cloud-intelligence-dashboards-on-aws.pdf)Step 1AWS Data Exports delivers AWS CUR reports daily to the S3 bucket in the Management (Payer) Account.Step 2An Amazon S3 replication rule copies Export data from the S3 bucket in a Management (Payer) Account to the S3 bucket in the dedicated Data Collection Account automatically.Step 3Athena allows querying data directly from the S3 bucket using an AWS Glue table schema definition.Step 4QuickSight creates datasets from Athena, refreshes daily, and caches them in SPICE for QuickSight.Step 5User teams (such as executives, FinOps, and engineers) can access Cloud Intelligence Dashboards in QuickSight. Access is secured through IAM, IAM Identity Center, and optional row-level security.Step 6Optionally, the advanced data collection can be deployed to enable advanced dashboards based on AWS Trusted Advisor, AWS Health Events, and other sources. Additional data is retrieved from AWS Organizations or Linked Accounts. In this case, an Amazon EventBridge rule triggers AWS Step Functions for data collection modules on a configurable schedule.Step 7The Account Collector AWS Lambda function in Step Functions retrieves linked account details using an Organizations API.Step 8The Data Collection Lambda function in Step Functions assumes the role in each linked account to retrieve account-specific data using AWS SDK.Step 9Retrieved data is stored in a centralized S3 bucket.Step 10Advanced Cloud Intelligence Dashboards leverage Athena and QuickSight for comprehensive data analysis.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](/guidance/latest/cloud-intelligence-dashboards/getting-started.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code: framework](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework)
[Go to sample code: data collection](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-data-collection)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudFormation automates the deployment process in a dedicated account, adhering to best practices. This solution processes data from AWS CUR, and Trusted Advisor, storing it in Amazon S3. AWS Glue processes this information, which Athena then queries to update QuickSight visualizations. This streamlined workflow helps ensure you always have access to up-to-date cost insights through your dashboards.

### Security

This solution employs role-based access controls and follows the principle of least privilege. Administrators can manage different user personas through a QuickSight and IAM integration or IAM Identity Center, while CloudFormation templates help ensure deployment with minimal required permissions. You can maintain data sovereignty by keeping all cost and usage information within your own S3 buckets, eliminating the need for third-party tools. Even if your organization has multiple Management Accounts, you can enhance security through row-level security, restricting access to only your owned linked accounts' data. Additionally, AWS CUR stored in Amazon S3 can be encrypted at rest for enhanced data protection.

### Reliability

Amazon S3 is a durable storage service for cost and usage data, which AWS Glue and Lambda process before visualization through Athena and QuickSight. This serverless approach provides resilient data processing with automatic retries and failover capabilities. This solution also offers reliability insights, including information on single-Availability Zone virtual private cloud (VPC) endpoints and Trusted Advisor recommendations across the organization. By using a highly available and durable serverless architecture, this solution offers reliable visualization of service usage and billing information, minimizing the risk of downtime or data loss.

### Performance Efficiency

This solution combines Athena views and QuickSight datasets to efficiently process and visualize large-scale data. This approach offers automatic scaling without compromising performance, adapting seamlessly to changing workload demands. By leveraging services like Amazon S3, AWS Glue, Athena, QuickSight, and Lambda, you can maintain high performance efficiency while scaling up or down as needed. This helps you to access and analyze your cost and usage data quickly and efficiently, regardless of the volume of information being processed.

### Cost Optimization

QuickSight offers cost-effective visualization of AWS usage data. You can customize dashboards without incurring additional fees to maximize value. By primarily using serverless services like Amazon S3, AWS Glue, Athena, and Lambda, you pay only for the resources you use, aligning costs directly with actual usage and demand.

### Sustainability

Built on serverless services, including Amazon S3, AWS Glue, Athena, QuickSight, and Lambda, this solution enables organizations to improve financial accountability, cost optimization, and sustainability initiatives. The serverless architecture consumes resources only as needed, supporting a sustainable approach, potentially reducing overall energy consumption and environmental impact.

[Read usage guidelines](/solutions/guidance-disclaimers/)
