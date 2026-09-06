---
source_url: https://docs.aws.amazon.com/whitepapers/latest/unpicking-vendor-lock-in/unpicking-vendor-lock-in.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Unpicking Vendor Lock-in
<a name="unpicking-vendor-lock-in"></a>

Publication date: **June 21, 2021** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 Customers should be able to switch their Cloud Services Provider (CSP) if they want to.

This whitepaper looks at what customers should require from CSPs so they have the freedom to choose the innovative services they need, coupled with the ability to turn things off and move, should they decide to do so. It provides a practical approach to defining, understanding, and eliminating sources of vendor lock-in.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected) (sign-in required), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

A CSP, or vendor, should earn customer business by providing the best services and capabilities at the best price. If a CSP makes it difficult to switch away from them (the essential element of vendor lock-in), it suggests that their services are not earning customer trust through the value they bring, and that they are restricting customer choice.

Amazon Web Services (AWS), provides customers with full control, ownership,and portability of their data, and allows customers to quickly move to another CSP should they choose to. AWS never wants to trap customers with *lock-in* tactics such as fixed-price, mandatory long-term contracts, or technical hurdles to changing CSP that amount to vendor lock-in.

AWS wants customers to stay by choice, because AWS offers the broadest choice of the best cloud services. The AWS outlook is that customers are loyal right up until the moment that somebody else offers them a better service. This drives the AWS customer-obsessed approach to innovation, and ensures AWS earns customer trust on a continuous basis.

The commentary in this whitepaper is based on many years of experience in delivering a secure cloud infrastructure to millions of customers worldwide.
