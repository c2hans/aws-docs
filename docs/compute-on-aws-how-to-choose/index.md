---
source_url: https://docs.aws.amazon.com/compute-on-aws-how-to-choose/index.html
---

# Choosing an AWS compute service for your workload

Find the AWS compute services and tools that are the best fit for your needs and your organization.

## Overview of AWS compute services

AWS compute services are designed to meet the varied demands of modern applications, from small-scale projects to enterprise-grade solutions. These services provide scalable computing power that helps you to build, deploy, and manage applications. Whether you need to launch virtual machines, run containerized applications, or run code without managing servers, AWS compute services provide the flexibility to match your specific workload needs.

## Key concepts

Choosing the right AWS compute service involves balancing the following factors to match your specific workload needs, technical requirements, and business objectives to help you optimize for performance, cost, and ease of management.

- **Workload type and requirements**: As you choose AWS compute services, the foundation lies in understanding your specific workload characteristics and performance requirements. Different application types demand distinct compute capabilities - batch processing jobs need robust, scalable capacity that can be scaled down after completion, while web applications require high availability and dynamic scaling to handle fluctuating traffic. Machine learning workloads present unique challenges with computationally intensive training phases requiring specialized hardware like GPUs, followed by inference phases needing highly available, low-latency environments. Performance optimization involves matching CPU/GPU power, memory capacity, storage I/O, and network bandwidth to your application's specific demands, whether that's compute-optimized instances for complex calculations or memory-optimized instances for large databases.

[Select the best compute options for your workload](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.html)

- **Scalability and management considerations**: Scalability and management overhead are critical factors that significantly impact operational efficiency. AWS offers both vertical scaling (adding more power to existing resources) and horizontal scaling (adding more instances), with services like Auto Scaling and serverless offerings providing automatic adjustment capabilities. Management overhead varies dramatically across services - from hands-on EC2 instance management requiring dedicated operations teams to serverless solutions like AWS Lambda that abstract away infrastructure concerns entirely. Services like AWS Elastic Beanstalk provide a middle ground, handling OS patches and runtime management while allowing you to focus on application code. The key is balancing your organization's operational capacity and need for control against the convenience of managed services.

[Overview of AWS - Compute](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html)

- **Cost optimization strategies**: Cost optimization requires strategic decision-making across multiple dimensions. AWS offers over 750 instance types, including cost-effective [AWS Graviton-based instances](https://aws.amazon.com/ec2/instance-explorer/) that deliver up to 40% better price performance and specialized accelerated computing instances for machine learning workloads. Purchase models provide flexibility with [on-demand instances](https://aws.amazon.com/ec2/pricing/on-demand/) for variable workloads, [savings plans](https://aws.amazon.com/savingsplans/) offering up to 72% savings with commitment, and [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) providing up to 90% discounts for fault-tolerant applications. Right-sizing tools like [Compute Optimizer](https://aws.amazon.com/compute-optimizer/getting-started/#topic-0) and [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) help identify optimization opportunities, while Auto Scaling ensures you only pay for resources you actually need.

[Identifying opportunities with Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html)

- **Security, reliability, and integration factors**: Beyond performance and cost considerations, successful AWS compute service selection must address security, reliability, and integration requirements. Compliance with industry standards like the [Health Insurance Portability and Accountability Act (HIPAA)](https://aws.amazon.com/compliance/hipaa-compliance/) for healthcare, [General Data Protection Regulation (GDPR)](https://aws.amazon.com/compliance/gdpr-center/) for data protection in the EU, or [AWS System and Organization Controls (SOC)](https://aws.amazon.com/compliance/soc-faqs/) for service organizations is essential for many businesses, while the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) provides enhanced security through hardware-based protection and continuous monitoring. Reliability and availability are ensured through features like multi-Availability Zone deployment, Service Level Agreements, and global AWS Region distribution. Integration capabilities with other AWS services and third-party applications, combined with comprehensive APIs and SDKs, enable seamless workflows and reduce development complexity. The development and deployment experience should align with your team's skills and existing CI/CD pipelines to maximize productivity and innovation.

[How do you protect your compute resources?](https://docs.aws.amazon.com/wellarchitected/2025-02-25/framework/sec-06.html)

## Use cases

Match the right compute service to your workload needs for optimal performance and cost efficiency. To get the most from your investment in these services, it's important to choose the right services for the right task or use case, whether it involves processing simple web app requests or running complex, data-intensive algorithms. You can also use multiple types of compute solutions in a single workload, as each one has its own advantages. Here are some common use cases and services that can help:

### Launch and manage virtual servers

Design your ideal computing environment with virtual servers that you can configure to your exact specifications. Scale resources up or down based on demand, choose from hundreds of pre-configured options, and only pay for what you use.

[Amazon EC2](/ec2)

### Deploy and manage web applications with minimal management of the underlying infrastructure

Deploy and scale full-stack applications while minimizing infrastructure management tasks. This approach automates application operations and infrastructure provisioning, allowing development teams to concentrate on writing code and implementing business logic.

[AWS Elastic Beanstalk](/elastic-beanstalk)

### Run code without having to provision or manage servers

Run your code in response to events without managing any infrastructure. Your code runs only when needed, and scales automatically from a few requests per day to thousands per second, with you paying only for the compute time consumed.

[AWS Lambda](/lambda)

### Run and manage containers

Deploy, manage, and scale containerized applications without worrying about the complexity of the underlying infrastructure. Container orchestration services handle tasks like scheduling, cluster management, and service discovery, allowing you to focus on application development rather than operational overhead.

[Amazon Elastic Container Service](/ecs)
[Amazon Elastic Kubernetes Service](/eks)

### Run containers on AWS managed compute

Deploy containerized applications without provisioning or managing the underlying servers. The compute resources automatically scale to match your application's needs, eliminating capacity planning and infrastructure management while you focus on container configuration and application code.

[AWS Fargate](/ecs)

### Process large volumes of data in parallel

Run batch computing workloads efficiently without managing the underlying infrastructure. Computing resources are automatically provisioned based on volume and specific requirements of your jobs, with scheduling and resource allocation handled dynamically while you focus on analyzing results.

[AWS Batch](/batch)

## Compare services

Now that you know how to evaluate your compute options, you're ready to choose which AWS compute services might be a good fit for your organizational requirements. The following graphic shows categories of compute services available in AWS, and lists services in each category.

| Compute category | What is it optimized for? | Compute services |
| --- | --- | --- |
| Amazon EC2 | Providing scalable high-performance computing resources for CPU-intensive workloads. | [Amazon EC2 instance types](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html) <br> [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) <br> [Amazon EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) <br> [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) <br> [Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html) |
| Container services | Helping your teams focus on building applications rather than the runtime environment or managing a control plane. | [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) <br> [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) <br> [Amazon Elastic Container Service Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html) <br> [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) <br> [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/overview/) <br> [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) <br> [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) |
| Serverless compute | Minimizing your AWS management overhead, allowing you to focus on implementing your business logic. | [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) <br> [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) |
| On-premises and edge compute | Allowing you to run familiar AWS interfaces to your premises and the edge, providing lower latency and local data processing needs. | [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html) <br> [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/faqs/) <br> [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) <br> [AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html) |
| Cost and savings optimization | Helping you reduce your costs for your workloads. | [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) <br> [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) <br> [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) |
| Elastic Load Balancing | Increasing the availability and fault tolerance of your applications. | [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) <br> [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) <br> [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html) |

AWS compute services provide secure and resizable compute capacity in the cloud. AWS offers a range of compute services to meet various application requirements. These include Amazon EC2 for resizable virtual servers, AWS Elastic Beanstalk for deploying web applications on your choice of a number of popular platforms, Lambda for serverless computing, Amazon ECS and Amazon EKS for container orchestration, and AWS Fargate for serverless containers.

AWS Batch facilitates batch computing. AWS hybrid and edge services such as Local Zones and AWS Outposts bring AWS infrastructure and services to metropolitan areas, on-premises locations, and edge sites, addressing requirements for low latency, digital sovereignty, and local data processing. Additionally, Amazon EC2 Auto Scaling automatically adjusts capacity. These services cater to different workload needs, from basic virtual machines (VMs) to fully managed serverless and container solutions.

![Understand compute services](/images/compute-on-aws-how-to-choose/images/understand.png)

### Amazon EC2 services

- [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html): Amazon EC2 provides on-demand, scalable computing capacity in the AWS Cloud, including AWS Graviton4 instances for improved price-performance and lower latency in compute-intensive applications, Trn2 instances for high-performance artificial intelligence and machine learning training and inference, and P5eN instances optimized for deep learning (DL), high-performance computing (HPC) workloads, and generative AI applications.
- [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html): Amazon EC2 Auto Scaling helps you maintain application availability and lets you automatically add or remove Amazon EC2 instances by using scaling policies that you define.
- [Amazon EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html): Amazon EC2 Image Builder is a fully managed AWS service that helps you to automate the creation, management, and deployment of customized, secure, and up-to-date server images.
- [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html): AWS Elastic Beanstalk supports applications developed in Python, Node.js, Java, .NET, PHP, Ruby, and GO. Elastic Beanstalk also supports Docker platforms. With Docker containers you can choose your own programming language and application dependencies that may not be supported by other Elastic Beanstalk platforms.
- [Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html): Amazon Lightsail provides an easy way to build web applications providing instances, container services, managed databases, content delivery network distributions, load balancers, SSD-based storage, and DNS management.

### Container services

- [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html): Amazon Elastic Container Service is a fully managed container orchestration service that helps you easily deploy, manage, and scale containerized applications.
- [Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html): Amazon ECS Anywhere provides support for registering an external instance such as an on-premises server or virtual machine to your Amazon ECS cluster.
- [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html): Amazon Elastic Kubernetes Service is a managed service that helps you easily deploy, manage, and scale containerized applications using Kubernetes on AWS infrastructure. Amazon EKS removes the need to install, operate, and maintain your own Kubernetes control plane on AWS.
- [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/): Amazon EKS Anywhere is a container management software that makes it easier to run and manage Kubernetes clusters for on-premises and edge instances.
- [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html): Amazon ECR is an AWS managed container image registry service that is secure, scalable, and reliable.
- [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html): AWS Batch is a fully managed batch computing service that plans, schedules, and runs your containerized batch machine learning, simulation, and analytics workloads across the full range of AWS compute offerings, such as Amazon ECS, Amazon EKS, Fargate, and Spot or On-Demand instances.

### Serverless compute

- [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html): AWS Fargate is a technology that you can use with Amazon Elastic Container Service to run containers without having to manage servers or clusters of Amazon EC2 instances.
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html): Lambda runs your code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, and logging.

### On-premises and edge compute

- [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html): AWS Local Zones places compute, storage, database, and other select AWS resources close to large population and industry centers. You can use Local Zones to provide your users with low-latency access to your applications.
- [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/faqs/): AWS Dedicated Local Zones is a type of AWS infrastructure that is fully managed by AWS, built for exclusive use by a customer or community, and placed in a customer-specified location or data center to comply with regulatory requirements.
- [AWS Outposts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html): AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises.
- [AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html): AWS Wavelength helps developers to build applications that deliver ultra-low latencies to mobile devices and end users. Wavelength deploys standard AWS compute and storage services to the edge of communications service provider (CSPs) 5G networks.

### Cost optimization

- [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html): Savings Plans is a flexible pricing model that can help you reduce your bill compared to on-demand prices, in exchange for a one- or three-year hourly spend commitment.
- [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html): AWS Compute Optimizer provides artificial intelligence and machine learning-based analytics to help you right-size your workloads, reduce costs, and improve the performance of your workloads.
- [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html): Amazon EC2 Spot Instances let you take advantage of unused EC2 capacity at a significant discount to on-demand pricing, helping you to lower your Amazon EC2 costs.

### Elastic Load Balancing

- [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html): An Application Load Balancer functions at the application layer, the seventh layer of the OSI model. After the load balancer receives a request, it evaluates the listener rules in priority order to determine which rule to apply, and then selects a target from the target group for the rule action.
- [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html): A Network Load Balancer functions at the fourth layer of the Open Systems Interconnection (OSI) model. It can handle millions of requests per second. After the load balancer receives a connection request, it selects a target from the target group for the default rule.
- [Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html): Gateway Load Balancers help you to deploy, scale, and manage virtual appliances, such as firewalls, intrusion detection and prevention systems, and deep packet inspection systems.

## Start building

You should now have a clear understanding of each AWS compute service (and the supporting AWS tools and services) and which one might be the best fit for your organization and use case. To explore how to use and learn more about each of the available AWS compute services, we have provided a pathway to learn how each of the services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

### Amazon EC2

**[Tutorial: Get started with Amazon EC2 Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)**
Use this tutorial to get started with Amazon EC2. You'll learn how to launch, connect to, and use a Linux instance.

**[Tutorial: Get started with Amazon EC2 Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)**
Use this tutorial to get started with Amazon EC2. You'll learn how to launch, connect to, and use a Windows instance.

**[Amazon EC2 instance types](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html)**
This guide provides an overview of the various families of EC2 instance types and discusses the appropriate application for each family.

**[Get Started with Amazon EC2 Graviton instances](https://aws.amazon.com/ec2/graviton/getting-started/)**
This guide will help you get started with Amazon EC2 Graviton instances and provides steps-by-step instructions to migrate your workload to Graviton.

### Amazon EC2 Auto Scaling

**[Get started with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html)**
In this tutorial, you set up an Auto Scaling group, terminate your instance, and verify the instance was removed from service and replaced.

**[Tutorial: Scale the size of your Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html)**
In this tutorial, you learn how to scale your Auto Scaling group using either manual scaling, scheduled scaling, dynamic scaling, or predictive scaling.

**[Amazon EC2 Auto Scaling FAQs](https://aws.amazon.com/ec2/autoscaling/faqs/)**
Dive deep into the intricacies of EC2 Auto Scaling by reviewing the FAQ.

### Amazon EC2 Image Builder

**[Get started with EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-image-pipeline.html)**
This guide will help you set up your environment and create an automated image pipeline for the first time.

**[Building golden images using Amazon EC2 Image Builder workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/d6c7ecdc-c75f-4ad1-910f-fdd994cc4aed/en-US/100-ec2-ib)**
This workshop will guide you through creating an EC2 Image Builder pipeline and then developing your own custom components.

**[Implementing up-to-date images with automated EC2 Image Builder pipelines](https://aws.amazon.com/blogs/compute/implementing-up-to-date-images-with-automated-ec2-image-builder-pipelines/)**
This blog post demonstrates how to automatically keep your base or standard images current, incorporating patches and any other changes using EC2 Image Builder pipelines.

### Elastic Beanstalk

**[Get started with AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html)**
This tutorial walks you through creating, exploring, updating, and deleting an Elastic Beanstalk application. It takes less than an hour to complete.

**[Security best practices for AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security-best-practices.html)**
This guide provides you with general guidelines for securing your Elastic Beanstalk application.

**[Creating an ECS managed Docker environment with the Elastic Beanstalk console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_ecstutorial.html)**
In this tutorial, you’ll implement an ECS managed Docker environment that uses two containers.

### Amazon Lightsail

**[Launch a Linux virtual machine with Amazon Lightsail](https://aws.amazon.com/getting-started/hands-on/launch-a-virtual-machine/)**
In this tutorial, you create an Amazon Linux instance in Amazon Lightsail in seconds. After the instance is up and running, you connect to it via SSH within the Lightsail console using the browser-based SSH terminal.

## Resources

- **Learn**: [Explore whitepapers](https://aws.amazon.com/whitepapers/) to help you get started and learn best practices for compute services and use cases.
- **Build**: [Explore vetted solutions](https://aws.amazon.com/solutions/compute/) and architectural guidance for common use cases for compute.
- **Discover**: [Explore reference architecture diagrams](https://aws.amazon.com/architecture/) for compute on AWS.

---
