---
source_url: https://docs.aws.amazon.com/solutions/low-latency-high-throughput-model-inference-using-amazon-sagemaker/index.html
---

---
title: 'Guidance for Low-Latency, High Throughput Model Inference Using Amazon SageMaker'
canonical_url: https://docs.aws.amazon.com/solutions/low-latency-high-throughput-model-inference-using-amazon-sagemaker/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Low-Latency, High Throughput Model Inference Using Amazon SageMaker

## Overview

This Guidance shows how to use Amazon SageMaker to support high-throughput model inferencing workloads like programmatic advertising and real-time bidding (RTB). For instance, your demand-side platform could use machine learning (ML) models to determine whether to place a bid for an advertising campaign and at what price. By using this Guidance, you can cost-effectively scale to millions of requests per second at a low latency. Note: Before beginning this Guidance, you will need to containerize your models. [SageMaker Model Training](https://aws.amazon.com/sagemaker/train/) provides a wide range of built-in algorithms and frameworks (such as for scikit-learn and XGBoost) you can use to train and tune your ML models. Alternatively, you can bring your own script.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/low-latency-high-throughput-model-inference-using-amazon-sagemaker.pdf)

![Architecture diagram](/images/solutions/low-latency-high-throughput-model-inference-using-amazon-sagemaker/images/low-latency-high-throughput-model-inference-using-amazon-sagemaker-1.png)

1. **Step 1**: A consumer application is deployed within a virtual private cloud (VPC) in your AWS account, using Amazon Virtual Private Cloud (Amazon VPC). This application can be hosted on Amazon Elastic Compute Cloud (Amazon EC2) instances or as containers running on either Amazon Elastic Kubernetes Service (Amazon EKS) or Amazon Elastic Container Service (Amazon ECS).
1. **Step 2**: The consumer application connects to Amazon SageMaker Real-Time inference servers using VPC endpoints powered by AWS PrivateLink. This means that all API calls happen over the private network of AWS and not the public internet, minimizing the latency of the invocations and improving your security posture.
1. **Step 3**: The inference requests are routed through a Network Load Balancer to the SageMaker real-time inference servers. These servers are hosted across multiple Availability Zones (AZs) within an Amazon EC2 Auto Scaling group. This allows the model inference infrastructure to be elastic and highly available. SageMaker real-time inferences provide a choice of Amazon EC2 instance types. These include Amazon EC2 Inf1 instances based on AWS Inferentia, high-performance machine learning (ML) inference chips designed and built by AWS, and GPU instances, such as Amazon EC2 G4dn. Multiple hosting options, including shadow testing and an inference recommendation feature in the managed service, reduce operational burden and accelerates time to value.
1. **Step 4**: Consumer applications and batch applications use Amazon Simple Storage Service (Amazon S3) to store and retrieve data and use it for offline ML training and experiments. Access to Amazon S3 from the VPC is secured through PrivateLink.
1. **Step 5**: Data scientists use SageMaker to experiment, build, and train the ML model. Once the model is ready, it is saved in Amazon S3 for the model inference task to load. Access to Amazon S3 from the VPC is again secured through PrivateLink.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/advertising-marketing/low-latency-high-throughput-model-inference-using-amazon-sagemaker.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-low-latency-high-throughput-model-inference-using-amazon-sagemaker)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch aggregates logs and creates observability metrics and dashboards, providing visualizations to help you identify performance bottlenecks and troubleshoot requests. You can also set up CloudWatch alarms to identify trends that could be problematic and alert you before they impact your application or business. Additionally, you can use AWS CloudTrail, which keeps track of account activity, to enable governance and risk auditing, as well as facilitate the compliance of your AWS account. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The principle of least privilege is the industry best practice for reducing the surface area of security risks. AWS Identity and Access Management (IAM) policies use least-privilege access so that every policy is restrictive to the specific resource and operation. Additionally, to implement security in layers, this Guidance encrypts data in transit and transfers it over HTTPS, and AWS Key Management Service (AWS KMS) keys encrypt data at rest in Amazon S3 buckets. Finally, real-time bidding (RTB) applications access SageMaker endpoints and Amazon S3 only through PrivateLink, enhancing your security posture. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

All the services used in this Guidance are serverless and can automatically scale horizontally based on workload demand. In the SageMaker inference endpoints, Amazon EC2 Auto Scaling groups launch instances across AZs to provide high availability. Additionally, Amazon S3 supports features like S3 Versioning, which helps you maintain data version control, prevent accidental deletions, and replicate data to the same or a different AWS Region. With the ability to preserve, retrieve, and restore every version of an object stored in Amazon S3, you can recover from unintended user actions and application failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS managed services offload infrastructure management and scaling from you so that you can focus on solving your business needs. In this Guidance, SageMaker manages the hosting of your model inference endpoints. It retrieves the models from Amazon S3 buckets at deployment time, then hosts the most optimal implementation runtime containers. By using its inference recommender and a load-testing tool, SageMaker can choose the optimal instance size based on throughput capacity and incurred latencies. This enables it to manage the scaling of the inference compute through load balancers and Amazon EC2 Auto Scaling groups. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses serverless technologies and managed services so that you only pay for the resources you consume. You can also select options to further reduce costs. For example, Amazon SageMaker Savings Plans offer a flexible, usage-based pricing model in exchange for a commitment to a consistent amount of usage. You can also store data cost-effectively by choosing from a range of Amazon S3 storage classes built for specific use cases and access patterns. For example, if you use Amazon S3 Intelligent-Tiering for data with changing, unknown, or unpredictable access patterns—such as data lakes, analytics, or new applications—it will automatically optimize costs by moving your data between tiers for frequent, infrequent, and rare access. Additionally, by securing traffic over a private network using PrivateLink, you can reduce data transfer fees. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses serverless technologies that scale up and down to meet demand so that resources don’t consume energy while idle. Additionally, SageMaker endpoints use custom infrastructure that is optimal to the workload demands of model training and inference, helping you achieve more with fewer resources and a lower carbon footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
