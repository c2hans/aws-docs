---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html
---

# Building a Data Perimeter on AWS
<a name="building-a-data-perimeter-on-aws"></a>

Publication date: **June 13, 2023** ([Document history](document-revisions.md))

Many organizations want to implement perimeter controls to help protect against unintended access and configuration errors through always-on permissions guardrails. This paper outlines the best practices and available services for creating a perimeter around your identities, resources, and networks in AWS.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

In traditional, on-premises data center environments, a trusted network and strong authentication are the foundation of security. They establish a high-level perimeter to help prevent untrusted entities from coming in and data from going out. This perimeter provides a clear boundary of trust and ownership. When customers think about creating an AWS perimeter as part of their responsibility for security “in the cloud” in the [AWS Shared Responsibility Model](https://aws.amazon.com/), they want to achieve the same outcomes. They want to draw a circle around their AWS resources, like Amazon Simple Storage Service (Amazon S3) buckets and Amazon Simple Queue Service (Amazon SQS) queues, that clearly separates “my AWS” from other customers.

 The circle that defines an AWS perimeter is typically represented as an AWS organization managed by AWS Organizations. AWS Organizations is an account management service that lets you consolidate multiple AWS accounts into an organization that you create and centrally manage.

 Each AWS account you own is a logical container for AWS identities, resources, and networks. The AWS organization groups of all of those items into a single entity. Along with on-premises networks and systems that access AWS resources, it is what most customers think of as the perimeter of “my AWS”.

 The perimeter defines the things you intend or expect to happen. It refers to the access patterns among your identities, resources, and networks that should be allowed. Using those three elements, we make the following assertion to define our perimeter’s goal: access can only be allowed if the identity is trusted, the resource is trusted, and the network is expected.

 If any of these conditions are false, then the access inside the perimeter is unintended and should be denied. The perimeter is composed of controls implemented on your identities, resources, and networks to ensure the necessary conditions are true.

 This paper discusses the perimeter objectives and how the applied controls prevent unintended access patterns, particularly to data. It is designed to help customers understand how to create a complete AWS data perimeter as part of their responsibility in the AWS Shared Responsibility Model.

![A diagram showing an AWS perimeter.](http://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/images/defining-aws-perimeter.png)
