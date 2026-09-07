---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/simplyfing-operations.html
---

# Simplifying operations
<a name="simplyfing-operations"></a>

 To further simplify the operational efforts needed to run, maintain, and monitor microservices, we can use a fully serverless architecture.

## Deploying Lambda-based applications
<a name="deploying-lambda-based-applications"></a>

 You can deploy your Lambda code by uploading a `zip` file archive or by creating and uploading a container image through the console UI using a valid Amazon ECR image URI. However, when a Lambda function becomes complex, meaning it has layers, dependencies, and permissions, uploading through the UI can become unwieldy for code changes.

 Using AWS CloudFormation and the AWS Serverless Application Model ([AWS SAM](https://github.com/awslabs/serverless-application-model)), AWS Cloud Development Kit (AWS CDK), or Terraform streamlines the process of defining serverless applications. AWS SAM, natively supported by CloudFormation, offers a simplified syntax for specifying serverless resources. AWS Lambda Layers help manage shared libraries across multiple Lambda functions, minimizing function footprint, centralizing tenant-aware libraries, and improving the developer experience. Lambda SnapStart for Java enhances startup performance for latency-sensitive applications.

 To deploy, specify resources and permissions policies in a CloudFormation template, package deployment artifacts, and deploy the template. SAM Local, an AWS CLI tool, allows local development, testing, and analysis of serverless applications before uploading to Lambda.

 Integration with tools like AWS Cloud9 IDE, AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline streamlines authoring, testing, debugging, and deploying SAM-based applications.

 The following diagram shows deploying AWS Serverless Application Model resources using CloudFormation and AWS CI/CD tools.

![Diagram showing AWS Serverless Application Model (AWS SAM)](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/aws-sam.png)

## Abstracting multi-tenancy complexities
<a name="abstracting-multi-tenancy-complexities"></a>

 In a multi-tenant environment like SaaS platforms, it's crucial to streamline the intricacies related to multi-tenancy, freeing up developers to concentrate on feature and functionality development. This can be achieved using tools such as [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html), which offer shared libraries for addressing cross-cutting concerns. The rationale behind this approach is that shared libraries and tools, when used correctly, efficiently manage tenant context.

 However, they should not extend to encapsulating business logic due to the complexity and risk they may introduce. A fundamental issue with shared libraries is the increased complexity surrounding updates, making them more challenging to manage compared to standard code duplication. Thus, it's essential to strike a balance between the use of shared libraries and duplication in the quest for the most effective abstraction.

## API management
<a name="api-management"></a>

 Managing APIs can be time-consuming, especially when considering multiple versions, stages of the development cycle, authorization, and other features like throttling and caching. Apart from [API Gateway](https://aws.amazon.com/api-gateway/), some customers also use ALB (Application Load Balancer) or NLB (Network Load Balancer) for API management. Amazon API Gateway helps reduce the operational complexity of creating and maintaining RESTful APIs. It allows you to create APIs programmatically, serves as a "front door" to access data, business logic, or functionality from your backend services, Authorization and access control, rate limiting, caching, monitoring, and traffic management and runs APIs without managing servers.

 Figure 3 illustrates how API Gateway handles API calls and interacts with other components. Requests from mobile devices, websites, or other backend services are routed to the closest CloudFront Point of Presence (PoP) to reduce latency and provide an optimal user experience.

![Diagram showing API Gateway call flow](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/api-gateway-call-flow.png)
