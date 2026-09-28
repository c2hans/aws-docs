---
source_url: https://docs.aws.amazon.com/solutions/kubernetes-based-game-load-testing-on-aws/index.html
---

---
title: 'Guidance for Kubernetes-Based Game Load Testing on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/kubernetes-based-game-load-testing-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Kubernetes-Based Game Load Testing on AWS

Deploy distributed load testing across integrated environments

## Overview

This Guidance demonstrates how to set up a game load testing solution using AWS services and Locust, an open-source load testing tool. It leverages Amazon Elastic Kubernetes Service (Amazon EKS) with AWS Fargate to create a secure, scalable and cost-effective environment. The Guidance allows load test operators to manage the cluster through their local machine's terminal and interact with Locust's web dashboard through port forwarding.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/kubernetes-based-game-load-testing-on-aws.pdf)

![Architecture diagram](/images/solutions/kubernetes-based-game-load-testing-on-aws/images/kubernetes-based-game-load-testing-on-aws-1.png)

1. **Step 1**: Create an Amazon Elastic Kubernetes Service (Amazon EKS) cluster, which spans multiple public and private subnets.
1. **Step 2**: Create an AWS Fargate profile to define the namespace and private subnets that will run the load-generating Locust pods on Fargate.
1. **Step 3**: NAT gateways on the cluster's public subnets provide the Locust pods with the ability to generate traffic towards the external target.
1. **Step 4**: The load test operator interacts with the Amazon EKS cluster using simple AWS CLI and kubectl commands through the terminal.
1. **Step 5**: Using the provided deployment files, the load test operator can customize and deploy the Locust control and Locust worker pods, containing a particular load testing script in a Fargate-managed node.
1. **Step 6**: A ClusterIP service is created to facilitate communication within the cluster.
1. **Step 7**: Once containers are up and running, the load is generated towards the external target according to the load testing script.
1. **Step 8**: The load test operator initiates port forwarding to the Locust control pod and accesses its web dashboard through a local web browser.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-kubernetes-based-game-load-testing-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon EKS packages, manages, and deploys applications in a lightweight, portable, and efficient manner. Fargate automatically provisions, scales, and manages the nodes your containers run on, simplifying infrastructure management. Use Locust to efficiently simulate high-concurrency, distributed load on your applications, uncovering potential issues and gaining valuable insights. By harnessing these powerful tools and services, you can create a secure, scalable, and fully-managed load testing environment, allowing you to evaluate your system's performance under realistic conditions and proactively address any bottlenecks, inefficiencies, or service degradation. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Fargate removes the attack surface associated with securing the underlying infrastructure, reducing the risk of vulnerabilities and misconfigurations. Fargate also deploys your workloads in private subnets, isolating them from direct internet access and minimizing the risk of unauthorized access. AWS Identity and Access Management (IAM) secures your workloads by providing fine-grained control over user and resource permissions, so that only authorized entities can access and interact with your AWS resources. By offloading the responsibility of securing the hardware and network environment, you can focus on safeguarding your application and mitigating the risks associated with manual configurations and human errors. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Conduct thorough load testing to simulate varying levels of user traffic and load, revealing whether your application's scaling mechanisms are working as expected and scaling thresholds are properly configured. This process exposes pain points and allows you to implement robust error handling, graceful degradation, circuit breakers, and other fault-tolerance mechanisms, leading to more resilient, self-healing applications that handle downtime better and maintain critical functionality under stress. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Leverage AWS CLI, Terraform, and kubectl to programmatically define, deploy, and scale your infrastructure and applications, enabling faster provisioning, more consistent configurations, and better utilization of resources compared to manual, error-prone processes. By automating these tasks, you can streamline your operations, reduce the risk of human errors, and focus your engineering efforts on more value-adding activities. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Use Fargate to only pay for the compute resources your containers actually consume, avoiding expenses associated with idle, over-provisioned, self-managed resources needed to handle peak loads. The serverless nature of Fargate also removes the costs and operational overhead related to infrastructure management. Locust.io, a free and open-source load testing framework, offers the benefits of a powerful testing tool at no cost. By optimizing your resource utilization and leveraging cost-effective solutions, you can maximize the return on your investment and redirect resources towards more strategic initiatives. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Fargate reduces your infrastructure footprint and environmental impact, as AWS data centers are designed for optimal energy efficiency and powered by renewable energy sources. Additionally, the dynamic scaling capabilities of Fargate also leads to more efficient use of energy and resources. Use Locust, an event-based load testing framework, to simulate large-scale, real-world load conditions without requiring extensive hardware or infrastructure, further contributing to your sustainability efforts. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
