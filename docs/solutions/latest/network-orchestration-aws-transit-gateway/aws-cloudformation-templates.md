---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/aws-cloudformation-templates.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-templates"></a>

This solution uses CloudFormation to automate its deployment in the AWS Cloud. It includes the following AWS CloudFormation templates, which you can download before deployment.

**Note**
AWS CloudFormation resources are created from AWS CDK constructs.

 [![network orchestration hub view template button](http://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/network-orchestration-for-aws-transit-gateway/latest/network-orchestration-hub.template) **network-orchestration-hub.template** - Use this template to launch the solution and all associated components in your AWS network hub account. The default configuration deploys the following:
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

 [![network orchestration hub service-linked roles view template button](http://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/network-orchestration-for-aws-transit-gateway/latest/network-orchestration-hub-service-linked-roles.template) **network-orchestration-hub-service-linked-roles.template** - Optionally use this template to launch the service-linked role for AWS RAM in your hub account. This stack is optional because it fails if the `AWSServiceRoleForResourceAccessManager` role already exists in the hub account.

 [![network orchestration hub view template button](http://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/network-orchestration-for-aws-transit-gateway/latest/network-orchestration-spoke.template) **network-orchestration-spoke.template** - Use this template to launch the solution and all associated components in your spoke account(s). The default configuration deploys EventBridge rules and IAM roles.

 [![network orchestration hub view template button](http://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/network-orchestration-for-aws-transit-gateway/latest/network-orchestration-organization-role.template) **network-orchestration-organization-role.template** - Use this template to create an IAM role in the Organizations management account. The hub account requires this role to create easily-identifiable names for the transit gateway attachments, using a combination of OU path and VPC name.
