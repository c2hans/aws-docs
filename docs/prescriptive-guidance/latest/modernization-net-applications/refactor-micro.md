---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/refactor-micro.html
---

# Re-architecting as microservices without containers
<a name="refactor-micro"></a>

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers, creating workload-aware cluster scaling logic, maintaining event integrations, or managing runtimes. Lambda runs your function only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time that you consume—there is no charge when your code isn't running. In this approach, a monolithic application is broken down into smaller services, where each service serves a single purpose. If the service isn't constantly running, it can be implemented as a Lambda function; otherwise, the service should run in a container.

## Use cases
<a name="refactor-micro-use-cases"></a>

You can use this migration strategy in the following scenarios:
+ Your monolithic system is ready to break into microservices.
+ You have the resources and time available for refactoring.
+ You can resolve all .NET Framework dependencies.
+ Your applications do not run constantly; they run for a very short period of time.

## Advantages
<a name="refactor-micro-pros"></a>

This migration approach provides the following benefits, when compared with on-premises .NET applications:
+ Faster innovation because it's easier to add new features in a microservices architecture
+ High availability and reliability
+ Increased agility and on-demand scalability
+ Independent deployment and modern CI/CD pipelines
+ Strong module boundaries and technical diversity
+ Cost savings
+ Reduced infrastructure provisioning efforts

## Disadvantages
<a name="refactor-micro-cons"></a>
+ Effort and cost of refactoring
+ Potential operational complexity
+ No support for long-running applications

## AWS services
<a name="refactor-micro-services"></a>

These are some of the important AWS services that you can use to develop a microservices architecture with AWS Lambda:
+ [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
+ [Amazon SNS](https://aws.amazon.com/sns/)
+ [Amazon SQS](https://aws.amazon.com/sqs/)
+ [AWS Lambda](https://aws.amazon.com/lambda/)
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or [AWS CDK](https://aws.amazon.com/cdk/)
+ [IAM](https://aws.amazon.com/iam/)
+ [Amazon S3](https://aws.amazon.com/s3/)

## Tools and offerings
<a name="refactor-micro-tools"></a>

AWS Professional Services offers custom tools and services to help you refactor your monolithic applications into microservices.

## Deployment decisions
<a name="refactor-micro-deployment"></a>

This migration and modernization approach is supported by AWS Lambda.

![Re-architecting legacy .NET apps as microservices on AWS](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/images/guide-img/e6435ff7-ff5b-43b9-841d-7a90ca834432/images/973f5bbd-9eae-48f3-ab47-9bd3529f205c.png)
