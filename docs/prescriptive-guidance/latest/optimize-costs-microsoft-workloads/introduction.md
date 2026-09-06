---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/introduction.html
---

# Optimize costs for Microsoft workloads on AWS
<a name="introduction"></a>

*Bill Pfeiffer, Chase Lindeman, and Kevin Sookhan, Amazon Web Services*

## Overview
<a name="introduction-overview"></a>

This guide provides recommendations, best practices, and strategies to help optimize costs for your Microsoft workloads on AWS. The guide also includes foundational AWS knowledge, cost optimization techniques, and reference architectures to help you build and automate cost-effective, high-performing workloads that meet your business objectives. Collectively, this guidance is referred to as *Microsoft on AWS Cost Optimization (MACO)*. MACO guidance was developed by industry experts and is based on real-world scenarios.

This guide covers the following Microsoft workloads:
+ Windows on Amazon Elastic Compute Cloud (Amazon EC2)
+ SQL Server
+ Containers
+ Storage
+ Active Directory
+ .NET

## Audience
<a name="introduction-audience"></a>

This guide is intended for architects, engineers, administrators, directors, CTOs, technical decision makers, and AWS Partners. It's helpful but not necessary to have prior experience with and a basic understanding of AWS billing, Microsoft technologies, and AWS systems administration.

## How to use this guide
<a name="introduction-how-to-use"></a>

You can use this guide to plan and implement your MACO journey to the cloud. We recommend that you read this guide from start to finish to get a comprehensive understanding of the options and approaches for optimizing the costs of your Microsoft workloads on AWS. You can review the following workload sections based on your organization's needs:
+ [Windows on Amazon EC2](windows-ec2.md)
+ [SQL Server](sql-server.md)
+ [Containers](containers-main.md)
+ [Storage](storage-main.md)
+ [Active Directory](active-directory-main.md)
+ [.NET](net-main.md)

**Important**
** **The code samples provided in this guide are for demonstration purposes only. It's a best practice to test all code in a development environment prior to using it in a production environment. Before you implement any code, we recommend that you test your code in small batches and then review the cost changes that result from the code by using [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html). This can help you troubleshoot edge cases and other issues that can become problematic later on.

**Important**
The pricing examples in this guide are based on prices at the time of publication. Prices are subject to change. Additionally, your costs may vary depending on your AWS Region, AWS service quotas, and other factors related to your cloud environment.
