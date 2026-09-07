---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/refactor-linux-micro.html
---

# Re-architecting as microservices in Linux containers
<a name="refactor-linux-micro"></a>

A microservices architecture is an approach to developing a single application as a suite of small services. Each service runs in its own process and communicates with other services through lightweight mechanisms. This approach breaks down a monolithic application into smaller services, where each service serves a single purpose and is deployed as a container.

## Use cases
<a name="refactor-linux-micro-use-cases"></a>

This migration strategy is useful if:
+ You want to break your monolithic system into microservices.
+ You have the resources and time available for refactoring.
+ You can resolve all .NET Framework dependencies.
+ You have a long-running application.

## Advantages
<a name="refactor-linux-micro-pros"></a>

This migration approach provides the following benefits, when compared with on-premises .NET applications:
+ Faster innovation because it's easier to add new features in a microservices architecture
+ High availability and reliability
+ Increased agility and on-demand scalability
+ Independent deployment and modern continuous integration and continuous deployment (CI/CD) pipelines
+ Strong module boundaries and technical diversity

## Disadvantages
<a name="refactor-linux-micro-cons"></a>
+ Effort and cost of refactoring
+ Potential operational complexity

## AWS services
<a name="refactor-linux-micro-services"></a>

You can use the following AWS services to develop a microservices-based architecture:
+ [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
+ [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/)
+ [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/)
+ [Amazon ECS](https://aws.amazon.com/ecs)
+ [Amazon EKS](https://aws.amazon.com/eks/)
+ [AWS Lambda](https://aws.amazon.com/lambda/)
+ [AWS Fargate](https://aws.amazon.com/fargate/)
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/)
+ [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)
+ [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/)
+ [Amazon ECR](https://aws.amazon.com/ecr/)

## Tools and offerings
<a name="refactor-linux-micro-tools"></a>

AWS Professional Services offers custom tools and services to help you refactor your monolithic applications into microservices.

## Deployment decisions
<a name="refactor-linux-micro-deployment"></a>

You can choose from five deployment options:
+ If you want complete control over the configuration of your compute environment, including memory and storage settings, and control over operating system patches: deploy your application as a Linux container on an EC2 instance.
+ If you want the container to be managed by Kubernetes and run as a serverless container: deploy your application as a Linux container on Amazon EKS with Fargate.
+ If you want the container to be managed by Amazon ECS and run as a serverless container: deploy your application as a Linux container on Amazon ECS with Fargate.
+ If you want the container to be managed by Kubernetes, but you want to manage the compute resources of the container yourself: deploy your application as a Linux container on Amazon EKS.
+ If you want the container to be managed by Amazon ECS, but you want to manage the compute resources of the container yourself: deploy your application as a Linux container on Amazon ECS.

![Re-architecting legacy .NET apps as microservices in Linux containers on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/images/guide-img/e6435ff7-ff5b-43b9-841d-7a90ca834432/images/ff6e0b59-be97-405e-abcf-2c08b13a9272.png)
