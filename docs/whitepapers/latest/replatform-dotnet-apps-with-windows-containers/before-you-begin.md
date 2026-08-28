---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/before-you-begin.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Before you begin
<a name="before-you-begin"></a>

## Understand your drivers
<a name="understand-your-drivers"></a>

 Before you begin, take the time to understand your business and technical drivers and work backwards from your desired results to form a plan of action. Common business and technical drivers that motivate the approach to replatforming existing .NET Framework applications to Windows containers are outlined in the following tables.

 *Table 1 — Business drivers *

|  Driver  |  Description  |  Solution  |
| --- | --- | --- |
|  Accelerate innovation  |  Development and IT teams spend most of their time maintaining existing applications rather than innovating.  |  Adopt containers to facilitate DevOps practices and automation.  |
|  Lower total cost of ownership (TCO)  |  Infrastructure is underutilized and operational overhead slows teams down.  |  Move to containers to optimize resource utilization, and invest in automation to reduce manual processes for operations.  |
|  Address skills gap  |  Internal expertise in cloud-native technologies creates barriers to cloud adoption and modernization.  |  Use Amazon Web Services (AWS) official trainings and experts to upskill your staff.  |
|  Standardize technology  |  Different teams are using different tools which creates inefficiencies and prevents standardization.  |  Adopt containers for both Linux and Windows workloads to harmonize technology investments and internal knowledge base.  |

 *Table 2 — Technical drivers *

|  Driver  |  Description  |  Solution  |
| --- | --- | --- |
|  Increase productivity  |  Manual processes slow teams down and cause delays in release cycles.  |  Adopt DevOps practices and automation.  |
|  Scale with traffic demands  |  Applications are provisioned for peak load and underutilize infrastructure resources.  |  Use container auto scaling and stateless applications to scale up and down as traffic demands.  |
|  Predictable performance across environments  |  Application behavior is not consistent across environments leading to unforeseen problems.  |  Use containers for isolation and consistent behavior across environments.  |

 If these drivers resonate with you and your teams, then replatforming your .NET Framework applications to Windows containers might be a good approach to optimize your existing Windows workloads. There are many options for modernizing your existing .NET Framework applications that also include refactoring to the cross-platform .NET 5\+ and Linux, breaking down monoliths to microservices, and rewriting the application to be event-driven with serverless functions and [AWS Lambda](https://aws.amazon.com/lambda/). Although these other approaches have their own unique set of benefits, replatforming to Windows containers is a common approach to optimize existing deployments, introduce cloud-native technologies to your teams, prepare for migrations, and to harden security.

## Choosing container orchestration
<a name="choosing-container-orchestration"></a>

 As you replatform your application, you can select a container orchestrator that is most suitable for your requirements. When choosing your container orchestration option, start with the question “How much of the container infrastructure do you want to manage?”
+  **Amazon Elastic Container Service (Amazon ECS) on AWS Fargate** — [AWS Fargate](https://aws.amazon.com/fargate/) is a technology that you can use with [Amazon ECS](https://aws.amazon.com/ecs/) to run [containers](https://aws.amazon.com/what-are-containers) without having to manage servers or clusters of [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instances. With AWS Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing.

   When you run your tasks and services with the Fargate launch type, you package your application in containers, specify the CPU and memory requirements, define networking and identity and access management policies, and launch the application. Each Fargate task has its own isolation boundary and does not share the underlying kernel, CPU resources, memory resources, or elastic network interface with another task.
+  **Amazon Elastic Kubernetes Service (Amazon EKS)** — [Amazon EKS](https://aws.amazon.com/eks/) is a managed service that allows you to run Kubernetes on AWS without needing to install and operate your own [Kubernetes](https://kubernetes.io/) control plane or worker nodes. Amazon EKS provisions and scales the Kubernetes control plane, including the API servers and backend persistence layer, across multiple AWS Availability Zones for high availability and fault tolerance. Amazon EKS integrates with various AWS services such as [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) (ELB), [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM), [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC), and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to provide scalability and security for your applications.
+  **Amazon Elastic Container Service (Amazon ECS)** — [Amazon ECS](https://aws.amazon.com/ecs/) is a highly scalable, high-performance container management service that supports Docker containers and allows you to run applications on a managed cluster of Amazon EC2 instances. With simple API calls, you can launch and stop container-enabled applications, query the complete state of your cluster, and access many familiar features like security groups, ELB, [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) volumes, and [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). You can use Amazon ECS to schedule the placement of containers across your cluster based on your resource needs and availability requirements.
+  **Self-managed containers on Amazon EC2** — EC2 [virtual machines](https://aws.amazon.com/getting-started/launch-a-virtual-machine-B-0/) give you full control of your server clusters and provide a broad range of customization options. You can choose Amazon EC2 to run your container orchestration if you need full control over the installation, configuration, and management of the container orchestration environment.

## Tools and libraries
<a name="tools-and-libraries"></a>

 AWS has many tools available for developers and IT practitioners to build and run container applications and infrastructure. The following table covers some of the primary tools that are useful for the replatforming process. You will use many of these tools and Amazon ECS in the [*Walkthrough*](walkthrough.md) section of this guide. For the latest news and releases, refer to the [.NET on AWS](https://aws.amazon.com/developer/language/net/) landing page.

* Table 3 – Tools and libraries *

|  Tool or library  |  Description  |
| --- | --- |
|  [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/)  |  Use AWS services with purpose-built .NET libraries and APIs  |
|  [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/)  |  Define AWS infrastructure directly in code with the Cloud Development Kit for .NET  |
|  [AWS Toolkit for Visual Studio](https://aws.amazon.com/visualstudio/)  |  Extension for Visual Studio to create, debug, and deploy applications on AWS  |
|  [AWS App2Container](https://aws.amazon.com/app2container/)  |  Command-line tool to automate packaging applications into container images  |
|  [AWS Porting Assistant for .NET](https://aws.amazon.com/porting-assistant-dotnet/)  |  An analysis tool to assist with porting .NET Framework applications to .NET Core  |
|  [AWS Extensions for .NET CLI](https://github.com/aws/aws-extensions-for-dotnet-cli)  |  Build .NET Core applications with the .NET command-line interface (CLI)  |
|  [AWS Tools for PowerShell](https://aws.amazon.com/powershell/)  |  Manage AWS services and resources with PowerShell  |
|  [AWS Toolkit for Azure DevOps](https://aws.amazon.com/vsts/)  |  Extension for Azure DevOps to deploy applications on AWS  |
|  [AWS CLI](https://aws.amazon.com/cli/)  |  Unified tool to manage your AWS services  |
|  [AWS Copilot CLI](https://aws.amazon.com/containers/copilot/)  |  Simple declarative set of commands to deploy containers  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
