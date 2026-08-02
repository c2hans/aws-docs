---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/app2container-main.html
---

# Replatform Windows applications with App2Container
<a name="app2container-main"></a>

## Overview
<a name="app2container-overview"></a>

[AWS App2Container](https://docs.aws.amazon.com/app2container/latest/UserGuide/what-is-a2c.html) is a command-line tool for migrating and modernizing Java and .NET web applications into containers. App2Container analyzes and builds an inventory of all applications running in bare metal, virtual machines, Amazon Elastic Compute Cloud (Amazon EC2) instances, or in other cloud providers. You select the application you want to containerize. App2Container packages the application artifacts and dependencies into container images, configures the network ports, and generates the necessary Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS) deployment artifacts, which are infrastructure as code (IaC) templates. App2Container provisions the cloud infrastructure and CI\\CD pipelines required to deploy the containerized application into a production environment. For more information, see [How App2Container works](https://docs.aws.amazon.com/app2container/latest/UserGuide/what-is-a2c.html) in the App2Container documentation.

With App2Container, you can migrate to AWS and modernize your applications as containers while also standardizing the deployment and operations for your applications. You can use App2Container to help quickly build a proof of concept (PoC) or accelerate deployment of production workloads in containers.

There are several things to keep in mind when working with Windows applications. App2Container supports containerization of ASP.NET applications deployed on Microsoft Internet Information Services (IIS), including IIS-hosted Windows Communication Foundation (WCF) applications that run on Windows Server 2016, Windows Server 2019, or Windows Server Core 2004. For more information, see [Supported applications for Windows](https://docs.aws.amazon.com/app2container/latest/UserGuide/supported-applications.html) in the App2Container documentation. App2Container uses Windows Server Core as a base image for its container artifacts, matching the Windows Server Core container version to the operating system (OS) version of the server where you run containerization commands. This approach decouples the application from the underlying OS so that you can upgrade the OS without performing a traditional migration.

If you use a worker machine to containerize your application, the container base image, such as Windows Server 2019 long-term servicing channel (LTSC), matches your worker machine OS, such as Windows Server 2019. If you are running containerization directly on application servers, the version matches your application server OS. If your applications are running on Windows Server 2008 or 2012 R2, you can still use App2Container by setting up a worker machine for containerization and deployment steps. App2Container does not support applications running on Windows client operating systems, such as Windows 7 or Windows 10. App2Container supports Tomcat, TomEE, and JBoss (standalone mode) frameworks for Java processes. For more information, see [App2Container compatibility](https://docs.aws.amazon.com/app2container/latest/UserGuide/compatibility-a2c.html).

## Cost benefits
<a name="app2container-cost-benefits"></a>

Containerizing and consolidating your applications can yield up to [60% compute savings](https://catalog.workshops.aws/msft-costopt/en-US/containers/moving-to-containers) when compared to a one-application-to-one-server deployment design pattern. App2Container helps expedite the application containerization process. The following are some of the benefits of using App2Container for your modernization needs:
+ App2Container is offered at no additional charge.
+ App2Container supports multiple applications in a container image.
+ Address operating systems that are approaching end of support by using App2Container to move your legacy .NET applications to containers. You can move to a newer operating system, avoid paying for extended support, and reduce security risks.
+ Containers are an efficient and cost-effective method of packaging your .NET applications. Review the benefits of containers in the [MACO Recommendation - Moving to containers](https://catalog.workshops.aws/msft-costopt/en-US/containers/moving-to-containers).
+ Application consolidation and containerization help reduce your compute, storage, and licensing footprint by using your compute resources more efficiently.
+ Moving to containers can reduce operational overhead and infrastructure costs and increase development portability and deployment agility.

## Cost optimization recommendations
<a name="app2container-recommendations"></a>

For instructions about how to use App2Container, see [Getting started with AWS App2Container](https://docs.aws.amazon.com/app2container/latest/UserGuide/start-intro.html). For information about the App2Container commands, see the [App2Container command reference](https://docs.aws.amazon.com/app2container/latest/UserGuide/a2c-commands.html).

## Next steps
<a name="app2container-next-steps"></a>

App2Container can accelerate the process of containerizing applications and deploying to Amazon EKS or Amazon ECS. The deployment of applications to containers reduces compute, networking, and storage costs and reduces the operational overhead for application operators.

For a hands-on experience with App2Container, see the [Modernize with AWS App2Container Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/2c1e5f50-0ebe-4c02-a957-8a71ba1e8c89/en-US). If you would like to have a deep-dive learning experience, ask your AWS account team to set up an App2Container immersion day.

## Additional resources
<a name="app2container-resources"></a>
+ [Containerizing Complex Multi-tier Windows Applications using AWS App2Container](https://aws.amazon.com/blogs/modernizing-with-aws/containerizing-complex-multi-tier-windows-applications-aws-app2container/) (AWS blog post)
+ [Containerizing legacy ASP.NET applications using AWS App2Container](https://aws.amazon.com/blogs/modernizing-with-aws/containerizing-legacy-asp-net-applications-using-aws-app2container-a2c/) (AWS blog post)
+ [App2Container supported applications](https://docs.aws.amazon.com/app2container/latest/UserGuide/supported-applications.html) (AWS documentation)
+ [Modernize with AWS App2Container Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/2c1e5f50-0ebe-4c02-a957-8a71ba1e8c89/en-US) (AWS Workshop Studio)
+ [AWS App2Container FAQs](https://aws.amazon.com/app2container/faqs/) (AWS website)
