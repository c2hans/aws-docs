---
source_url: https://docs.aws.amazon.com/solutions/training-protein-language-models-esm-2-with-amazon-sagemaker-ai-hyperpod/index.html
---

---
title: 'Guidance for Training Protein Language Models (ESM-2) with Amazon SageMaker HyperPod'
canonical_url: https://docs.aws.amazon.com/solutions/training-protein-language-models-esm-2-with-amazon-sagemaker-ai-hyperpod/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Training Protein Language Models (ESM-2) with Amazon SageMaker HyperPod

## Overview

This Guidance demonstrates how to streamline and accelerate the training of complex protein folding AI models using AWS SageMaker HyperPod's managed platform. By leveraging NVIDIA GPUs and automated cluster provisioning, researchers can significantly simplify the distributed training process for generative AI models like ESM-2. The solution addresses key challenges in high-performance computing for life sciences, enabling efficient model customization and deployment at scale. This approach helps research teams reduce operational complexity while maximizing computational resources, ultimately accelerating breakthrough discoveries in protein research and drug development.

## Benefits

### Accelerate ML model training deployment

Streamline ESM-2 model training with pre-configured HyperPod clusters that automatically handle distributed computing requirements. Reduce time-to-market while maintaining operational excellence through automated infrastructure deployment.

### Optimize ML infrastructure costs

Reserve compute capacity through Flexible Training Plans and On-Demand Capacity Reservations for predictable pricing. Scale ML training resources efficiently while maintaining cost optimization through managed infrastructure.

### Enhance ML operations visibility

Monitor training progress through comprehensive observability tools that provide real-time metrics. Track cluster health and performance indicators while maintaining operational excellence through unified dashboards.

## How it works

### Deploy SageMaker HyperPod cluster with SLURM orchestrator

This reference architecture demonstrates how to deploy Amazon SageMaker AI HyperPod clusters based on HPC (SLURM) orchestrator.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/training-protein-language-models-esm-2-with-amazon-sagemaker-ai-hyperpod.pdf)Step 1The account team reserves compute capacity with On-Demand Capacity Reservations (ODCR) or Amazon SageMaker HyperPod Flexible Training Plans for projected jobs.Step 2Admin/DevOps Engineers use the Amazon Sagemaker HyperPod Virtual Private Cloud VPC Amazon CloudFormation stack to deploy networking, storage and Identity and Access Management IAM resources into the Customer Account.Step 3Admin/DevOps Engineers push Lifecycle scripts to the designated Amazon Simple Storage Service (Amazon S3) bucket created in the previous step.Step 4Admin/DevOps Engineers use the Amazon SageMaker AI CLI to provision the SageMaker AI HyperPod cluster.Step 5Admin/DevOps Engineers generate key-pairs to establish SSH access to the Controller Node of the HyperPod cluster.Step 6Once the HyperPod cluster is created, Admin/DevOps or ML Engineers can test SSH access to the Controller and Compute Nodes and examine the cluster.Step 7Admin/DevOps Engineers configure IAM Identity Center to use Amazon Managed Service for Prometheus for collection of cluster metrics and Amazon Managed Grafana to set up the observability stack.Step 8Admin/DevOps Engineers can make further changes to the cluster using the HyperPod CLI.### Run protein language model distributed training workloads on HyperPod-SLURM clusters

This reference architecture demonstrates how to run distributed ESM-2 model training jobs on a SLURM based HyperPod cluster.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/training-protein-language-models-esm-2-with-amazon-sagemaker-ai-hyperpod.pdf)Step 1Admin/DevOps Engineers move their training data from on-premise to an Amazon Simple Storage Service (Amazon S3) bucket.Step 2Admin/DevOps Engineers create Data Repository Associations between an Amazon S3 bucket and Amazon FSx for Lustre.Step 3Data Scientists/ML Engineers build AWS optimized Docker container images with a set base image.Step 4Data Scientists/ML Engineers create an NVIDIA Enroot image based on the Docker image.Step 5Data Scientists/ML Engineers create a SLURM training jobs submission script using the NVIDIA Enroot image.Step 6Data Scientists/ML Engineers submit model training SLURM jobs that reference the ESM dataset and use container images built in steps 3 and 4 to run on the Amazon SageMaker AI HyperPod compute nodes via Controller Node.Step 7Amazon SageMaker AI HyperPod SLURM cluster compute nodes run training job tasks and write checkpoints to the shared FSx for Lustre file system. Data Scientists can monitor the training process via logs to determine when the training job is completed.Step 8(Optional) Admin/DevOps Engineers can create Login Nodes for Data Scientists/ML Engineers to only submit training jobs but without access to making cluster configuration changes.### Deploy SageMaker HyperPod cluster with Amazon EKS (Kubernetes) orchestrator

This reference architecture demonstrates how to deploy SageMaker HyperPod clusters based on Amazon EKS orchestrator.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/training-protein-language-models-esm-2-with-amazon-sagemaker-ai-hyperpod.pdf)Step 1Account team reserves capacity with ODCRs or Amazon SageMaker AI HyperPod Flexible Training Plans.Step 2Admin/DevOps Engineers can use eksctl CLI to provision an Amazon Elastic Kubernetes Service (Amazon EKS) cluster.Step 3Admin/DevOps Engineers use the Amazon SageMaker AI HyperPod VPC stack to deploy HyperPod managed node group on the Amazon EKS cluster.Step 4Admin/DevOps Engineers verify access to Amazon EKS cluster API via Network Load Balancer (NLB).Step 5Admin/DevOps Engineers can install FSx for Lustre CSI driver and mount that file system on the Amazon SageMaker AI HyperPod Amazon EKS cluster.Step 6Admin/DevOps Engineers install Amazon Elastic Fabric Adaptor (EFA) Kubernetes device plugins connected to compute nodes for Elastic Network Interface (ENI) based connectivity cross account.Step 7Admin/DevOps Engineers can configure AWS Container Insights to push Amazon SageMaker HyperPod cluster workloads metrics into Amazon Cloudwatch.Step 8Admin/DevOps Engineers configure IAM to use Amazon Managed Prometheus to collect metrics and Amazon Managed Grafana to set up the observability stack.### Run protein language model distributed training workloads on HyperPod-EKS clusters

This reference architecture demonstrates how to run distributed ESM-2 training jobs on an Amazon EKS based HyperPod cluster.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/training-protein-language-models-esm-2-with-amazon-sagemaker-ai-hyperpod.pdf)Step 1Admin/DevOps Engineers move their training data from on-prem to an Amazon Simple Storage Service (Amazon S3) bucket.Step 2Admin/DevOps Engineers can create Data Repository Associations between Amazon S3 and Amazon FSx for Lustre.Step 3Data Scientists/ML Engineers build AWS optimized Docker container images with a designated base image.Step 4Data Scientists/ML Engineers push Docker images to Amazon Elastic Container Registry (Amazon ECR).Step 5Administrators/DevOps Engineers deploy Kubeflow Training Operators to Amazon SageMaker AI HyperPod Amazon Elastic Kubernetes Service (Amazon EKS) cluster to orchestrate PyTorch based distributed training jobs.Step 6Data Scientists/ML Engineers deploy Kubernetes model training manifests that reference the ESM-2 dataset and use container images built in Step 3 to kickstart model training jobs on the compute nodes.Step 7Amazon SageMaker AI HyperPod cluster Compute Nodes write model training job checkpoints to the shared FSx for Lustre file system. Data Scientists can monitor the training process via logs to determine when training job is completed.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/training-protein-language-models-esm-2-with-amazon-sagemaker-ai-hyperpod.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-protein-language-esm-model-training-with-sagemaker-hyperpod)

[Read usage guidelines](/solutions/guidance-disclaimers/)
