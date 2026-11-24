---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/planning-prerequisites.html
---

# Prerequisites

## AWS Account Requirements
<a name="aws-account-requirements"></a>
+ Active AWS account with appropriate permissions
+ Don’t use the AWS Organizations management account – Deploy to a member account instead. The management account should be used only for AWS Organizations administrative tasks. For details, see [AWS Organizations Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html).
+ AWS Command Line Interface (AWS CLI) configured with credentials (optional)
+ AWS CloudFormation stack creation permissions
+ Selected deployment AWS Region

## Permission Requirements
<a name="permission-requirements"></a>

Before deploying the Spatial Data Management solution, verify that your AWS user or role has the necessary permissions to create and manage AWS resources.

 **Console Access Check**

Verify you can access and create resources in these AWS Console sections:

 **Core Services (Required):**
+ CloudFormation
+ IAM
+ Amazon S3
+ AWS Lambda
+ Amazon DynamoDB
+ AWS KMS

 **Application Services (Required):**
+ Amazon Cognito
+ Amazon API Gateway
+ Amazon OpenSearch
+ Amazon VPC/EC2
+ Amazon CloudWatch Logs
+ AWS Deadline Cloud
+ Amazon Location Services

 **Content & Security Services (Required):**
+ Amazon CloudFront
+ AWS Secrets Manager
+ AWS Systems Manager
+ Amazon SQS
+ Amazon EventBridge
+ Amazon Verified Permissions

 **Analytics Services (Required):**
+ AWS Glue
+ Amazon Athena
+ AWS CloudTrail

### Troubleshooting Permission Issues
<a name="troubleshooting-permission-issues"></a>

If deployment fails with permission errors:

1. Check **CloudFormation Events** in the AWS Console for specific error messages

1. Look for "Access Denied" errors in the stack events

1. Verify you can access the failing service in the AWS Console

1. Contact your AWS administrator to grant missing permissions

## Knowledge Requirements
<a name="knowledge-requirements"></a>
+ Basic understanding of AWS services
+ Familiarity with AWS CloudFormation

## Deployment Modes
<a name="deployment-modes"></a>

You can configure the deployment mode during AWS CloudFormation deployment. Dev and Prod are feature compatible. They differ in scale and cost.

### Development Mode
<a name="development-mode"></a>
+ Reduced provisioned concurrency
+ Suitable for testing and development

### Production Mode
<a name="production-mode"></a>
+ Provisioned concurrency for AWS Lambda

### Minimal Mode
<a name="minimal-mode"></a>
+ A reduced-footprint deployment for accounts with reduced AWS service limits
+ AWS Lambda functions have no reserved concurrency
+ Lower performance. Use it only for short-term, very low volume, single-user trials, not for production or proof-of-concept workloads

### AWS Lambda Concurrency
<a name="lambda-concurrency-requirement"></a>

In Dev and Prod modes, the solution reserves AWS Lambda concurrency for four functions: 240 for the resource operation function, 80 for the asset watcher, 40 for connector invocation, and 40 for asynchronous connector invocation. That is 400 in total. Lambda requires at least 100 unreserved concurrent executions in the account, so the account’s concurrent executions quota must be at least 500. If it is lower, request an increase in the Service Quotas console, or use Minimal mode for a trial.
