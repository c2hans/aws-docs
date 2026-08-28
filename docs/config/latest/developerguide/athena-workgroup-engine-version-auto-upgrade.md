---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/athena-workgroup-engine-version-auto-upgrade.html
---

# athena-workgroup-engine-version-auto-upgrade
<a name="athena-workgroup-engine-version-auto-upgrade"></a>

Checks if Amazon Athena workgroups using Athena engine are configured to auto upgrade. The rule is NON\_COMPLIANT if configuration.WorkGroupConfiguration.EngineVersion.SelectedEngineVersion is not 'AUTO'.

**Identifier:** ATHENA\_WORKGROUP\_ENGINE\_VERSION\_AUTO\_UPGRADE

**Resource Types:** AWS::Athena::WorkGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d211c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
