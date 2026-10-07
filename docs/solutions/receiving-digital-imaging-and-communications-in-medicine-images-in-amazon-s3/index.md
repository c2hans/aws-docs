---
source_url: https://docs.aws.amazon.com/solutions/receiving-digital-imaging-and-communications-in-medicine-images-in-amazon-s3/index.html
---

---
title: 'Guidance for Receiving Digital Imaging and Communications in Medicine (DICOM) Images in Amazon S3'
canonical_url: https://docs.aws.amazon.com/solutions/receiving-digital-imaging-and-communications-in-medicine-images-in-amazon-s3/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Receiving Digital Imaging and Communications in Medicine (DICOM) Images in Amazon S3

## Overview

This Guidance helps you send DICOM images directly to the cloud and store these images in Amazon Simple Storage Service (Amazon S3). This is accomplished by configuring a DICOM destination in your existing Picture Archiving and Communication System (PACS) or Vendor Neutral Archive (VNA) systems. The DICOM destination will be capable of receiving instances using DICOM Message Service Element (DIMSE). In this Guidance, image data is encrypted, and data storage is scalable to support variable workloads.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/receiving-digital-imaging-and-communications-in-medicine-images-in-amazon-s3.pdf)

![Architecture diagram](/images/solutions/receiving-digital-imaging-and-communications-in-medicine-images-in-amazon-s3/images/receiving-digital-imaging-and-communications-in-medicine-images-in-amazon-s3-1.png)

1. **Step 1**: Clients connect to the application through a Network Load Balancer (NLB) and send DIMSE C-STORE requests to the backend service.
1. **Step 2**: The NLB is deployed to a public subnet. Targets are one or more Amazon Elastic Container Service (Amazon ECS) on AWS Fargate task elastic network interfaces (ENIs) in a private subnet.
1. **Step 3**: An Amazon Virtual Private Cloud (Amazon VPC) security group allows fine-grained network access control to the application.
1. **Step 4**: Connections are passed to Amazon ECS on Fargate service tasks. Service task scaling is controlled through an AWS Auto Scaling rule, allowing the service to adjust its capacity according to demand. Container permissions are granted through the task AWS Identity Access and Management (IAM) role, avoiding the use of hard-coded credentials.
1. **Step 5**: Tasks access Amazon Simple Storage Service (Amazon S3) using reliable and private connectivity provided by a VPC gateway endpoint.
1. **Step 6**: Received DICOM images are stored in Amazon S3. Optionally, DICOM metadata can also be extracted and stored.
1. **Step 7**: Container definitions are stored in Amazon Elastic Container Registry (Amazon ECR) and are used by Amazon ECS on Fargate during deployment.
1. **Step 8**: Amazon CloudWatch collects container logs and metrics.
1. **Step 9**: The Guidance components access the internet using a VPC NAT gateway, avoiding the need to provision public IP addresses for all tasks.
1. **Step 10**: The Guidance is deployed as infrastructure-as-code using AWS Cloud Development Kit (AWS CDK).
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-receiving-digital-imaging-and-communications-in-medicine-images-into-amazon-s3)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance is deployed using AWS CDK, which allows operators to reduce deployment risk and gives them better control over the deployment process. By using Amazon ECR to store versioned container images, operators can more easily test changes and revert failed deployments with minimal impact to end users or the availability of the system. CloudWatch collects metrics and logs to provide insight into the operation of the system, making it easier to troubleshoot issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM roles and policies allow the system to contain no hard-coded credentials. AWS security groups and VPC endpoints are used to provide fine-grained access control. Further, this Guidance provides network segregation using public and private subnets. Data in transit is protected using TLS encryption. Data at rest is encrypted while stored on Amazon S3. Communication between tasks and Amazon S3 occurs over a VPC gateway endpoint and does not traverse the public internet. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Elastic Load Balancing (ELB) routes requests to multiple Fargate tasks, running in different Availability Zones (AZs). Using managed services such as ELB and Fargate improves reliability by removing single points of failure. The Fargate scheduler replaces failed tasks, and auto scaling allows the system to respond to changes in load without impacting clients or end users. As more DICOM images are received and processed in parallel, auto scaling helps ensure necessary resources are available across multiple AZs. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Fargate provides flexible task-sizing for both compute and memory capacity. This helps match resources to workload requirements to avoid overprovisioning. Amazon S3 provides performant object storage with virtually unlimited scalability, high availability, and multiple access tiers. Amazon S3 allows parallel access to objects without performance impact, and you can choose the most appropriate storage class based on data access for your workload. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 Intelligent-Tiering can reduce storage cost by automatically transitioning objects into a lower cost tier based on access patterns. Additionally, VPC endpoints allow connectivity between AWS services over private networking and can be used to reduce public data transfer and NAT gateway costs. This helps minimize data transfer outside of the VPC, reducing overall data transfer charges. Fargate allows for tracking and automated adjustment of provisioned compute based on current system load, and tasks can be appropriately sized to maximize cost efficiency. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3 and Fargate are managed services (operated at scale by AWS), which reduces the amount of infrastructure needed to support your workloads. Additionally, Amazon S3 Lifecycle policies can be used to reduce storage resources by automating the deletion of unneeded data. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
