---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/evidently-project-description.html
---

# evidently-project-description
<a name="evidently-project-description"></a>

Checks if Amazon CloudWatch Evidently projects have a description. The rule is NON\_COMPLIANT if configuration.Description does not exist or is an empty string.

**Identifier:** EVIDENTLY\_PROJECT\_DESCRIPTION

**Resource Types:** AWS::Evidently::Project

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d827c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
