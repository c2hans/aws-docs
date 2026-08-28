---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/transfer-connector-logging-enabled.html
---

# transfer-connector-logging-enabled
<a name="transfer-connector-logging-enabled"></a>

Checks if AWS Transfer Family Connector publishes logs to Amazon CloudWatch. The rule is NON\_COMPLIANT if a Connector does not have a LoggingRole assigned.

**Identifier:** TRANSFER\_CONNECTOR\_LOGGING\_ENABLED

**Resource Types:** AWS::Transfer::Connector

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1581c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
