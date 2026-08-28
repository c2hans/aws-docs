---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/introduction.html
---

# Creating an enterprise encryption strategy for data at rest
<a name="introduction"></a>

*Venki Srivatsav, Vikramaditya Bhatnagar, and Andrea Di Fabio, Amazon Web Services*

Many enterprises are concerned about the cybersecurity threat of a data breach. When a data breach occurs, an unauthorized person gains access to your network and steals enterprise data. Firewalls and anti-malware services can help protect against this threat. Another protection that you can implement is data encryption. In the About data encryption section of this guide, you can learn more about how data encryption works and the types available.

When you're discussing encryption, generally speaking, there are two types of data. *Data in transit* is data that is actively moving through your network, such as between network resources. *Data at rest* is data that is stationary and dormant, such as data that is in storage. This strategy focuses on data at rest. For more information about encrypting data in transit, see [Protecting data in transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-data-in-transit.html) (AWS Well-Architected Framework).

An *encryption strategy* consists of four parts that you develop in sequential phases. The *encryption* *policy *is determined by senior management and outlines the regulatory, compliance, and business requirements for encryption. The *encryption* *standards* help those who implement the policy to understand it and comply with it. Standards can be technological or procedural. The *framework* is the standard operating procedures, structures, and guardrails that support implementation of the standards. Finally, the *architecture* is the technical implementation of your encryption standards, such as the environment, services, and tools you use. The objective of this document is to help you create an encryption strategy that suits your business, security, and compliance needs. It includes recommendations for how to review and implement security standards for data at rest so that you can meet your compliance and business needs in a holistic manner.

This strategy uses AWS Key Management Service (AWS KMS) to help you create and manage cryptographic keys that help protect your data. AWS KMS integrates with many AWS services to encrypt all your data at rest. Even if you choose a different encryption service, you can still adopt the recommendations and phases in this guide.

## Intended audience
<a name="intended-audience"></a>

The strategy is designed to address the following audiences:
+ Executive officers who formulate policies for their enterprise, such as CEOs, chief technology officers (CTOs), chief information officers (CIOs), and chief information security officers (CISOs)
+ Technology officers who are responsible for setting up technical standards, such as technical vice presidents and directors
+ Compliance and governance officers who are in charge of monitoring adherence to compliance policies, including statutory and voluntary compliance regimes

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>
+ **Data-at-rest encryption policy** – Decision and policy makers can create an encryption policy and understand the critical factors that affect the policy.
+ **Data-at-rest encryption standards** – Technical leaders can develop encryption standards that are based on the encryption policy.
+ **Framework for encryption** – Technical leaders and implementers can create a framework that acts as a bridge between those who determine the policy and those who create the standards. *Framework*, in this context, means identifying the appropriate process and workflow that helps you implement the standards within the confines of the policy. A framework is similar to a standard operating procedure or a change management process for changing policies or standards.
+ **Technical architecture and implementation** – Hands-on implementers, such as developers and architects, are aware of the available architecture references that can help them implement the encryption strategy.

## Limitations
<a name="limitations"></a>

This document is intended to help you formulate a custom encryption strategy that best suits your enterprise's needs. It isn't an encryption strategy itself, and it isn't a compliance checklist. The following topics aren't included in this document:
+ Encrypting data in transit
+ Tokenization
+ Hashing
+ Compliance and data governance
+ Budgeting for your encryption program

For more information about some of these topics, see the [Resources](resources.md) section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
