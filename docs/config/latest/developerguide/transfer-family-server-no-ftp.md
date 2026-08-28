---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/transfer-family-server-no-ftp.html
---

# transfer-family-server-no-ftp
<a name="transfer-family-server-no-ftp"></a>

Checks if a server created with AWS Transfer Family uses FTP for endpoint connection. The rule is NON\_COMPLIANT if the server protocol for endpoint connection is FTP-enabled.

**Identifier:** TRANSFER\_FAMILY\_SERVER\_NO\_FTP

**Resource Types:** AWS::Transfer::Server

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1585c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
