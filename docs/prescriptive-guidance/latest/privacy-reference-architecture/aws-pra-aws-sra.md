---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/aws-pra-aws-sra.html
---

# Using the AWS PRA and the AWS SRA
<a name="aws-pra-aws-sra"></a>

**Note**
We would love to hear from you. Please provide feedback on the AWS PRA by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cMxJ0MG3jU91Fk2).

The AWS PRA provides patterns that customers have found helpful in planning foundational and application-level privacy controls for their infrastructure and workloads in AWS. The [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html) provides a set of guidelines for building an architecture that implements and supports the right set of security controls across your AWS [landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html) and applications. In order to establish the privacy controls detailed in this guide, the AWS PRA assumes many of the same foundational guidelines and account structure that are described in the AWS SRA. The AWS PRA and AWS SRA detail many of the same key AWS services. This guide includes only brief descriptions of these services. You can learn more about these services and how they're used in a security context in the AWS SRA.

The AWS SRA can help you design, implement, and manage AWS security services so that they align with AWS recommended practices. You can use the AWS SRA as a standalone guide, or you can use the AWS SRA and AWS PRA as companion guides. Many of the security guidelines detailed in the AWS SRA can be followed in tandem with the privacy controls that are detailed in the AWS PRA. Similar to security, there are foundational privacy considerations that can be helpful to make early in your AWS Cloud journey because these decisions can affect the design of the organization's account structure. For example, some questions you might consider include:
+ How does my organization define personal data?
+ Does my organization support applications that process personal data?
+ What about applications that process other types of regulated data?
+ What organization-level controls can I implement to keep my developers and cloud engineers as far away from personal data as possible?
+ How do I segregate personal data from other types of data?
+ What are my organization's cross-border data transfer requirements?

The answers to many of these questions can have implications for the design of your cloud environment, such as your AWS account structure, service control policies, and AWS Identity and Access Management (IAM) roles.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
