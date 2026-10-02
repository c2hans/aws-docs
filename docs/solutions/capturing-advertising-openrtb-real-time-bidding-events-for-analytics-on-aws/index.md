---
source_url: https://docs.aws.amazon.com/solutions/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws/index.html
---

---
title: 'Guidance for Capturing Advertising OpenRTB (Real-Time Bidding) Events for Analytics on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Capturing Advertising OpenRTB (Real-Time Bidding) Events for Analytics on AWS

## Overview

This Guidance helps ad-tech companies capture Open Real-Time Bidding (OpenRTB) events and establish a foundation for near real-time and batch analytics. During a programmatic advertising transaction, a demand-side platform (DSP) service generates a series of events. Capturing these events helps ad-tech companies keep their budgets updated and understand signals for optimizing the bid response. By tracking events, such as a successful win bid, advertisers can better measure the effectiveness of their campaigns. They can also analyze these events to make informed decisions for future bids. For an overview of RTB and a description of the events that advertisers generate to win a bid request, visit [Guidance for Building a Real Time Bidder for Advertising on AWS](/solutions/building-a-real-time-bidder-for-advertising-on-aws/) .

## How it works

This architecture enables you to capture OpenRTB bid events for both near real-time and batch analytics.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws.pdf?target=_blank)

![Architecture diagram](/images/solutions/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws/images/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws-1.png)

1. **Step 1**: The supply-side platform (SSP) receives an ad request from a publisher and launches an auction.
1. **Step 2**: An OpenRTB bid request is sent to a DSP public endpoint that is configured on an Elastic Load Balancer.
1. **Step 3**: The bidder application service receives the bid request. This service runs on Amazon Elastic Kubernetes Service (Amazon EKS) within an Amazon Virtual Private Cloud (VPC).
1. **Step 4**: The bid request-response event capture service is hosted on a different container pod in the same cluster. To reduce latency of the bid response, combine the publishing of the bid request and response event as a single call per bid asynchronously to the bid request-response event capture service endpoint.
1. **Step 5**: Post bid events capture service is hosted on a separate container pod that exposes the service to SSPs. This service is used to receive post bid events.
1. **Step 6**: Implement the event capture service in Java to take advantage of Amazon Kinesis Producer Library (KPL). KPL simplifies implementation of an asynchronous producer application and reduces costs for sending data to the Amazon Kinesis Data Streams API.
1. **Step 7**: The event messages are routed to Kinesis Data Streams through a dedicated VPC endpoint.
1. **Step 8**: Amazon Kinesis Data Firehose consumes these aggregated records and deaggregates and sends individual events to Amazon Simple Storage Service (Amazon S3) for long-term storage and analytics.
1. **Step 9**: Amazon CloudWatch captures application logs for traceability.
1. **Step 10**: AWS Key Management Service (AWS KMS) stores and manages encryption keys used for securing persisted data in Kinesis Data Streams and Amazon S3.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The bidder application uses a microservices approach, meaning that the bid request-response event capture and post bid events capture services are decoupled from the bidder service. This enables independent release cycles and scaling mechanisms based on the transactions-per-second (TPS) requirements. For example, the post bid event capture TPS is multiple orders of magnitude less than other components and can be configured independently. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Data at rest in the Amazon S3 bucket is encrypted with AWS KMS keys. Data in transit is encrypted and transferred over HTTPS. The Amazon EKS clusters run in a VPC, and the connectivity between Amazon EKS and Kinesis is routed through a secure VPC endpoint. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The bid request-response and post bid event capture services are decoupled from the code bidder application. The bidder application needs to implement throttling, retry, and backpressure accordingly. Additionally, the architecture promotes a stateless implementation using containers. The KPL implements throttling, retry, and asynchronous publish of events. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

All components of this Guidance are co-located in a single Region and Availability Zone, and you can use automated deployments to deploy the architecture into any Region that meets your data residency and latency requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

With serverless services, you pay only for the resources you consume. The Amazon EKS cluster is the only component in this architecture that does not use serverless services. To meet the high TPS workload, we recommend a hybrid consumption model for the Amazon EKS cluster. Amazon Elastic Compute Cloud (Amazon EC2) Spot instances provide up to a 90% discount compared to on-demand instances and can support additional bursts in workloads. Additionally, the services in the bidder application run within an Amazon VPC and are deployed in a single Availability Zone to minimize data transfer costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

With Amazon EKS, you can implement scalability and elasticity. By decoupling components through microservices, you can allocate the right instance type and the right number of instances to dynamic workloads, helping you to not overprovision resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Guidance for Building a Real Time Bidder for Advertising on AWS**: This Guidance helps you assess ad opportunities at scale using real time bidding (RTB). It shows how demand side platforms (DSPs) bid on ad space available from supply side platforms (SSPs).

[Learn more](/solutions/building-a-real-time-bidder-for-advertising-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
