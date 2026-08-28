---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/introduction.html
---

# Implementing security controls on AWS
<a name="introduction"></a>

*Umair Iqbal, San Brar, Gurpreet Kaur Cheema, Wasim Hossain, Joseph Nguyen, and Lucia Vanta, Amazon Web Services*

Security is critical to every company, and it is a key pillar in the AWS Well-Architected Framework. However, many do not know how to work through security considerations and create a holistic automated security testing and remediation strategy for their cloud environments. By using AWS services and tools, such as AWS Config, Amazon GuardDuty, and AWS CloudFormation, you can create a security testing strategy and build it into your AWS Cloud environments.

To help meet your company's security policy and standards, *security controls* are the technical or administrative guardrails that help prevent, detect, or reduce the ability of a threat actor to exploit a security vulnerability. They are designed to protect the confidentiality, integrity, and availability of resources and data. The following are examples of security controls:
+ Implementing multi-factor authentication for users that need to sign in to an application
+ Logging, monitoring, and querying actions for the purposes of performing real-time audits of account activity
+ Making sure that sensitive data is encrypted
+ Making sure logs are stored according to your company's retention policy

There are four types of security controls: preventative, proactive, detective, and responsive. This guide describes each type in more detail and focuses on how to implement and automate these controls in the AWS Cloud. This guide helps you implement security controls that are continuous and proactive.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for architects and security engineers who are responsible for implementing security controls in the AWS Cloud. If your company has not defined a security policy, control objectives, or standards, as described in [Security controls in the governance framework](sec-controls-gov-model.md), we recommend that you complete these governance tasks before proceeding with this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
