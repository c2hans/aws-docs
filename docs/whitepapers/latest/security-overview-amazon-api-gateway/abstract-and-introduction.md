---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-api-gateway/abstract-and-introduction.html
---

# Security Overview of Amazon API Gateway
<a name="abstract-and-introduction"></a>

Publication date: **November 12, 2020** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 This whitepaper presents a deep dive into [Amazon API Gateway](https://aws.amazon.com/api-gateway/) and integrated Amazon Web Services (AWS) services through a security lens. It provides a well-rounded picture of the service for new adopters, and a deeper understanding of Amazon API Gateway for current users.

 The intended audience for this whitepaper includes Chief Information Security Officers (CISOs), information security groups, security analysts, enterprise architects, compliance teams, and anyone interested in understanding the security features of API Gateway and its related services.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Today, more business workloads use [Amazon API Gateway](https://aws.amazon.com/api-gateway/) to enable API-driven architectures, improving scalability, performance, and cost efficiency, without managing the underlying infrastructure. These workloads scale to thousands of concurrent requests per second. API Gateway is used by thousands of AWS customers to serve trillions of requests every month.

 The managed environment model of API Gateway intentionally hides many implementation details from the user. This makes some existing best practices for cloud security irrelevant, and creates the need for new best practices. This paper presents a detailed view of these best practices.
