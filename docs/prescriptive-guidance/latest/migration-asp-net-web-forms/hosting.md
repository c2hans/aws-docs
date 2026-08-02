---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-asp-net-web-forms/hosting.html
---

# Hosting ASP.NET Web Forms applications on AWS
<a name="hosting"></a>

AWS provides three options for rehosting your ASP.NET Web Forms applications: Amazon EC2, AWS Elastic Beanstalk, and containerization. Choose the approach that best fits your requirements, skills, and existing infrastructure when you migrate your ASP.NET Web Forms applications to the AWS Cloud.

## Hosting on Amazon EC2
<a name="ec2"></a>

Running ASP.NET Web Forms applications on Amazon Elastic Compute Cloud (Amazon EC2) is suitable for users who require granular control over the underlying virtual machine (VM). In this approach, you are responsible for provisioning and maintaining the EC2 instances, including operating system (OS) patching and updates. You are also responsible for scaling the instances horizontally by using Amazon EC2 Auto Scaling groups and configuring load balancers to handle incoming web traffic.

Use cases:
+ You need a specific Windows version that isn't available in other AWS services.
+ You want full control over OS patching and updates.
+ You already have an established pipeline and process for automating the provisioning and patching of EC2 instances.
+ You want to optimize costs by hosting multiple multi-tenant ASP.NET Web Forms applications on the same instance.
+ You are performing a bulk migration by using tools such as AWS Transform MGN.

## Using AWS Elastic Beanstalk
<a name="beanstalk"></a>

AWS Elastic Beanstalk simplifies the deployment process by automatically handling the provisioning, automatic scaling, and health monitoring of your application. At the same time, it lets you retain full control over the underlying infrastructure of your application if needed. Elastic Beanstalk supports Windows Server versions from 2012 R2 with IIS 8.5, to Windows Server 2019 with IIS 10.0. It also supports the .NET Framework (full) versions 1.x to 4.8. For more information about supported platforms, see the [Elastic Beanstalk documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.net).

Use cases:
+ You don't have expertise in AWS Cloud infrastructure.
+ Time constraints require rapid deployment of your application.
+ You don't require granular control over the underlying infrastructure.
+ You prefer managed OS and platform patching and updates.

## Using Windows containers on Amazon ECS or Amazon EKS
<a name="ecs-eks"></a>

Running an ASP.NET Web Forms application in a Windows Docker container enables greater consistency across environments, portability of the application, and simplified continuous integration and continuous deployment (CI/CD) pipelines. There are three ways to run Windows containers on AWS:
+ Use [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_windows_AMI.html) on an Amazon ECS-optimized Windows Server Amazon Machine Image (AMI)
+ Use [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/windows-support.html) on a Windows node
+ Use a self-managed Docker container on Amazon EC2

**Note**
Windows containers cannot be run in AWS Fargate (Amazon EKS).

Use cases:
+ You are already skilled and familiar with containers and orchestration technologies.
+ You already have an Amazon ECS or Amazon EKS cluster set up for your existing workloads.
+ The application source code isn't available, but you're planning to use [AWS App2Container](https://aws.amazon.com/app2container/) to package your application into a container image.
