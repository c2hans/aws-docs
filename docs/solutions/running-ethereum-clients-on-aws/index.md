---
source_url: https://docs.aws.amazon.com/solutions/running-ethereum-clients-on-aws/index.html
---

# Guidance for Running Ethereum Clients on AWS

## Overview

This Guidance helps you set up Ethereum nodes on AWS while optimizing the initial synchronization times. Many customers build applications integrated with the Ethereum blockchain and choose to run their own nodes to achieve more granular operational control and functionality that they can't find with serviced node providers. To help these customers, this Guidance proposes running nodes on AWS to speed up the initial sync process, which is the most time-consuming part of the setup. The reference architecture helps customers address operational problems by showing how to scale nodes and manage updates with minimal downtime.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/running-ethereum-clients-on-aws.pdf)

![Architecture diagram](/images/solutions/running-ethereum-clients-on-aws/images/running-ethereum-clients-on-aws-1.png)

1. **Step 1**: The sync node and Remote Procedure Call protocol (RPC) nodes, powered by Amazon Elastic Compute Cloud (Amazon EC2), synchronize their state with other nodes on the Ethereum blockchain network.
1. **Step 2**: The Amazon EC2 sync node periodically copies node state snapshot data to an Amazon Simple Storage Service (Amazon S3) bucket to provision new Amazon EC2 RPC nodes.
1. **Step 3**: When RPC nodes within an Amazon EC2 Auto Scaling Group start for the first time, they automatically download node state snapshot data from the S3 bucket.
1. **Step 4**: Applications and smart contract development tools access highly available RPC nodes behind an Application Load Balancer from the same virtual private cloud (VPC).
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The deployment is fully automated with infrastructure as code (IaC). IaC allows you to define your entire workload as code, helping you to automate procedures, quickly implement changes, and consistently respond to events. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

You can use security groups on AWS to control traffic to associated resources. The solution uses a default VPC but creates new security groups, limiting Internet access only to the ports required for peer-to-peer communication. These security groups help ensure that only specific instances on AWS can access the JSON RPC ports on Ethereum nodes. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The sync node is periodically stopped to copy data to an S3 bucket. In case the RPC nodes in the EC2 Auto Scaling group fails, it can use the most recent copy of the data to restore the latest state and avoid a long sync time for data recovery. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Because Ethereum nodes run stateful, long-running and monolithic software, EC2 instances are the optimal choice for compute. Amazon Elastic Block Store (Amazon EBS) gp3 volumes use higher than standard IOPS and throughput to provide better response times. An Application Load Balancer ensures requests are spread across a highly available EC2 instances running RPC nodes. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS Compute Optimizer assists in finding the right sizing for the Ethereum Sync and RPC nodes. The RPC nodes are inside an EC2 Auto Scaling group, which scales according to the demand. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Use instances powered by Graviton2 and Graviton3 instance types with lower specifications for sync nodes. You need only one node to stay in sync. The RPC nodes usually require more resources, so using instances powered by Graviton 3 processers are more preferrable. All RPC nodes are also inside an Autoscaling Group, which allows RPC nodes to scale according to the demand. Use Compute Optimizer to verify the initial choice. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Run Ethereum nodes on AWS**: This blog post demonstrates how to set up your own Ethereum nodes on AWS and the ways to speed up the initial sync to quickly bring up new ones when needed.

[Learn more](https://aws.amazon.com/blogs/web3/run-ethereum-nodes-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
