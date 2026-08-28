---
source_url: https://docs.aws.amazon.com/whitepapers/latest/containers-on-aws/key-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Key considerations
<a name="key-considerations"></a>

## Container runtime
<a name="container-runtime"></a>

 A container runtime, also known as container engine, is a software component that can run containers on a host operating system. Container runtimes are responsible for loading container images from a repository, monitoring local system resources, isolating system resources for use of a container, and managing container lifecycle. They come in two forms:
+  High-level container runtimes (such as *containerd* and *CRI-O*) provide functions that run on top of low-level runtime.
+  Low-level runtimes are responsible for creating and running containers. The primary job of the low-level container runtimes is to provide container lifecycle management. These runtimes implement the Runtime Specification provided by the OCI(Open Container Initiative), a Linux Foundation project started by Docker, which aims to provide open standards for Linux containers. The default reference implementation for low level runtimes specified by OCI is *runc*.

 It’s important to note that Kubernetes and Amazon EKS have started using *containerd* as the default runtime from version 1.24. This shouldn’t impact your existing images if they are OCI compliant. Refer to the blog post [All you need to know about moving to containerd on Amazon EKS](https://aws.amazon.com/blogs/containers/all-you-need-to-know-about-moving-to-containerd-on-amazon-eks/) for key factors when migrating to *containerd*.

## Container-enabled AMIs
<a name="container-enabled-amis"></a>

 AWS has developed a streamlined, purpose-built operating system for use with Amazon Elastic Container Service. The Amazon ECS-optimized AMI is built on top of Amazon Linux 2 and Amazon Linux 2023. It is pre-configured with the Amazon ECS container agent and containerd daemon with runtime dependencies. The Amazon EKS-optimized Amazon Linux AMI is based on Amazon Linux 2. It includes kubelet, AWS IAM Authenticator, Docker (for Amazon EKS version 1.23 and earlier), and containerd.

 Although you can create your own custom AMIs that meet the basic specifications needed to run your containerized workloads, the Amazon ECS and Amazon EKS-optimized AMIs are pre-configured with requirements and recommendations tested by AWS engineers. You can also use [*Bottlerocket*](https://github.com/bottlerocket-os/bottlerocket), a Linux-based open-source operating system purpose-built by AWS for running containers. Bottlerocket includes only the essential software required to run containers and ensures that the underlying software is always secure. With Bottlerocket, you can reduce maintenance overhead and automate workflows by applying configuration settings consistently as nodes are upgraded or replaced.

 You can run Windows containers on both Amazon EKS and Amazon ECS. This helps anyone who wants to run Windows workloads on Amazon EKS and Amazon ECS. Amazon ECS supports Windows containers on Fargate, but they are not supported for Amazon EKS Pods on Fargate. Refer to the [best practices guide](https://aws.github.io/aws-eks-best-practices/windows/docs/ami/) and [key considerations](https://docs.aws.amazon.com/eks/latest/userguide/windows-support.html) before running Windows containers on Amazon EKS.

## Compute options
<a name="compute-options"></a>

 From a compute choice perspective, AWS offers a wide range of [instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) for running applications. AWS also offers purpose-built compute for meeting specific requirements. For instance, customers can leverage Nitro-based Amazon EC2 instances for running IPv6-enabled Amazon EKS clusters.

### Graviton
<a name="compute-options-graviton"></a>

 Graviton-powered instances provide the best price performance across a wide variety of general-purpose, compute-optimized, memory-optimized and accelerated compute instances. [Graviton2 processors](https://aws.amazon.com/ec2/graviton/) on Amazon EC2 general purpose (M6g), compute-optimized (C6g), and memory-optimized (R6g) Amazon EC2 instances deliver up to 40% improved price/performance over current generation M5, C5, and R5 instances. Customers can leverage Graviton on AWS-managed services (Amazon RDS, Aurora, MemoryDB) and AWS compute options (Amazon EKS, Amazon ECS, Amazon EMR, Lambda, Fargate, Elastic Beanstalk). Amazon EC2 instances powered by next-generation ARM64-based Graviton processors are well-suited for a broad spectrum of workloads, including application servers, open source databases, in-memory caches, microservices, gaming servers, electronic design automation, high-performance computing, and video encoding. Both Graviton instance generations are available to Amazon EKS. Running performance-optimized workloads on the latest Graviton instances, you can observe up to 19% performance increase and up to 15% cost savings compared to Graviton2 instances. Running containers on Graviton 3 instances also helps build a sustainable architecture that’s 60% more energy efficient over comparable Amazon EC2 instances.

 AWS Graviton has broad support for using its instance types on Amazon ECS and Amazon EKS. Amazon ECR also supports storing multi-architecture images including images built for arm architectures and can use Graviton compute. Graviton is also supported on container-optimized operating systems like BottleRocket and on serverless AWS compute services like Fargate.

### Compute for specialized workloads
<a name="compute-options-for-specialized-workloads"></a>

 With the increasing importance of use cases in generative AI, machine mearning (ML) and big data and analytics to global businesses and industries, containers have emerged as a popular option to run data workloads. These workloads are often high-throughput, compute-intensive, and critical to business operations, requiring the right configuration to support their requirements. AWS container services such as Amazon ECS and Amazon EKS have native integration with AWS Batch to support batch-oriented workloads. For workloads that require GPUs, both Amazon ECS and Amazon EKS support using GPU-based instances. In addition, you can leverage Amazon EKS and Amazon ECS with instance types such as Inferentia and Trainium to run machine-learning workloads at scale, with comparable performance at a much lower cost to GPU instances.

 You can also take advantage of projects and frameworks such as Data on EKS (DoEKS) to simplify and speed up the process of building, deploying, and scaling data workloads on Amazon EKS. DoEKS offers IaC templates in Terraform and [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/), performance benchmark reports, best practices, and sample code to help users run applications like Spark, Kubeflow, MLFlow, Airflow, Presto, Kafka, Cassandra, and more on Amazon EKS with ease.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
