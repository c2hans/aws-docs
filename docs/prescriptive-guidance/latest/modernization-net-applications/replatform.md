---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/replatform.html
---

# Replatforming as a Windows container
<a name="replatform"></a>

Replatforming your .NET application as a Windows container helps you achieve your business objectives with less effort than refactoring. It lets you takes advantage of container technologies without changing the core architecture of your .NET application. Windows applications can be converted to containers without much effort.

.NET Framework-based containers support Windows Server 2016 or 2019 as the host operating system.

## Use cases
<a name="replatform-use-cases"></a>

This migration strategy is useful in any of the following scenarios:
+ You're unable to resolve .NET Framework dependencies.
+ You're unable to resolve Windows dependencies.
+ You don't have the resources to refactor the application to .NET Core or .NET 6.

## Advantages
<a name="replatform-pros"></a>

This migration approach provides the following benefits, when compared with on-premises .NET applications:
+ Minimal effort
+ Improved resource utilization
+ Improved security
+ Better deployment options

## Disadvantages
<a name="replatform-cons"></a>
+ License costs for the host Windows operating system

## AWS services
<a name="replatform-services"></a>

For storing container images:
+ [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) (Amazon ECR)

For orchestrating Windows containers:
+ [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS)
+ [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS)
+ [Amazon EC2](https://aws.amazon.com/ec2/) hosting Docker with Windows containers

## Tools
<a name="replatform-tools"></a>

|
|
| Tool | Purpose | Resources |
| --- |--- |--- |
| AWS App2Container (A2C) | A2C is a command line tool for modernizing .NET and Java applications by converting them into containerized applications with minimal effort. | + [Details](https://aws.amazon.com/app2container/)<br />+ [Documentation](https://docs.aws.amazon.com/app2container/latest/UserGuide/what-is-a2c.html) |

## Deployment decisions
<a name="replatform-deployment"></a>

You can choose from three deployment options:
+ If you want complete control over the configuration of your compute environment, including memory and storage settings, and control over operating system patches: deploy your application as a Windows container on an EC2 instance.
+ If you want the container to be managed by Kubernetes: deploy your application as a Windows container on Amazon EKS.
+ If you want the container to be managed by Amazon ECS: deploy your application as a Windows container on Amazon ECS.

![Replatforming legacy .NET apps as Windows containers on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/images/guide-img/e6435ff7-ff5b-43b9-841d-7a90ca834432/images/8f70c895-3f01-4e2f-b0f7-8cc90c28b9f3.png)
