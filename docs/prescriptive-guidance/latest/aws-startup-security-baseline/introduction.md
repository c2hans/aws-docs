---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/introduction.html
---

# AWS Startup Security Baseline
<a name="introduction"></a>

*Faisal Farooq, Matthew de Anda, Harsh Chunawala, and Justin Plock, Amazon Web Services*

The AWS Startup Security Baseline (AWS SSB) is a set of controls that establish a **foundational security baseline** for startups building on AWS. It is designed to reduce the most common security risks without adding significant operational overhead. The controls in this guide cover securing credentials, enabling logging and visibility, managing contact information, and implementing basic data boundaries.

The controls in this guide are designed with early-stage startups in mind. Many startups start on AWS with a single AWS account. As startups grow, they migrate to multi-account architectures. This guide is designed for single-account architectures. The controls are structured so they can be adapted as you transition to a multi-account architecture.

The AWS SSB organizes controls into two categories: account and workload. *Account* controls help keep your AWS account secure. They include recommendations for setting up user access, policies, and permissions, and include recommendations for monitoring your account for unauthorized or potentially malicious activity. *Workload* controls help secure your resources and code in the cloud, such as applications, backend processes, and data. They include recommendations such as encryption and reducing the scope of access.

**Note**
** **This guide does not cover all available security controls. It focuses on the foundational controls most relevant to early-stage startups. Some of the controls recommended in this guide replace the defaults configured during initial setup, while most configure new settings and policies.

## Intended audience
<a name="intended-audience"></a>

This guide is designed for startups in the earliest stages of development, typically pre-revenue or early-revenue companies, with minimal staff and operations.

Startups or other businesses that are in later stages of operation and growth can also benefit from reviewing these controls against their current practices. If you identify any gaps, you can implement the individual controls in this guide and evaluate them for appropriateness as a long-term solution.

**Note**
The recommended controls in this guide are foundational in nature. Startups or other companies operating at a later stage of scale or sophistication should implement additional controls beyond this baseline. For more advanced guidance, see the [AWS Security Reference Architecture](https://aws.amazon.com/prescriptive-guidance/security-reference-architecture/) provided by AWS Prescriptive Guidance.

## Foundational framework and security responsibilities
<a name="foundational-framework-and-security-responsibilities"></a>

[AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) provides guidance for building cloud infrastructure that meets security, reliability, performance, and cost requirements. The AWS SSB aligns to the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) of the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html). The *security pillar* provides guidance on protecting data, systems, and assets using AWS services and features.

You can assess your adherence to Well-Architected best practices by using the AWS Well-Architected Tool in your AWS account.

Security and compliance are a shared responsibility between AWS and the customer. Under the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), AWS is responsible for the security *of* the cloud (that is, protecting the infrastructure that runs all AWS Cloud services). You are responsible for the security *in* the cloud, as determined by the AWS services you select. The controls in this guide help you fulfill your responsibilities under the shared responsibility model.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
