---
source_url: https://docs.aws.amazon.com/solutions/distributed-model-training-on-aws/index.html
---

---
title: 'Guidance for Distributed Model Training on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/distributed-model-training-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Distributed Model Training on AWS

## Overview

This Guidance helps customers who have on-premises restrictions or who have existing Kubernetes investments to use either Amazon Elastic Kubernetes Service (Amazon EKS) and Kubeflow or Amazon SageMaker to implement a hybrid, distributed machine learning (ML) training architecture. Kubernetes is a widely adopted system for automating infrastructure deployment, resource scaling, and management of containerized applications. The open-source community developed a layer on top of Kubernetes called Kubeflow, which aims to make the deployment of end-to-end ML workflows on Kubernetes simple, portable, and scalable. With the ability to choose between two approaches at runtime in this architecture, customers gain maximum control over their ML deployments. They can continue using open-source libraries in their deep learning training script and still make it compatible to run on both Kubernetes and SageMaker.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/distributed-model-training-on-aws.pdf)

![Architecture diagram](/images/solutions/distributed-model-training-on-aws/images/distributed-model-training-on-aws-1.png)

1. **Step 1**: Deploy Kubeflow to Amazon Elastic Kubernetes Service (Amazon EKS) and access Jupyter Notebooks from the Kubeflow Central Dashboard. Kubernetes provides a command line tool (Kubectl) for communicating with a Kubernetes cluster's control plane, using the Kubernetes API.
1. **Step 2**: Use the Kubeflow Pipelines software development kit (SDK) to compile Python functions into workflow resources and to create Kubeflow pipelines.
1. **Step 3**: Use the Kubeflow Pipelines SDK client to call the pipeline service endpoint and run the pipeline.
1. **Step 4**: The pipeline evaluates the conditional runtime variables and decides between Amazon SageMaker or Kubernetes as the target run environment.
1. **Step 5**: Use the Kubeflow PyTorch Operator to run distributed training on the Kubernetes cluster, or use the SageMaker component to submit the training on the SageMaker managed platform.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/aws-do-kubeflow/tree/main/Container-Root/kubeflow/examples/distributed-training/pytorch/workshop)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

To support scalable simulation and key performance indicator (KPI) calculation models, use Amazon EKS and Amazon QuickSight. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Resources are stored in a virtual private cloud (VPC), which provides a logically isolated network. You can grant access to these resources using AWS Identity and Access Management (IAM) roles that grant least privilege, or the minimum number of permissions required to complete a task. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Kubeflow on AWS supports a data pipeline orchestration. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

If you have on-premises restrictions or existing Kubernetes investments, you can use Amazon EKS and Kubeflow on AWS to implement an ML pipeline for distributed training or use a fully managed SageMaker solution for production-scale training infrastructure. These two options help you scale to meet workload requirements of the training environment. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

We selected resource sizes and types based on resource characteristics and past workloads so you only pay for resources matched to your needs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

SageMaker is designed to handle training clusters that scale up as needed and shut down automatically when jobs are complete. SageMaker also reduces the amount of infrastructure and operational overhead typically required with training deep learning models on hundreds of GPUs. Amazon Elastic File System (Amazon EFS) integration with the training clusters and the development environment allow you to share your code and processed training dataset, so you don’t have to build the container image and load large datasets after every code change. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **AWS Machine Learning Blog**: Build flexible and scalable distributed training architectures using Kubeflow on AWS and Amazon SageMaker. This blog post demonstrates how Kubeflow on AWS (an AWS-specific distribution of Kubeflow) used with AWS Deep Learning Containers and Amazon EFS simplifies collaboration and provides flexibility in training deep learning models at scale on both Amazon EKS and Amazon SageMaker utilizing a hybrid architecture approach.

[Read the blog](https://aws.amazon.com/blogs/storage/machine-learning-with-kubeflow-on-amazon-eks-with-amazon-efs/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
