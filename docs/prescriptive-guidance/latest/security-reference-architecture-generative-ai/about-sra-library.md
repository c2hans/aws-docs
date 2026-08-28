---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/about-sra-library.html
---

# About the AWS SRA library
<a name="about-sra-library"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This guide is part of a library that provides architectural blueprints and technical guidance for designing and building security architectures on AWS. The library consists of implementation code ([AWS SRA code library](https://github.com/aws-samples/aws-security-reference-architecture-examples)), a validation tool ([SRA Verify](https://github.com/awslabs/sra-verify)), and two complementary categories of guides that cover the core architecture and deep dive architectures.

## AWS SRA – core architecture guide
<a name="9999999999999999aws--sra---core-architecture-guide.8d8c65f7-645a-504d-b231-81f137f611eb"></a>

The [AWS SRA – core architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/) guide represents a foundation for the recommended AWS security architecture. It is the starting point that applies to all organizations, regardless of their industry, application type, or any other considerations. This foundation helps you build a strong and scalable architecture on AWS and helps create a strong AWS multi-account security baseline that scales securely as your business grows.

## AWS SRA – deep dive architectures
<a name="9999999999999999aws--sra---deep-dive-architectures.27adff76-17c8-5846-8aab-9bff4c1187f9"></a>

The *AWS SRA – core architecture* guide is complemented by additional publications that provide architectural patterns aligned to specific security capabilities, application types, and compliance or regulatory requirements. These patterns extend the core architecture and should be used with the *AWS SRA – core architecture* guide.

The following guides provide architectural patterns aligned to specific security capabilities:
+ [AWS SRA – identity management](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/) provides guidance on how to implement a scalable, robust, and centralized identity and access management solution on AWS.
+ [AWS SRA – perimeter security](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-perimeter-security/) discusses architecture patterns and AWS services for implementing edge security in a central account or in individual accounts.
+ [AWS SRA – cyber forensics](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-cyber-forensics/) describes how to configure an AWS Forensics account as a starting point to develop your organization's forensic capabilities and to help improve your security incident response (IR) preparedness.

The following guides provide architectural patterns for specific application types. You might want to focus on these guides after you build your baseline security architecture:
+ *AWS SRA – AI* *security* (this guide) provides security architectural recommendations to protect AI workloads deployed on AWS.
+ [AWS SRA – IoT](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-iot/) provides security architectural recommendations for designing and building IoT applications on AWS.

In addition, the following guide describes architectural patterns that are aligned with specific compliance or regulatory frameworks:
+ [AWS Privacy Reference Architecture (AWS PRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/) provides a security architecture for applications that process personal data and must support broad privacy compliance requirements such as the General Data Protection Regulation (GDPR), the California Consumer Privacy Act (CCPA), or the Brazilian General Data Protection Law (LGPD). The AWS PRA provides a set of guidelines that are specific to the design and configuration of privacy controls in AWS services.

We recommend that you start with the *AWS SRA – core architecture* guide to understand the foundational architecture. Then consult the complementary guides to take advantage of advanced functionality and implementations. For more information about this content set, see [AWS Security Reference Architecture](https://aws.amazon.com/prescriptive-guidance/security-reference-architecture/).

**Note**
To customize the reference architecture diagrams in the AWS SRA library based on your business needs, you can download the following .zip file and extract its contents.

[Download the diagram source file (Microsoft PowerPoint format)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/samples/aws-security-reference-architecture-diagrams.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
