---
source_url: https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/advanced-multi-az-resilience-patterns.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Advanced Multi-AZ Resilience Patterns
<a name="advanced-multi-az-resilience-patterns"></a>

Publication date: **July 11, 2023** ([Document revisions](document-revisions.md))

Many customers run their workloads in highly available, multi-Availability Zone (AZ) configurations. These architectures perform well during binary failure events, but often encounter problems with *gray* failures. The manifestations of this type of failure can be subtle, and defy quick and definitive detection. This paper provides guidance on how to instrument workloads to detect impact from gray failures that are isolated to a single Availability Zone, and then take action to mitigate that impact in the Availability Zone.

## Introduction
<a name="introduction"></a>

 The purpose of this document is to help you more effectively implement resilient multi-AZ architectures. One of the best practices for building resilient systems in [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (VPC) networks is to [deploy each workload to multiple Availability Zones](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html).

 An [Availability Zone](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) is one or more discrete data centers with redundant power, networking, and connectivity. Using multiple Availability Zones allows you to operate workloads that are more highly available, fault tolerant, and scalable than would be possible from a single data center.

 Many AWS services, such as [Amazon Elastic Compute Cloud (EC2) Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) or [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS), provide a multi-AZ configuration. These services don't require you to build any additional observability or failover tooling. They make workloads resilient to easily detectable binary failure modes within an [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) that affect a single Availability Zone. This could be complete physical hardware failure, power loss, or a latent software bug affecting a majority of resources.

 But there is another category of failures termed *gray failures*, whose manifestations are subtle and defy quick and definitive detection. This in turn results in longer times to mitigate the impact caused by the failure. This paper focuses on the impacts gray failures can have on multi-AZ architectures, how to detect them, and, finally, how to mitigate them.

****
The guidance provided in this whitepaper is mostly applicable to specific classes of workloads that:
Primarily use zonal AWS services
Need to improve single Region resilience
Are willing to make a significant investment to build the required observability and resilience patterns
In these workloads, you might not be willing to make some, or all, of the tradeoffs presented in [Responding to gray failures](gray-failures.md#responding-to-gray-failures), or not have the option to use multiple Regions. These types of workloads are likely to represent a small subset of your overall portfolio and hence this guidance should be considered at the workload level versus at the platform level.
