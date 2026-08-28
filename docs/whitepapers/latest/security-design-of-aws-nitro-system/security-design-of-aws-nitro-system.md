---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/security-design-of-aws-nitro-system.html
---

# The Security Design of the AWS Nitro System
<a name="security-design-of-aws-nitro-system"></a>

Publication date: **February 15, 2024** ([Document revisions](document-revisions.md))

 [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. The [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) is the underlying platform for all modern EC2 instances. This whitepaper provides a detailed description of the security design of the Nitro System to assist you in evaluating EC2 for your sensitive workloads.

## Introduction
<a name="introduction"></a>

 Every day, customers around the world entrust Amazon Web Services (AWS) with their most sensitive applications. At AWS, keeping our customers’ workloads secure and confidential, while helping them meet their security, privacy, and data protection requirements, is our highest priority. We’ve invested in rigorous operational practices and security technologies that meet and exceed even our most demanding customers’ data security needs.

 The development of the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) has been a multi-year journey to reinvent the fundamental virtualization infrastructure of Amazon EC2. Since launching the Amazon EC2 beta in 2006, we continued to refine, optimize, and innovate in all facets of the service to meet the needs of our customers. With the AWS Nitro System, we undertook an effort to dramatically reimagine the architecture of virtualization to deliver the security, isolation, performance, cost, and pace of innovation that our customers require.

 Security has been a fundamental principle of that process from day one, and we continued to invest in the implementation of the design as part of our continuous improvement methodology to keep raising the bar of security and data protection for our customers. The AWS Nitro System is a combination of purpose-built server designs, data processors, system management components, and specialized firmware which provide the underlying platform for all Amazon EC2 instances launched since the beginning of 2018. Together, the limited and discretely designed components of the AWS Nitro System deliver faster innovation, enhanced security, and improved performance for EC2 customers.

 Three key components of the Nitro System achieve these goals:
+  **Purpose-built Nitro Cards** — Hardware devices designed by AWS that provide overall system control and input/output (I/O) virtualization independent of the main system board with its CPUs and memory.
+  **The Nitro Security Chip** — Enables a secure boot process for the overall system based on a hardware root of trust, the ability to offer bare metal instances, as well as defense in depth that offers protection to the server from unauthorized modification of system firmware.
+  **The Nitro Hypervisor** — A deliberately minimized and firmware-like hypervisor designed to provide strong resource isolation, and performance that is nearly indistinguishable from a bare metal server.

**Note**
 These components are complementary but do not need to be used together.

 This paper provides a high-level introduction to virtualization and the fundamental architectural change introduced by the Nitro System. It discusses each of the three key components of the Nitro System, and provides a demonstration of how these components work together by walking through what happens when a new [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) volume is added to a running EC2 instance. The whitepaper discusses how the Nitro System, by design, eliminates the possibility of administrator access to an EC2 server, the overall passive communications design of the Nitro System, and the Nitro System change management process. Finally, the paper surveys important aspects of the EC2 system design that provide mitigations against potential side-channels issues that can arise in compute environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
