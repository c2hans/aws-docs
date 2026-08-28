---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/introduction.html
---

# AWS Security Reference Architecture (AWS SRA) – identity management
<a name="introduction"></a>

*Avik Mukherjee, Amazon Web Services*

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This guidance provides architectural patterns for building identity management capability on AWS. This is an extension of the [AWS SRA – Core Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/) guide. It dives deep into AWS identity management services and how they fit into the core security architecture defined by the AWS SRA. Identities include workforce, application, and consumer identities.

To operate securely in the cloud, your starting point is to determine who can access what in your environment. This guide provides recommendations on how you can implement a scalable, robust, and centralized identity and access management solution on AWS. You can design a centralized identity and access management system, a delegated identity and access management system, or a combination of both while ensuring strict adherence to security standards. Achieving these requirements means ensuring that the right identities can access the right resources under the right conditions. These identities could be humans within your organizations (workforce identities), applications or services within and outside AWS (machine identities), or your customers who want to sign into your applications in ways that are comfortable for them (customer identities).

Identity is now considered the primary perimeter for security. This means that getting identity management right can significantly improve your cloud security posture by eliminating unauthorized use of access, preventing accidental or intentional introduction of malicious code to systems, and ensuring secure, efficient, and compliant operations.

AWS provides fault-tolerant and highly available identity services that can help you to adequately meet your identity management requirements. These services include AWS IAM Identity Center, AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) to centrally manage workforce access to multiple AWS accounts and applications, AWS Identity and Access Management (IAM) roles and IAM Roles Anywhere for secure machine-to-machine communications, and Amazon Cognito to implement secure and frictionless customer identity and access management into your web and mobile applications.

The sections in this guide provide detailed information about managing different identity types and recommendations for implementing AWS identity services, to help you scale as your identities scale with your environment.

In this guide:
+ [About the AWS SRA library](about-sra-library.md)
+ [Workforce identity management](workforce-identity-management.md)
+ [Machine-to-machine identity management](m2m-identity-management.md)
+ [Customer identity management](customer-identity-management.md)
+ [Contributors](contributors.md)
+ [Document history](doc-history.md)

## Attachments
<a name="attachments-1bf8562a-50f2-4dfa-9a24-c4edfe7b936c"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
