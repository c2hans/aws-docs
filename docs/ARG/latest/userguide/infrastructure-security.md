---
source_url: https://docs.aws.amazon.com/ARG/latest/userguide/infrastructure-security.html
---

# Infrastructure Security in AWS Resource Groups
<a name="infrastructure-security"></a>

There are no additional ways of isolating service or network traffic provided by Resource Groups. If applicable, use AWS-specific isolation. You can use the Resource Groups API and console in a VPC to help maximize privacy and infrastructure security.

As a managed service, AWS Resource Groups is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Resource Groups through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Resource Groups does not support resource-based policies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
