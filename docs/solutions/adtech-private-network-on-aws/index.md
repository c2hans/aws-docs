---
source_url: https://docs.aws.amazon.com/solutions/adtech-private-network-on-aws/index.html
---

---
title: 'Guidance for AdTech Private Network on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/adtech-private-network-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for AdTech Private Network on AWS

## Overview

This Guidance enables supply-side and demand-side platforms to optimize data transfer cost and improve security. When you connect over the AWS PrivateLink service, real-time bidding (RTB) traffic is routed on the AWS backbone network through a private endpoint.

## How it works

This architecture diagram is designed for publishers of ad-supported websites. It enables supply side platforms (SSPs) and demand side platforms (DSPs) to deploy their programmatic bidding application in the same AWS Region to create a private connection using AWS PrivateLink services to route real-time bidding (RTB) traffic in a highly scalable, secure, and cost-optimized design.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/adtech-private-network-on-aws.pdf)

![Architecture diagram](/images/solutions/adtech-private-network-on-aws/images/adtech-private-network-on-aws-1.png)

1. **Step 1**: When a reader accesses a webpage with an ad impression, an ad request is sent to the Publisher Ad Server.
1. **Step 2**: The Publisher Ad Server processes the request and sends it to the endpoint URL provided by the supply-side platform (SSP) to fill the ad impression. The Elastic Load Balancer (ELB) on the SSP's virtual private cloud (VPC) forwards the request to the Auction Server, which sends out a bid request to endpoint web address (URL) of participating demand-side platforms.
1. **Step 3**: The SSP VPC does a DNS lookup with the VPC DNS or the Private Hosted Zone and routes the request either through the interface endpoint or out to the internet.
1. **Step 4**: If the DSP is set up with AWS PrivateLink, the bid request is then routed to the endpoint Elastic Network Interface (ENI) in the SSP's private subnet. The request is then forwarded to the endpoint service on DSP side.
1. **Step 5**: The endpoint service then routes the bid request to associated Network Load Balancer (NLB), which load balances the bid request to the Bidder fleet. The Bidder instance will process the request and return a bid response back to the SSP Auction Server. All the requests and responses are routed through the AWS network.
1. **Step 6**: In order for demand side platforms (DSPs) to use a private hostname for their endpoint URL, the DSP should verify the domain by creating a TXT record on their DNS. This architecture assumes that DSP uses Amazon Route 53 for DNS.
1. **Step 7**: Both the SSP and the DSP can set up Amazon CloudWatch dashboards to gain visibility into active connections and bytes processed per endpoint.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

For optimal operational support, we recommend having a secondary route to the internet in case PrivateLink services fail. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AdTech customers deploy their programmatic workload on a public subnet to reduce data transfer and NAT Gateway costs. This architecture helps customers move to a private subnet and route the traffic over private endpoints. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This architecture is powered by PrivateLink, which is built on top ofAWS Hyperplane, a highly scalable and reliable distributed system used for managing connections that allows PrivateLink to have defined SLAs in place. For more information about PrivateLink and AWS Hyperplane, visit the AWS Blog: Understanding VPC links in Amazon API Gateway private integrations. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The major component in the architecture is PrivateLink, which is a managed service and is available in all AWS regions. PrivateLink is easy to set up and configure, which helps customers to go global in minutes. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Both demand-side (DSP) and supply-side (SSP) customers can save costs by moving to Private Network for AdTech. DSPs will bring their data transfer cost to connected partners to zero and SSP will use PrivateLink tiered pricing. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

PrivateLink is a managed service and AWS managed services shift responsibility for maintaining high average utilization and sustainability optimization of the deployed hardware. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
