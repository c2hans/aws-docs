---
source_url: https://docs.aws.amazon.com/solutions/media-provenance-with-c2pa-on-aws/index.html
---

---
title: 'Guidance for Media Provenance with C2PA on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/media-provenance-with-c2pa-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Media Provenance with C2PA on AWS

Establishing digital content authenticity

## Overview

The Guidance demonstrates how to implement the Coalition for Content Provenance and Authenticity (C2PA) standard for tracking provenance in fragmented MP4 (fMP4) and non-fragmented MP4 media workloads on AWS. C2PA enables the creation of digitally signed manifests that accompany digital media assets to document their provenance in a secure, tamper-evident format, which is particularly crucial in an era of sophisticated AI-generated content. This Guidance automates the provenance tracking process by integrating the C2PA open-source tools within a containerized environment optimized for media workflows. The implementation, which can be deployed with a CloudFormation template, uses Docker containers deployed on AWS infrastructure, giving an option for leveraging AWS Fargate for container orchestration and AWS Lambda for serverless processing for signing of the asset with C2PA.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/media-provenance-with-c2pa-on-aws.pdf)

![Architecture diagram](/images/solutions/media-provenance-with-c2pa-on-aws/images/media-provenance-with-c2pa-on-aws-1.png)

1. **Step 1**: Users access UI with Amazon Cognito managed authentication workflow.
1. **Step 2**: Users upload images, videos, or fragmented MP4s with AWS Amplify to an Amazon Simple Storage Service (Amazon S3) using AWS Key Management Service (AWS KMS) to encrypt and decrypt stored objects.
1. **Step 3**: AWS AppSync provides the API to Amplify for the UI.
1. **Step 4**: AWS Lambda routes requests and responses between the frontend and the compute.
1. **Step 5**: Users select Lambda or AWS Fargate options to create or extend the C2PA manifests.
1. **Step 6**: Lambda can be used for short tasks such as signing of images.
1. **Step 7**: Fargate can be used for longer tasks such as signing of videos. An Application Load Balancer (ALB) exposes the REST API on Fargate.
1. **Step 8**: The container image on Amazon Elastic Container Registry (Amazon ECR) contains the signing tool.
1. **Step 9**: Amazon Elastic Container Service (Amazon ECS) pulls the container image from Amazon ECR, then Fargate runs the containers in a serverless environment.
1. **Step 10**: AWS Secrets Manager securely stores root CA certificates and private keys which are used to sign a claim in a C2PA manifest.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-media-provenance-with-c2pa-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The AWS Cloud Development Kit (AWS CDK), which enables you to manage infrastructure as code, lets your developers automatically deploy, update, or delete this Guidance for different environments. Additionally, it enables a scalable and structured approach to managing infrastructure. As a result, you can reduce potential manual operational error risk on the console and easily deploy the solution to other parts of your business. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM roles protect the API that is exposed by Lambda function URLs, so only users with the right permissions can call endpoints. Additionally, users must access the API exposed by Fargate by using an internal Application Load Balancer that is only available to callers within your VPC. You can incorporate Amazon Virtual Private Cloud (Amazon VPC) advanced security features to configure specific access rules. Finally, Secrets Manager securely stores digital certificates and the private keys that are used to sign C2PA manifests, and it also provides auditing and monitoring tools. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda generates C2PA manifests in a serverless environment that is designed to be highly available and reliable. For example, it automatically scales functions to maintain availability, retries processes in the event of failure, and can be configured to run in multiple Availability Zones (AZs) to provide resilience. Amazon Elastic Container Service (Amazon ECS), used with Fargate, is an alternative architecture to generate C2PA manifests. This architecture uses a fully managed service to deploy and manage containerized applications, and it supports reliability through health checks and automatic healing to handle unexpected system errors. For example, Fargate continuously monitors and replaces any failed or unhealthy containers and scales based on workload to maintain application reliability and responsiveness. Additionally, if you configure Fargate to run in multiple AZs, Application Load Balancer will automatically route requests to healthy containers, making request handling more resilient. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda supports function URLs, simplifying the architecture by exposing a REST API without an API gateway. These functions scale automatically based on demand, so your DevOps teams do not have to provision and manage Amazon Elastic Compute Cloud (Amazon EC2) instances or plan and manage Amazon EC2 Auto Scaling groups. Additionally, Fargate simplifies containerized application deployment by launching tasks in a serverless environment without the need to provision and maintain Amazon EC2 instances. You can also size Fargate tasks to match workload characteristics and configure it to automatically scale the number of running tasks up or down to maximize the use of computing resources. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda only bills for the time it is processing data and scales based on demand so that you are not billed for idle computational resources. Additionally, you can configure Fargate to use the right CPU and memory sizes to balance performance against cost. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda only uses the computational energy required for your workload. Fargate is a managed service, so instead of implementing your own container infrastructure, you can rely on AWS for the high utilization and sustainability optimization of the deployed hardware. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Ensuring media authenticity, traceability, and integrity by running C2PA on AWS**: This blog post demonstrates how C2PA gives media companies a powerful tool to track the provenance of assets and build trust and transparency.

[Learn more](https://aws.amazon.com/blogs/media/ensuring-media-authenticity-traceability-and-integrity-by-running-c2pa-on-aws/)

- **AWS Innovation with Sinclair**: This podcast demonstrates how Sinclair, a diversified media company, rapidly built and tested a cloud-native solution using AWS Lambda and Amazon ECS to cryptographically sign content across production workflows for provenance validation.

[Learn more](https://aws.amazon.com/podcasts/innovation-ambassadors/ia-podcast-ep-47-sinclair/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
