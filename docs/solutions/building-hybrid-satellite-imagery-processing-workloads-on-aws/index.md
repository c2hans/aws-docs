---
source_url: https://docs.aws.amazon.com/solutions/building-hybrid-satellite-imagery-processing-workloads-on-aws/index.html
---

---
title: 'Guidance for Building Hybrid Satellite Imagery Processing Workloads on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-hybrid-satellite-imagery-processing-workloads-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Building Hybrid Satellite Imagery Processing Workloads on AWS

## Overview

This Guidance demonstrates how to deploy satellite data processing pipelines on AWS and on-premises environments with consistent infrastructure and user experiences. In the aerospace industry, a dual deployment is important for a variety of reasons, such as satisfying data residency requirements or protecting existing investments. With the same APIs and automation, deployment, and security tools, this Guidance helps you maintain your pace of innovation in either deployment while also diminishing your operational overhead. This approach allows for flexibility in managing hybrid infrastructure, streamlining operations, and maximizing efficiency in satellite data processing.

## Benefits

### Accelerate satellite imagery deployment cycles

Deploy containerized processing pipelines using GitOps automation with AWS CodePipeline and Flux CD. Reduce manual configuration errors while maintaining consistent environments across hybrid infrastructure.

### Process imagery where data resides

Run machine learning inferencing and batch processing locally using Amazon EKS on Outposts or EKS Anywhere. Meet data residency requirements while leveraging AWS-managed Kubernetes orchestration for satellite workloads.

### Unify monitoring across hybrid environments

Gain centralized visibility into your satellite processing pipelines with Amazon CloudWatch. Track performance metrics and operational health across both AWS Region and on-premises infrastructure from a single interface.

## How it works

### Deployment on AWS Outposts

This architecture diagram shows how to build a hybrid workload containing a satellite imagery processing pipeline deployed on an AWS Outposts rack.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-hybrid-satellite-imagery-processing-workloads-on-aws.pdf)Step 1Create a continuous integration (CI) pipeline for your imagery processing workloads using a Git repository, AWS CodePipeline, and AWS CodeBuild. Store the container images in Amazon Elastic Container Registry (Amazon ECR).Step 2Develop and train your machine learning (ML) models using Amazon SageMaker in the AWS Region, an alternative ML solution in an AWS Region, or as part of the on-premises deployment. AWS DataSync can be used to transfer model artifacts from Amazon Simple Storage Service (Amazon S3) in the AWS Region to Amazon S3 on Outposts.Step 3Use Amazon CloudWatch to centrally monitor AWS and on-premises resources.Step 4Achieve a consistent hybrid experience and fully managed infrastructure using an Outposts rack for the on-premises deployment.Step 5Host your processing pipeline in Amazon Elastic Kubernetes Service (Amazon EKS) on Outposts. Choose your preferred orchestrator solution, such as Prefect or Apache Airflow.Step 6Following GitOps practices, use a continuous delivery (CD) tool like Flux CD to retrieve and deploy the latest container images.Step 7Run batch operations to optimize processing time using Amazon EMR on Amazon EKS or another solution, such as Apache Beam.Step 8Use the ML framework chosen during model development, such as TensorFlow or PyTorch, for the processing pipeline steps that require ML inferencing.Step 9Store your raw and processed satellite imagery data in Amazon S3 on Outposts. Maintain metadata in Amazon Relational Database Service (Amazon RDS).Step 10A service link will connect the Outposts rack with your chosen AWS Region. Optionally, you can use AWS Direct Connect.### Deployment on premises

This architecture diagram shows how to build a hybrid workload containing a satellite imagery processing pipeline deployed on your infrastructure.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-hybrid-satellite-imagery-processing-workloads-on-aws.pdf)Step 1Create a CI pipeline for your imagery processing workloads using a Git repository, CodePipeline, and CodeBuild. Store the container images in Amazon ECR.Step 2Develop and train your machine learning (ML) models using Amazon SageMaker in the AWS Region, an alternative ML solution in an AWS Region, or as part of the on-premises deployment. DataSync can be leveraged to transfer model artifacts from Amazon S3 in the AWS Region to your on-premises storage solution.Step 3Use CloudWatch to centrally monitor AWS and on-premises resources.Step 4For cases where requirements do not allow for an Outposts rack deployment, this hybrid architecture can be deployed directly on your infrastructure.Step 5Host your processing pipeline in Amazon EKS Anywhere. Choose your preferred orchestrator solution, such as Prefect or Airflow.Step 6Following GitOps practices, use a continuous delivery (CD) tool like Flux CD to retrieve and deploy the latest container images.Step 7Run batch operations to optimize processing time using your preferred solution, such as Beam or Spark.Step 8Use the ML framework chosen during model development, such as TensorFlow or PyTorch, for the processing pipeline steps that require ML inferencing.Step 9Store your raw and processed satellite imagery data in your chosen object storage solution. Maintain metadata in a PostgreSQL database.Step 10Connect your AWS Region deployment with your corporate data center using AWS Site-to-Site VPN or Direct Connect.## Related content

- **Building hybrid satellite imagery processing pipelines in AWS**: This blog post demonstrates how companies operating in AWS can design highly-flexible architectures that can support both cloud and on-premises deployment use cases.

[Learn more](https://aws.amazon.com/blogs/publicsector/building-hybrid-satellite-imagery-processing-pipelines-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
