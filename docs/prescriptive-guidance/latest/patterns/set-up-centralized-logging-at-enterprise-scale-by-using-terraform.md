---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html
---

# Set up centralized logging at enterprise scale by using Terraform
<a name="set-up-centralized-logging-at-enterprise-scale-by-using-terraform"></a>

*Aarti Rajput, Yashwant Patel, and Nishtha Yadav, Amazon Web Services*

## Summary
<a name="set-up-centralized-logging-at-enterprise-scale-by-using-terraform-summary"></a>

Centralized logging is vital for an organization's cloud infrastructure, because it provides visibility into its operations, security, and compliance. As your organization scales its AWS environment across multiple accounts, a structured log management strategy becomes fundamental for running security operations, meeting audit requirements, and achieving operational excellence.

This pattern provides a scalable, secure framework for centralizing logs from multiple AWS accounts and services, to enable enterprise-scale logging management across complex AWS deployments. The solution is automated by using Terraform, which is an infrastructure as code (IaC) tool from HashiCorp that ensures consistent and repeatable deployments, and minimizes manual configuration. By combining Amazon CloudWatch Logs, Amazon Data Firehose, and Amazon Simple Storage Service (Amazon S3), you can implement a robust log aggregation and analysis pipeline that delivers:
+ Centralized log management across your organization in AWS Organizations
+ Automated log collection with built-in security controls
+ Scalable log processing and durable storage
+ Simplified compliance reporting and audit trails
+ Real-time operational insights and monitoring

The solution collects logs from Amazon Elastic Kubernetes Service (Amazon EKS) containers, AWS Lambda functions, and Amazon Relational Database Service (Amazon RDS) database instances through CloudWatch Logs. It automatically forwards these logs to a dedicated logging account by using CloudWatch subscription filters. Firehose manages the high-throughput log streaming pipeline to Amazon S3 for long-term storage. Amazon Simple Queue Service (Amazon SQS) is configured to receive Amazon S3 event notifications upon object creation. This enables integration with analytics services, including:
+ Amazon OpenSearch Service for log search, visualization, and real-time analytics
+ Amazon Athena for SQL-based querying
+ Amazon EMR for large-scale processing
+ Lambda for custom transformation
+ Amazon Quick Sight for dashboards

All data is encrypted by using AWS Key Management Service (AWS KMS), and the entire infrastructure is deployed by using Terraform for consistent configuration across environments.

This centralized logging approach enables organizations to improve their security posture, maintain compliance requirements, and optimize operational efficiency across their AWS infrastructure.

## Prerequisites and limitations
<a name="set-up-centralized-logging-at-enterprise-scale-by-using-terraform-prereqs"></a>

**Prerequisites**
+ A landing zone for your organization that's built by using [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)
+ [Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-getting-started.html), deployed and configured with required accounts
+ [Terraform](https://developer.hashicorp.com/terraform/downloads) for provisioning the infrastructure
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html) roles and policies for cross-account access

For instructions for setting up AWS Control Tower, AFT, and Application accounts, see the [Epics section](#set-up-centralized-logging-at-enterprise-scale-by-using-terraform-epics).

**Required accounts**

Your organization in AWS Organizations should include these accounts:
+ **Application account** – One or more source accounts where the AWS services (Amazon EKS, Lambda, and Amazon RDS) run and generate logs
+ **Log Archive account** – A dedicated account for centralized log storage and management

**Product versions**
+ [AWS Control Tower version 3.1](https://docs.aws.amazon.com/controltower/latest/userguide/2023-all.html#lz-3-1) or later
+ [Terraform version 0.15.0](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) or later

## Architecture
<a name="set-up-centralized-logging-at-enterprise-scale-by-using-terraform-architecture"></a>

The following diagram illustrates an AWS centralized logging architecture that provides a scalable solution for collecting, processing, and storing logs from multiple Application accounts into a dedicated Log Archive account. This architecture efficiently handles logs from AWS services, including Amazon RDS, Amazon EKS, and Lambda, and routes them through a streamlined process to Regional S3 buckets in the Log Archive account.

![AWS centralized logging architecture for collecting logs from multiple Application accounts.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9fc71a10-65d6-437b-9128-cc27bda11af4/images/2e916040-0f11-4712-a8dd-31c95194ce5d.png)

The workflow includes five processes:

1. **Log flow process**
   + The log flow process begins in the Application accounts, where AWS services generate various types of logs, such as general, error, audit, slow query logs from Amazon RDS, control plane logs from Amazon EKS, and function execution and error logs from Lambda.
   + CloudWatch serves as the initial collection point. It gathers these logs at the log group level within each application account.
   + In CloudWatch, [subscription filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html) determine which logs should be forwarded to the central account. These filters give you granular control over log forwarding, so you can specify exact log patterns or complete log streams for centralization.

1. **Cross-account log transfer**
   + Logs move to the Log Archive account. CloudWatch subscription filters facilitate the cross-account transfer and preserve Regional context.
   + The architecture establishes multiple parallel streams to handle different log sources efficiently, to ensure optimal performance and scalability.

1. **Log processing in the Log Archive account**
   + In the Log Archive account, Firehose processes the incoming log streams.
   + Each Region maintains dedicated Firehose delivery streams that can transform, convert, or enrich logs as needed.
   + These Firehose streams deliver the processed logs to S3 buckets in the Log Archive account, which is located in the same Region as the source Application accounts (Region A in the diagram) to maintain data sovereignty requirements.

1. **Notifications and additional workflows**
   + When logs reach their destination S3 buckets, the architecture implements a notification system by using Amazon SQS.
   + The Regional SQS queues enable asynchronous processing and can trigger additional workflows, analytics, or alerting systems based on the stored logs.

1. **AWS KMS for security**

   The architecture incorporates AWS KMS for security. AWS KMS provides encryption keys for the S3 buckets. This ensures that all stored logs maintain encryption at rest while keeping the encryption Regional to satisfy data residency requirements.

## Tools
<a name="set-up-centralized-logging-at-enterprise-scale-by-using-terraform-tools"></a>

**AWS services**
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) is a monitoring and observability service that collects monitoring and operational data in the form of logs, metrics, and events. It provides a unified view of AWS resources, applications, and services that run on AWS and on-premises servers.
+ [CloudWatch Logs subscription filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html) are expressions that match a pattern in incoming log events and deliver matching log events to the specified AWS resource for further processing or analysis.
+ [AWS Control Tower Account Factory For Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html) sets up a Terraform pipeline to help you provision and customize accounts in AWS Control Tower. AFT provides Terraform-based account provisioning while allowing you to govern your accounts with AWS Control Tower.
+ [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) delivers real-time streaming data to destinations such as Amazon S3, Amazon Redshift, and Amazon OpenSearch Service. It automatically scales to match the throughput of your data and requires no ongoing administration.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) is a managed container orchestration service that makes it easy to deploy, manage, and scale containerized applications by using Kubernetes. It automatically manages the availability and scalability of the Kubernetes control plane nodes.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) creates and controls encryption keys for encrypting your data. AWS KMS integrates with other AWS services to help you protect the data you store with these services.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a serverless compute service that lets you run code without provisioning or managing servers. It automatically scales your applications by running code in response to each trigger, and charges only for the compute time that you use.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) is a managed relational database service that makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while automating time-consuming administration tasks.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) is a message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. It eliminates the complexity of managing and operating message-oriented middleware.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that offers scalability, data availability, security, and performance. It can store and retrieve any amount of data from anywhere on the web.

**Other tools**
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code**

The code for this pattern are available in the GitHub[ Centralized logging](https://github.com/aws-samples/sample-centralised-logging-at-enterprise-scale-using-terraform) repository.

## Best practices
<a name="set-up-centralized-logging-at-enterprise-scale-by-using-terraform-best-practices"></a>
+ Use [multiple AWS accounts in a single organization in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html). This practice enables centralized management and standardized logging across accounts.
+ Configure [S3 buckets with versioning, lifecycle policies, and cross-Region replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html). Implement encryption and access logging for security and compliance.
+ Implement [common logging standards by using JSON format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData-discoverable-fields.html) with standard timestamps and fields. Use a consistent prefix structure and correlation IDs for easy tracking and analysis.
+ Enable [security controls with AWS KMS encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) and least privilege access. Maintain AWS CloudTrail monitoring and regular key rotation for enhanced security.
+ Set up [CloudWatch metrics and alerts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) for delivery tracking. Monitor costs and performance with automated notifications.
+ Configure [Amazon S3 retention policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to meet compliance requirements and enable Amazon S3 server access logging to track all requests made to your S3 buckets. Maintain documentation for S3 bucket policies and lifecycle rules. Conduct periodic reviews of access logs, bucket permissions, and storage configurations to help ensure compliance and [security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html).

## Epics
<a name="set-up-centralized-logging-at-enterprise-scale-by-using-terraform-epics"></a>

### Set up AWS Control Tower, AFT, and Application accounts
<a name="set-up-ctowerlong-aft-and-application-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up an AWS Control Tower environment with AFT. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | AWS administrator |
| Enable resource sharing for the organization. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | AWS administrator |
| Verify or provision Application accounts. | To provision new Application accounts for your use case, create them through AFT. For more information, see [Provision a new account with AFT](https://docs.aws.amazon.com/controltower/latest/userguide/aft-provision-account.html) in the AWS Control Tower documentation. | AWS administrator |

### Set up configuration files for Application accounts
<a name="set-up-configuration-files-for-application-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Copy `Application_account` folder contents into the `aft-account-customizations` repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | DevOps engineer |
| Review and edit the input parameters for setting up the Application account. | In this step, you set up the configuration file for creating resources in Application accounts, including CloudWatch log groups, CloudWatch subscription filters, IAM roles and policies, and configuration details for Amazon RDS, Amazon EKS, and Lambda functions.<br />In your `aft-account-customizations` repository, in the `Application_account` folder, configure the input parameters in the `terraform.tfvars` file based on your organization's requirements:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | DevOps engineer |

### Set up configuration files for the Log Archive account
<a name="set-up-configuration-files-for-the-log-archive-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Copy `Log_archive_account` folder contents into the `aft-account-customizations` repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | DevOps engineer |
| Review and edit the input parameters for setting up the Log Archive account. | In this step, you set up the configuration file for creating resources in the Log Archive account, including Firehose delivery streams, S3 buckets, SQS queues, and IAM roles and policies.<br />In the `Log_archive_account` folder of your `aft-account-customizations` repository, configure the input parameters in the `terraform.tfvars` file based on your organization's requirements:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | DevOps engineer |

### Run Terraform commands to provision resources
<a name="run-terraform-commands-to-provision-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Option 1 - Deploy the Terraform configuration files from AFT. | In AFT, the AFT pipeline is triggered after you push the code with the configuration changes to the GitHub `aft-account-customizations` repository. AFT automatically detects the changes and initiates the account customization process.<br />After you make changes to your Terraform (`terraform.tfvars`) files, commit and push your changes to your `aft-account-customizations` repository:<pre>$ git add *<br />$ git commit -m "update message"<br />$ git push origin main</pre>If you're using a different branch (such as `dev`), replace `main` with your branch name. | DevOps engineer |
| Option 2 - Deploy the Terraform configuration file manually. | If you aren't using AFT or you want to deploy the solution manually, you can use the following Terraform commands from the `Application_account` and `Log_archive_account` folders:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | DevOps engineer |

### Validate resources
<a name="validate-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify subscription filters. | To verify that the subscription filters forward logs correctly from the Application account log groups to the Log Archive account:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | DevOps engineer |
| Verify Firehose streams. | To verify that the Firehose streams in the Log Archive account process application logs successfully:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | DevOps engineer |
| Validate the centralized S3 buckets. | To verify that the centralized S3 buckets receive and organize logs properly:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | DevOps engineer |
| Validate SQS queues. | To verify that the SQS queues receive notifications for new log files:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | DevOps engineer |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Option 1 - Decommission the Terraform configuration file from AFT. | When you remove the Terraform configuration files and push the changes, AFT automatically initiates the resource removal process.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | DevOps engineer |
| Option 2 – Clean up  Terraform resources manually. | If you aren't using AFT or you want to clean up resources manually, use the following Terraform commands from the `Application_account` and `Log_archive_account` folders:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) | DevOps engineer |

## Troubleshooting
<a name="set-up-centralized-logging-at-enterprise-scale-by-using-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The CloudWatch Logs destination wasn't created or is inactive. | Validate the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) |
| The subscription filter failed or is stuck in pending status. | Check the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) |
| The Firehose delivery stream shows no incoming records. | Verify the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-centralized-logging-at-enterprise-scale-by-using-terraform.html) |

## Related resources
<a name="set-up-centralized-logging-at-enterprise-scale-by-using-terraform-resources"></a>
+ [Terraform infrastructure setup](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) (Terraform documentation)
+ [Deploy AWS Control Tower Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-getting-started.html) (AWS Control Tower documentation)
+ [IAM tutorial: Delegate access across AWS accounts using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) (IAMdocumentation)
