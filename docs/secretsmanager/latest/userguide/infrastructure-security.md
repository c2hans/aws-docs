---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/infrastructure-security.html
---

# Infrastructure security in AWS Secrets Manager
<a name="infrastructure-security"></a>

As a managed service, AWS Secrets Manager is protected by the AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

Access to Secrets Manager via the network is through [AWS published APIs using TLS](asm_access.md#endpoints). Secrets Manager APIs are callable from any network location. However, Secrets Manager supports [resource-based access policies](auth-and-access_resource-policies.md), which can include restrictions based on the source IP address. You can also use Secrets Manager resource policies to control access to secrets from [specific virtual private cloud (VPC) endpoints](auth-and-access_resource-policies.md#auth-and-access_examples_vpc), or specific VPCs. Effectively, this isolates network access to a given secret from only the specific VPC within the AWS network. For more information, see [Using an AWS Secrets Manager VPC endpoint](vpc-endpoint-overview.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
