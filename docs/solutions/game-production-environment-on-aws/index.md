---
source_url: https://docs.aws.amazon.com/solutions/game-production-environment-on-aws/index.html
---

---
title: 'Guidance for a Game Production Environment on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/game-production-environment-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for a Game Production Environment on AWS

## Overview

This Guidance helps you set up a complete game production environment for the Unreal Engine that is highly available and delivered with reduced latency to users. It also accelerates compute-heavy tasks by distributing work to other machines on demand through a high-performance virtual workstation and a centralized version control system. The sample code shows you how to set up this game production environment for your team.

## How it works

This architecture diagram shows how game developers can build a cloud-based Unreal Engine 5 (UE5) development environment featuring a virtual workstation and version control with Perforce Helix Core and how they can build acceleration with Incredibuild and Unreal Engine Swarm. The virtual workstation with GPU-accelerated graphics allows developers to work in their environment remotely and securely, while taking advantage of the high speed AWS network to accelerate build and version control sync tasks.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/game-production-environment-on-aws.pdf)

![Architecture diagram](/images/solutions/game-production-environment-on-aws/images/game-production-environment-on-aws-1.png)

1. **Step 1**: NICE DCV remote client connects to the virtual workstation instance hosted on Amazon Elastic Compute Cloud (Amazon EC2) by providing the public IP address of the instance and authentication credentials.
1. **Step 2**: The GPU-based virtual workstation hosts a NICE DCV server, providing end-to-end security between the remote client and the EC2 instance. The virtual workstation can access private resources, such as the Perforce Helix Core version control system through the Amazon Virtual Private Cloud (Amazon VPC).
1. **Step 3**: The NAT gateway allows resources in the private subnet to access resources over the public internet, such as license and update services.
1. **Step 4**: The Unreal Engine Swarm coordinator, which is responsible for distributing build tasks, is a private resource, available only to resources in the Amazon VPC. The Swarm coordinator has its own EC2 instance, isolating it from any downtime in other instances and creating a microservices environment.
1. **Step 5**: Unreal Engine Swarm Agents are responsible for using system resources to complete jobs assigned by the Swarm Coordinator. Instances hosting the agents are placed in an Amazon EC2 Auto Scaling group which allows Swarm Agents to be added or removed as workload demands change.
1. **Step 6**: The version control system (Perforce) is in its own instance, following the microservice pattern. This isolates it from any downtime in other instances and facilitates more complex repository structures if required.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-game-production-environment-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS Cloud Development Kit (AWS CDK) allows for consistent, repeatable deployments of the development environment elements. This removes sources of error during deployment, which improves security and reliability and reduces cost. Amazon CloudWatch provides operational metrics and logging for development environment resources. Automated, consistent, repeatable deployments through AWS CDK logging with CloudWatch allows application components of the development environment to have a single location to log, no matter how many resources have been scaled up. Operational and health metrics also scale and are on by default for all services in this Guidance. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

NICE DCV secures both pixels and end-user inputs using end-to-end AES-256 encryption between the client and server. It also requires authentication from the client before allowing a connection. Since the workstation is in a public subnet, it’s important that communication between the workstation remote service and client is secure and that clients without authentication credentials are unable to access the workstation. Amazon VPC allows separation of concerns. Its “private by default” policy adds security to resources that don’t need to be exposed to the public internet. Most of the resources in the development environment have no need to be exposed to the public internet and are placed in private subnets in the Amazon VPC that can only be accessed by other resources in the Amazon VPC. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon Elastic Block Store (Amazon EBS) decouples storage from the instance. Amazon EC2 allows deployment to multiple isolated Availability Zones within an AWS Region, which maximizes availability of the application and provides robust disaster recovery. Amazon EBS allows Workspace, Perforce, and Unreal Swarm Coordinator instances to fail while preserving data and allowing easy snapshots for backups. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EC2 Auto Scaling allows build resources in the development environment to scale out on demand. Specifically, Unreal Engine Swarm and Incredibuild agents can scale up when there are large build tasks or a large number of build tasks, thereby decreasing build times and increasing iteration times. Amazon EC2 allows you to deploy to AWS Regions or AWS Local Zones that are geographically close to users, helping reduce latency between local clients and remote servers and optimize the virtual workstation experience. NICE DCV provides optimized protocols to minimize the amount of data that needs to be transferred between the client and server, allowing higher frames-per-second rendering and less perceptible latency between inputs and display. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon EC2 allows you to choose a variety of instance types and payment models to optimize costs for their specific workloads. This helps you match workloads with lower cost options. Additionally, on-demand instances minimize the need to pay for servers that aren’t in use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EC2 Auto Scaling and Amazon EC2 instance types help you provision the minimum required resources to match workload needs. Minimizing resources to fit workloads—whether through scaling or choice of instance types—allows you to build efficient services that minimize the environmental impact of your workload. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
