---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/msk-enhanced-monitoring-enabled.html
---

# msk-enhanced-monitoring-enabled
<a name="msk-enhanced-monitoring-enabled"></a>

Checks if enhanced monitoring is enabled for an Amazon MSK cluster set to PER\_TOPIC\_PER\_BROKER or PER\_TOPIC\_PER\_PARTITION. The rule is NON\_COMPLIANT if enhanced monitoring is enabled and set to DEFAULT or PER\_BROKER.

**Identifier:** MSK\_ENHANCED\_MONITORING\_ENABLED

**Resource Types:** AWS::MSK::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1129c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
