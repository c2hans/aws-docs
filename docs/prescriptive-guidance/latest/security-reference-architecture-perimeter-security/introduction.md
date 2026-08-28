---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-perimeter-security/introduction.html
---

# AWS Security Reference Architecture (AWS SRA) – perimeter security
<a name="introduction"></a>

*Avik Mukherjee, Amazon Web Services*

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This guidance provides architectural patterns for building a secure perimeter on AWS. This is an extension of the [AWS SRA – Core Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/) guide. It dives deep into AWS perimeter services and how they fit into the core security architecture defined by the AWS SRA.

In the context of this guidance, a *perimeter* is defined as the boundary where your applications connect to the internet. The security of the perimeter includes secure content delivery, application-layer protection, and distributed denial of service (DDoS) mitigation. AWS perimeter services include Amazon CloudFront, AWS WAF, AWS Shield, Amazon Route 53, and AWS Global Accelerator. These services are designed to provide secure, low-latency, high-performance access to AWS resources and content delivery. You can use these perimeter services with other security services such as Amazon GuardDuty and AWS Firewall Manager to help build a secure perimeter for your applications.

Multiple architecture patterns for perimeter security are available to support different organizational needs. This section focuses on two common patterns: deploying perimeter services in a central (Network) account, and deploying some of the perimeter services into individual workload (Application) accounts. The section covers the benefits of both architectures and their key considerations.

In this guide:
+ [About the AWS SRA library](about-sra-library.md)
+ [Deploying perimeter services in a single Network account](perimeter-single-account.md)
+ [Deploying perimeter services in individual Application accounts](perimeter-individual-account.md)
+ [Additional AWS services for perimeter security](perimeter-additional-services.md)
+ [Contributors](contributors.md)
+ [Document history](doc-history.md)

## Attachments
<a name="attachments-36fc75a2-a16a-4cf6-bea6-724dfeddb825"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
