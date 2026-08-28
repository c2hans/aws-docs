---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/datasync-task-data-verification-enabled.html
---

# datasync-task-data-verification-enabled
<a name="datasync-task-data-verification-enabled"></a>

Checks if AWS DataSync tasks have data verification enabled to perform additional verification at the end of your transfer. The rule is NON\_COMPLIANT if configuration.Options.VerifyMode is 'NONE'.

**Identifier:** DATASYNC\_TASK\_DATA\_VERIFICATION\_ENABLED

**Resource Types:** AWS::DataSync::Task

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d441c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
