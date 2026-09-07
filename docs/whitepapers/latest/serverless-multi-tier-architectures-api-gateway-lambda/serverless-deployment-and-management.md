---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/serverless-deployment-and-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Serverless deployment and management
<a name="serverless-deployment-and-management"></a>

 To help you deploy and manage your Lambda functions, use [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/) (AWS SAM), an open-source framework that includes:
+  **AWS SAM template specification - ** Syntax used to define your functions and describe their environments, permissions, configurations, and events for simplified upload and deployment.
+  **AWS SAM CLI - ** Commands that enable you to verify SAM template syntax, invoke functions locally, debug Lambda functions, and deploy package functions.

 You can also use AWS CDK, which is a software development framework for defining cloud infrastructure using programming languages and provisioning it through CloudFormation. CDK provides an imperative way to define AWS resources, whereas AWS SAM provides a declarative way.

 Typically, when you deploy a Lambda function, it is invoked with permissions defined by its assigned IAM role, and is able to reach internet-facing endpoints. As the core of your logic tier, AWS Lambda is the component directly integrating with the data tier. If your data tier contains sensitive business or user information, it is important to ensure that this data tier is appropriately isolated (in a private subnet).

 You can configure a Lambda function to connect to private subnets in a virtual private cloud (VPC) in your AWS account if you want the Lambda function to access resources that you cannot expose publicly, like a private database instance. When you connect a function to a VPC, Lambda creates an elastic network interface for each subnet in your function's VPC configuration and elastic network interface is used to access your internal resources privately.

![Lambda architecture pattern inside a VPC](https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/images/lambda-architecture-pattern.png)

* Lambda architecture pattern inside a VPC *

 The use of Lambda with VPC means that databases and other storage media that your business logic depends on can be made inaccessible over the internet. The VPC also ensures that the only way to interact with your data from the internet is through the APIs that you’ve defined and the Lambda code functions that you have written.
