---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/architecture-overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Architecture overview
<a name="architecture-overview"></a>

 It’s common for enterprise .NET applications built in the last decade to follow a layered [n-tier](https://en.wikipedia.org/wiki/Multitier_architecture) architectural approach. The functionality for different aspects of the application is logically separated yet bundled together as interdependent code modules. There are multiple advantages of an n-tier architecture. They’re easy to develop, more feasible to test if the application size is small, and can scale vertically. However, as more functionality is added and the code base grows, the applications become cumbersome to manage, change, and scale. State-dependent applications are particularly difficult to scale horizontally, and the compute capacity must be provisioned to consider the peak load.

 This guide uses the familiar [MvcMusicStore](https://github.com/aws-samples/dotnet-modernization-music-store) reference application, which is built on an n-tier approach using ASP.NET MVC and .NET Framework. It maintains a session state in memory, and it can scale vertically by default. The data persistence layer uses Microsoft SQL Server. The high-level architecture for this application follows.

![Architecture diagram showing the legacy architecture of the MvcMusicStore application.](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/legacy-architecture.jpg)

 Many customers start their cloud journey with a lift-and-shift approach, running their n-tier .NET Framework applications on EC2 without any code changes. It’s common for these deployments to have more than one EC2 Windows instance with an [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/), routing the user requests to one of the EC2 instances. A stateful application can have session affinity (sticky sessions) enabled at the Application Load Balancer level to create an affinity between a client and a specific EC2 instance.

 Along with the Application Load Balancer, developers can use [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) to monitor an application and automatically adjust capacity to maintain steady, predictable performance at the lowest possible cost. [Amazon RDS for SQL Server](https://aws.amazon.com/rds/sqlserver/) is a managed database service that frees you up to focus on application development by managing time-consuming database administration tasks, including provisioning, backups, software patching, monitoring, and hardware scaling.

 In this guide, you replatform this traditional n-tier .NET Framework application to run on Amazon ECS using [AWS App2Container](https://aws.amazon.com/app2container/). As mentioned in the previous sections, running self-managed containers on Amazon EC2 and Amazon EKS is also an option, but Amazon ECS is a simple yet powerful place to start if you and your teams are new to containers.

 Amazon ECS runs natively with AWS services such as Application Load Balancer and Auto Scaling, allowing developers to start with the minimum amount of compute to meet user requirements and scale dynamically as the incoming traffic increases. The high-level architecture for the containerized version of this application follows, and is the target of the transformation detailed in this guide. In the following diagram, the 1 vCPU, 2 GB blocks represent the Amazon ECS tasks where the application containers run.

![Architecture diagram showing MvcMusicStore architecture on Amazon ECS.](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/ecs-architecture.jpg)

 Additional benefits of moving to containers are realized when teams also implement automation and DevOps. A cloud-optimized, containerized application allows you to quickly and frequently deliver consistent applications to your users. A common development pipeline for nearly continuous deployment with AWS follows.

![Diagram illustrating a code development pipeline and its interaction with the infrastructure](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/development-pipeline.jpg)

 Now that you have an idea of the before and after state of the application that you will modernize in this guide, walk through the procedural guidance to complete this transformation quickly and safely.
