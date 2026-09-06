---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/aws-cloudformation-template.html
---

# AWS CloudFormation template
<a name="aws-cloudformation-template"></a>

 To automate deployment, this Guidance uses the following AWS CloudFormation templates, which you can download before deployment:

 [![View template button](http://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/data-transfer-hub/latest/DataTransferHub-cognito.template) **DataTransferHub-cognito.template:** Use this template to launch the Guidance and all associated components in **AWS Regions** where Amazon Cognito is available. The default configuration deploys Amazon S3, Amazon CloudFront, AWS AppSync, Amazon DynamoDB, AWS Lambda, Amazon ECS, and Amazon Cognito, but you can customize the template to meet your specific needs.

 [![View template button](http://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/data-transfer-hub/latest/DataTransferHub-openid.template) **DataTransferHub-openid.template:** Use this template to launch the Guidance and all associated components in **AWS China Regions** where Amazon Cognito is **not** available. The default configuration deploys The default configuration deploys Amazon S3, Amazon CloudFront, AWS AppSync, Amazon DynamoDB, AWS Lambda, and Amazon ECS, but you can customize the template to meet your specific needs.
