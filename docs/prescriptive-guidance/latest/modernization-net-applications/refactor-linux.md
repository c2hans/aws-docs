---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/refactor-linux.html
---

# Re-architecting as a Linux container
<a name="refactor-linux"></a>

By porting your .NET Framework applications to .NET Core or .NET 6, you can run your applications on multiple platforms, reduce your license costs, increase performance, and improve scalability.

## Use cases
<a name="refactor-linux-use-cases"></a>

This migration strategy is useful in any of the following scenarios:
+ You have the resources and time available to refactor your application.
+ You're able to resolve all .NET Framework dependencies.
+ You have a long-running application.

## Advantages
<a name="refactor-linux-pros"></a>

This migration approach provides the following benefits, when compared with on-premises .NET applications:
+ Lower total cost of ownership (TCO)
+ Improved security and performance
+ Accelerated innovation
+ Benefits of converting to cloud-native applications
+ Open-source

## Disadvantages
<a name="refactor-linux-cons"></a>
+ Effort and cost of refactoring

## AWS services
<a name="refactor-linux-services"></a>

For storing container images:
+ [Amazon ECR](https://aws.amazon.com/ecr/)

For orchestrating containers:
+ [Amazon ECS](https://aws.amazon.com/ecs), or Amazon ECS with [AWS Fargate](https://aws.amazon.com/fargate/)
+ [Amazon EKS](https://aws.amazon.com/eks/), or Amazon EKS with AWS Fargate

AWS Fargate is a serverless, pay-as-you-go compute engine that lets you focus on building applications without managing servers. AWS Fargate is compatible with both Amazon ECS and Amazon EKS.

## Tools
<a name="refactor-linux-tools"></a>

|
|
| Tool | Purpose | Resources |
| --- |--- |--- |
| Porting Assistant for .NET | This analysis tool scans .NET Framework applications and generates a .NET Core compatibility assessment. This assessment helps you port your applications to Linux faster. | + [Details](https://aws.amazon.com/porting-assistant-dotnet/)<br />+ [Documentation](https://docs.aws.amazon.com/portingassistant/latest/userguide/what-is-porting-assistant.html) |
| AWS App2Container (A2C) | A2C is a command line tool for modernizing .NET and Java applications by converting them into containerized applications with minimal effort. | + [Details](https://aws.amazon.com/app2container/)<br />+ [Documentation](https://docs.aws.amazon.com/app2container/latest/UserGuide/what-is-a2c.html) |

## Deployment decisions
<a name="refactor-linux-deployment"></a>

You can choose from five deployment options:
+ If you want complete control over the configuration of your compute environment, including memory and storage settings, and control over operating system patches: deploy your application as a Linux container on an EC2 instance.
+ If you want the container to be managed by Kubernetes and run as a serverless container: deploy your application as a Linux container on Amazon EKS with Fargate.
+ If you want the container to be managed by Amazon ECS and run as a serverless container: deploy your application as a Linux container on Amazon ECS with Fargate.
+ If you want the container to be managed by Kubernetes, but you want to manage the compute resources of the container yourself: deploy your application as a Linux container on Amazon EKS.
+ If you want the container to be managed by Amazon ECS, but you want to manage the compute resources of the container yourself: deploy your application as a Linux container on Amazon ECS.

![Re-architecting legacy .NET apps as Linux containers on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/images/guide-img/e6435ff7-ff5b-43b9-841d-7a90ca834432/images/514648f6-867a-4737-aa7a-8619bf89edd5.png)
