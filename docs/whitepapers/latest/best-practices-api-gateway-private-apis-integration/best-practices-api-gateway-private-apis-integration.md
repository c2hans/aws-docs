---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/best-practices-api-gateway-private-apis-integration.html
---

# Best Practices for Designing Amazon API Gateway Private APIs and Private Integration
<a name="best-practices-api-gateway-private-apis-integration"></a>

Publication date: **July 14, 2026** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 For many enterprise customers, [AWS Direct Connect](https://aws.amazon.com/directconnect/) or a virtual private network (VPN) is often used to build a network connection between an on-premises network and an Amazon Web Services (AWS) virtual private cloud (VPC). This can add additional complexity to a network design, and introduces challenges to [Amazon API Gateway](https://aws.amazon.com/api-gateway/) private API and private integration setup. This whitepaper introduces best practices for deploying private APIs and private integrations in API Gateway, and discusses security, usability, and architecture.

 It is aimed at developers who use API Gateway, or are considering using API Gateway in the future.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—see the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 [Amazon API Gateway](https://aws.amazon.com/api-gateway/) is a fully managed service that helps you create, publish, maintain, monitor, and secure APIs at any scale. API Gateway private integration makes it simple to expose your HTTP/HTTPS resources behind an Amazon VPC, for access by clients outside of the VPC. Additionally, private integration can integrate with private APIs, so the APIs can send requests to backend resources through a private link. For REST APIs, VPC links V2 support both [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) (ALB) and [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) (NLB) as integration targets. Private integration forwards external traffic sent to APIs to private resources, without exposing the APIs to the internet.

 Based on security requirements, different security measures can be placed at different security layers. To secure VPC resources such as Elastic Network Interface (ENI), associate resources are associated with a security group. VPC endpoints are associated with both the security group and the resource policy. For NLB, Transport Layer Security (TLS) listeners are used to secure a listener. For ALB, security groups and HTTPS listeners are used.

 Compared to regional and edge-optimized API implementation, private API implementations and private integrations add additional components, such as interface VPC endpoints and load balancers. This can lead to additional complexity in application architectures.

 This whitepaper includes sample architectures to help understand private APIs, along with private integration implementation and best practices. It also covers security and cost optimizations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
