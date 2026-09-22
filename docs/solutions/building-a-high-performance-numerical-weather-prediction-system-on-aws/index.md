---
source_url: https://docs.aws.amazon.com/solutions/building-a-high-performance-numerical-weather-prediction-system-on-aws/index.html
---

---
title: 'Guidance for Building a High-Performance Numerical Weather Prediction System on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-high-performance-numerical-weather-prediction-system-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Building a High-Performance Numerical Weather Prediction System on AWS

## Overview

This Guidance shows how to predict the weather over the Continental United States (CONUS) by deploying the Weather Research and Forecasting (WRF) model on AWS. Provided by the National Center for Atmospheric Research (NCAR), the WRF model helps support atmospheric research and operational forecasting applications. By running the WRF model using high performance computing (HPC) clusters on AWS, you can maximize the performance of your weather prediction workloads to accurately and reliably predict, plan, and manage weather forecasts.

## How it works

### HPC Cluster Deployment

This architecture diagram shows how to provision the AWS ParallelCluster user interface (UI) and configure an HPC cluster with compute and storage capabilities. For the numerical weather prediction workflow, open the other tab.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-a-high-performance-numerical-weather-prediction-system-on-aws.pdf)Step 1Users deploy the Guidance AWS CloudFormation stack to provision networking resources (Amazon Virtual Private Cloud [Amazon VPC] and subnets), storage (Amazon FSx for Lustre), and the AWS ParallelCluster UI.Step 2The AWS ParallelCluster UI endpoint is available for user authentication using Amazon API GatewayStep 3Users authenticate to the AWS ParallelCluster UI endpoint through an AWS Lambda function integrated with Amazon Cognito to handle log-in details.Step 4Authenticated users provision HPC clusters through the AWS ParallelCluster UI using cluster specifications available with the Guidance code. Each HPC cluster contains several node groups dynamically provisioned for application workload implementation.Step 5Users authenticated through the AWS ParallelCluster UI can connect to the HPC clusters either by using Session Manager from AWS Systems Manager or by using Amazon Desktop Cloud Visualization (Amazon DCV) sessions.### Prediction Workflow

This architecture diagram shows how to predict the weather for CONUS by deploying the WRF model on AWS and setting up the numerical weather prediction workflow. For the HPC cluster deployment, open the other tab.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-a-high-performance-numerical-weather-prediction-system-on-aws.pdf)Step 1Users authenticate to the AWS ParallelCluster UI (as detailed in the previous HPC Cluster Deployment architecture diagram).Step 2Users connect to the HPC cluster using either the AWS ParallelCluster UI through the Session Manager or by using a Amazon DCV connectionStep 3Slurm Workload Manager (an HPC resource manager) is used to manage and scale the resources of AWS ParallelCluster, such as dynamically provisioned Amazon Elastic Compute Cloud (Amazon EC2) instances connected by the Elastic Fabric Adapter (EFA) network. Scaling is managed in an Amazon EC2 Auto Scaling placement group.Step 4Spack (a software package manager for supercomputers) is installed. Spack is used to install necessary compilers, libraries like NCAR Command Language, and the Weather Research & the Forecasting (WRF) model.

Step 5FSx for Lustre storage was created along with the HPC cluster. The input data used to simulate the WRF test model (12-km CONUS) is copied to a local directory mounted to that storage.Step 6Users create an sbatch script to run the CONUS 12-km model, submit that job, and monitor its implementation status by using a squeue command.Step 7Numerical weather prediction results are stored in a locally mounted directory. Users can retrieve and visualize the results using NCAR Command Language scripts.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/building-a-high-performance-numerical-weather-prediction-system-on-aws.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-building-a-high-performance-numerical-weather-prediction-system-on-aws/tree/main)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses a combination of fully managed services (including API Gateway, Amazon Cognito, and Lambda) and self-managed services (including FSx for Lustre and Amazon EC2). The latter services are deployed to a configurable HPC cluster by means of a template and can be reconfigured or updated if cluster performance requirements change. You can use Amazon CloudWatch to monitor all these services through event logging. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito and API Gateway provide secure authentication and authorization and secure API access management. You can then log in to the HPC cluster’s head node for application deployment and management, using the AWS Systems Manager Session Manager secure shell—which provides greater security—or by using NICE DCV. Additionally, FSx for Lustre provides data encryption both in transit and at rest. By scoping AWS Identity and Access Management (IAM) policies to the minimum permissions required, you can limit unauthorized access to resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS ParallelCluster uses HPC cluster job scheduling to enable parallel computational task implementation, using Slurm Workload Manager, which optimally allocates resources based on job requirements, priorities, and user-defined policies. This reduces the chance of application failure so that you can run weather simulations and avoid downtime errors. Additionally, this Guidance deploys EC2 instances in different Availability Zones for increased reliability, and FSx for Lustre provides highly reliable storage for your HPC clusters. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance lets you efficiently manage and provision HPC clusters using AWS ParallelCluster and a YAML-based configuration. AWS ParallelCluster efficiently scales its CPU and RAM footprint and the instance number both horizontally and vertically to handle increased workloads. This Guidance also uses Message Passing Interface to provide efficient parallel processing and distributed data processing capabilities. Additionally, FSx for Lustre provides a high-performance storage layer for the HPC clusters. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

As a managed service, Amazon Cognito provides cost-effective user authentication and authorization. Additionally, Amazon EC2 Auto Scaling scales cluster node instances horizontally or vertically based on workload demand, so that you won’t have to provision and pay for unused resources. FSx for Lustre also provides a cost-efficient storage layer that makes it easy to launch, run, and scale storage for your HPC tasks. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses specialized Amazon EC2 instances (including Hpc6a instances powered by third-generation AMD Epyc processors) that offer high performance for compute-intensive HPC workloads. This performance, combined with the elasticity and scalability of serverless of AWS services, helps you achieve optimal resource utilization, helping you avoid overprovisioning resources. Additionally, FSx for Lustre supports concurrent access to the same files and directories from thousands of compute instances, further helping you minimize your workloads’ environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
