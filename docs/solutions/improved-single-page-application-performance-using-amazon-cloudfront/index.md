---
source_url: https://docs.aws.amazon.com/solutions/improved-single-page-application-performance-using-amazon-cloudfront/index.html
---

---
title: 'Guidance for Improved Single-Page Application Performance Using Amazon CloudFront'
canonical_url: https://docs.aws.amazon.com/solutions/improved-single-page-application-performance-using-amazon-cloudfront/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Improved Single-Page Application Performance Using Amazon CloudFront

## Overview

This Guidance demonstrates how your Amazon CloudFront distribution can be configured to serve content with multiple origins while using the same domain. It details how a CloudFront distribution is used to improve the performance of single-page applications (SPAs) when accessing dynamic content through Amazon API Gateway REST APIs, or any other RESTful backends, while serving static content through Amazon Simple Storage Service (Amazon S3).

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/improved-single-page-application-performance-using-amazon-cloudfront.pdf?target=_blank)

![Architecture diagram](/images/solutions/improved-single-page-application-performance-using-amazon-cloudfront/images/improved-single-page-application-performance-using-amazon-cloudfront-1.png)

1. **Step 1**: The web browser makes a request to Amazon CloudFront for the Single Page Application (SPA).
1. **Step 2**: CloudFront checks the requested URL path, and retrieves the static content for the SPA from an Amazon Simple Storage Service (Amazon S3) bucket as the origin.
1. **Step 3**: A user interaction on the web browser makes another request to CloudFront, requesting data from a REST API.
1. **Step 4**: CloudFront checks the URL path which contains "/apis." CloudFront is configured with a behavior for this path to get data from Amazon API Gateway as the origin. Additionally, caching is disabled for this behavior, so requests on this path are always served from API Gateway. The origin request policy is also set to "AllViewerExceptHostHeader," which is required for the API Gateway origin.
1. **Step 5**: CloudFront gets the data from the backend applications through the API Gateway origin and sends it to the web browser.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudFront offers fast change propagation and invalidations, where changes are propagated to the edge in a matter of a few minutes, and invalidation times are under two minutes. After an API is deployed and in use, API Gateway provides you with a dashboard to visually monitor calls to the services. Your CloudFront distribution can be configured with multiple behaviors which govern how CloudFront will process your request and what features will be applied. This feature allows you to configure multiple origins to serve content while using the same domain. Using API Gateway allows you to monitor requests to the backend applications without additional configuration. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

By leveraging the managed services used throughout this Guidance, you can provide a secure experience for end users, authorize and authenticate requests, and encrypt all data at rest. Specifically, Amazon S3 offers flexible security features to block unauthorized users from accessing your data and encrypts all new data uploads. API Gateway allows you to configure authorization and authentication based on workload requirements. CloudFront can create and configure out-of-the-box AWS WAF protection for your application as a first line of defence against common web threats. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

CloudFront supports multiple origins for backend architecture redundancy. The native origin failover capability for CloudFront automatically serves content from a backup origin when the primary origin is unavailable. The origins setup with origin failover can be any combination of AWS origins, like Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon S3 buckets, media services, or non-AWS origins, like an on-premises HTTP server. Additionally, you can implement advanced origin failover capabilities with CloudFront and Lambda@Edge. It's important to note a few things about API Gateway when configuring the service for this Guidance. One, it sets a limit on a steady-state rate and a burst of request submissions against all APIs in your account. Two, you can configure custom throttling for your APIs. Three, you can use Amazon Route 53 to customize your Domain Name System (DNS). And four, you can run health checks to control DNS failover from an API Gateway API in a primary Region to an API Gateway API in a secondary Region. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

CloudFront pairs with thousands of tier 1, 2, and 3 telecom carriers globally, is well connected with all major access networks for optimal performance, and has hundreds of terabits of deployed capacity. To deliver content to end users with lower latency, CloudFront uses a global network of 450+ Points of Presence and 13 Regional edge caches in 90+ cities across 49 countries. Furthermore, your applications can easily achieve thousands of transactions per second in request performance when uploading and retrieving storage from Amazon S3, with Amazon S3 automatically scaling to high request rates. Finally, API Gateway allows you to configure caching and payload compression to optimize performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Not all origins are alike, and some may involve processes, such as just-in-time packaging, that are more computationally expensive per gigabyte (GB) than fetching content out of storage. With CloudFront, you get Regional edge caches at no additional cost to decrease the operational burden on origins and lower operating costs. With Amazon S3, you get strong read-after-write consistency automatically for all applications, without changes to performance or availability, without sacrificing Regional isolation for applications, and at no additional cost. Amazon S3 simplifies the migration of on-premises analytics workloads by removing the need to make changes to applications; it also reduces costs by removing the need for extra infrastructure to provide strong consistency. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The serverless and managed services used throughout this Guidance scale to meet changes in demand, which allows you to use resources only when required. And because AWS handles the provisioning of the underlying resources, you avoid provisioning unneeded resources and reduce the overall infrastructure footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Improve Single-Page Application (SPA) Performance with a Same Domain policy using Amazon CloudFront**: This post demonstrates how you can use a same domain policy withAmazon CloudFront.

[Improve Single-Page Application (SPA) Performance with a Same Domain policy using Amazon CloudFront](https://aws.amazon.com/blogs/networking-and-content-delivery/improve-single-page-application-spa-performance-with-a-same-domain-policy-using-amazon-cloudfront/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
