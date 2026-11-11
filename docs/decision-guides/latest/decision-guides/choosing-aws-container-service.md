---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-aws-container-service.html
---

# Choosing an AWS container service
<a name="choosing-aws-container-service"></a>

**Taking the first step**

|  |  |
| --- |--- |
| **Purpose** | Determine which AWS container service is the right fit for your organization. |
| **Last updated** | November 11, 2026 |
| **Covered services** |  +  [Amazon EC2](https://docs.aws.amazon.com/ec2/index.html) <br />+  [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) <br />+  [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) <br />+  [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) <br />+  [Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-services.html) <br />+  [AWS App Runner](https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html) <br />+  [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) <br />+  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) <br />+  [AWS Outposts](https://docs.aws.amazon.com/outposts/) <br />+  [Red Hat OpenShift Service on AWS (ROSA)](https://docs.aws.amazon.com/ROSA/latest/userguide/getting-started.html)   |

## Introduction
<a name="intro"></a>

Containers are a key component of modern application development. They are the standard for organizing compute resources and managing the content of your application deployments.

Containers provide a discrete reproducible compute environment for building software to deploy in the cloud. They also simplify packaging and dependency management. You can use them for everything from orchestrating web applications or large multi-cluster estates to testing your work and doing a proof of concept on your laptop.

This decision guide helps you get started and choose the right AWS container service for your modern application development.

## Understand
<a name="understand"></a>

Containers offer a number of advantages for packaging, deploying, and running applications:
+ **Portability:** Benefit from a consistent configuration that can run on any platform that supports the container runtime.
+ **Scalability:** Scale applications up or down, based on demand, by replicating containers.
+ **Consistency:** Ensure that the application runs the same way in every environment.
+ **Efficiency:** Use fewer resources than traditional virtual machines by sharing host resources across containers.
+ **Isolation:** Improve security and reliability with process-level isolation between containers.
+ **Agility:** Reduce the time that it takes to bring new features or applications to market by quickly packaging and deploying applications.

You can think about the universe of AWS container services in three service layers: orchestration, compute capacity, and vertical solutions. A container registry works across all three layers. Expand each of the following to learn more:

### Orchestration layer
<a name="understand.orchestration-layer"></a>

The **orchestration layer** schedules and scales your containers. This is the service you choose first, because it frames the compute decisions that follow. This layer includes:
+ ** Amazon Elastic Container Service (Amazon ECS):** Amazon ECS is a managed container orchestration service that simplifies the deployment, management, and scaling of containerized applications. You can use Amazon ECS to define tasks and services, handle service discovery, and manage the lifecycle of containers. Amazon ECS natively supports blue/green, linear, and canary deployment strategies, and Amazon ECS Service Connect provides service discovery and zone-aware routing for service-to-service communication.
+ ** Amazon Elastic Kubernetes Service (Amazon EKS):** Amazon EKS is a managed Kubernetes service with which you can deploy, manage, and scale containerized applications using Kubernetes. It provides a highly available and secure Kubernetes control plane. For fully managed cluster compute, Amazon EKS offers Amazon EKS Auto Mode (see the compute capacity layer). Amazon EKS Capabilities provide fully managed, Kubernetes-native platform features, such as GitOps continuous delivery and infrastructure provisioning. Your teams can adopt them without self-managing the platform layer.
+ ** Red Hat OpenShift Service on AWS (ROSA):** ROSA is a fully managed service with which you can deploy and run Red Hat OpenShift clusters on AWS infrastructure. OpenShift is an enterprise-grade Kubernetes platform that extends the capabilities of Kubernetes with additional features and tools for building, deploying, and managing containerized applications.

### Compute capacity layer
<a name="understand.compute-capacity-layer"></a>

The **compute capacity layer** is where your containers actually run. Within your chosen orchestrator, you decide how much of the underlying compute you manage. The following options range from compute that you manage yourself to compute that AWS manages for you:
+ **Self-managed Amazon Elastic Compute Cloud (Amazon EC2) instances:** You provision and manage the Amazon EC2 instances that provide the underlying compute capacity for your containers. You choose from a wide range of instance types and sizes, and you handle provisioning, scaling, patching, and maintenance. You can use self-managed Amazon EC2 instances with both Amazon Elastic Container Service and Amazon Elastic Kubernetes Service. This option gives you the most control and the most responsibility.
+ **Managed instances:** The managed instances tier removes instance-level management, such as provisioning, scaling, and patching, while still running your containers on Amazon EC2 instances. You choose the path that matches your orchestrator. These options are not alternatives to each other: one is the Amazon ECS path, the other the Amazon EKS path.
  + **Amazon ECS Managed Instances** is the Amazon ECS path. AWS provisions, scales, patches, and maintains the Amazon EC2 instances that run your containers. You get access to the full range of Amazon EC2 instance types, including GPU-accelerated, memory-optimized, and AWS Graviton instances, without managing the instances yourself.
  + **Amazon EKS Auto Mode** is the Amazon EKS path. AWS manages your cluster's compute, storage, and networking, and provisions nodes on demand, including GPU instances for machine learning workloads. Auto Mode manages more than instances: it also manages cluster storage and networking.
+ **AWS Fargate:** Fargate is a serverless compute engine with which you can run containers without managing the underlying infrastructure. It removes the need to provision and manage Amazon EC2 instances. Amazon ECS and AWS Batch can run your tasks on Fargate. Amazon EKS can also run pods on Fargate; for a low-overhead way to run Amazon EKS without managing nodes, we recommend Amazon EKS Auto Mode (described in the managed instances tier).

**Note**
AWS Outposts extends AWS infrastructure and services to your on-premises or hybrid environment, so it is more than a compute capacity option. With AWS Outposts, you can run containers on AWS infrastructure deployed in your own data center. For on-premises and hybrid guidance, see the Choose section.

### Vertical solutions layer
<a name="understand.vertical-solutions-layer"></a>

The **Vertical solutions layer** is a set of vertical integration services that provide higher-level and bundled services that simplify the process of deploying and managing applications. The AWS services in this layer are:
+ **Amazon ECS Express Mode:** Amazon ECS Express Mode is a simplified path to deploy a containerized web application or API from a container image. You provide the image, and Amazon ECS Express Mode creates an AWS Fargate-based Amazon ECS service in your own account. This service includes a unique URL, an Application Load Balancer with HTTPS, automatic scaling, and monitoring.
+ **Amazon Lightsail:** Amazon Lightsail container services provide a simplified way to run containerized applications in the cloud. You push your container images to the service, and Lightsail runs them on managed compute with a load balancer, an HTTPS endpoint, and automatic scaling, at a predictable monthly price.
+ **AWS Batch:** AWS Batch is a fully managed service with which you can run batch computing workloads on AWS. It dynamically provisions the optimal compute resources based on the volume and specific resource requirements of the batch jobs that you submit. It automatically handles job scheduling, resource provisioning, and scaling based on the workload requirements. AWS Batch runs your jobs on AWS Fargate or Amazon EC2 compute, or on Amazon EKS, which makes it a common choice for high performance computing (HPC) and machine learning workloads.

**Note**
AWS App Runner is closed to new customers. Existing customers can continue to use it as normal. New and migrating customers should use Amazon ECS Express Mode. For more information, see [AWS App Runner availability change](apprunner/latest/dg/apprunner-availability-change.html).

### Container registry
<a name="understand.container-registry"></a>

**Amazon Elastic Container Registry (Amazon ECR):** Amazon ECR is a fully managed container registry that you use with Amazon ECS, Amazon EKS, and other container services. With Amazon ECR, you can store, manage, and deploy container images. It is designed to provide secure and scalable storage for your container images and simplify provisioning containers with the desired images. The Amazon ECR Archive storage class provides lower-cost storage for container images that you do not access actively. You can move images to the Archive storage class with a lifecycle policy or manually to help manage retention and cost.

## Consider
<a name="consider"></a>

It's important to choose a container service that aligns with your application requirements and operational preferences. The following section outlines some of the key criteria to consider when choosing a container service, as well as supporting tools and services.

------
#### [ Managed service and operation overhead ]

Organizations might choose to build on managed container services to reduce their operational overhead. This approach allows developers and operators to focus on their unique activities that add value, instead of on undifferentiated tasks.

AWS container services span a spectrum of managed overhead. At one end, self-managed Amazon Elastic Compute Cloud (Amazon EC2) instances give you the most control and the most responsibility: you provision, scale, and patch the instances yourself. In the middle, the managed instances tier removes instance-level management while still running your containers on Amazon EC2 instances: Amazon Elastic Container Service (Amazon ECS) Managed Instances and Amazon Elastic Kubernetes Service (Amazon EKS) Auto Mode both handle provisioning, scaling, patching, and maintenance for you. At the other end, AWS Fargate and Amazon ECS Express Mode remove instances entirely with serverless compute.

------
#### [ Workload characteristics ]

Understanding your workload patterns can help you make architecture choices. Workload patterns can include web applications, API-based microservices, event-driven applications, streaming and messaging, data pipelines, IT automations, and more. Some workloads perform or scale differently, or have different cost profiles, depending on the compute environment.

Accelerated workloads are one factor to weigh. If you run GPU-accelerated or machine learning workloads, consider the compute options that give you access to GPU instance types within your chosen orchestrator.

------
#### [ Application portability ]

If you want to preserve the ability to move applications between environments, weigh these distinct forms of portability:
+ **Portability across AWS compute services:** Build competency in software architecture and packaging so that you can readily move your business logic between compute options, such as AWS Fargate, Amazon ECS Managed Instances, and Amazon EC2.
+ **Portability between the cloud and on premises:** If you must run the same application both on premises and in the cloud, consider options that extend to your own infrastructure.
+ **Cross-provider portability:** Standard, open APIs, such as the Kubernetes API, can make it easier to move workloads across providers.

------
#### [ Organization size and skills ]

The skills of your organization are a major factor when deciding which container services you use. The approach you take can require some investment in DevOps and Site Reliability Engineer (SRE) teams. Building out an automated pipeline to deploy applications is common for most modern application development.

Some choices elevate the amount of management you need to do. For example, some organizations have the skills and resources to run and manage a Kubernetes implementation. They invest in strong SRE teams to manage Kubernetes clusters and find value in the associated skill portability. These teams handle frequent cluster upgrades. For example, Kubernetes has about three minor releases a year and deprecates old versions.

Organization size is a key factor. Smaller organizations might have a more limited IT team made up of people fulfilling multiple roles. Larger enterprises can support hundreds of workloads in production at once.

Teams with limited container or infrastructure experience can use Amazon ECS Express Mode. It deploys a web application or API from a container image without managing the underlying infrastructure. For platform teams that run Kubernetes, Amazon EKS Capabilities provide fully managed GitOps and infrastructure-provisioning features.

------
#### [ Ease of deployment ]

Different AWS container services meet unique needs in terms of deployment complexity. Here's how each service is optimized for its own role:
+ **Amazon ECS Express Mode** deploys a containerized web application or API from a container image to an AWS Fargate-based service with a unique URL, load balancing, and automatic scaling, without you managing or customizing the underlying infrastructure.
+ **Amazon ECS** provides more control over the network and security configurations without sacrificing scale or features. Amazon ECS also supports native deployment strategies, such as blue/green, so you can manage safe rollouts without additional deployment tooling.
+ **Amazon EKS** provides flexibility and control over application deployment and orchestration provided by Kubernetes technology.

------
#### [ Cost and pricing ]

Container services differ in how you pay for compute and how they scale. AWS Fargate bills the vCPU and memory that you request for each task. Amazon ECS Express Mode has no separate charge: you pay for the Fargate compute, the Application Load Balancer, and the other resources it creates. Amazon ECS service auto scaling adjusts the number of tasks in response to demand. Amazon ECS Managed Instances add a management charge on top of the Amazon EC2 instances they run. Self-managed Amazon EC2 charges for the instances you provision. Amazon EKS charges a per-cluster fee in addition to the compute you run. Amazon EKS Auto Mode and Amazon ECS Managed Instances each add a management fee, with reduced fees for GPU instances. For current pricing, see each service's pricing page.

------
#### [ Well-Architected Framework alignment ]

You can map container choices to the pillars of the AWS Well-Architected Framework:
+ For operational excellence and reliability, managed options such as AWS Fargate, Amazon ECS Managed Instances, and Amazon EKS Auto Mode reduce the infrastructure that you operate.
+ For security, Amazon ECS and Amazon EKS integrate with IAM and support network isolation.
+ For cost optimization, Fargate and Amazon ECS Express Mode scale with demand.
+ For performance efficiency, Amazon ECS Managed Instances and Amazon EKS Auto Mode give you access to GPU and AWS Graviton instances.

For more information, see the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

------

## Choose
<a name="choose"></a>

Now that you know the criteria by which you are evaluating your container options, you are ready to choose which AWS container services might be a good fit for your organizational requirements. You make this choice in three steps: first choose an orchestrator, then choose a compute model within that orchestrator, and finally decide where your containers run.

**Step 1: Choose your orchestrator**

The primary decision is which orchestrator runs and scales your containers. This choice is essentially a choice of operational model: an AWS-native, serverless-oriented model centered on Amazon Elastic Container Service (Amazon ECS), or a Kubernetes model centered on Amazon Elastic Kubernetes Service (Amazon EKS). In practice, many customers use both to varying degrees. Use the following guidance to choose:
+ **Amazon ECS**, for an AWS-native orchestrator with lower operational overhead, when you prefer not to manage a Kubernetes control plane or your team values a simpler, serverless-oriented operational model.
+ **Amazon EKS**, for the Kubernetes API and ecosystem, portability across clouds and on-premises environments through standard Kubernetes APIs, or an existing investment in Kubernetes skills and tooling.
+ **Red Hat OpenShift Service on AWS (ROSA)**, when your organization standardizes on Red Hat OpenShift and you want a fully managed OpenShift platform on AWS.

Amazon ECS Express Mode and Amazon Lightsail container services are not separate orchestrators. Amazon ECS Express Mode is the simplest path to deploy a web application or API from a container image, without choosing or managing an orchestrator yourself. Amazon Lightsail container services offer a simple, predictably priced platform for small containerized applications. AWS Batch runs batch computing workloads, scheduling jobs and provisioning compute for you.

For a deeper discussion of the serverless and Kubernetes operational models, see the [Choosing a modern application strategy decision guide](https://aws.amazon.com/getting-started/decision-guides/modern-apps-strategy-on-aws-how-to-choose/) and the [Containers and Serverless Recommendation Guide](https://aws.amazon.com/modern-apps/recommendation-guide/).

**Step 2: Choose your compute model**

After you choose an orchestrator, decide how much of the underlying compute you want AWS to manage, from fully managed to self-managed. Amazon ECS and Amazon EKS each offer a different set of compute options, so use the matrix that matches the orchestrator that you selected in Step 1.

### Amazon ECS compute options
<a name="choose.ecs-compute-options"></a>

The following matrix compares the Amazon ECS compute options across common decision factors.

| Feature | Amazon ECS on AWS Fargate | Amazon ECS Managed Instances | Amazon EC2 |
| --- | --- | --- | --- |
| Scaling limits | Up to 32 vCPU and 244 GiB per Linux task. | Full range of Amazon EC2 instance types and sizes. | Full range of Amazon EC2 instance types and sizes. |
| Networking | Per-task elastic network interface in your VPC. | Amazon EC2 networking in your VPC. | Amazon EC2 networking in your VPC. |
| IAM | Task-level IAM roles. | Task-level and instance IAM roles. | Task-level and instance IAM roles. |
| GPU support | No GPU support. | GPU instance types supported. | GPU instance types supported. |
+ **Amazon ECS on AWS Fargate**, when you need serverless container compute and your tasks fit within 32 vCPU and 244 GiB (Linux).
+ **Amazon ECS Managed Instances**, when you need Amazon EC2 flexibility, such as GPU, specific instance families, or large instance sizes, with AWS managing the instances.
+ **Amazon EC2**, when you need full control over the instances that run your containers.

### Amazon EKS compute options
<a name="choose.eks-compute-options"></a>

The following matrix compares the Amazon EKS compute options across the same decision factors.

| Feature | Amazon EKS Auto Mode | Managed node groups | Self-managed nodes |
| --- | --- | --- | --- |
| Node management | AWS provisions nodes and manages the operating system, including patching and upgrades. | AWS provisions Amazon EC2 nodes; you manage the node group configuration and trigger updates. | You provision and manage the Amazon EC2 nodes. |
| Scaling mechanism | Automatic, using Karpenter managed by AWS. | Karpenter or Cluster Autoscaler that you configure. | Karpenter or Cluster Autoscaler that you configure and operate. |
| Instance-type control | AWS selects instance types within the constraints that you set. | You select the instance types for the node group. | You select and configure the instance types. |
| GPU support | GPU instances provisioned on demand. | GPU instance types supported. | GPU instance types supported. |
+ **Amazon EKS Auto Mode**, when you want AWS to manage your cluster's compute, storage, and networking and to provision nodes on demand, including GPU instances for machine learning workloads.
+ **Amazon EKS managed node groups**, when you want AWS to help provision and manage Amazon EC2 nodes while you keep control over node configuration.
+ **Self-managed nodes**, when you need full control over the cluster data plane and the nodes that run your containers.

For managed node groups and self-managed nodes, Karpenter provides data-plane autoscaling by launching right-sized nodes in response to pending pods. Amazon EKS Auto Mode uses Karpenter under the hood, so you get this scaling without managing it yourself. To attach on-premises or edge nodes to an Amazon EKS control plane that runs in AWS, use Amazon EKS Hybrid Nodes.

**Note**
Amazon EKS Capabilities are an add-on that stacks on top of Amazon EKS, not a separate orchestrator choice. After you choose Amazon EKS, you can enable Amazon EKS Capabilities for fully managed, Kubernetes-native platform features, such as GitOps continuous delivery and infrastructure provisioning, without self-managing the platform layer.

**Step 3: Decide where your containers run**

Most workloads run in an AWS Region. If you must run containers on premises or at the edge, choose the option that matches the orchestrator you selected in Step 1 and where you want the control plane to run:
+ **[Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html)**, when you use Amazon ECS and want to register your own on-premises servers or virtual machines as external instances to an Amazon ECS control plane that runs in AWS.
+ **Amazon EKS Anywhere**, when you want to run Kubernetes on your own infrastructure with a control plane that also runs on your infrastructure, independent of an AWS-cloud control plane. For more information, see [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/overview/) on the Amazon EKS Anywhere website.
+ **[Amazon EKS Hybrid Nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html)**, when you use Amazon EKS and want to attach your on-premises or edge nodes to an Amazon EKS control plane that runs in AWS.

AWS Outposts extends AWS infrastructure to your data center, so you can run Amazon ECS or Amazon EKS on AWS-managed hardware on premises.

## Use
<a name="use"></a>

You should now have a clear understanding of each AWS container service (and the supporting AWS tools and services) and which one fits your organization and use case.

The following section provides a pathway to learn more about each AWS container service. It includes links to in-depth documentation, hands-on tutorials, and resources to get you started.

### Capacity
<a name="capacity"></a>

------
#### [ Amazon EC2 ]
+ **What is Amazon EC2?**

  Get an overview of Amazon EC2. This guide not only provides an introduction to the service, but also covers how to get started using it and then provides in-depth descriptions of key features and how to use them.

  [Explore the guides](https://docs.aws.amazon.com/ec2/index.html)
+ **Amazon EC2 instance types**

  When you launch an EC2 instance, the instance type that you specify determines the hardware of the host computer used for your instance. Each instance type offers different compute, memory, and storage capabilities, and is grouped in an instance family based on these capabilities. This guide walks you through EC2 instance types.

  [Explore the guide](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html)
+ **Amazon EC2 Auto Scaling with EC2 Spot Instances**

  Learn how to create a stateless, fault-tolerant workload using Amazon EC2 Auto Scaling with launch templates to request Amazon EC2 Spot Instances.

  [Get started with the tutorial ](https://aws.amazon.com/getting-started/hands-on/ec2-auto-scaling-spot-instances/)

------
#### [ AWS Fargate ]
+ **Getting started with AWS Fargate**

  This guide explains the basics of AWS Fargate, a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances. Amazon ECS tasks on Fargate support up to 32 vCPU and 244 GiB of memory for Linux tasks.

  [Explore the guide ](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html)
+ **Getting started with the console using Linux containers on AWS Fargate**

  Get started with Amazon ECS on AWS Fargate by using the Fargate launch type for your tasks in the Regions where Amazon ECS supports AWS Fargate.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/userguide/getting-started-fargate.html)
+ **Creating a cluster with a Fargate Linux task using the AWS CLI**

  Set up a cluster, register a task definition, run a Linux task, and perform other common scenarios in Amazon ECS with the AWS CLI.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/userguide/ECS_AWSCLI_Fargate.html)

------
#### [ Amazon ECS Managed Instances ]
+ **What is Amazon ECS Managed Instances?**

  Learn how Amazon ECS Managed Instances runs your containers on Amazon EC2 instances while AWS manages provisioning, scaling, patching, and maintenance.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html)
+ **Amazon EC2 instance types**

  Review the Amazon EC2 instance types, including GPU, memory-optimized, and AWS Graviton families, that you can run with Amazon ECS Managed Instances.

  [Explore the guide](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html)
+ **Amazon ECS pricing**

  Learn how Amazon ECS Managed Instances pricing adds a management charge on top of the Amazon EC2 instances that run your containers.

  [Explore pricing](https://aws.amazon.com/ecs/pricing/)

------
#### [ Amazon EKS Auto Mode ]
+ **Automate cluster infrastructure with Amazon EKS Auto Mode**

  Learn how Amazon EKS Auto Mode manages compute, storage, and networking for your cluster and provisions nodes on demand, including GPU instances for machine learning workloads.

  [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/automode.html)
+ **Getting started with Amazon Elastic Kubernetes Service**

  Learn how to create a cluster and run Kubernetes workloads on Amazon EKS, including with Amazon EKS Auto Mode.

  [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)

------

### Orchestration
<a name="orchestration"></a>

------
#### [ Amazon ECS ]
+ **Getting started with Amazon ECS**

  Get an introduction to the tools available to access Amazon ECS and introductory step-by-step procedures to run containers.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html)
+ **Tutorials for Amazon ECS**

  Learn how to perform common tasks—including the creation of clusters and VPCs—when using Amazon ECS.

  [ Get started with the tutorials](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-tutorials.html)
+ **Amazon ECS Immersion Day**

  This workshop expands on your foundational understanding of containers and provides practical experience scaling, monitoring, and managing container workflows using Amazon ECS and AWS Fargate.

  [Explore the workshop](https://catalog.workshops.aws/ecs-immersion-day/en-US)
+ **Deploy containers on Amazon ECS**

  Learn how to run a sample application on an Amazon ECS cluster behind a load balancer, test the sample application, and delete your resources to avoid charges.

  [ Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-container-service.html)
+ **Amazon ECS deployment strategies**

  Learn how Amazon ECS natively supports blue/green, linear, and canary deployments with bake time, deployment lifecycle hooks, and automatic rollback based on Amazon CloudWatch alarms.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-deployment-implementation.html)
+ **Amazon ECS Service Connect**

  Learn how Amazon ECS Service Connect provides service discovery and zone-aware routing that prefers traffic within the same Availability Zone for lower latency and cost, along with Envoy access logs for per-request observability. For workloads that span AWS accounts, Service Connect supports cross-account workloads through shared AWS Cloud Map namespaces that you share with AWS Resource Access Manager (AWS RAM) within the same AWS Region.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-shared-namespaces.html)

------
#### [ Amazon EKS ]
+ **Getting started with Amazon EKS **

  Learn more about Amazon EKS, a managed service that you can use to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes.

  [Explore the guide ](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
+ **Amazon EKS deployment **

  Explore Amazon EKS deployment options on AWS and learn how to use it to manage a general containerized application.

  [Explore the guide ](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-kubernetes-service.html)
+ **Amazon EKS workshop **

  Explore practical exercises to learn about Amazon EKS.

  [ Visit the workshop ](https://www.eksworkshop.com/)
+ **Amazon EKS Auto Mode**

  Learn how Amazon EKS Auto Mode manages the compute, storage, and networking for your cluster and provisions nodes on demand, including GPU instances for machine learning workloads.

  [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/automode.html)
+ **Amazon EKS Capabilities**

  Learn how Amazon EKS Capabilities provide fully managed, Kubernetes-native platform features, such as GitOps continuous delivery and infrastructure provisioning, without self-managing the platform layer.

  [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/capabilities.html)

------
#### [ Red Hat OpenShift Service on AWS ]
+ **What is Red Hat OpenShift Service on AWS?**

  Learn how to use this managed service to build, scale, and deploy containerized applications with the Red Hat OpenShift enterprise Kubernetes platform on AWS.

  [Explore the guide](https://docs.aws.amazon.com/rosa/latest/userguide/what-is-rosa.html)
+ **Getting started with Red Hat OpenShift Service on AWS**

  Learn how to get started using Red Hat OpenShift Service on AWS (ROSA).

  [Explore the guide](https://docs.aws.amazon.com/ROSA/latest/userguide/getting-started.html)
+ **Why would you use ROSA?**

  Watch a video to learn when to use Red Hat OpenShift over standard Kubernetes and explore ROSA in depth.

  [ Watch the video](https://pages.awscloud.com/apn-tv-596.html)

------

### Vertical solutions
<a name="vertical-solutions"></a>

------
#### [ Amazon ECS Express Mode ]
+ **What is Amazon ECS Express Mode?**

  Learn how Amazon ECS Express Mode deploys a containerized web application or API from a container image to an AWS Fargate-based service with a unique URL, load balancing, automatic scaling, and monitoring.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html)
+ **How Amazon ECS Express Mode works**

  Learn how Amazon ECS Express Mode creates and manages the Amazon ECS service, Application Load Balancer, and supporting resources in your account.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-work.html)
+ **Getting started with Amazon ECS Express Mode**

  Follow step-by-step procedures to create and deploy your first Amazon ECS Express Mode service.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-getting-started.html)

------
#### [ AWS App Runner ]
+ **AWS App Runner availability change**

  AWS App Runner is closed to new customers. Learn what the availability change means and which options are available to new and migrating customers.

  [Explore the guide](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html)
+ **What is AWS App Runner?**

  If you are an existing customer, learn how to use App Runner to deploy from source code or a container image to a scalable and secure web application in the AWS Cloud.

  [Explore the guide](https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html)
+ **Getting started with AWS App Runner**

  If you are an existing customer, use this tutorial to configure the source, build, and runtime to deploy your application to App Runner.

  [Use the tutorial](https://docs.aws.amazon.com/apprunner/latest/dg/getting-started.html)

------
#### [ Amazon Lightsail ]
+ **What is Amazon Lightsail?**

  Get the full story on Amazon Lightsail, including what it does and how you can benefit from it. This guide also includes step-by-step guidance to help you get started using Lightsail and then configure it to meet your needs.

  [Explore the guide](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)
+ **Creating Lightsail container service images**

  Learn how to create a container image on your local machine using a Dockerfile. You can then push it to your Lightsail container service to deploy it.

  [Explore the guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-container-images.html)
+ **Amazon Lightsail resource center**

  Explore Lightsail tutorials, videos, and links to core concept documentation.

  [Visit the resource center](https://aws.amazon.com/lightsail/resources/)

------
#### [ AWS Batch ]
+ **What is AWS Batch?**

  Learn how to use AWS Batch to run batch computing workloads in the AWS Cloud.

  [Explore the guide](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)
+ **Best practices for AWS Batch**

  Consider this guidance on how to run and optimize your workloads when using AWS Batch.

  [Explore the guide](https://docs.aws.amazon.com/batch/latest/userguide/best-practices.html)
+ **AWS Batch workshops center**

  Use these workshops, organized in a progressive manner from beginner to advanced, to explore and learn AWS Batch.

  [Explore the workshops](https://batch.hpcworkshops.com)

------

### Tools and services with container support
<a name="tools-and-services"></a>

------
#### [ Amazon ECR ]
+ **Amazon ECR documentation**

  Use the Amazon ECR documentation to explore how to use this fully managed container registry.

  [Explore the guides](https://docs.aws.amazon.com/ecr/)
+ **What is Amazon Elastic Container Registry (Amazon ECR)?**

  A guide to getting started with—and using—Amazon ECR.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
+ **Amazon ECR in Multi-Account and Multi-Region Architectures**

  Explore key considerations for Amazon ECR architectures that span across AWS accounts and AWS Regions, and architectures related to hypothetical customer use cases.

  [Read the blog post](https://aws.amazon.com/blogs/containers/amazon-ecr-in-multi-account-and-multi-region-architectures/)
+ **Amazon ECR Archive storage class**

  Learn how the Amazon ECR Archive storage class provides lower-cost storage for container images that you access rarely, which you can move with a lifecycle policy or manually.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/archive_restore_image.html)

------

### On-premises
<a name="on-premises"></a>

------
#### [ Amazon ECS Anywhere ]
+ **What is Amazon ECS Anywhere?**

  Learn how Amazon ECS Anywhere provides support for registering an *external instance*, such as an on-premises server or virtual machine (VM), to your Amazon ECS cluster.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html)
+ **Amazon ECS Anywhere pricing**

  Use this pricing guide to understand Amazon ECS Anywhere pricing, which is based on a model in which you are charged based on the amount of time the instances you have registered to an Amazon ECS cluster are connected to the ECS control plane, rounded up to the nearest second.

  [Explore the pricing guide](https://aws.amazon.com/ecs/anywhere/pricing/)
+ **Amazon ECS Anywhere FAQs**

  Get answers to frequently asked questions about Amazon ECS Anywhere.

  [Explore the FAQs](https://aws.amazon.com/ecs/anywhere/faqs/)

------
#### [ Amazon EKS Anywhere ]
+ **Amazon EKS Anywhere documentation**

  Use the documentation to understand the use of and best practices for Amazon EKS Anywhere.

  [Read the documentation](https://anywhere.eks.amazonaws.com/docs/)
+ **Amazon EKS Anywhere pricing**

  Use this pricing guide to understand Amazon EKS Anywhere pricing.

  [Explore the pricing guide](https://aws.amazon.com/eks/eks-anywhere/pricing/)
+ **Amazon EKS Anywhere FAQs**

  Get answers to frequently asked questions about Amazon EKS Anywhere.

  [Explore the FAQs](https://aws.amazon.com/eks/eks-anywhere/faqs/)

------
#### [ Amazon EKS Hybrid Nodes ]
+ **Amazon EKS Hybrid Nodes overview**

  Use the documentation to understand the use of and best practices for Amazon EKS Hybrid Nodes. The Amazon EKS Hybrid Nodes gateway automates networking between your Amazon EKS control plane, on-premises nodes, and AWS services.

  [Read the documentation](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html)
+ **Amazon EKS Hybrid Nodes pricing**

  Use the pricing guide to understand Amazon EKS Hybrid Nodes pricing.

  [Explore the pricing guide](https://aws.amazon.com/eks/pricing/)
+ **A deep dive into Amazon EKS Hybrid Nodes**

  Explore how you can use your existing on-premises and edge infrastructure as nodes in Amazon EKS clusters.

  [Read the blog post](https://aws.amazon.com/blogs/containers/a-deep-dive-into-amazon-eks-hybrid-nodes/)

------
#### [ AWS Outposts ]
+ **What is AWS Outposts?**

  Get an introduction to this fully managed service that extends AWS infrastructure, services, APIs, and tools to your data center so that you can run Amazon ECS or Amazon EKS on premises.

  [Explore the guide](https://docs.aws.amazon.com/outposts/latest/server-userguide/what-is-outposts.html)
+ **Getting started with AWS Outposts**

  Access the complete set of AWS Outposts technical documentation.

  [Explore the guides](https://docs.aws.amazon.com/outposts/)
+ **AWS Outposts servers pricing**

  Get details on the pricing of AWS Outposts servers.

  [Get details on pricing](https://aws.amazon.com/outposts/servers/pricing/)

------

## Explore
<a name="explore"></a>
+ **For your role**
  + [Developers](https://aws.amazon.com/getting-started/hands-on/?intClick=dev-center-2021_main&getting-started-all.sort-by=item.additionalFields.content-latest-publish-date&getting-started-all.sort-order=desc&awsf.getting-started-category=category%23containers&awsf.getting-started-level=*all&awsf.getting-started-content-type=*all)
  + [Solution Architects](https://aws.amazon.com/architecture/containers/?achp_navtc3&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all)
  + [Professional development](https://explore.skillbuilder.aws/learn/public/learning_plan/view/83/containers-learning-plan)
  + [Startups](https://aws.amazon.com/startups/start-building/how-to-choose-compute-option/)
  + [Decision makers](https://aws.amazon.com/free/containers/)
+ **For an introduction**
  + [Docker](https://aws.amazon.com/docker/)
  + [Kubernetes](https://aws.amazon.com/kubernetes/)
  + [Breaking a monolith into microservices](https://aws.amazon.com/getting-started/hands-on/break-monolith-app-microservices-ecs-docker-ec2/?e=gs2020&p=deepdivecontainers&p=gsrc&c=dd_c)
+ **For a video**
  + [Containers from the couch](https://containersfromthecouch.com/)
  + [How to containerize anything\!](https://youtu.be/JpHlAV7P-Sw)
  + [Building a container CI/CD pipeline](https://youtu.be/b16Gpvjxxnc)
  + [Building a container app with AWS CDK](https://youtu.be/64DzoDM_kQc)
+ **Architecture diagrams**

  Explore reference architecture diagrams for containers on AWS.

  [ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23containers&awsf.industries=*all&awsf.business-category=*all)
+ **Whitepapers**

  Explore whitepapers to help you get started and learn best practices.

  [Explore whitepapers ](https://aws.amazon.com/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=content-type%23whitepaper&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=tech-category%23containers&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all)
+ **AWS solutions**

  Explore vetted solutions and architectural guidance for common use cases for containers.

  [Explore solutions](https://aws.amazon.com/solutions/compute/containers-orchestration-operations/)
