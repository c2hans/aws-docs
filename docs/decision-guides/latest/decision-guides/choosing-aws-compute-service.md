---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-aws-compute-service.html
---

# Choosing an AWS compute service

**Taking the first step**

|  |  |
| --- |--- |
| **Purpose** | Help determine which AWS compute service is the best fit for your organization. |
| **Last updated** | November 13, 2026 |
| **Covered services** |  +  [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) <br />+  [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) <br />+  [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) <br />+  [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) <br />+  [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) <br />+  [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) <br />+  [Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html) <br />+  [Amazon ECS Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html) <br />+  [Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html) <br />+  [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) <br />+  [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) <br />+  [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/) <br />+  [Amazon EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html) <br />+  [Amazon EKS Hybrid Nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html) <br />+  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) <br />+  [AWS Lambda Event Functions](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) <br />+  [AWS Lambda Web Functions](https://docs.aws.amazon.com/lambda/latest/dg/web-functions.html) <br />+  [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/microvms.html) <br />+  [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html) <br />+  [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/faqs/) <br />+  [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) <br />+  [AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html) <br />+  [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) <br />+  [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) <br />+  [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) <br />+  [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) <br />+  [Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)   |

## Introduction
<a name="intro"></a>

AWS compute services are designed to meet the varied demands of modern applications, from small-scale projects to enterprise-grade solutions. These services provide scalable computing power that helps you to build, deploy, and manage applications.

To get the most from your investment in these services, it's important to choose the right services for the right task or use case, whether it involves processing basic web app requests or running complex, data-intensive algorithms.

 You can, for example, use:
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) to launch and manage virtual servers
+ [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/) to quickly deploy and manage web applications with minimal management of the infrastructure that runs those applications
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/?icmpid=docs_homepage_featuredsvcs) to run code without provisioning or managing servers. Lambda offers three form factors:
  + Lambda Event Functions for event-driven processing
  + Lambda Web Functions for HTTP web applications and APIs
  + Lambda MicroVMs for isolated, stateful sandboxes that run user-generated or AI-generated code
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) or [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) to run and manage [containers](https://aws.amazon.com/what-are-containers)
+ [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) to run containers on AWS managed compute, or [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) to process large volumes of data in parallel

 You can also use multiple types of compute solutions in a single workload, as each one has its own advantages.

 This guide helps you select the AWS compute services and tools that are the best fit for your needs and your organization.

[![AWS Videos](https://img.youtube.com/vi/E0dYLPXrX_w/0.jpg)](https://www.youtube.com/watch?v=E0dYLPXrX_w&t=1577s)

This two-minute excerpt is from a presentation at re:Invent 2023 by Lorenzo Winfrey, an AWS Senior Business Development Specialist. He provides an overview of AWS compute application use cases.

## Understand
<a name="understand"></a>

 AWS compute services provide secure and resizable compute capacity in the cloud. AWS offers a range of compute services to meet various application requirements. These include Amazon EC2 for resizable virtual servers, Elastic Beanstalk for deploying web applications on your choice of a number of popular platforms, AWS Lambda for serverless compute (offered as Event Functions, Web Functions, and MicroVMs), Amazon ECS and Amazon EKS for container orchestration, and AWS Fargate for serverless containers.

 Furthermore, AWS Batch facilitates batch computing. AWS hybrid and edge services such as [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html) and [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) bring AWS infrastructure and services to metropolitan areas, on-premises locations, and edge sites, addressing requirements for low latency, digital sovereignty, and local data processing. Additionally, Amazon EC2 Auto Scaling automatically adjusts capacity. These services cater to different workload needs, from basic virtual machines (VMs) to fully managed serverless and container solutions.

![](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/understand.png)

Expand each of the following categories to learn more:

### Amazon EC2 services
<a name="understand.ec2-services"></a>

 Amazon EC2 offers a wide range of instance types tailored to different workloads and applications. You can choose from a range of configurations, including different combinations of CPU, memory, storage, and networking capacity. EC2 provides a large variety of compute capacity options optimized for various workloads: general purpose, compute optimized, memory optimized, storage optimized, accelerated computing, and high-performance computing.
+  [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html): Amazon EC2 provides on-demand, scalable computing capacity in the Amazon Web Services (AWS) Cloud. Amazon EC2 includes AWS Graviton-based instances for price-performance on general purpose and compute-intensive applications, with Graviton5-based families such as C9g and M9g and Graviton4-based families such as the 8g generation. For AI/ML and accelerated workloads, Amazon EC2 offers Trn3 UltraServers powered by AWS Trainium3 and Trn2 instances powered by AWS Trainium2 for training and inference, P6-B200 instances powered by NVIDIA Blackwell GPUs for large-scale GPU training and inference, and G6f instances with fractional GPUs for cost-optimized inference and graphics workloads.
+  [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html): Amazon EC2 Auto Scaling helps you maintain application availability and lets you automatically add or remove Amazon EC2 instances by using scaling policies that you define.
+  [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html): EC2 Image Builder is a fully managed AWS service that helps you automate the creation, management, and deployment of customized, secure, and up-to-date server images.
+  [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html): AWS Elastic Beanstalk supports applications developed in Python, Node.js, Java, .NET, PHP, Ruby, and Go. Elastic Beanstalk also supports Docker platforms. With Docker containers you can choose your own programming language and application dependencies that may not be supported by the other Elastic Beanstalk platforms. Elastic Beanstalk platform branches run on Amazon Linux 2023. Elastic Beanstalk set all platform branches based on Amazon Linux 2 to retired on August 6, 2026, so you must migrate existing Amazon Linux 2 environments to Amazon Linux 2023. Elastic Beanstalk offers two deployment modes:
  +  **Standard Mode**: The existing experience. Each application gets its own dedicated environment on Amazon EC2 instances, and all current platforms are supported.
  +  **Cluster Mode**: Runs multiple applications on shared infrastructure in your account, powered by Amazon EKS. You provide source code, a Dockerfile, or a container image in Amazon ECR, and Elastic Beanstalk handles containerization, provisioning, and operations. Cluster Mode can lower the compute cost per application as the number of applications grows. It supports event-driven autoscaling, OpenTelemetry-based observability, AWS Secrets Manager integration, and HTTPS by default. There's no extra charge for Cluster Mode; you pay for the resources it uses, including the Amazon EKS cluster and EKS Auto Mode charges.
+  [Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html): Amazon Lightsail provides an easy way to build web applications providing instances, container services, managed databases, content delivery network distributions, load balancers, SSD-based storage, and DNS management.

### Accelerated and AI/ML compute
<a name="understand.accelerated-ai-ml"></a>

 We offer Amazon EC2 instances with hardware accelerators for machine learning and high-performance computing. These instances support model training, inference, and other compute-intensive workloads.
+  Choose [Trn3 UltraServers](https://aws.amazon.com/ec2/instance-types/trn3/), powered by AWS Trainium3 chips, when you need to train and serve frontier-scale generative AI models. Trn3 UltraServers scale up to 144 Trainium3 chips. Compared with Trainium2, each chip delivers up to 2x MXFP8 compute and 1.7x memory bandwidth.
+  Choose [Trn2 instances](https://aws.amazon.com/ec2/instance-types/trn2/), powered by AWS Trainium2 chips, when you need to train and run inference for large machine learning and generative AI models.
+  Choose [P6-B200 instances](https://aws.amazon.com/ec2/instance-types/p6/), powered by NVIDIA Blackwell GPUs, when you need GPU-based compute for medium-to-large scale training and inference.
+  Choose [G6f instances](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-ec2-g6f-instances-fractional-gpus/), which provide fractional GPU allocations, when you need cost-optimized GPU compute for inference and graphics workloads.

### Container services
<a name="understand.container-services"></a>

 AWS container compute options are designed to help you deploy, manage, and scale containerized applications efficiently. Amazon ECS, for example, allows you to run and manage Docker containers at scale, handling cluster management and orchestration of containers. Amazon EKS provides a fully managed Kubernetes service, simplifying the deployment, management, and scaling of containerized applications using Kubernetes.

 You have the option of running containers on EC2 instances that you manage, or you can run them on Fargate on AWS managed compute. Additionally, AWS offers Amazon Elastic Container Registry (Amazon ECR), a fully managed Docker container registry.
+  [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html): Amazon ECS is a fully managed container orchestration service that helps you deploy, manage, and scale containerized applications.
+  [Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html): Amazon ECS Anywhere provides support for registering an *external instance* such as an on-premises server or VM, to your Amazon ECS cluster.
+  [Amazon ECS Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html): Amazon ECS Express Mode helps you deploy a web application and its supporting infrastructure, including a Fargate-based service, a load balancer, and auto scaling, from a container image.
+  [Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html): Amazon ECS Managed Instances is a fully managed compute option that runs your containers on Amazon EC2 instances that AWS provisions, patches, and scales for you. It provides a compute tier between Fargate and self-managed Amazon EC2, giving you access to specific Amazon EC2 instance types, including GPU instances, while AWS manages the underlying infrastructure.
+  [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html): Amazon EKS is a managed service that helps you deploy, manage, and scale containerized applications using Kubernetes on AWS infrastructure. Amazon EKS removes the need to install, operate, and maintain your own Kubernetes control plane on AWS. You can run the Amazon EKS data plane with EKS Auto Mode, with managed node groups or self-managed nodes (commonly scaled with Karpenter), on Fargate, or on your own infrastructure with EKS Hybrid Nodes.
+  [EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html): EKS Auto Mode extends AWS management beyond the Kubernetes control plane to the cluster infrastructure that runs your workloads. We set up, scale, patch, and upgrade nodes, and run compute autoscaling, pod and service networking, application load balancing, cluster DNS, block storage, and GPU support as built-in components rather than add-ons. Nodes use immutable, locked-down AMIs and are replaced automatically after a maximum lifetime of 21 days. You keep using standard Kubernetes tools, and you can customize behavior with NodePools and NodeClasses.
+  [EKS Hybrid Nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html): EKS Hybrid Nodes let you use your on-premises and edge servers or virtual machines as nodes in an Amazon EKS cluster. We manage the Kubernetes control plane in the AWS Region, and you manage the hybrid nodes. A single cluster can combine hybrid nodes with nodes in AWS Regions, AWS Local Zones, or AWS Outposts. You pay per hour for the vCPUs of attached hybrid nodes.
+  [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/): Amazon EKS Anywhere is a container management software built by AWS that helps you run and manage Kubernetes clusters on-premises and at the edge.
+  [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html): Amazon ECR is an AWS managed container image registry service that is secure, scalable, and reliable.
+  [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html): AWS Batch is a fully managed batch computing service that plans, schedules, and runs your containerized batch machine learning, simulation, and analytics workloads across the full range of AWS compute offerings, such as Amazon ECS, Amazon EKS, Fargate, and Spot or On-Demand Instances. AWS Batch also supports Amazon ECS Managed Instances compute environments, and you can use AWS Batch to schedule Amazon SageMaker AI training jobs through job queues.

### Serverless compute
<a name="understand.serverless-compute"></a>

 AWS offers serverless compute options, including AWS Lambda and AWS Fargate. With these options, you can run workloads without provisioning or managing servers. We take on as much of the underlying infrastructure management as possible, so developers can focus on writing code.
+  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html): AWS Fargate is a serverless compute engine for containers. You can use it with Amazon ECS, Amazon EKS, and AWS Batch to run containers without managing servers or clusters of Amazon EC2 instances. Each task or pod runs in its own isolated environment. For Linux workloads, Fargate supports task sizes up to 32 vCPU for compute-intensive containerized workloads.
+  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html): Lambda is a serverless compute service. It handles all administration of the compute resources, including server and operating system maintenance, capacity provisioning, automatic scaling, and logging. Lambda offers three form factors. All three are built on Firecracker virtualization technology, and each is designed for a different programming model:
  +  **Lambda Event Functions**: Lambda Event Functions are the new name for what were previously called Lambda functions. They use an event-driven handler model: the function receives an event, processes it, and returns a response. Each execution environment processes one request at a time, and you're billed for the duration your code runs. Event Functions suit event processing, queue and stream consumers, scheduled jobs, and invocations triggered by other AWS services. To reduce cold-start latency, you can enable [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html), which supports Java, Python, and .NET functions and container image functions.
  +  **Lambda Web Functions**: Lambda Web Functions use an HTTP-native programming model. Your code is a standard web server that listens on a port. You can use Node.js web frameworks such as Express, Hono, Fastify, or Next.js without Lambda-specific adapters or wrappers.
    +  **Concurrency**: Each execution environment handles multiple concurrent requests (up to 128), so traffic bursts can share warm environments.
    +  **Billing**: You pay for requests, the CPU time your code actively uses, memory for the lifetime of each execution environment, and data transfer. Time spent waiting on a database or downstream API uses little CPU. This makes Web Functions cost-effective for I/O-heavy workloads such as API backends, server-side rendering, and streaming AI responses.
    +  **Multi-Region deployment**: You can deploy one Web Function to multiple AWS Regions behind a single global endpoint. Lambda routes each request to the lowest-latency Region.
    +  **Deployment and traffic controls**: Web Functions support immutable revisions, weighted traffic shifting between revisions for canary releases, response streaming, and scaling to zero.
    +  **Launch scope**: At launch, Web Functions support Node.js runtimes on Arm64 in a subset of AWS Regions. For the current runtimes and Regions, see the [Lambda Web Functions documentation](https://docs.aws.amazon.com/lambda/latest/dg/web-functions.html).
  +  **Lambda MicroVMs**: Lambda MicroVMs are isolated, stateful sandbox environments whose lifecycle you manage. They provide VM-level isolation, near-instant launch and resume, and the ability to suspend and resume execution for up to 8 hours. You can give each user, session, or job its own MicroVM.
    +  **Images and access**: You build a MicroVM image from a Dockerfile. Each MicroVM gets a dedicated HTTPS URL that supports HTTP/2, gRPC, and WebSockets.
    +  **Use cases**: MicroVMs fit multi-tenant applications that run code supplied by end users or generated by AI. Examples include interactive coding environments, coding assistants and agentic workflows, data analytics notebooks, and vulnerability scanning.
    +  **Billing**: You pay for baseline compute resources while a MicroVM runs. You also pay for the active duration of any additional resources your workload uses above that baseline.

   The three form factors complement each other and share the same operational model. For example, a single application might use:
  + Event Functions for asynchronous backend processing
  + Web Functions for its user-facing API and server-side rendering
  + MicroVMs for an interactive code-execution feature

   **Capacity option: Lambda Managed Instances**: Lambda Managed Instances run Lambda Event Functions on current-generation Amazon EC2 instances in your account, including AWS Graviton4 and network-optimized instance types. Lambda still manages instance lifecycle, OS and runtime patching, routing, load balancing, and scaling.
  +  **Concurrency and scaling**: Each execution environment handles multiple concurrent invocations. Scaling is based on CPU utilization, without cold starts. Managed Instances don't scale to zero: they maintain a configured minimum number of execution environments.
  +  **Isolation**: Isolation comes from containers on Amazon EC2 Nitro instances rather than from Firecracker microVMs.
  +  **Pricing**: You pay the Amazon EC2 instance price plus a management fee. Amazon EC2 Savings Plans, Reserved Instances, and other Amazon EC2 discounts apply to the instance portion. Managed Instances currently support Event Functions only. For containerized workloads on managed Amazon EC2 capacity, see Amazon ECS Managed Instances in Container services.

### On-premises and edge compute
<a name="understand.on-premises-edge"></a>

 AWS provides hybrid and edge compute options that allow you to extend AWS infrastructure and services to your premises and the edge. These edge and hybrid compute options provide flexibility and scalability for a wide range of use cases across different network environments.
+  [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html): AWS Local Zones places compute, storage, database, and other select AWS resources close to large population and industry centers. You can use Local Zones to provide your users with low-latency access to your applications.
+  [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/faqs/): AWS Dedicated Local Zones are a type of AWS Infrastructure that is fully managed by AWS, built for exclusive use by a customer or community, and placed in a customer-specified location or data center to comply with regulatory requirements.
+  [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html): AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises. AWS Outposts is available as multi-rack deployments or as a self-contained single rack. The single-rack option fits locations with limited space and power and supports current x86-based Amazon EC2 instance families.
+  [AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html): AWS Wavelength helps developers to build applications that deliver ultra-low latencies to mobile devices and end users. Wavelength deploys standard AWS compute and storage services to the edge of communications service providers' (CSPs') 5G networks.

### Cost optimization
<a name="understand.cost-optimization"></a>

 AWS provides cost optimization services that allow you to reduce your AWS costs by committing to a usage level and generating recommendations to reduce the cost of your workloads.
+  [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html): Savings Plans is a flexible pricing model that can help you reduce your bill compared to On-Demand prices, in exchange for a one- or three-year hourly spend commitment.
+  [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html): AWS Compute Optimizer provides artificial intelligence and machine learning-based analytics to help you right size your workloads, reduce costs, and improve the performance of your workloads.
+  [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html): Amazon EC2 Spot Instances let you use unused Amazon EC2 capacity at a lower price than On-Demand pricing.

### Elastic Load Balancing
<a name="understand.load-balancing"></a>

 [Elastic Load Balancing (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones.
+  [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html): An Application Load Balancer functions at the application layer, the seventh layer of the Open Systems Interconnection (OSI) model. After the load balancer receives a request, it evaluates the listener rules in priority order to determine which rule to apply, and then selects a target from the target group for the rule action.
+  [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html): A Network Load Balancer functions at the fourth layer of the OSI model. It can handle millions of requests per second. After the load balancer receives a connection request, it selects a target from the target group for the default rule.
+  [Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html): Gateway Load Balancers help you to deploy, scale, and manage virtual appliances, such as firewalls, intrusion detection and prevention systems, and deep packet inspection systems.

## Consider
<a name="consider"></a>

 Consider the following key factors when choosing an AWS compute service. Balancing these factors against your workload needs, technical requirements, and business objectives helps you optimize for performance, cost, and ease of management.

------
#### [ Workload type and requirements ]

 Workload planning means understanding the operational patterns and technical demands of your applications. For example, **batch processing jobs** run a series of tasks on a large volume of data. They need substantial compute capacity, which you can scale down when the job completes to manage costs.

 **Web applications** demand high availability and consistent performance to serve end-user requests at any scale. They typically need a compute service that adjusts to fluctuating traffic, so users get a smooth experience during demand surges and you save costs during quieter periods. When you evaluate web workloads, consider whether you want to run an existing web framework without changes, whether you need to scale to zero between requests, how many concurrent requests each environment should handle, whether you need to serve users from multiple Regions, and how much control over the runtime and instance you need. AWS supports web workloads on serverless functions, containers (including managed paths such as Amazon ECS Express Mode), managed platforms such as Elastic Beanstalk, and Amazon EC2 instances.

 **Machine learning models** have distinct phases for training and inference. Training is computationally intensive and often needs specialized hardware accelerators, such as GPUs or custom chips, for a limited duration. Inference needs a highly available environment that responds quickly to prediction requests, and it often benefits from auto scaling and low-latency processing.

 **Applications that run untrusted code** have their own requirements. This includes code written by your end users or generated by AI agents, such as coding assistants, notebooks, and agentic workflows. Each user or session typically needs its own isolated environment, so incorrect or malicious code can't affect other tenants, and these environments often must preserve state between interactions. Evaluate how strong an isolation boundary you need, how quickly you must create a fresh environment, and how long each environment must keep its state.

 Match these workload characteristics to the capabilities of each service to achieve operational efficiency, strong performance, and cost management.

------
#### [ Performance needs ]

 Performance encompasses compute power (CPU and GPU capabilities) for processing, memory for data caching and operations, storage I/O for data throughput, and network bandwidth for data transfer.

 **High-performance applications**, such as those that run complex calculations or data-intensive processing, need fast CPUs or GPUs, which you find in compute-optimized or GPU-based EC2 instances. **Memory-intensive applications**, such as those that run large databases or in-memory caches, need memory-optimized instances with a higher memory-to-CPU ratio.

 Applications with **heavy input/output operations**, such as high-traffic web applications or big data processing systems, need storage-optimized instances with high I/O throughput. Network performance is critical for **distributed systems and applications** that require rapid data transfer across instances or services.

 Choose services that meet your current demands and scale with your application's growth, so you maintain a consistent user experience without overspending.

------
#### [ Processor architecture ]

 Amazon EC2 and the compute services built on it offer a choice of processor architectures. The processor you choose affects price-performance, compatibility, and the instance families available to your workload.

 Choose **AWS Graviton** processors, which are Arm-based, when you want price-performance for general purpose, compute-intensive, and memory-intensive workloads that can run on Arm. Graviton5-based families, such as C9g and M9g, and Graviton4-based families, such as the 8g generation, are available in Amazon EC2.

 Choose **x86** processors from Intel or AMD when your workload depends on x86 instructions or on software that is only validated for x86.

 Choose **hardware accelerators**, such as AWS Trainium or NVIDIA GPUs, when you run machine learning training, inference, or other accelerated workloads. For more information about matching instances to workloads, see the Accelerated and AI/ML compute options in the Understand section.

------
#### [ Programming model and isolation ]

 The way your code receives work, and the isolation boundary it runs within, can narrow your choice of compute service quickly.
+  **How your code receives work**: Determine whether your code reacts to discrete events (from queues, streams, storage, schedules, or other AWS services), serves HTTP requests as a long-lived web server, or runs as a dedicated session for a single user or job. Some compute options expect a specific model, such as an event handler or a port-listening server, while others run any process you package.
+  **Concurrency per environment**: Consider whether each execution environment should handle one request at a time or many. Single-concurrency simplifies state and thread safety. Multi-concurrency uses capacity more efficiently for I/O-heavy workloads, but your code must be safe to run concurrent requests.
+  **Framework and runtime portability**: Consider whether you need to run existing framework code (such as an HTTP framework) without adapters, which languages and runtimes you need, and whether a service's supported runtimes meet those needs today.
+  **State and lifecycle**: Consider whether environments can be stateless and disposable, or whether you need state preserved across interactions and control over when an environment starts, suspends, resumes, and stops.
+  **Trust in the code you run**: If you run code that you don't control, such as code written by end users or generated by AI agents, consider how strong an isolation boundary you need between tenants and how quickly you need to create a fresh environment per user or session.
+  **Isolation boundaries**: Each option has a different isolation boundary:
  + Lambda Event Functions, Web Functions, and MicroVMs: Firecracker microVMs
  + Lambda Managed Instances: containers on Amazon EC2 Nitro instances, with the capacity provider as the security boundary
  + Amazon EC2: the instance boundary
  + AWS Fargate: each task or pod runs in its own isolated environment.
  + Amazon ECS Managed Instances: multiple tasks share an instance by default; you can configure one task per instance for VM-level isolation.
  + Self-managed Amazon EC2 (Amazon ECS or Amazon EKS): containers on a shared instance, with the instance as the boundary.
  + Amazon EKS (including EKS Auto Mode): pods share a node by default; you can use node selectors and taints and tolerations to place one pod per node.
  + Nitro Sandboxes: provide VM-level isolation between workloads that share an instance, so you can isolate individual tasks or pods even when several run on the same instance. Nitro Sandboxes are available on Amazon ECS Managed Instances and Amazon EKS.

   Consider these boundaries alongside your compliance and multi-tenancy requirements.

------
#### [ Scalability ]

 Scalability defines how well a system handles growth and increased demand. Effective scalability lets your application accommodate more users, handle more transactions, and process larger datasets without degrading performance.

 Scalability can be **vertical**, where you scale up by adding power to existing infrastructure (such as more CPU or memory on an instance), or **horizontal**, where you scale out by adding more instances. Horizontal scalability is essential for dynamic workloads with fluctuating demand.

 A service that adjusts its scale automatically, such as AWS Auto Scaling or serverless offerings, helps you manage workload spikes and lulls. It maintains performance and optimizes cost, because you pay only for the resources you use. Automatic scaling also differs in what triggers it and where it stops. Some options add capacity per incoming request or event and scale to zero when idle. Others scale on resource utilization and keep a minimum capacity, which avoids cold starts but means you pay for idle capacity. Consider how bursty your traffic is and whether your workload can tolerate the latency of starting new capacity. For the scaling behavior of each serverless option, see Serverless compute in the Understand section.

------
#### [ Management overhead ]

 Management overhead is the effort and resources required to maintain your computing infrastructure. On AWS, this ranges from hands-on management of virtual servers to fully managed services.

 For example, **managing** EC2 instances means you handle setup, scaling, patching, and securing servers. This can be resource-intensive and might require a dedicated operations team. When you need granular control over the compute environment, the overhead is often justified.

 AWS also offers services that **abstract** away much of the infrastructure management. Serverless compute options remove server management entirely:
+ Lambda Event Functions run code in response to events.
+ Lambda Web Functions run HTTP applications.
+ Lambda MicroVMs provide isolated sandboxes without your having to operate virtualization infrastructure.

 If you need specific Amazon EC2 hardware or pricing with Lambda's operational model, Lambda Managed Instances run Event Functions on Amazon EC2 capacity that Lambda provisions, patches, and scales. Managed container services, including Amazon ECS Managed Instances, help optimize deployment and scaling of containers, providing a middle ground between control and convenience. Elastic Beanstalk provides managed updates for OS patches, runtime, and framework on the Amazon EC2 instances it manages, so you can just run your application code.

 To balance management overhead, assess your organization's operational capacity and expertise, your need for control versus convenience, and your total cost of ownership, including the hidden cost of operational labor. A service that aligns with your management capabilities lets you focus on building applications.

------
#### [ Cost optimization ]

 Cost optimization helps you find an economical solution for your needs without sacrificing performance or scalability. Consider the following ways to save money on compute on AWS.

1. **Selecting the right instance**

   AWS has more than 750 instance types, with most of these instances built on the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/). Each instance type provides a choice of processor, storage, networking, operating system, and size, so you can choose the instance configuration that best fits your specific workload and budget.

    [AWS Graviton-based Instances](https://aws.amazon.com/ec2/instance-explorer/?ec2-instances-cards.sort-by=item.additionalFields.category-order&ec2-instances-cards.sort-order=desc&awsf.ec2-instances-filter-category=*all&awsf.ec2-instances-filter-processors=*all&awsf.ec2-instances-filter-accelerators=*all&awsf.ec2-instances-filter-additional-capabilities=*all&awsf.ec2-instances-filter-workload-tags=*all) are designed to deliver the best price performance for your cloud workloads running in Amazon EC2. EC2 instances powered by AWS Graviton processors deliver up to 40% better price performance than comparable non-Graviton-based instances.

    [Accelerated computing instances](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing) help you lower the cost of machine learning and other accelerated workloads:
   + **Trn3 UltraServers and Trn2 instances**: Powered by AWS Trainium3 and Trainium2, for cost-efficient training and inference of large machine learning and generative AI models. Trn3 UltraServers scale up to 144 Trainium3 chips for frontier-scale workloads.
   + **Inf2 instances**: Powered by AWS Inferentia2, for cost-efficient, high-throughput inference.
   + **G6f instances**: Provide fractional GPU allocations, so you pay for only the GPU capacity your inference or graphics workload needs.

    For guidance on matching instances to workloads, see Accelerated and AI/ML compute in the Understand section.

1. **Choosing the right purchase plans**

   You have several purchase models to choose from to maximize saving.

   [On-Demand Instances](https://aws.amazon.com/ec2/pricing/on-demand/) let you pay for compute capacity by the hour or second with no long-term commitments. This frees you from the costs and complexities of planning, purchasing, and maintaining hardware.

   [Savings Plans](https://aws.amazon.com/savingsplans/) is a flexible pricing model that can help you reduce your bill by up to 72% compared to On-Demand prices, in exchange for a one- or three-year hourly spend commitment.

   [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) let you take advantage of unused EC2 capacity in the AWS Cloud and are available at a discount of up to 90% compared to On-Demand prices.

1. **Right size your workloads**

   With AWS, you scale up or down as demand fluctuates. The following tools help you to right size your workload.

   **Amazon EC2 Auto Scaling** helps you maintain application availability and helps you to automatically add or remove EC2 instances by using scaling policies that you define.

   **Compute Optimizer** provides artificial intelligence and machine learning-based analytics to help you right size your workloads and reduce costs by up to 25%. [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) can help you identify unused resources and opportunities to lower your costs.

1. **Matching the serverless billing model to your workload**

   Serverless options use different billing models. To compare them, consider how your code spends its time: how long it runs per request, how much of that time it waits on I/O, how steady your traffic is, and whether you can use existing Amazon EC2 commitments. The Lambda billing models are:
   + **Lambda Event Functions**: Billed per request and for the duration your code runs.
   + **Lambda Web Functions**: Billed per request, for CPU time actively consumed, and for memory over the lifetime of each execution environment.
   + **Lambda MicroVMs**: Billed for baseline resources while running, plus the active duration of resources used above the baseline.
   + **Lambda Managed Instances**: Billed at Amazon EC2 instance pricing plus a management fee. Amazon EC2 Savings Plans and Reserved Instances apply to the instance portion.

   To compare running a function on Lambda (default), Lambda Managed Instances, and self-managed Amazon EC2, see [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/).

------
#### [ Latency and throughput ]

 Latency and throughput influence the responsiveness and data-handling capacity of your applications. **Low latency** is essential for time-sensitive applications, so user interactions or transactions process rapidly. **High throughput** is necessary for applications that process large volumes of data quickly, such as video streaming services or big data analysis platforms.

 Consider the **geographical distribution** of your user base and the location of AWS data centers. Proximity to users reduces latency, and services with edge computing capabilities minimize it further by processing data closer to the source. Consider whether you need to serve users from multiple AWS Regions, and whether the compute service routes requests to the nearest Region for you or whether you must configure multi-Region routing yourself. For mixed static and dynamic content, consider placing a content delivery network such as Amazon CloudFront in front of your compute.

 For throughput, evaluate the **network bandwidth** and **I/O capacity** of the compute service so that it handles peak data loads efficiently. The right choice prevents bottlenecks and keeps data processing, analysis, and transfer running without delays.

------
#### [ Compliance and security ]

 Compliance and security help ensure that your infrastructure adheres to regulatory standards and protects data integrity. Many businesses require compliance with industry-specific frameworks, such as [Health Insurance Portability and Accountability Act (HIPAA)](https://aws.amazon.com/compliance/hipaa-compliance/) for healthcare, [General Data Protection Regulation (GDPR)](https://aws.amazon.com/compliance/gdpr-center/) for data protection in the EU, or [AWS System and Organization Controls (SOC)](https://aws.amazon.com/compliance/soc-faqs/) for service organizations. AWS provides services that meet these standards, with features such as data encryption, identity and access management, and logging and monitoring.

 Security extends beyond compliance to the broader protection of your infrastructure from unauthorized access and cyber threats. The service you choose should offer security features such as network security groups, firewalls, and options for private connectivity. AWS regularly attains third-party validations for its security and compliance controls, which provides assurance that its infrastructure can support your compliance needs and protect sensitive data. A compute service that aligns with these requirements is essential for risk management and customer trust.

 The AWS Nitro System continuously monitors, protects, and verifies instance hardware and firmware. It offloads virtualization resources to dedicated hardware and software, which minimizes the attack surface. The Nitro System security model is locked down and prohibits administrative access, which reduces the risk of human error and tampering. AWS Local Zones, AWS Dedicated Local Zones, AWS Outposts, and AWS Wavelength are all built on the same Nitro System that powers modern EC2 instances in AWS Regions today.

------
#### [ Integration ]

 Integration refers to how compute services work with other AWS offerings and third-party applications. Select a compute service that connects with the databases, analytics, machine learning, and other services that form the backbone of your cloud architecture. This supports a cohesive workflow, where data and processes move smoothly across services, which aids automation and reduces manual intervention.

 The service you choose should offer APIs, SDKs, and integration points that align with your existing tools and practices, so you can implement it in your development pipeline. The breadth of AWS services and its [partner network](https://aws.amazon.com/partners/) can extend application capabilities, and prebuilt integrations can save development time. Evaluating how well a compute service fits your broader architecture is essential for building a scalable, agile, and efficient cloud environment.

------
#### [ Reliability and availability ]

 Reliability and availability determine the resilience and uptime of your applications. Reliability is how consistently a service performs its intended function under specific conditions. Availability is the proportion of time the service is operational and accessible.

 Consider the service's track record for stability and its ability to recover from failures. Look for features such as redundancy, failover processes, and backup capabilities that support continuous operation. AWS services often come with service level agreements (SLAs) that guarantee a percentage of uptime.

 Deploying across multiple Availability Zones mitigates the impact of outages, and the global spread of AWS Regions helps keep your application available to users worldwide during regional disruptions. A compute service with high reliability and availability minimizes downtime, which maintains business continuity and safeguards the user experience.

------
#### [ Development and deployment experience ]

 The development and deployment experience directly affects the efficiency and agility of your development team. Services that offer streamlined workflows, thorough documentation, and strong tooling can reduce the time to market for new features and applications.

 Consider whether the service integrates with your existing CI/CD pipelines, supports your preferred languages and frameworks, and provides SDKs and APIs for application integration. Containerization and serverless options can simplify deployment and let developers focus on writing code instead of managing infrastructure. Also consider whether you can run your existing application and framework code without adapters, whether you can develop and test locally the same way you run in production, and whether the service supports gradual rollouts (such as canary or weighted traffic shifting) without extra tooling.

 Detailed monitoring, logging, and debugging tools in the AWS Cloud improve the development experience and help you identify and resolve issues quickly. A compute service that aligns with your team's skills and workflows supports a more productive development environment.

------

## Choose
<a name="choose"></a>

Now that you know the criteria by which you're evaluating your compute options, you're ready to choose which AWS compute services might be a good fit for your organizational requirements.

Start by choosing the compute model that fits how you want to build and operate your workload. Then use the category table and, for Lambda, the form-factor table to narrow your choice.

**Choose a compute model**

| Your goal | Compute model | Start with |
| --- | --- | --- |
| Control the operating system, instance type, and full software stack | Virtual machines | Amazon EC2 (with Amazon EC2 Auto Scaling), or Elastic Beanstalk or Amazon Lightsail for a managed platform |
| Package applications as containers and choose your orchestrator | Containers | Amazon ECS or Amazon EKS; then choose capacity such as Fargate, Amazon ECS Managed Instances, EKS Auto Mode, or Amazon EC2 instances you manage. See [Choosing an AWS container service](choosing-aws-container-service.md). |
| Run code without managing servers or containers | Serverless functions and sandboxes | AWS Lambda; then choose a form factor in the Choosing a Lambda form factor table |
| Run large-scale batch or high performance computing (HPC) jobs | Batch | AWS Batch (on Amazon EC2, Fargate, Amazon ECS Managed Instances, or Amazon EKS) |
| Run on premises, at the edge, or close to end users | Hybrid and edge | AWS Outposts, AWS Local Zones, AWS Dedicated Local Zones, AWS Wavelength, Amazon ECS Anywhere, Amazon EKS Anywhere, or EKS Hybrid Nodes |

The following table highlights which services are optimized for which circumstances.

|  Compute category  |  What is it optimized for?  |  Compute services  |
| --- | --- | --- |
|  Amazon EC2  |  Providing scalable high-performance computing resources for CPU-intensive workloads.  |  [Amazon EC2](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html) <br /> [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) <br /> [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) <br /> [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) <br /> [Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)  |
|  Container services  |  Helping your teams focus on building applications rather than the runtime environment or managing a control plane.  |  [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) <br /> [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) <br /> [Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html) <br /> [Amazon ECS Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html) <br /> [Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html) <br /> [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) <br /> [EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html) <br /> [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/overview/) <br /> [EKS Hybrid Nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html) <br /> [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) (Cluster Mode) <br /> [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)  |
|  Serverless compute  |  Minimizing your AWS management overhead, allowing you to focus on implementing your business logic.  |  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) <br /> [AWS Lambda Event Functions](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) (optionally on Lambda Managed Instances) <br /> [AWS Lambda Web Functions](https://docs.aws.amazon.com/lambda/latest/dg/web-functions.html) <br /> [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/microvms.html)  |
|  On-premises and edge compute  |  Allowing you to run familiar AWS interfaces to your premises and the edge, providing lower latency and local data processing needs.  |  [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html) <br /> [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/faqs/) <br /> [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) <br /> [AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html)  |
|  Cost and savings optimization  |  Helping you reduce your AWS costs for your workloads.  |  [AWS Savings Plan](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) <br /> [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) <br /> [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)  |
|  Elastic Load Balancing  |  Increasing the availability and fault tolerance of your applications.  |  [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) <br /> [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) <br /> [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html)  |

If you've decided that Lambda fits your workload, use the following table to choose a form factor. The Event Functions row also notes when to run Event Functions on Lambda Managed Instances.

**Choosing a Lambda form factor**

| Your goal | Choose | Why |
| --- | --- | --- |
| Process events from queues, streams, Amazon S3, schedules, or other AWS services | Lambda Event Functions | Event-driven handler model; scales to zero. For steady, high-volume traffic or specific Amazon EC2 hardware or pricing, run Event Functions on Lambda Managed Instances. |
| Serve web applications, REST or GraphQL APIs, server-side rendering, or streaming HTTP responses using Node.js web frameworks | Lambda Web Functions | HTTP-native and multi-concurrent, with a multi-Region endpoint. Active CPU billing can lower cost for I/O-heavy workloads. Node.js only at launch. |
| Run user-generated or AI-generated code in a dedicated, isolated, stateful environment per user, session, or job | Lambda MicroVMs | VM-level isolation, fast launch and resume, suspend for up to 8 hours |
| Run HTTP services in other languages, long-running processes, or workloads that need more runtime control | Containers (for example, Amazon ECS Express Mode, or AWS Fargate with Amazon ECS or Amazon EKS) | Any language and runtime. Amazon ECS Express Mode provisions the service, load balancer, HTTPS, and auto scaling from a container image. For help choosing, see [AWS Fargate or AWS Lambda?](fargate-or-lambda.md). |

## Use
<a name="use"></a>

You should now have a clear understanding of each AWS compute service (and the supporting AWS tools and services) and which one might be the best fit for your organization and use case.

 To explore how to use and learn more about each of the available AWS compute services, we have provided a pathway to learn how each of the services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

### Amazon EC2
<a name="amazon-ec2-section"></a>

------
#### [ Amazon EC2 ]
+  **Tutorial: Get started with Amazon EC2 Linux instances**

   Use this tutorial to get started with Amazon EC2. You'll learn how to launch, connect to, and use a Linux instance.

   [Use the tutorial ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
+  **Tutorial: Get started with Amazon EC2 Windows instances**

   Use this tutorial to get started with Amazon EC2. You'll learn how to launch, connect to, and use a Windows instance.

   [Use the tutorial](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html)
+  **Amazon EC2 instance types**

   This guide gives you an overview of the various families of EC2 instance types and discusses the appropriate application for each family.

   [Explore the guide](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html)
+  **Get Started with Amazon EC2 Graviton instances**

   This guide helps you get started with Amazon EC2 Graviton instances and provides step-by-step instructions to migrate your workload to Graviton.

   [Explore the guide](https://aws.amazon.com/ec2/graviton/getting-started/)

------
#### [ Amazon EC2 Auto Scaling ]
+  **Get started with Amazon EC2 Auto Scaling**

   In this tutorial, you set up an Auto Scaling group, terminate your instance, and verify the instance was removed from service and replaced.

   [Use the tutorial](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html)
+  **Tutorial: Scale the size of your Auto Scaling Group**

   In this tutorial, you learn how to scale your Auto Scaling group using either manual scaling, scheduled scaling, dynamic scaling, or predictive scaling.

   [Use the tutorial](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html)
+  **Amazon EC2 Auto Scaling FAQs**

   Find answers to common questions about Amazon EC2 Auto Scaling.

   [Explore the Amazon EC2 Auto Scaling FAQ on the AWS website](https://aws.amazon.com/ec2/autoscaling/faqs/)

------
#### [ EC2 Image Builder ]
+  **Get started with EC2 Image Builder**

   This guide helps you set up your environment to create an automated image pipeline for the first time.

   [Use the tutorial](https://docs.aws.amazon.com/imagebuilder/latest/userguide/set-up-ib-env.html)
+  **Building golden images using Amazon EC2 Image Builder workshop**

   This workshop guides you through creating an EC2 Image Builder pipeline and then developing your own custom components.

   [Use the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/d6c7ecdc-c75f-4ad1-910f-fdd994cc4aed/en-US/100-ec2-ib)
+  **Implementing up-to-date images with automated EC2 Image Builder pipelines**

   This post demonstrates how to automatically keep your base or standard images current, incorporating patches and any other changes using EC2 Image Builder pipelines.

   [Read the blog](https://aws.amazon.com/blogs/compute/implementing-up-to-date-images-with-automated-ec2-image-builder-pipelines/)

------
#### [ AWS Elastic Beanstalk ]
+  **Get started with AWS Elastic Beanstalk**

   This tutorial walks you through creating, exploring, updating, and deleting an Elastic Beanstalk application. It takes less than an hour to complete.

   [Use the tutorial](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html)
+  **Security best practices for Elastic Beanstalk**

   This guide provides you with general guidelines for securing your Elastic Beanstalk application.

   [Read the guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security-best-practices.html)
+  **Creating an ECS managed Docker environment with the Elastic Beanstalk console**

   In this tutorial, you’ll implement an ECS managed Docker environment that uses two containers.

   [Use the tutorial](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_ecstutorial.html)
+  **AWS Elastic Beanstalk Cluster Mode**

   Learn how to run multiple applications on shared, Amazon EKS-powered infrastructure.

   [Explore the AWS Elastic Beanstalk documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)

------
#### [ Amazon Lightsail ]
+  **Launch a Linux virtual machine with Amazon Lightsail**

   In this tutorial, you create an Amazon Linux instance in Amazon Lightsail in seconds. After the instance is up and running, you connect to it via SSH within the Lightsail console using the browser-based SSH terminal.

   [Use the tutorial](https://aws.amazon.com/getting-started/hands-on/launch-a-virtual-machine/)

------

### Container services
<a name="container-services-section"></a>

------
#### [ AWS Batch ]
+  **Getting started with AWS Batch – Amazon EC2**

   In this tutorial, you set up an AWS Batch compute environment using Amazon EC2 orchestration.

   [Use the tutorial](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-ec2.html)
+  **Getting started with AWS Batch - Fargate**

   In this tutorial, you set up an AWS Batch compute environment using AWS Fargate.

   [Use the tutorial](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-fargate.html)
+  **Getting started with AWS Batch - Amazon EKS**

   In this tutorial, you set up an AWS Batch compute environment using Amazon EKS.

   [Use the tutorial](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-eks.html)
+  **Getting started with AWS Batch on SageMaker AI**

   In this tutorial, you set up and run an Amazon SageMaker AI training job using AWS Batch service jobs and job queues.

   [Use the tutorial](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-sagemaker.html)
+  **AWS Batch Deep Dive workshop**

   This workshop provides a deep dive into the basic concepts and use of AWS Batch.

   [Use the workshop](https://catalog.workshops.aws/aws-batch-deep-dive/en-US)

------
#### [ Amazon Elastic Container Service ]
+  **Getting started with Amazon ECS**

   We provide an introduction to the tools available to access Amazon ECS and introductory step-by-step procedures to run containers.

   [Explore the guides](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html)
+  **Create your first Amazon ECS Express Mode service**

   Learn how to deploy a web application and its supporting infrastructure with Amazon ECS Express Mode.

   [Use the tutorial](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-getting-started.html)
+  **Create a task for Amazon ECS Managed Instances**

   Learn how to run containers on fully managed Amazon EC2 capacity with Amazon ECS Managed Instances.

   [Use the tutorial](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-managed-instances.html)
+  **Tutorials for Amazon ECS**

   Explore more than a dozen tutorials on how to perform common tasks - including the creation of clusters and VPCs.

   [Get started with the tutorials](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-tutorials.html)
+  **What's new and what's next with Amazon ECS**

   Learn what's new since the launch of Amazon ECS Anywhere, new features of AWS Fargate, and a look ahead at the exciting enhancements to Amazon ECS.

   [Watch the video ](https://youtu.be/El64yANTmIA)
+  **Amazon ECS deployment**

   This guide offers an overview of Amazon ECS deployment options on AWS and shows how it can be used to manage a simple containerized application.

   [* *Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-container-service.html)
+  **Amazon ECS workshop**

   This workshop is designed to educate those that might not be familiar with AWS Fargate, Amazon ECS, and Docker container workflow.

   [Explore the workshop ](https://ecsworkshop.com/)
+  **Deploy Docker containers on Amazon ECS**

   Learn how to run a Docker-enabled sample application on an Amazon ECS cluster behind a load balancer, test the application, and delete your resources to avoid charges.

   [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/deploy-docker-containers/)

------
#### [ Amazon ECS Anywhere ]
+  **Amazon ECS Anywhere FAQs**

   Answers to frequently asked questions about Amazon ECS Anywhere.

   [Read the FAQ](https://aws.amazon.com/ecs/anywhere/faqs/)
+  **Registering an external instance with Amazon ECS Anywhere**

   Amazon ECS Anywhere provides support for registering an external instance such as an on-premises server or VM, to your Amazon ECS cluster. Here’s how to use that support.

   [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html)
+  **Getting Started with Amazon ECS Anywhere **

   Amazon ECS Anywhere provides consistent tooling and APIs for all container-based applications and the same Amazon ECS experience for cluster management, workload scheduling, and monitoring both in the cloud and on customer-managed infrastructure. This blog details how and why you might want to use it.

   [Read the blog](https://aws.amazon.com/blogs/aws/getting-started-with-amazon-ecs-anywhere-now-generally-available/)

------
#### [ Amazon EKS ]
+  **Getting started with Amazon EKS**

   Learn more about Amazon EKS, a managed service that you can use to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes.

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
+  **Amazon EKS deployment**

   Explore Amazon EKS deployment options on AWS and learn how it can be used to manage a general containerized application.

   [Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-kubernetes-service.html)
+  **Amazon EKS cluster deployment **

   Use this guide to create an Amazon EKS cluster.

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html)
+  **Deploy a Kubernetes application**

   Learn how to deploy a containerized application onto a Kubernetes cluster managed by Amazon EKS.

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html)
+  **Amazon EKS workshop **

   Explore practical exercises to learn about Amazon Elastic Kubernetes Service.

   [Visit the workshop](https://www.eksworkshop.com/)
+  **Automate cluster infrastructure with EKS Auto Mode**

   Learn how EKS Auto Mode manages compute, networking, storage, and upgrades for your clusters.

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/automode.html)
+  **Amazon EKS Hybrid Nodes overview**

   Learn how to use on-premises and edge infrastructure as nodes in Amazon EKS clusters.

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html)

------
#### [ Amazon EKS Anywhere ]
+  **Getting started with Amazon EKS Anywhere**

   This guide helps you get started with Amazon EKS Anywhere, container management software built by AWS that makes it easier to run and manage Kubernetes clusters on-premises and at the edge.

   [Explore the guide](https://anywhere.eks.amazonaws.com/docs/overview/)
+  **Amazon EKS Anywhere FAQs**

   Get answers to your frequently asked questions about Amazon EKS.

   [Read the FAQs](https://aws.amazon.com/eks/eks-anywhere/faqs/)
+  **Running Hybrid Container workloads with Amazon EKS Anywhere**

   This whitepaper provides cloud engineers and architects best practices for operating Amazon EKS Anywhere on customer-managed infrastructure.

   [Read the whitepaper](https://d1.awsstatic.com/kubernetes-pmm/eks-a/getting-started/AWS_Whitepaper_Running_Hybrid_Container_Workloads_with_Amazon_EKS_Anywhere.pdf)

------
#### [ Amazon ECR ]
+  **Getting started with Amazon ECR**

   This guide explains how to use Amazon ECR, an AWS managed container image registry service that is secure, scalable, and reliable.

   [Explore the guide](https://aws.amazon.com/ecr/getting-started/)
+  **Amazon ECR FAQs**

   Answers to frequently asked questions about Amazon ECR.

   [Read the FAQs](https://aws.amazon.com/ecr/faqs/)

------

### Serverless
<a name="serverless-section"></a>

------
#### [ AWS Fargate ]
+  **AWS Fargate for Amazon ECS**

   Understand the basics of AWS Fargate, a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances.

   [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
+  **Learn how to create an Amazon ECS Linux task for the Fargate launch type**

   Get started with Amazon ECS on Fargate by using the Fargate launch type for your tasks in the Regions where Amazon ECS supports AWS Fargate.

   [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html)
+  **Creating a cluster with a Fargate Linux task using the AWS CLI **

   Learn how to set up a cluster, register a task definition, run a Linux task, and perform other common scenarios in Amazon ECS with the AWS CLI.

   [Get started with the tutorial](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html)

------
#### [ AWS Lambda ]
+  **What is AWS Lambda?**

   Learn about AWS Lambda and its three form factors: Event Functions, Web Functions, and MicroVMs.

   [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+  **Create your first Lambda Event Function**

   Build and test an event-driven Lambda function by using the Lambda console.

   [Use the tutorial](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
+  **AWS Lambda Web Functions**

   Learn how to run web applications and API backends as serverless HTTP servers.

   [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/web-functions.html)
+  **Announcing AWS Lambda Web Functions**

   Walk through deploying an Express.js app, multi-Region routing, and canary releases.

   [Read the blog on the AWS website](https://aws.amazon.com/blogs/aws/announcing-aws-lambda-web-functions-for-fast-consistent-web-app-performance-anywhere/)
+  **AWS Lambda MicroVMs**

   Learn how to create MicroVM images and launch isolated, stateful environments for user-generated or AI-generated code.

   [Learn more](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lambda-microvms/)
+  **Lambda Managed Instances**

   Learn when and how to run Event Functions on Lambda-managed Amazon EC2 instances.

   [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html)
+  **AWS Lambda pricing**

   Compare billing for Event Functions, Web Functions, MicroVMs, and Managed Instances.

   [Visit the page](https://aws.amazon.com/lambda/pricing/)
+  **Using AWS Lambda with other services**

   Explore common use cases and learn how invocation works. Navigate a table that covers the services that work with Lambda Event Functions and how each one invokes them.

   [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)
+  **Serverless Land: Lambda Web Functions**

   Find patterns, samples, and learning resources for Web Functions.

   [Explore the resources on the Serverless Land website](https://serverlessland.com/)

------

### On-premises and hybrid
<a name="on-premises-hybrid-section"></a>

------
#### [ AWS Outposts ]
+  **Get started with AWS Outposts**

   This guide demonstrates how to order AWS Outposts and launch an Amazon EC2 instance on your on-premises network.

   [Explore the guide](https://docs.aws.amazon.com/outposts/latest/userguide/get-started-outposts.html)
+  **Planning an AWS Outposts implementation**

   In this free AWS Skill Builder course, you learn about implementation planning for AWS Outposts, including security responsibilities, facilities requirements, networking requirements, and where to deploy your code.

   [Start the course](https://explore.skillbuilder.aws/learn/course/external/view/elearning/75/planning-an-aws-outposts-implementation)
+  **AWS Outposts Rack FAQs **

   Learn more about AWS Outposts Rack by reviewing the FAQ.

   [Explore the FAQ](https://aws.amazon.com/outposts/rack/faqs/)
+  **AWS Outposts Server FAQs **

   Learn more about AWS Outposts Servers by reviewing the FAQ.

   [Explore the FAQ](https://aws.amazon.com/outposts/servers/faqs/)

------
#### [ AWS Local Zones ]
+  **Get started with AWS Local Zones**

   This guide walks you through the steps to enable a Local Zone through the Amazon EC2 console and create resources in the Local Zone subnet.

   [Explore the guide](https://docs.aws.amazon.com/local-zones/latest/ug/getting-started.html)
+  **Connectivity options for Local Zones**

   This guide discusses the various ways to connect users and applications to resources running in a Local Zone.

   [Use the workshop](https://docs.aws.amazon.com/local-zones/latest/ug/local-zones-connectivity.html)
+  **Deploying your first 5G enabled application with AWS Wavelength**

   This blog walks you through deploying one of the most common Wavelength use cases: machine learning inference.

   [Read the blog](https://aws.amazon.com/blogs/compute/deploying-your-first-5g-enabled-application-with-aws-wavelength/)

------

### Cost and savings optimization
<a name="cost-savings-optimization-section"></a>

------
#### [ AWS Savings Plans  ]
+  **Get started with AWS Savings Plans**

   This guide walks you through enabling your settings and permissions in Cost Explorer before using the AWS Billing and AWS Cost Management Console to view, analyze, and manage your Savings Plans.

   [Explore the guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/get-started.html)
+  **Blog post: Getting Started with AWS Savings Plans**

   This post covers how you can use the AWS Cost Management product suite to purchase, manage, and monitor Savings Plans.

   [Read the blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/getting-started-with-aws-savings-plans/)
+  **Savings Plans FAQ **

   Learn more about AWS Savings Plans by reviewing the FAQ.

   [Explore the FAQ](https://aws.amazon.com/savingsplans/faq/)
+  **AWS cost management decision guide**

   Get what you need to decide how best to optimize AWS costs.

   [Read the guide](https://aws.amazon.com/getting-started/decision-guides/cost-management-on-aws-how-to-choose/)

------
#### [ Amazon EC2 Spot Instances ]
+  **Best practices for Amazon EC2 Spot Instances**

   This guide covers the best practices for using Amazon EC2 Spot Instances.

   [Explore the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html)
+  **Work with Spot Instances**

   This guide covers how to use and work with Spot Instances.

   [Explore the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html)
+  **Amazon EC2 Spot Instances workshop**

   This set of workshops is designed to help you get familiar with Amazon EC2 Spot Instances and how to use them in different scenarios, highlighting best practices to follow when using Spot Instances.

   [Use the workshops ](https://ec2spotworkshops.com/)

------
#### [ Amazon EC2 Auto Scaling ]
+  **Get started with Amazon EC2 Auto Scaling**

   In this tutorial, you set up an Auto Scaling group, terminate your instance, and verify that the instance was removed from service and replaced.

   [Use the tutorial](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html)
+  **Increase or decrease compute capacity of your application with scaling**

   Learn how to scale your Auto Scaling group using either manual scaling, scheduled scaling, dynamic scaling, or predictive scaling.

   [Explore the guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html)
+  **Amazon EC2 Auto Scaling FAQs**

   Find answers to common questions about Amazon EC2 Auto Scaling.

   [Explore the Amazon EC2 Auto Scaling FAQ on the AWS website](https://aws.amazon.com/ec2/autoscaling/faqs/)

------
#### [ AWS Compute Optimizer ]
+  **Get started with AWS Compute Optimizer**

   This guide walks you through opting into AWS Compute Optimizer.

   [Explore the guide](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html)
+  **AWS Compute Optimizer workshop**

   The goal of this lab is to use AWS Compute Optimizer to gain insights into rightsizing recommendations to optimize your migrated environment on AWS.

   [Use the workshop](https://catalog.workshops.aws/well-architected-migration/en-US/3-post-migration/compute-optimizer)
+  **AWS Compute Optimizer FAQs**

   Learn more about AWS Compute Optimizer by reviewing the FAQ.

   [Explore the FAQ](https://aws.amazon.com/compute-optimizer/faqs/)

------

### Elastic Load Balancing
<a name="elastic-load-balancing-section"></a>

------
#### [ Elastic Load Balancing  ]
+  **Get started with Application Load Balancers**

   This tutorial provides a hands-on introduction to Application Load Balancers through the AWS Management Console, a web-based interface.

   [Use the tutorial](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancer-getting-started.html)
+  **Getting started with Network Load Balancers**

   This tutorial provides a hands-on introduction to Network Load Balancers through the AWS Management Console, a web-based interface.

   [Use the tutorial](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancer-getting-started.html)
+  **Getting started with Gateway Load Balancers **

   In this tutorial, you’ll implement an inspection system using a Gateway Load Balancer and a Gateway Load Balancer endpoint.

   [Use the tutorial](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started.html)

------

## Explore
<a name="explore"></a>
+ **Architecture diagrams**

  Explore reference architecture diagrams for compute on AWS.

  [ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23compute&awsf.industries=*all&awsf.business-category=*all)
+ **Whitepapers**

  Explore whitepapers to help you get started and learn best practices for compute services and use cases.

  [Explore whitepapers ](https://aws.amazon.com/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=content-type%23whitepaper&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=tech-category%23compute&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all)
+ **AWS Solutions**

  Explore vetted solutions and architectural guidance for common use cases for compute.

  [Explore solutions](https://aws.amazon.com/solutions/compute/?nc=sn&loc=3&dn=cp)
