---
source_url: https://docs.aws.amazon.com/solutions/building-a-containerized-and-scalable-web-application-on-aws/index.html
---

---
title: 'Guidance for Building a Containerized and Scalable Web Application on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-containerized-and-scalable-web-application-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Building a Containerized and Scalable Web Application on AWS

Gain application scalability and serverless computing capabilities for your workload

## Overview

This Guidance provides a streamlined way for you to build, deploy, and manage a highly scalable, containerized three-tier web application for your small- or medium-size business. This Guidance captures the entire lifecycle of the application, from setting up the architecture to deploying the containers and monitoring the system’s performance. By focusing on containerization, you can dynamically adjust resources based on demand, so your web application can handle increased traffic and sudden spikes without compromising performance or user experience. Containerized web applications can help you optimize application resources and improve your web application development.

## How it works

This architecture diagram shows how you can deploy a scalable, secure three-tier web application using containerization on AWS without needing extensive knowledge in containerization or infrastructure management.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-a-containerized-and-scalable-web-application-on-aws.pdf?target=_blank)

![Architecture diagram](/images/solutions/building-a-containerized-and-scalable-web-application-on-aws/images/building-a-containerized-and-scalable-web-application-on-aws-1.png)

1. **Step 1**: Route traffic from your web client based on the request path for static and dynamic content using domain name service (DNS) Amazon Route 53.
1. **Step 2**: Protect and control access to your web application using Amazon Cognito.
1. **Step 3**: Use a content delivery network (CDN) like Amazon CloudFront to reduce the latency for delivering your static content.
1. **Step 4**: Use Amazon Simple Storage Service (Amazon S3) to store static content and backups.
1. **Step 5**: Handle all incoming API calls and traffic management with authorization, access control, and throttling using Amazon API Gateway.
1. **Step 6**: Configure Application Load Balancer to be internet-facing, and use it to distribute web traffic to your application across multiple Availability Zones (AZs).
1. **Step 7**: Run the application on Amazon Elastic Container Service (Amazon ECS), and use AWS Fargate for serverless compute. Send API calls for dynamic content.
1. **Step 8**: Retrieve application data and content from Amazon DynamoDB anytime there is an API call.
1. **Step 9**: Store the container image running the application in Amazon Elastic Container Registry (Amazon ECR). Use Amazon ECS to pull the image to run the application.
1. **Step 10**: Use Amazon CloudWatch to monitor and observe the application and all the resources.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses CloudWatch to help you define, capture, and analyze workload metrics to gain visibility and useful insights into workload events. You can implement CloudWatch dashboards with business and technical viewpoints to understand the health of your workload and help team members make informed decisions. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance promotes a robust security posture, helping you safeguard your data and protect against potential vulnerabilities without having to build the complex security controls yourself. It uses Amazon Cognito for user identity and access management, authentication, and synchronization across devices. CloudFront provides distributed denial of service protection and field-level encryption and integrates with AWS Shield to mitigate network attacks. This Guidance also uses DynamoDB, which provides encryption at rest and in transit and fine-grained access controls, and it integrates with AWS Identity and Access Management (IAM) to secure the web application’s data. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses managed AWS services that automatically scale to match changes in demand. API Gateway accepts and processes up to hundreds of thousands of concurrent API calls. It handles automatic scaling, throttling, and monitoring to help you build a resilient and observable architecture that recovers rapidly from failures. Application Load Balancer distributes loads to healthy Amazon ECS services, balances traffic across multiple AZs, and performs health checks on targets, helping you improve workload availability, handle spikes in traffic, and react to failures quickly. Application Load Balancer also integrates with the automatic scaling of Fargate, which is built on a fault-tolerant infrastructure and enhances workload availability and resilience. Additionally, this Guidance uses Route 53, a DNS that routes end users to healthy application endpoints through automatic failover, latency-based routing, and health checks. In a case of failure, it can redirect traffic to an alternate AZ. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses managed services that handle infrastructure management so that you can focus on your application code. These services scale dynamically so that your web application can handle increased traffic without compromising performance or user experience. Amazon ECS uses Fargate, which handles scaling and infrastructure management, increasing resource utilization and availability without any need for you to provision or optimize servers yourself. DynamoDB handles provisioning, replication, scaling, and hardware maintenance automatically. Additionally, CloudFront provides a global CDN that caches content closer to your users, with low latency and high transfer speeds. This reduces data transfer costs, requires no servers to manage, and seamlessly scales to handle traffic spikes without provisioning capacity. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses AWS services to help you optimize resource allocation through scaling. For example, using Fargate, you pay only for the virtual CPU and memory resources consumed by your containers, thus removing the need to provision and manage infrastructure and reducing costs. DynamoDB scales throughput and storage to avoid overprovisioning and has no servers to manage, removing administrative overhead and offering predictable, on-demand capacity pricing with no minimum fees. Additionally, CloudFront integrates with Amazon S3. You can serve static content directly from an S3 bucket without needing to provision a web server, and CloudFront caches content at the edge to minimize data transfer costs, compressing objects to reduce size and automatically scaling to handle traffic spikes. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance runs Amazon ECS on Fargate so you can run containers without managing servers, increasing resource utilization and helping you avoid overprovisioning and waste. DynamoDB, which also helps you avoid overprovisioning, has an energy-efficient infrastructure that uses renewable energy, and its serverless model scales throughput and storage to meet demand. Additionally, DynamoDB has a global footprint, which lets you locate tables close to users to reduce network transit impacts. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
