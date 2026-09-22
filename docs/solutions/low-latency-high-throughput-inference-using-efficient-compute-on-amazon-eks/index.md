---
source_url: https://docs.aws.amazon.com/solutions/low-latency-high-throughput-inference-using-efficient-compute-on-amazon-eks/index.html
---

---
title: 'Guidance for Low Latency, High Throughput Inference using Efficient Compute on Amazon EKS'
canonical_url: https://docs.aws.amazon.com/solutions/low-latency-high-throughput-inference-using-efficient-compute-on-amazon-eks/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Low Latency, High Throughput Inference using Efficient Compute on Amazon EKS

## Overview

This Guidance demonstrates how to deploy a machine learning inference architecture on Amazon Elastic Kubernetes Service (Amazon EKS). It addresses the basic implementation requirements as well as ways you can pack thousands of unique PyTorch deep learning (DL) models into a scalable architecture. PyTorch is an open-source machine learning framework that can help accelerate your machine learning journey from prototyping to deployment. We also explore a mix of Amazon Elastic Compute Cloud (Amazon EC2) instance families to develop an optimal design using efficient compute (such as AWS Graviton and AWS Inferentia) that allows you to scale inferences efficiently and cost effectively.

## How it works

### Infrastructure

This infrastructure diagram provides a way to setup an Amazon Elastic Kubernetes Service (Amazon EKS) cluster that is compatible with this Guidance. Optionally, a pre-existing Amazon EKS cluster can be used. To learn more about running inference workloads on this infrastructure, open theArchitecturetab.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/low-latency-high-throughput-inference-using-efficient-compute-on-amazon-eks.pdf#page=1)Step 1Administrator or DevOps user obtains Infrastructure as Code (IaC) code with Amazon EKS specification from Git repository.Step 2Amazon Elastic Compute Cloud (Amazon EC2) Management Instance provisioning is started by Admin/DevOps user via the AWS CloudFormation code obtained from the Git repo.Step 3Management Instance userData script starts Amazon EKS cluster resource deployment processes against target AWS environment (using eksctl command and cluster specification).Step 4Required AWS Identity and Access Management (IAM) roles, polices, and AWS Key Management Service (AWS KMS) keys are created.Step 5The Amazon EKS virtual private cloud (VPC) for the control plane component is deployed.Step 6The Amazon EKS cluster control plane components are deployed into the Amazon EKS VPC. The cluster control plane is provisioned across multiple Availability Zones and fronted by Elastic Load Balancing (ELB).Step 7Cluster VPC is deployed for the Amazon EKS compute plane.Step 8Public and Private subnets and other networking components are deployed in cluster VPCs.Step 9The Amazon EKS compute plane node groups. containing Amazon Elastic Compute Cloud (Amazon EC2) node instances in auto scaling groups, are deployed into the cluster VPC and join the Amazon EKS cluster.Step 10The Amazon EKS cluster is available for application deployment. The Kubernetes API is accessible for the command line interface (CLI) clients and applications through an ELB.### Architecture

This diagram provides a simple, scalable, and highly available architecture for running machine learning (ML) inference workloads on AWS. It uses a standard Amazon Elastic Kubernetes Service (Amazon EKS) infrastructure that can be deployed across multiple Availability Zones for high availability. For instructions to setup an Amazon EKS cluster compatible with this Guidance, open theInfrastructuretab.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/low-latency-high-throughput-inference-using-efficient-compute-on-amazon-eks.pdf#page=2)Step 1The Amazon Elastic Kubernetes Service (Amazon EKS) cluster has several compute node groups with one Amazon Elastic Compute Cloud (Amazon EC2) instance family per node group. Each node group can support different instance types, such as AWS Graviton Processors (c7g) or AWS Inferentia processors (inf2)-based instances deployed across Availability Zones (AZs).Step 2The natural language processing (NLP) models, serving application and machine learning (ML) framework dependencies, are built by users as container images using the automation framework. These images are uploaded to Amazon Elastic Container Registry (Amazon ECR). Decoupling the model container images from the model data reduces the size of the model container images.Step 3Using the automation framework, the model container images customized for each compute node instance, are obtained from the respective Amazon ECR repositories. They are deployed to the Amazon EKS cluster using generated deployment manifests via Kubernetes API exposed through Elastic Load Balancing (ELB).Step 4ML model application containers download the model artifacts from the model repository, such as Amazon Simple Storage Service (Amazon S3), or other repositories upon their initialization. This component of the architecture decouples the model data from its service definition. ML inference services are available in the Amazon EKS cluster.Step 5Load testing of the deployed ML inference services is performed using containerized test clients deployed using images from Amazon ECR repository by the automation framework. Test clients send simultaneous requests to the ML model service pool running in the Amazon EKS cluster. Performance Test results are obtained and aggregated.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/low-latency-high-throughput-inference-on-amazon-eks.html?target=_blank)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-machine-learning-inference-on-aws?target=_blank)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon EKS, Amazon ECR, and a test automation framework are used in this Guidance to enhance your operational excellence. It helps you visualize, customize, and understand the concept of serving ML models using a FastAPI framework, providing you the flexibility to choose the Amazon EKS node compute instances of your choice in order to optimize performance and costs. Amazon EKS and Amazon ECR are managed Kubernetes and image repository services, respectively, and fully support API-based automation of all phases of the machine learning operations (MLOps) cycle. We also show how you can automatically deploy and run a large number of customized machine learning models, as well as automate load and scale testing of those models' performance using an automation framework. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon EKS, Amazon VPC, IAM roles and policies, and Amazon ECR work in tandem to protect your information and systems. The Amazon EKS cluster resources are deployed into a VPC that provides a logical isolation of its resources from the public internet. A VPC supports a variety of security features, such as security groups and network access control lists (ACLs), which are used to control inbound and outbound traffic to resources, as well as IAM roles and policies for authorization to limit access. The Amazon ECR image registry provides additional container-level security features, such as vulnerability scanning. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon EKS and Amazon ECR are used throughout this Guidance to help your workloads perform their intended functions correctly and consistently. Amazon EKS deploys the Kubernetes control plane (the instances that control how, when, and where your containers run) and the compute planes (the instances where your containers run) across multiple Availability Zones (AZs) in AWS Regions. This ensures that both the control and compute planes are always available, even if one AZ goes down. Also, Elastic Load Balancing (ELB) will route application traffic to functional nodes. Additionally, the Amazon EKS cluster components are sending metrics to an Amazon CloudWatch portal, where events can be configured to invoke alerts in case certain thresholds are crossed. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon ECR, Amazon EKS, and Amazon EC2 were used in this Guidance to support a structured and streamlined allocation of IT and computing resources. The compute nodes within the Amazon EKS cluster (that are Amazon EC2 instances) can be scaled up and down based on the application's workload requirement while conducting the tests. Moreover, Amazon ECR and Amazon EKS are highly available services, optimized for scalability and performance of containerized applications. This Guidance leverages those and other services (such as Amazon S3, and the GitHub open-source software) to monitor and optimize performance characteristics of machine learning inference workloads through customization and automation. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon ECR is a managed service that optimizes the costs of both storing and serving container image applications that are deployed on Amazon EKS. The compute nodes of the Amazon EKS cluster can scale up or down, based on projected workloads, when performing tests. Also, Amazon EKS node groups can be efficiently scaled, helping you to identify the most cost-efficient compute node configuration for running ML inferences at scale. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EKS with the Amazon EC2 compute node instances deployed into the VPC and Amazon ECR do not use custom hardware. Meaning, you do not need to purchase or manage any physical servers. Instead, this Guidance uses managed services that run on the AWS infrastructure. Furthermore, by supporting the use of energy-efficient processor instance types, like AWS Graviton Processors, this architecture provides increased sustainability. Using Graviton running in Amazon EC2 can improve the performance of your workloads with less resources and thereby decreasing your overall resource footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
