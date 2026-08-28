---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-controls-by-caf-capability/introduction.html
---

# Recommended security controls for implementing AWS CAF security capabilities
<a name="introduction"></a>

*Rishi Singla and Rovan Omar, Amazon Web Services*

Security is the top priority at AWS. To help relieve your operational burden, you [share responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) for cloud security and compliance with AWS. AWS is responsible for security *of* the cloud, which means protecting the infrastructure that runs the services offered in the AWS Cloud. You are responsible for security *in* the cloud, such as your data and applications. This guide provides security controls that can help you meet your security responsibilities in the AWS Cloud.

The [AWS Cloud Adoption Framework (AWS CAF)](https://aws.amazon.com/cloud-adoption-framework/) provides best practices that are designed to improve your cloud readiness. AWS CAF categorizes those best practices into six perspectives: business, people, governance, platform, security, and operations. This guide focuses on the following capabilities in the security perspective:
+ **Identity and access management** – Manage human and machine identities and their permissions at scale.
+ **Threat detection** – Configure logging and monitoring to detect and investigate a potential security misconfiguration, threat, or unexpected behavior.
+ **Protecting infrastructure** – Protect systems and services from unintended or unauthorized access and potential vulnerabilities.
+ **Protecting data** – Categorize data based on levels of sensitivity. Maintain visibility and control over data and how it is accessed and used in your organization.
+ **Incident response** – Establish mechanisms to respond to and mitigate the potential impact of security incidents.

Failure to implement preventative, detective, and responsive security controls for these AWS CAF security capabilities can pose a critical risk to your cloud environment, and it can disrupt your business. Implementing the security controls in this guide can help your organization protect its cloud environment.

**Note**
AWS provides services, tools, and frameworks that can help you operate securely in the AWS Cloud. This guide aligns with and supplements the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/),  [AWS Cloud Adoption Framework (AWS CAF)](https://aws.amazon.com/cloud-adoption-framework/),  the [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/), and other security recommendations published by AWS. The controls in this guide aren't comprehensive of all cloud security considerations, and this guide isn't intended to replace these frameworks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
