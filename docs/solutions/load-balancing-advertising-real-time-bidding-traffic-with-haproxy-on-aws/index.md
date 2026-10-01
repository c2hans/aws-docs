---
source_url: https://docs.aws.amazon.com/solutions/load-balancing-advertising-real-time-bidding-traffic-with-haproxy-on-aws/index.html
---

---
title: 'Guidance for Load Balancing Advertising Real-Time Bidding Traffic with HAProxy on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/load-balancing-advertising-real-time-bidding-traffic-with-haproxy-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Load Balancing Advertising Real-Time Bidding Traffic with HAProxy on AWS

## Overview

This Guidance demonstrates how implementing HAProxy Enterprise can help modernize ad-tech infrastructure, delivering substantial business and technical advantages. It shows how to harness advanced load balancing and traffic management capabilities to significantly enhance the performance and reliability of high-frequency ad bidding systems. The Guidance helps ad-tech companies optimize real-time data processing, enabling faster decision-making and improved ad targeting accuracy. By following this Guidance, companies can achieve greater operational efficiency, improved scalability, and a competitive edge in the fast-paced digital advertising landscape.

## Benefits

### Accelerate real-time bidding performance

Process millions of ad requests per second with optimized HAProxy on Graviton instances. Reduce latency through direct pod routing and efficient TLS termination, ensuring sub-500ms response times critical for RTB revenue optimization.

### Scale instantly for traffic spikes

Deploy hardened AMIs with 30-second faster bootstrap times and automatic registration to the HAProxy Fusion Control Plane. Respond dynamically to advertising traffic patterns while maintaining consistent performance during peak demand periods.

### Reduce operational complexity and costs

Centralize configuration management across your HAProxy fleet while leveraging intelligent log sampling and Graviton instances. Cut energy usage by up to 60% compared to standard instances while maintaining the high performance required for ad-tech workloads.

### Ensure high availability for revenue-critical traffic

Eliminate single points of failure with multi-AZ deployments and comprehensive health checks at every layer. Maintain continuous service even during component failures through redundant NLB distribution and automatic instance replacement.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/load-balancing-advertising-real-time-bidding-traffic-with-haproxy-on-aws.pdf)

![Architecture diagram](/images/solutions/load-balancing-advertising-real-time-bidding-traffic-with-haproxy-on-aws/images/load-balancing-advertising-real-time-bidding-traffic-with-haproxy-on-aws-1.png)

1. **Step 1**: Publisher web pages generate ad requests that route through Amazon Route 53 to network load balancers (NLBs) at the supply side platform (SSP). NLBs operate in transmission control protocol (TCP) mode with proxy protocol v2 and, overall, provide consistent connection management and high availability.
1. **Step 2**: HAProxy Enterprise deployed on Amazon Elastic Compute Cloud (Amazon EC2) instances across multiple Availability Zones (AZs) receive ad requests from NLBs, running on AWS Graviton for best cost-performance. They provide advanced routing, preserve client IP information, and perform TLS termination using both Elliptic Curve Cryptography (ECC) and Rivest-Shamir-Adleman (RSA) certificates.
1. **Step 3**: The HAProxy Fusion Control Plane runs on three EC2 instances for high availability, managing service discovery, configuration, and real time monitoring of HAProxy fleet.
1. **Step 4**: SSP auction services run on Amazon Elastic Kubernetes Service (Amazon EKS) pods which filter and enrich ad requests before sending bids to demand partners. Service discovery is configured through the Kubernetes API integration, enabling direct pod routing and health checks for backend auction services with real time service discovery updates.
1. **Step 5**: The monitoring infrastructure logs hundreds of thousands of requests per second for high volume traffic and metrics collection at the control plane, including alerts for key performance indicators as well as integration with operational monitoring tools.
1. **Step 6**: The networking layer leverages public subnets for services requesting bids to demand partners and private subnets for internal services, blending cost efficiency with properly configured security groups and networking features for optimal performance.
1. **Step 7**: HAProxy auto scaling uses either Auto Scaling Groups or Karpenter with hardened Amazon Machine Images (AMIs) and bootstrap processes managed by the control plane for rapid scaling.
1. **Step 8**: Ad responses are routed to publishers through HAProxy and returned to the browser, completing the RTB process in under 500 milliseconds.
[Read usage guidelines](/solutions/guidance-disclaimers/)
