---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in the your AWS account.

![architecture diagram](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/architecture-diagram.png)

**Note**
AWS CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) constructs.

The high-level process flow for the solution components deployed with the AWS CloudFormation template is as follows:

1.  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) caches and delivers a single-page application built in React [hosted](https://repost.aws/knowledge-center/cloudfront-serve-static-website) as a static website in an [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket.

1. A [REST API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html) integrates with [Amazon Cognito](https://aws.amazon.com/cognito/) and then passes along authenticated requests to an [AWS Lambda](https://aws.amazon.com/lambda/) function. The Lambda function handles all API requests coming from the frontend.

1.  [Amazon Dynamo DB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) contains several tables that manage information about available modules and the state of enabled modules.

1. External location which hosts [Custom modules](custom-modules.md) developed by AWS Partners.

1.  [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html) hosts the [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) templates for all previously included modules and Third-Party Modules that are registered post-deployment.

1.  [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is used to manage registering and de-registering Third-Party Modules.

1.  [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) contains module parameters that contain sensitive information. Some parameters are deployed by the MCS stack while others are deployed by modules. See the [Developer guide](developer-guide.md) for more information.

1.  [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) contains module parameters that contain sensitive information.

1.  [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is configured to listen to CloudFormation events about modules that are passed along to a Lambda function. The Lambda function processes the events and updates the module’s information in the solution’s [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) tables.

1.  [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) log groups collect and store logs across the solution.

1. The solution registers resources deployed by the stack against [AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) and an application on [myApplications](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/aws-myApplications.html).

1.  [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) roles and policies are used across the solution to manage access and permissions.

1. You can launch this solution’s modules via the web console or API.

1.  [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) delivers operational metrics to [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) where they are transformed and sent to an API destination for monitoring.
