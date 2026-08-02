---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/planning-prerequisites.html
---

# Prerequisites
<a name="planning-prerequisites"></a>

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

You can configure the deployment mode during AWS CloudFormation deployment. These modes provide simpler configuration options for proof of concept or test environments. Both modes are feature compatible.

### Development Mode
<a name="development-mode"></a>
+ Reduced provisioned concurrency
+ Suitable for testing and development

### Production Mode
<a name="production-mode"></a>
+ Provisioned concurrency for AWS Lambda
