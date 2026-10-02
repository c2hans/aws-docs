---
source_url: https://docs.aws.amazon.com/solutions/aws-rtb-fabric-with-real-time-bidding-workloads-on-aws/index.html
---

---
title: 'Guidance for AWS RTB Fabric with Real-Time Bidding Workloads on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/aws-rtb-fabric-with-real-time-bidding-workloads-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for AWS RTB Fabric with Real-Time Bidding Workloads on AWS

## Overview

This Guidance demonstrates how advertising technology (AdTech) companies can revolutionize their real-time bidding (RTB) operations with AWS RTB Fabric. It shows how supply-side platforms (SSPs), publishers, demand-side platforms (DSPs), and other ad platforms can improve the performance and cost-efficiency of their real-time bidding workloads. AWS RTB Fabric helps AdTech companies connect with their partners over a purpose-built, private network to run real-time bidding workloads with single-digit millisecond latency, optimized data transfer costs, and enhanced infrastructure utilization. This Guidance helps AdTech companies streamline the adoption of a dedicated, high-performance network for managing large-scale daily ad traffic volumes while maintaining seamless integration with third-party services.

## Benefits

### Accelerate bidding decisions

Deploy a fully managed RTB gateway that enables direct, low-latency communication between demand and supply platforms. Reduce bid response times by leveraging AWS's optimized RTB network with load balancing and Availability Zone awareness.

### Maintain data isolation

Implement secure cross-account communication while preserving strict data boundaries between AdTech participants. Each platform maintains control of their own metrics and logs in dedicated Amazon CloudWatch and S3 resources to help uphold compliance with data privacy requirements.

### Customize bidding workflows

Extend RTB capabilities with modular, pluggable components that adapt to specific business requirements. AWS RTB Fabric enables both requesters and responders to implement custom processing modules without compromising the core bidding infrastructure.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/aws-rtb-fabric-with-real-time-bidding-workloads-on-aws.pdf)

![Architecture diagram](/images/solutions/aws-rtb-fabric-with-real-time-bidding-workloads-on-aws/images/aws-rtb-fabric-with-real-time-bidding-workloads-on-aws-1.png)

1. **Step 1**: The Requester's AWS account for a supply-side platform (SSP) produces bid requests through its Real-Time Bidding (RTB) application.
1. **Step 2**: The AWS RTB Fabric Service facilitates communication from requesters to responders providing request/response orchestration.
1. **Step 3**: The AWS account of the demand-side platform (DSP) account receives bid requests from one or more requesters.
1. **Step 4**: The SSP requester application hosted in Amazon Elastic Kubernetes Service (Amazon EKS) initiates a bid request.
1. **Step 5**: The SSP bid request routes through AWS RTB Fabric's cross-account elastic network interface (ENI) to the RTB Flow Orchestrator.
1. **Step 6**: The AWS RTB Fabric service identifies the requester RTB gateway and selects the appropriate link configuration for the target responder.
1. **Step 7**: The AWS RTB Fabric service executes requester modules that customize bid processing through plugins or customer-specific extensions.
1. **Step 8**: The AWS RTB Fabric service then invokes responder-side modules to prepare the request for specific DSP requirements.
1. **Step 9**: The AWS RTB Fabric service locates the responder RTB gateway and identifies its managed Amazon EKS endpoint.
1. **Step 10**: The request is then routed to the managed EKS endpoint, delivering the request directly to the DSP responder pods with load balancing and Availability Zone (AZ) awareness of the originating request.
1. **Step 11**: DSP responder pods process the bid request and return responses or no-bid decisions back through the AWS RTB Fabric service to the requester gateway.
1. **Step 12**: Throughout the RTB flow AWS RTB Fabric participant-specific metrics are delivered to Amazon CloudWatch and debug logs are delivered to Amazon Simple Storage Service (Amazon S3) buckets through CloudWatch vended logs maintaining data isolation.
[Read usage guidelines](/solutions/guidance-disclaimers/)
