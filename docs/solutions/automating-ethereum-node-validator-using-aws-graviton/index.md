---
source_url: https://docs.aws.amazon.com/solutions/automating-ethereum-node-validator-using-aws-graviton/index.html
---

---
title: 'Guidance for Automating Ethereum Node Validator using AWS Graviton'
canonical_url: https://docs.aws.amazon.com/solutions/automating-ethereum-node-validator-using-aws-graviton/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Automating Ethereum Node Validator using AWS Graviton

## Overview

This Guidance helps customers simplify the deployment of an ETH2 validator on Rocket Pool, powered by AWS Graviton-based instances. Rocket Pool is one of many decentralized staking pools that supports the Ethereum beacon chain. Validators who wish to earn rewards for staking may use Rocket Pool to create their own validation nodes. This Guidance uses AWS Cloud Development Kit (AWS CDK) and AWS Graviton-based instances to deploy ETH2 validators on the AWS Cloud with minimal setup time.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automating-ethereum-node-validator-using-aws-graviton.pdf)

![Architecture diagram](/images/solutions/automating-ethereum-node-validator-using-aws-graviton/images/automating-ethereum-node-validator-using-aws-graviton-1.png)

1. **Step 1**: Set up the node package manager (NPM) and AWS Cloud Development Kit (AWS CDK), and then clone the GitHub repo. Connect to Amazon Elastic Compute Cloud (Amazon EC2) using AWS Systems Manager.
1. **Step 2**: Deploy the CDK template, which deploys an Amazon EC2 instance with an Amazon Elastic Block Store (Amazon EBS) volume attached.
1. **Step 3**: Run the "aws ssm start-session command" to use Systems Manager and securely remote into your instance.
1. **Step 4**: Configure and start the Rocket Pool services and Ethereum's Geth/Lighthouse client on the instance.
1. **Step 5**: Set up and configure the included Grafana dashboard running on the Amazon EC2 instance.
1. **Step 6**: A Rocket Pool full node is one that runs both an Execution (ETH1) client and Consensus (ETH2) client in addition to the Rocket Pool stack. This starts up all the containers, including the Prometheus and Grafana containers. Once you have deployed this architecture, continue with the Rocket Pool documentation on funding your wallet on the Prater test network.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

In this architecture, we use infrastructure as code (IaC) to deploy AWS resources in a reliable and repeatable way. AWS CDK is a key aspect of achieving IaC in this Guidance. AWS CDK is an open-source software development framework that enables the creation and deployment of AWS resources using familiar programming languages such as TypeScript, Python, and Java. It allows developers to define cloud infrastructure in code, which can then be versioned, reviewed, and tested like any other software code. Using AWS CDK to deploy AWS resources provides several technical benefits, including repeatability and consistency, higher-level abstraction, code reuse, and support for standard software development practices. These benefits can help improve the reliability and efficiency of the deployment process, reducing the risk of errors and improving the overall quality of the AWS resources. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This architecture uses Systems Manager to access resources instead of using secure shell (SSH) access (which can be a security risk if not properly managed). To minimize the attack surface, no ports are open. Systems Manager enables secure remote management of instances, making it easier to manage instances across multiple accounts and AWS Regions. In addition to Systems Manager, this architecture uses AWS Identity and Access Management (IAM) to manage user access to resources. With Systems Manager and IAM, only authorized users will have access to AWS resources, reducing the risk of unauthorized access and data breaches. Systems Manager and IAM also provide audit trails and monitoring capabilities, enabling you to track user activity and identify any potential security issues. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This is a loosely-coupled microservices architecture, where everything runs as a Docker container. A loosely coupled microservices architecture provides several benefits for building a reliable system, including increased flexibility and agility, better fault isolation, improved resource utilization, and enhanced testing and debugging capabilities. Additionally, using Prometheus and Grafana as a containerized monitoring stack supports log collection and metrics visualization. Prometheus is an open-source monitoring system that collects and stores time-series data from various sources, including applications and systems. Grafana is a visualization tool that provides a powerful and user-friendly dashboard for displaying metrics and logs collected by Prometheus. The combination of Prometheus and Grafana provides a powerful and comprehensive monitoring solution for AWS resources. The ability to collect and store time-series data and visualize it in an application and user-friendly dashboard enables easy monitoring and troubleshooting of this Guidance, improving the reliability and performance of the AWS resources and reducing the risk of downtime or performance issues to adjacent systems. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Scaling, traffic patterns, and data access patterns are important considerations when designing a blockchain node architecture, as they can have a significant impact on the performance and reliability of the node. Scaling is the ability of the blockchain node to handle increasing numbers of transactions and users. With this Guidance, a single AWS CDK command can increase the number of nodes in the network, which helps distribute the load and improve performance. Traffic patterns are types of requests and data that are sent and received by the blockchain node. Data access patterns are how data is accessed and queried from the blockchain database. Understanding traffic patterns and data access patterns can help you optimize the performance of the node, allocate resources appropriately, and improve the user experience. The Prometheus and Grafana containers can help with monitoring and visualizing these metrics. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

We use a c6g.2xlarge AWS Graviton-based instance based on Rocket Pool's current recommendation. This is the optimized instance for this blockchain deployment. After the node validator is deployed, we recommend using AWS Cost Explorer to evaluate the cost of the c6g.2xlarge instance over time and to identify any potential savings opportunities. Additionally, we recommend using Amazon EC2 Reserved Instances (RIs), which can provide a discount of up to 72% compared to on-demand pricing. By continuously evaluating the cost of the selected instance type and identifying opportunities to optimize, you can use the most cost-effective services without compromising on performance or reliability. This is a single node architecture. Blockchain nodes are highly decentralized, meaning you can spin up new nodes with single AWS CDK command. In this architecture, you do not need automatic scaling mechanisms to save on costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

In this Guidance, we prioritize energy efficiency, reduce hardware requirements, and minimize the carbon footprint of running the node. We run the validator node on AWS Graviton-based instances, which use a lower energy footprint and cost less. The validator node in this Guidance uses a lightweight Ethereum client (Geth), which consumes fewer resources than a full node. The validator node stores data on a solid-state drive (SSD) rather than a traditional hard disk drive (HDD), because SSDs are energy-efficient and have a longer lifespan. By adopting a minimalistic architecture, the Ethereum node validator in this Guidance can significantly reduce its energy consumption and carbon footprint, contributing to a more sustainable blockchain network. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Automate Ethereum node validator deployment on Amazon EC2 using AWS CDK**: This post demonstrates how an AWS Cloud Development Kit (AWS CDK) app simplifies the deployment of Rocket Pool on Amazon EC2.

[Automate Ethereum node validator deployment on Amazon EC2 using AWS CDK](https://aws.amazon.com/blogs/database/automate-ethereum-node-validator-deployment-on-amazon-ec2-using-aws-cdk/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
