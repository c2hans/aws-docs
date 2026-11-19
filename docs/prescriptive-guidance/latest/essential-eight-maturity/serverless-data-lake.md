---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/serverless-data-lake.html
---

# Workload example: Serverless data lake

This workload is an example of [Theme 1: Use managed services](theme-1.md).

The data lake uses Amazon S3 for storage and AWS Lambda for extract, transform, and load (ETL). You define these resources in an AWS Cloud Development Kit (AWS CDK) app. The application team deploys changes to the system through AWS CodePipeline. Only the application team can access this pipeline. When the application team makes a pull request for the code repository, the team follows the [two-person rule](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-5.2---implement-least-privilege-policies-for-source-and-downstream-systems..html).

For this workload, the application team takes the following actions to address the Essential Eight strategies.

## Application control
<a name="application-control.97d64278-e088-56d7-9692-c56f2ebdf59f"></a>
+ The application team enables [Lambda Protection](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection.html) in GuardDuty and [Lambda scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html) in Amazon Inspector.
+ The application team implements mechanisms to inspect and [manage Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-automating-responses.html#findings-managing-eventbridge-tutorial).

## Patch applications
<a name="patch-applications.dcde01ad-6505-5393-b5a2-b8cc660f093d"></a>
+ The application team enables Lambda scanning in Amazon Inspector and configures alerts for deprecated or vulnerable libraries.
+ The application team enables AWS Config to track AWS resources for asset discovery.

## Restrict administrative privileges
<a name="restrict-administrative-privileges.09aecd65-5732-55a3-8bbc-af66581a8633"></a>
+ As described in the [Core architecture](scenario.md#core-architecture) section, the application team already restricts access to production deployments through an approval rule on their deployment pipeline.
+ The application team relies on the centralized identity federation and centralized logging solutions that the [Core architecture](scenario.md#core-architecture) section describes.
+ The application team creates an AWS CloudTrail trail and Amazon CloudWatch filters.
+ The application team sets up Amazon Simple Notification Service (Amazon SNS) alerts for CodePipeline deployments and AWS CloudFormation stack deletions.

## Patch operating systems
<a name="patch-operating-systems.f8197a7d-998d-5538-aa6b-82421e27b53e"></a>
+ The application team enables Lambda scanning in Amazon Inspector and configures alerts for deprecated or vulnerable libraries.

## Multi-factor authentication
<a name="multi-factor-authentication.d18dffe7-82e3-5307-9d97-d66e87eca3bf"></a>
+ The application team relies on the centralized identity federation solution described in the [Core architecture](scenario.md#core-architecture) section. This solution enforces multi-factor authentication (MFA), logs authentications, and alerts on or automatically responds to suspicious MFA events.

## Regular backups
<a name="regular-backups.15145daa-55f2-51c6-8b4d-4c39c5c4e829"></a>
+ The application team stores code, such as AWS CDK apps and Lambda functions and configurations, in a [code repository](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider/).
+ The application team enables versioning and Amazon S3 Object Lock to help prevent objects from deletion or modification.
+ The application team relies on built-in Amazon S3 durability rather than replicating their entire dataset to another AWS Region.
+ The application team runs a copy of the workload in another AWS Region that meets their data sovereignty requirements. They use Amazon DynamoDB global tables and Amazon S3 [Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario) to replicate data automatically from the primary Region to the secondary Region.
