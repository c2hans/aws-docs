---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/migrating-net-workloads.html
---

# Migrating .NET applications
<a name="migrating-net-workloads"></a>

Migrating your .NET applications to AWS enables you to create highly available workloads with elastic scaling capabilities, reduce operation overhead, and increase your business agility by focusing on your differentiating value.

This section focuses on the different options for hosting your .NET applications on AWS. You can choose between using a VM, a managed solution such as [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), containerizing your code, or refactoring your code to a microservices- or serverless-based architecture.

## Assess
<a name="migrating-net-workloads-assess"></a>

Choosing a migration path for your .NET workload relies on the following key factors:
+ **Find the .NET version used** – There are two different .NET implementations supported by Microsoft: .NET Framework (1.0–4.8) and .NET (.NET Core 1.0–3.1 and .NET 5 and later). Both share many of the same components and can run application code written using the different .NET programming languages (such as C\#, F\#, and VB.NET). Choosing a migration strategy and hosting service depends on the runtime used since .NET Framework runs on Windows while the newer .NET is multi-platform. For the .NET Framework, you can either host on a Windows OS or refactor your code to use the newer .NET. The newer .NET can also be hosted on Linux OS-based services. When modernizing .NET Framework-based workloads, you can use [AWS Transform for .NET](https://docs.aws.amazon.com/transform/latest/userguide/dotnet.html) to scan your code and generate a compatibility assessment report. By finding if there are incompatible .NET Framework APIs referenced by your project, you can plan for the complexity of a migration project and decide if and when to refactor your code to use a newer runtime.
+ **Review your current deployment** – Check if the currently migrated workload has existing CI/CD pipelines that can be updated to deploy the same workloads to the cloud. Using an existing build and deploy pipeline can reduce the time it takes to deploy your application to the cloud by automating the steps necessary for building, configuring, and deploying your workloads.
+ **Review your roadmap** – Depending on the current state of the project, you might already be planning to rearchitect or redesign your applications. Any modernization performed should take the product roadmap into consideration. For example, deciding to containerize existing code or refactoring a monolithic architecture into microservices is ideally part of the product roadmap and aligned with other development efforts.

## Mobilize
<a name="migrating-net-workloads-mobilize"></a>

There are three different migration paths to consider when migrating your .NET workloads to AWS. You can choose between the different options depending on the complexity of your existing codebase, time allocated for migration, and the size of the team allocated to support the migration effort. When considering modernization as part of your migration, it's a best practice to be aligned with the product's roadmap.
+ **Rehost (lift & shift) **– You may choose this approach if your priority is faster migration to AWS with little to no changes. You can rehost ASP.NET-based websites to Internet Information Services (IIS) running on Amazon EC2 instances. You can rehost your desktop-based applications (such as Windows Presentation Foundation, Web Forms, and .NET MAUI) to one of the end user computing platforms such as [Amazon WorkSpaces Applications](https://aws.amazon.com/appstream2/) or [Amazon WorkSpaces](https://aws.amazon.com/workspaces-family/).
+ **Replatform** – Replatforming is best suited for when you want to host your application using a managed service without making code changes but want to reduce your operational overhead by offloading undifferentiated heavy lifting such as installation, patching, upgrades, and instance management. This strategy is also suited for teams who want to move to container-based workloads. You can replatform your existing applications to [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), or use Docker containers hosted on [Amazon ECS](https://aws.amazon.com/ecs/), [Amazon EKS](https://aws.amazon.com/eks/), or [AWS App Runner](https://aws.amazon.com/apprunner/).
+ **Refactor **– Choose this approach if you can invest time and effort into making code and architecture changes that reduce operational overhead and achieve better scaling, high availability, and disaster recovery by using AWS cloud-native services. Refactoring involves modernizing your codebase by porting existing .NET framework applications to .NET (previously .NET Core) or modernizing an existing codebase to run better in the cloud. You can use the [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/) to call many AWS cloud services from within your .NET code. Tools such as [AWS Transform for .NET](https://docs.aws.amazon.com/transform/latest/userguide/dotnet.html) can be used to port your codebase from .NET Framework to .NET. By refactoring your existing .NET workloads to run on [AWS Lambda](https://aws.amazon.com/lambda/), you can use serverless computing to avoid provisioning and managing infrastructure.

## Migrate
<a name="migrating-net-workloads-migrate"></a>

The steps of your .NET workloads migration depend on the migration path that you chose during the assess stage and your type of application.

### Rehost .NET applications
<a name="rehost-.net-applications.b0c7b99f-506f-533e-9f59-f7a5983fd31d"></a>

Choose this migration path if you want to migrate your application without making any code changes but want to benefit from automatic scaling, load balancing, and elasticity in the cloud. For Windows-based websites, rehosting usually means running them on Internet Information Services (IIS) on AWS. For desktop-based applications, you must install the application and enable users to connect to the application from outside.

### Internet Information Services on AWS
<a name="internet-information-services-on-9999999999999999aws-.27596ba4-6f58-503c-bc20-aa6b605462e1"></a>

Internet Information Services (IIS) is a Microsoft web server that runs on a Windows operating system and is used to host websites and web services. IIS can be installed on any Amazon EC2 instance running Windows Server. After IIS is enabled and configured, you can deploy your ASP.NET websites and services by using the same deployment mechanism that you use for on-premises environments.

If you host IIS on EC2 Windows instances, it's important to follow the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) by using load balancing, Auto Scaling groups, and multi-AZ deployment depending on your workload and HADR needs. We recommend using the [AWS Launch Wizard](https://docs.aws.amazon.com/launchwizard/latest/userguide/what-is-launch-wizard-iis.html) because it guides you through the sizing, configuration, and deployment of a Windows Server workload running IIS resources on AWS. Launch Wizard deploys a highly available architecture that spans two Availability Zones with the required compute, networking, and storage components for a newly created or existing VPC.

### Hosting desktop applications on AWS
<a name="hosting-desktop-applications-on-9999999999999999aws-.7120da5d-49d0-5a00-b27b-f0b7abe8ba69"></a>

Many clients have the need to access Windows based thick client applications. You have the choice between three different platforms:
+ [Amazon EC2](https://aws.amazon.com/pm/ec2/) – Choose this option if you want your users to connect to a Windows Server-based environment by using Microsoft Remote Desktop. With this option you're responsible for patching and maintaining your operating system. You must also purchase additional Remote Desktop Services client access licenses (RDS CALs) for your users and [active Software Assurance (SA)](https://aws.amazon.com/windows/resources/licensemobility/). For more information, see [Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/) in the AWS documentation.
+ [Amazon WorkSpaces](https://aws.amazon.com/workspaces-family/) – Choose this option if you need a fully managed virtual desktop infrastructure (VDI) for your users. You can use WorkSpaces to provide a persistent Windows Desktop experience to your users. You can also customize your WorkSpaces environment and install .NET applications by using a custom image, or use [AWS Systems Manager](https://aws.amazon.com/systems-manager/) to deliver your .NET applications to your WorkSpaces environments. Users can connect either by using their browser or the [Amazon WorkSpaces client](https://clients.amazonworkspaces.com/).
+ [Amazon WorkSpaces Applications](https://aws.amazon.com/appstream2/) – Choose this option to provide secure, reliable, and scalable access to applications and non-persistent desktops from any location. You can use WorkSpaces Applications to enable your users to access your .NET applications from the web. If you already have existing RDS CALs and active SA, then you can use those licenses with WorkSpaces Applications by using [License Mobility](https://aws.amazon.com/windows/resources/licensemobility/).

## Replatform
<a name="migrating-net-workloads-replatform"></a>

Replatforming involves changing your hosting environment with little to no code changes. Choose this strategy to reduce your operational overhead and take advantage of cloud capabilities and services.

### AWS Elastic Beanstalk
<a name="9999999999999999aeblong-.b1ad9bba-a8c8-5118-a045-651973a20ae6"></a>

You can use [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) to replatform your .NET Framework workloads. If you package your ASP.NET-based or ASP.NET Core-based applications, then you can quickly deploy and manage applications in AWS without having to learn about the infrastructure that runs those applications. This reduces complexity without restricting choice or control. You simply upload your application, and Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.

To learn more, see the following resources:
+ [Creating and deploying .NET applications on Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.html) (Elastic Beanstalk documentation)
+ [Working with .NET Core on Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-dotnet-core-linux.html) (Elastic Beanstalk documentation)
+ [Multi-App Support with Custom Domains for .NET and AWS Elastic Beanstalk](https://aws.amazon.com/blogs/developer/multi-app-support-with-custom-domains-for-net-and-aws-elastic-beanstalk/) (AWS Developer Tools Blog)

### Containerize existing applications
<a name="containerize-existing-applications.703834d0-770f-5967-86b9-940d5ac75530"></a>

You can use Amazon ECS or Amazon EKS to host your Docker-based containerized applications. AWS manages both services. The choice between the two depends on existing knowledge and preference. Both options can run either Linux-based containers or Windows-based containers.

To learn more, see the following resources:
+ [Amazon EC2 Windows containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_Windows.html) (Amazon ECS documentation)
+ [Enabling Windows support for your Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/windows-support.html) (Amazon EKS documentation)
+ [Running Windows Containers with Amazon ECS on AWS Fargate](https://aws.amazon.com/blogs/containers/running-windows-containers-with-amazon-ecs-on-aws-fargate/) (AWS Blog)
+ [Speeding up Windows container launch times with EC2 Image builder and image cache strategy](https://aws.amazon.com/blogs/containers/speeding-up-windows-container-launch-times-with-ec2-image-builder-and-image-cache-strategy/) (AWS Blog)
+ [Quick start: CI/CD for .NET Applications on AWS Fargate](https://aws.amazon.com/quickstart/architecture/dotnet-cicd-fargate/) (AWS documentation)

Containerizing .NET based applications depends on the .NET runtime used. Consider the following:
+ **.NET Framework-based applications run on Windows containers** – Adding Docker support to existing applications is done by creating a Docker file that outlines how the application needs to be containerized.
+ **.NET or .NET Core** – In addition to running newer .NET-based web applications on Amazon ECS or Amazon EKS, you can also use [AWS App Runner](https://aws.amazon.com/apprunner/). App Runner is a serverless, fully managed solution that runs your code or container image and manages load balancing, auto scaling, logging, certificates, and networking.

### Refactor/re-architect existing code
<a name="refactor-re-architect-existing-code.e5e88d09-c509-5e44-a599-c4e51f098e62"></a>

Choose this option if you have a strong business need to add features, scale, or performance that's otherwise difficult to achieve in the application's current environment. Depending on your application roadmap you can choose to change your code to use the latest framework, cloud-native services, or re-architect it to better run in the cloud.

The first refactoring option available is to migrate your existing .NET Framework application to .NET. The move to .NET gives you the benefit of running on Linux instead of Windows. This reduces your total licensing cost, gives you the latest frameworks, and offers the newest versions of the .NET programming languages.

### AWS SDK for .NET
<a name="9999999999999999netlong-.019361eb-ab4f-5c78-a85f-b00c6d725e58"></a>

[AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/) simplifies the use of AWS services by providing a set of libraries that are consistent and familiar for .NET developers. The AWS SDK offers cross-platform support and is distributed using NuGet. Developers can use the AWS SDK to easily call cloud services from their .NET code, meeting their application's storage, queuing, authentication, and configuration requirements.

### Modernize .NET Framework applications
<a name="modernize-.net-framework-applications.bcad7367-dd72-5dd8-8cdf-f6f663c666f1"></a>

You can migrate from the .NET Framework by using [AWS Transform for .NET](https://docs.aws.amazon.com/transform/latest/userguide/dotnet.html), which scans your code files and creates a report that helps plan your application portfolio migration roadmap. Porting Assistant for .NET can also reduce your porting overhead by identifying incompatible .NET Core APIs and packages and finding known replacements. Migrating .NET Framework applications to .NET enables running them on ARM64-based Graviton processors for a better price-to-performance ratio. For more information, see [.NET on Graviton](https://github.com/aws/aws-graviton-getting-started/blob/main/dotnet.md) on GitHub and [Graviton and containers](https://catalog.workshops.aws/graviton/en-US/amazoncontainers) in the AWS Workshop Studio documentation.

### Monolith to microservices
<a name="monolith-to-microservices.a924eb29-ab39-541c-879e-67dd14e0662f"></a>

Many development teams want to re-architect their existing monolithic applications into microservices. By moving to microservice-based architectures, your development teams can increase development agility, decrease compute costs, scale services individually, and decrease their deployment times. By identifying components and grouping functionality, development teams can incrementally extract functionality from .NET Framework monolithic applications into .NET services.

### Refactor to serverless applications
<a name="refactor-to-serverless-applications.52e26f51-3a34-533a-b3a9-cb731142ac74"></a>

[AWS Lambda](https://aws.amazon.com/lambda/) is a serverless, event-driven compute service that enables you run code for virtually any type of application or backend service without provisioning or managing servers. You can extract logic from your existing application to create event-based serverless workflows that scale automatically when needed by using .NET and Lambda. [Common use cases for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/applications-usecases.html) include event driven workloads that run for a few seconds or minutes with varying scaling needs, such as file processing, analytics, websites, and mobile applications. For more information, see [Building Lambda functions with C\#](https://docs.aws.amazon.com/lambda/latest/dg/lambda-csharp.html) in the Lambda documentation.

## Additional resources
<a name="migrating-net-workloads-resources"></a>
+ [AWS Toolkit for Azure DevOps](https://aws.amazon.com/vsts/) (AWS documentation)
+ [Setting up a CI/CD pipeline by integrating Jenkins with AWS CodeBuild and AWS CodeDeploy](https://aws.amazon.com/blogs/devops/setting-up-a-ci-cd-pipeline-by-integrating-jenkins-with-aws-codebuild-and-aws-codedeploy/) (AWS DevOps Blog)
+ [About the AWS Deploy Tool for .NET](https://aws.github.io/aws-dotnet-deploy/) (AWS GitHub)
+ [.NET on AWS](https://aws.amazon.com/developer/language/net/) (AWS documentation)
+ [aws/dotnet](https://github.com/aws/dotnet) (GitHub)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
