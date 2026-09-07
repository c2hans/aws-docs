---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/aws-cloudformation-templates.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-templates"></a>

This solution uses AWS CloudFormation to automate the deployment of the Cloud Migration Factory on AWS solution in the AWS Cloud. It includes the following AWS CloudFormation template, which you can download before deployment.

 [![View Template](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/cloud-migration-factory-on-aws/latest/aws-cloud-migration-factory-solution.template) **aws-cloud-migration-factory-solution.template** - Use this template to launch the Cloud Migration Factory on AWS solution and all associated components. The default configuration deploys AWS Lambda functions, Amazon DynamoDB tables, an Amazon API Gateway, Amazon CloudFront, Amazon S3 buckets, an Amazon Cognito user pool, AWS Systems Manager Automation Document, and [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) secrets, but you can also customize the template based on your specific needs.

 [![View Template](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/cloud-migration-factory-on-aws/latest/aws-cloud-migration-factory-solution-target-account.template) **aws-cloud-migration-factory-solution-target-account.template** - Use this template to launch the Cloud Migration Factory on AWS solution target account(s). The default configuration deploys IAM roles and a user, but you can also customize the template based on your specific needs.
