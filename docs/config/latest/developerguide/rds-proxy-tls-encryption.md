---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rds-proxy-tls-encryption.html
---

# rds-proxy-tls-encryption
<a name="rds-proxy-tls-encryption"></a>

Checks if Amazon RDS proxies enforce TLS for all connections. The rule is NON\_COMPLIANT if an Amazon RDS proxy does not have TLS enforced for all connections.

**Identifier:** RDS\_PROXY\_TLS\_ENCRYPTION

**Resource Types:** AWS::RDS::DBProxy

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1277c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
