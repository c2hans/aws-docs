---
source_url: https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/infrastructure-security.html
---

# Infrastructure Security in Amazon MWAA Serverless
<a name="infrastructure-security"></a>

For information about AWS security services and how AWS protects infrastructure, [see AWS Cloud Security](https://aws.amazon.com/security/). To design your workflows using the best practices for infrastructure security, see [ Infrastructure Protectiony](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html)) in Security Pillar AWS Well‐Architected Framework.

You use AWS published API calls to access Amazon MWAA Serverless through the network. Clients must support
+ Transport Layer Security (TLS) 1.0 or later. We recommend TLS 1.2 or later.
+ Clients must also support cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
