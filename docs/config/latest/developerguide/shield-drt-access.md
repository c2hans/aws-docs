---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/shield-drt-access.html
---

# shield-drt-access
<a name="shield-drt-access"></a>

Checks if the Shield Response Team (SRT) can access your AWS account. The rule is NON\_COMPLIANT if AWS Shield Advanced is enabled but the role for SRT access is not configured.

**Identifier:** SHIELD\_DRT\_ACCESS

**Trigger type:** Periodic

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1531c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
