---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/your-business-logic-goes-here-no-servers-necessary.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Your business logic goes here, no servers necessary
<a name="your-business-logic-goes-here-no-servers-necessary"></a>

 Lambda requires you to write code functions, called *handlers*, which will run when initiated by an event. To use Lambda with API Gateway, you can configure API Gateway to launch handler functions when an HTTPS request to your API occurs. In a serverless multi-tier architecture, each of the APIs you create in API Gateway will integrate with a Lambda function (and the handler within) that invokes the business logic required.

 Using AWS Lambda functions to compose the logic tier enables you to define a desired level of granularity for exposing the application functionality (one Lambda function per API or one Lambda function per API method). Inside the Lambda function, the handler can reach out to any other dependencies (for example, other methods you’ve uploaded with your code, libraries, native binaries, and external web services), or even other Lambda functions.

 Creating or updating a Lambda function requires either uploading code as a Lambda deployment package in a zip file to an Amazon S3 bucket, or packaging code as a container image along with all the dependencies. The functions can use different deployment methods, such as [AWS Management Console](https://aws.amazon.com/console/), running AWS Command Line Interface (AWS CLI), or running infrastructure as code templates or frameworks such as [CloudFormation](https://aws.amazon.com/cloudformation/), [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) (AWS SAM), or [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/). When you create your function using any of these methods, you specify which method inside your deployment package will act as the request handler. You can reuse the same deployment package for multiple Lambda function definitions, where each Lambda function might have a unique handler within the same deployment package.
