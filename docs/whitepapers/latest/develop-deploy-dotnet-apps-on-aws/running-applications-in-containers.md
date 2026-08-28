---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/running-applications-in-containers.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Running Applications in Containers
<a name="running-applications-in-containers"></a>

Containers allow applications to be bundled with their own libraries and configuration files, and then executed in isolation on a single OS kernel, bringing a number of benefits, including:
+  **Isolation and high-density** — Containerization ensures application isolation in terms of security and data access, and as resource allocation. It’s a reliable solution to run multiple tasks or applications on the same host. This approach enables you to maximize overall resource utilization and minimize idle capacity, also known as a “high-density” deployment.
+  **Runtime packaging and seamless deployment** — Containers include application code or binaries along with all the dependencies needed to keep the application running. This approach ensures the application behaves consistently in all environments, from a developer laptop to a production environment. It also simplifies migrating applications from one host to another.
+  **High availability (HA)** — Container orchestrators provide an abstraction layer on top of conventional hosting environments and keep track of running containers. You don’t have to run applications, just tell the orchestrator which applications are expected to run. The orchestration engine keeps track of the existing state, evaluates it against the expected state, and corrects as needed. If an application goes down, the orchestrator immediately spins up another container to run your application in the next available host.
+  **Resource management for distributed systems** — Containerization is an effective approach to run microservices and other types of distributed systems. The deployment abstraction provided by containers enables you to focus on your applications rather than their dependencies with underlying hosts and infrastructure.

The following sections discuss the four container services available in AWS.

## Amazon Elastic Container Service
<a name="amazon-elastic-container-service"></a>

[Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS) is a highly scalable and high-performance container orchestration service. It was natively developed in AWS, and offers deep integration with AWS services such as [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/), [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC), [IAM](https://aws.amazon.com/iam/), [AWS Batch](https://aws.amazon.com/batch/), and [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/).

Amazon ECS is suitable for a broad range of containerized applications, from long-running applications and microservices to batch jobs and High-Performance Computing workloads, and supports both Linux and Windows containers. Linux containers are available in Amazon Linux and other Linux distributions, and Windows containers are available in Windows 2016 and later.

To use Amazon ECS, you can either use one of the prebuilt Amazon ECS optimized AMIs to spin up a cluster of host instances, or build your own AMIs by adding the Amazon ECS container agent to an existing or custom-built EC2 host.

For more information on running Windows containers on ECS, see [this entry](https://aws.amazon.com/blogs/compute/migrating-net-classic-applications-to-amazon-ecs-using-windows-containers/) on the [AWS Compute Blog](https://aws.amazon.com/blogs/compute/).

## Amazon Elastic Kubernetes Service
<a name="amazon-elastic-kubernetes-service"></a>

[Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) is one of the most popular open-source orchestration engines for containerized workloads. Amazon EKS enables you to run containerized applications using the same toolset on-premises and in the cloud.

Amazon EKS enables you to deploy, manage, and scale containerized applications using Kubernetes on AWS by managing clusters of Amazon EC2 instances, and running containers on those instances. Amazon EKS provides a management plane for a highly available Multi-AZ Kubernetes cluster, which you can join to your additional worker nodes as EC2 instances.

Because Linux containers are available in all versions of Kubernetes, you can run .NET Core applications on any version of it. In contrast, Windows containers are only available starting with Kubernetes 1.14, and they are supported only in Windows 2019 and later.

## Amazon Elastic Container Registry
<a name="amazon-elastic-container-registry"></a>

[Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) (Amazon ECR) is a fully-managed, highly-available and secure [Docker](https://www.docker.com/) container registry that helps developers store, manage, and deploy Docker container images.

Amazon ECR is integrated with other AWS services, such as AWS IAM, and provides a repository to store container images which you can use from Amazon ECS, AWS Fargate, and Amazon EKS.

## AWS Fargate
<a name="aws-fargate"></a>

[AWS Fargate](https://aws.amazon.com/fargate/) is a serverless compute engine for Amazon ECS and EKS that abstracts away details of the underlying host infrastructure such as the instance types, instance sizes, and host OS version.

By letting you focus on designing and building your applications and removing the need to manage the underlying infrastructure, AWS Fargate can help reduce the operational overheads of using containers.

AWS Fargate supports Linux containers and is a powerful option for running .NET 5 applications. For details, see [this entry](https://aws.amazon.com/blogs/compute/hosting-asp-net-core-applications-in-amazon-ecs-using-aws-fargate/) on the [AWS Compute Blog](https://aws.amazon.com/blogs/compute/).

**AWS App2Container (A2C)**

[AWS App2Container](https://aws.amazon.com/app2container/) is a tool provided by AWS to help you modernize .NET and Java applications into containerized applications. Containerizing existing applications requires you to identify application dependencies, network port configurations, and software delivery process. These tasks can be manual, time consuming, and error prone.

Using App2Container, you simply select the applications you want to containerize, and A2C analyzes your applications and automatically generates a container image that is configured with the correct dependencies, network configurations, and deployment instructions for ECS or Kubernetes. A2C provisions, through CloudFormation, the cloud infrastructure and [CI/CD](https://en.wikipedia.org/wiki/CI/CD) pipelines required to deploy the containerized .NET or Java application into production.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
