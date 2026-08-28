---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-reference-architecture-pci-data-security-standard-dss/introduction.html
---

# AWS Security Reference Architecture - Payment Card Industry (PCI) Data Security Standard (DSS)
<a name="introduction"></a>

*Avik Mukherjee, Amazon Web Services*

This guidance extends the [AWS Security Reference Architecture (AWS SRA) - Core Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html) to help organizations design and operate a multi-account AWS environment that aligns with the [Payment Card Industry Data Security Standard (PCI DSS)](https://www.pcisecuritystandards.org/document_library/). It is an architecture guide that shows how to apply AWS SRA security best practices in a way that satisfies PCI DSS requirements for workloads that store, process, or transmit cardholder data.

This guide is intended for:
+ Security architects designing or extending an AWS multi-account landing zone for workloads under PCI DSS scope
+ Compliance engineers mapping AWS controls to PCI DSS requirements during an assessment
+ Cloud platform teams building shared security services that must accommodate a cardholder data environment (CDE)
+ Qualified Security Assessors (QSAs) and Internal Security Assessors (ISAs) who want to understand how AWS SRA patterns satisfy PCI DSS intent

## PCI DSS Primer
<a name="pci-dss-primer.cdeca00d-efda-5dae-84ef-a5a2692759a4"></a>

The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard maintained by the [PCI Security Standards Council (PCI SSC)](https://www.pcisecuritystandards.org/). It applies to any organization that stores, processes, or transmits payment card data, regardless of size, transaction volume, or geography.

The standard was created jointly by Visa, Mastercard, American Express, Discover, and JCB to establish a consistent baseline of security controls that protect cardholder data throughout its lifecycle. Compliance is enforced contractually by the payment brands through acquiring banks and payment processors.

PCI DSS version 4.0.1 (effective December 31, 2024, with a transition deadline of March 31, 2025 for future-dated requirements) organizes its controls into six goals and twelve principal requirements:

|
|
| Goal | Requirements |
| --- |--- |
| Build and Maintain a Secure Network and Systems | 1. Install and maintain network security controls <br />2. Apply secure configurations to all system components |
| Protect Account Data | 3. Protect stored account data <br />4. Protect cardholder data with strong cryptography during transmission |
| Maintain a Vulnerability Management Program | 5. Protect all systems and networks from malicious software (out-of-scope for this guide)<br />6. Develop and maintain secure systems and software |
| Implement Strong Access Control Measures | 7. Restrict access to system components and cardholder data by business need to know <br />8. Identify users and authenticate access <br />9. Restrict physical access to cardholder data (out-of-scope for this guide) |
| Regularly Monitor and Test Networks | 10. Log and monitor all access to system components and cardholder data <br />11. Test security of systems and networks regularly |
| Maintain an Information Security Policy | 12. Support information security with organizational policies and programs |

In a cloud environment, PCI DSS responsibilities are shared between the cloud service provider (CSP) and the customer. AWS has a Service Provider PCI Report on Compliance (RoC) and operates under a shared responsibility model for PCI DSS. To meet requirement 12.9, both the RoC report and Shared Responsibility Matrix are available to download within AWS Artifacts.

The architectural patterns and controls described in this guidance apply equally to merchants and service providers, including multi-tenant hosting providers subject to PCI DSS Appendix A1. Organizations operating as service providers will find that the multi-account isolation model with dedicated accounts per customer, OU-level SCPs, per-account encryption keys, and centralized per-account logging directly addresses the logical separation and audit log requirements of Appendix A1. AWS provides the building blocks, customers are responsible for assembling them securely. This guide shows you how to do that using AWS SRA patterns.

## AWS SRA Context
<a name="aws-sra-context.f2bf141a-498e-5274-b530-b53d2fec9271"></a>

The AWS SRA is a holistic, prescriptive security architecture guide that describes how AWS security services fit together across a multi-account AWS environment. It is built around a modular, three-tier web architecture (web, application, and data tiers) and is intentionally designed to be adapted — not every workload needs every service, but AWS SRA provides the full range of options and their architectural relationships.

This PCI DSS deep dive does not replace the AWS SRA — it extends it by:
+ Mapping AWS SRA account types to PCI DSS scoping boundaries — showing which accounts are in scope, connected-to, or out-of-scope in a typical payment architecture
+ Layering PCI-specific controls onto the existing AWS SRA service configurations — e.g., additional logging granularity, encryption requirements, or network restrictions that go beyond AWS SRA baseline
+ Identifying where the standard AWS SRA guidance is necessary but not sufficient for PCI DSS, and providing additional prescriptive guidance to help align with PCI DSS requirement.

Key AWS SRA design principles relevant to PCI DSS include:
+ Implement a strong identity foundation ‒ Implement the principle of least privilege, and enforce separation of duties with appropriate authorization for each interaction with your AWS resources. Centralize identity management, and aim to eliminate reliance on long-term static credentials.
+ Enable traceability ‒ Monitor, generate alerts, and audit actions and changes to your environment in real time. Integrate log and metric collection with systems to automatically investigate and take action.
+ Apply security at all layers ‒ Apply a defense-in-depth approach with multiple security controls. Apply multiple types of controls (for example, preventive and detective controls) to all layers, including edge of network, virtual private cloud (VPC), load balancing, instance and compute services, operating system, application configuration, and code.
+ Protect data in transit and at rest ‒ Classify your data into sensitivity levels and use mechanisms such as encryption, tokenization, and access control where appropriate.
+ Keep people away from data ‒ Use mechanisms and tools to reduce or eliminate the need to directly access or manually process data. This reduces the risk of mishandling or modification and human error when handling sensitive data.
+ Prepare for security events ‒ Prepare for an incident by having incident management and investigation policy and processes that align to your organizational requirements. Run incident response simulations and use tools with automation to increase your speed for detection, investigation, and recovery.

### Attachments
<a name="attachments-348f03a4-c34e-48e6-ab09-09381dffd794"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
