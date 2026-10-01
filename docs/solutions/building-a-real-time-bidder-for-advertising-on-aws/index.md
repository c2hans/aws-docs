---
source_url: https://docs.aws.amazon.com/solutions/building-a-real-time-bidder-for-advertising-on-aws/index.html
---

---
title: 'Guidance for Building a Real Time Bidder for Advertising on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-real-time-bidder-for-advertising-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Building a Real Time Bidder for Advertising on AWS

## Overview

This Guidance shows how to assess ad opportunities at scale using real-time bidding (RTB) technology and NoSQL database tables. With a microservices approach, this offering enables rapid scalability, implements robust security mechanisms to protect data, and uses a deployment pipeline that allows for quick modifications. By capturing and analyzing bidding information in real-time, advertisers have a powerful tool to optimize their advertising strategies and react quickly to market dynamics.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-a-real-time-bidder-for-advertising-on-aws.pdf)

![Architecture diagram](/images/solutions/building-a-real-time-bidder-for-advertising-on-aws/images/building-a-real-time-bidder-for-advertising-on-aws-1.png)

1. **Step 1**: The supply-side platform (SSP) receives an ad request from a publisher, creates a real-time auction, and sends a bid request to a demand-side public endpoint that is configured on Elastic Load Balancing.
1. **Step 2**: The requests are routed to "bidder" pods hosted on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. The bidder uses Amazon Virtual Private Cloud (Amazon VPC) endpoints to access NoSQL database tables that hold information about audiences/segments, campaigns, and budgets. The bidder uses this information to process the bids.
1. **Step 3**: Based on the data from the NoSQL database (such as Aerospike or Amazon DynamoDB), the bidder decides whether to bid or not. If a sent bid wins, the bidder updates the budgets and campaign database tables. NOTE: Aerospike will run within the Amazon VPC and does not require an Amazon VPC endpoint. Configure the rack-aware feature on Aerospike for better performance.
1. **Step 4**: The bidder transactions are sent to Amazon Kinesis Data Streams through Kinesis Data Streams Amazon VPC endpoints in compressed micro batches of 25 KB PUTs. Amazon Data Firehose then sends this data to Amazon Simple Storage Service (Amazon S3) for downstream analytics and reporting. A data stream enables the bidder to respond faster and helps in scaling each component independently.
1. **Step A**: Use AWS Graviton Processor for bidder nodes. For additional cost optimization, implement auto-scaling and Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances.
1. **Step B**: Pre-install bidder container images with dependent libraries and binaries to minimize boot time. Upload the images to a container registry, like Amazon Elastic Container Registry (Amazon ECR).
1. **Step C**: Encrypt and decrypt data at rest and in transit across DynamoDB, Kinesis Data Streams, Amazon EKS, and Amazon S3 using AWS Key Management Service (AWS KMS). Grant least privilege access using AWS Identity and Access Management (IAM) to provide permissions for users, roles, and services.
1. **Step D**: Automate the deployment of the RTB platform using supported git repository, AWS CodeBuild, AWS CodePipeline and AWS CloudFormation to reduce time-consuming, manual processes.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-building-a-real-time-bidder-for-advertising-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance is designed using a stateless, microservices-based architecture where changes can be made independently on each component using a deployment pipeline. It can be used to optimize the cost of high-throughput, low-latency workloads, allowing you to process a greater number of bid requests at a reduced cost. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM policies grant least-privilege access to data so you only have the minimum permissions required for your specific tasks. Additionally, AWS KMS is used to encrypt data at rest and in transit, providing an additional layer of protection against unauthorized access. Lastly, access to the Amazon S3 bucket is secured through bucket policies and by blocking public access and data is routed through Amazon VPC endpoints between services. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

By enabling autoscaling for the Amazon EKS cluster, as well as provisioned throughput for DynamoDB and Amazon Kinesis Streams, the services configured in this Guidance will scale to meet your demand. Consider exploring Kinesis Auto Scaling to scale shards, the individual units of data storage, based on demand. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services selected for this architecture, such as AWS Gravitonprocessors, Amazon EKS, and DynamoDB, are purpose-built for high-throughput, low latency applications such as RTB. These services process millions of transactions per second. AWS Graviton processors provide 40 percent better price performance when compared to X86-based instances, processing more bids or transactions per second. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses AWS Graviton processors, Amazon EC2 Spot Instances, and managed services to optimize costs. Specifically, Amazon EC2 Spot Instances achieve scale and cost savings up to 90 percent compared to On-Demand Instances. Moreover, Amazon EKS and DynamoDB are designed to scale based on demand so you only pay for the resources used. The Amazon EKS cluster is configured with an autoscaler to scale bidder pods and nodes. This Guidance also employs compression and Amazon VPC endpoints to minimize data transfer costs. Lastly, Amazon VPC endpoints are used to route traffic over the AWS backbone network, avoiding data transfer out costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3 lifecycle policies provide effective storage management by defining the appropriate data archival or expiration timelines. Also, by using Amazon EC2 Graviton-based instances, you can optimize performance with a reduced number or smaller instances to host the bidder and Aerospike clusters. These Graviton-based instances demonstrate up to a 60 percent reduction in power consumption compared to similar-sized x86 CPU-based instances for the same workload. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
