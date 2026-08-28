---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-launchconfig-requires-imdsv2.html
---

# autoscaling-launchconfig-requires-imdsv2
<a name="autoscaling-launchconfig-requires-imdsv2"></a>

Checks whether only IMDSv2 is enabled. This rule is NON\_COMPLIANT if the Metadata version is not included in the launch configuration or if both Metadata V1 and V2 are enabled.

**Identifier:** AUTOSCALING\_LAUNCHCONFIG\_REQUIRES\_IMDSV2

**Resource Types:** AWS::AutoScaling::LaunchConfiguration

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d235c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
