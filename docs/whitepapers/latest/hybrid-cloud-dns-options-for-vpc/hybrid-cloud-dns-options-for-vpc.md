---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/hybrid-cloud-dns-options-for-vpc.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid Cloud DNS Options for Amazon VPC
<a name="hybrid-cloud-dns-options-for-vpc"></a>

Publication date: **December 02, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 The Domain Name System (DNS) is a foundational element of the internet that underpins many services offered by Amazon Web Services (AWS). [Amazon Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html) provides resolution with DNS for public domain names, [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC), and [Amazon Route 53](https://aws.amazon.com/route53/) private hosted zones (PHZs).

 This whitepaper includes solutions and considerations for advanced DNS architectures to help customers who have workloads with unique DNS requirements, or on-premises resources that require DNS resolution between on-premises data centers and [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instances in Amazon VPCs.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Many organizations have both on-premises resources and resources in the cloud. DNS name resolution is essential for on-premises and cloud-based resources. For customers with hybrid workloads, which include both on-premises and cloud-based resources, extra steps are necessary to configure DNS to work seamlessly across both environments.

 AWS services that require name resolution could include [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) (ELB), [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS), [Amazon Redshift](https://aws.amazon.com/redshift/), and Amazon EC2.

 Route 53 Resolver, which is available in all Amazon VPCs, responds to DNS queries for public records, Amazon VPC resources, and Route 53 PHZs.

You can configure Route 53 Resolver to forward queries to customer-managed authoritative DNS servers hosted on-premises, and to respond to DNS queries that your on-premises DNS servers forward to your Amazon VPC.

 This whitepaper illustrates several different architectures that you can implement on AWS using native and custom-built solutions. These architectures meet the need for name resolution of on-premises infrastructure from your Amazon VPC, and address constraints that have only been partially addressed by previously published solutions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
