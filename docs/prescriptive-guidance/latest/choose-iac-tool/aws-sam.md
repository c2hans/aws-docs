---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choose-iac-tool/aws-sam.html
---

# AWS SAM
<a name="aws-sam"></a>

The [AWS Serverless Application Model (AWS SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) is a toolkit that extends AWS CloudFormation. It includes additional features designed to help you create serverless applications more quickly. When you deploy an AWS SAM template, it is converted to CloudFormation in order to create the defined resources. AWS SAM consists of two parts, the [AWS SAM template specification](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html#what-is-sam-template) and the [AWS SAM Command Line Interface (AWS SAM CLI)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html#what-is-sam-cli). Although you can use CloudFormation syntax directly in the AWS SAM template, AWS SAM offers its own unique syntax that focuses specifically on speeding up serverless development. This short-hand syntax allows for optimized definitions of IaC for serverless resources, such as Amazon API Gateway, AWS Lambda, and AWS Step Functions resources. The AWS SAM CLI is a developer tool that includes features to help you test AWS Lambda functions locally, create continuous integration and continuous delivery (CI/CD) pipelines, and run commands to deploy serverless applications.

**Advantages of using AWS SAM:**
+ AWS SAM has the same advantages as CloudFormation.
+ Compared to CloudFormation, you can more easily use AWS SAM to create serverless applications and resources, such as an Amazon API Gateway that is backed by AWS Lambda.
+ Using the AWS SAM CLI, you can test AWS Lambda functions locally. When you locally invoke a Lambda function in debug mode, you can then attach a debugger to it. With the debugger, you can step through your code line by line, see the values of various variables, and fix issues the same way you would for any other application.

**Disadvantages of using AWS SAM:**
+ AWS SAM has the same disadvantages as CloudFormation.
+ AWS SAM cannot be used outside of AWS.
