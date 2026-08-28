---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-architecture-dod/introduction.html
---

# Secure Cloud Computing Architecture on AWS for the US Department of Defense
<a name="introduction"></a>

*Rob Higareda, Amazon Web Services*

The US Department of Defense (DoD) segments cloud information into impact levels (ILs). The impact level is associated with the sensitivity of the information and the risk of losing the confidentiality, integrity, or availability of that information. IL4 accommodates DoD Controlled Unclassified Information (CUI), and IL5 accommodates DoD CUI and National Security Systems (NSS) information. This guide is designed to help you build a landing zone that supports IL4 and IL5 information.

In order to build an IL4-compliant or IL5-compliant cloud infrastructure, you must build specific components. The Defense Information Systems Agency (DISA) Secure Cloud Computing Architecture (SCCA) is a selection of cloud security and management services. It provides a standardized approach for creating a cloud boundary. The SCCA also includes application-level security components for IL4 and IL5 information hosted in the cloud.

This guide helps you meet SCCA requirements by using the [Landing Zone Accelerator (LZA) on AWS](https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/). The LZA solution deploys a foundational set of capabilities that is designed to align with AWS best practices and multiple global compliance frameworks. The LZA can help you create many of the components necessary to adhere to the DoD SCCA. This guide also recommends how you can add additional components for SCCA compliance and establish a secure foundation for your cloud environments on AWS. Although this guide doesn't include every potential situation, it provides guidance about how to get started and about which AWS services can help you meet SCCA requirements.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for individuals who need to comply with the DoD Secure Cloud Computing Architecture in order to help secure IL4 and IL5 information in the AWS Cloud. If you haven't done so already, review the [DISA Cloud Computing Security Requirements Guide ](https://disa.mil/-/media/files/disa/news/events/symposium/cloud-computing-security-requirements-guide.ashx)before reading this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
