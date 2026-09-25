---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/aws-cloudformation-templates.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-templates"></a>

This Guidance uses CloudFormation to automate its deployment in the AWS Cloud. It includes the following AWS CloudFormation templates, which the build process generates in `./deployment/global-s3-assets/`.

**Note**
You can review the source templates in the repository’s [deployment/ directory](https://github.com/aws-solutions-library-samples/network-orchestration-for-aws-transit-gateway/tree/main/deployment). Don’t deploy these templates as-is. They are source templates that contain build placeholders, such as `%DIST_BUCKET_NAME%` and `%VERSION%`. They also load the Lambda code, AWS AppSync resolvers, and web console assets from `<BUCKET_BASE_NAME>-<region>` in your own account and Region. Run the steps in [Step 1: Build deployment assets](step-1-build-deployment-assets.md) first. Those steps fill in the placeholders, generate the templates in `./deployment/global-s3-assets/`, and stage the assets in your bucket.

**Note**
AWS CloudFormation resources are created from AWS CDK constructs.

 **network-orchestration-hub.template** - Use this template to launch the Guidance and all associated components in your AWS network hub account. The default configuration deploys the following:
+ One transit gateway
+ Four transit gateway route tables
+ One global network in Transit Gateway network manager
+ Step Functions (to orchestrate VPC and transit gateway attachments)
+ One [AWS Resource Access Manager](https://aws.amazon.com/ram) (AWS RAM) resource share
+ One optional web UI with the following resources:
  + One DynamoDB table
  + EventBridge event bus and rules
  + IAM roles
+ One optional web UI for network management with the following resources:
  + One Amazon SNS topic
  + AWS AppSync API with WAF
  + One Amazon Cognito user pool
  + One CloudFront distribution with a CloudFront function
  + Amazon S3 buckets

 **network-orchestration-hub-service-linked-roles.template** - Optionally use this template to launch the service-linked role for AWS RAM in your hub account. This stack is optional because it fails if the `AWSServiceRoleForResourceAccessManager` role already exists in the hub account.

 **network-orchestration-spoke.template** - Use this template to launch all associated components in your spoke account(s). The default configuration deploys EventBridge rules and IAM roles.

 **network-orchestration-organization-role.template** - Use this template to create an IAM role in the Organizations management account. The hub account requires this role to create easily identifiable names for the transit gateway attachments, using a combination of OU path and VPC name.
