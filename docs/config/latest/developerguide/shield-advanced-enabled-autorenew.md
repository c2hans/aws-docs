---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/shield-advanced-enabled-autorenew.html
---

# shield-advanced-enabled-autorenew
<a name="shield-advanced-enabled-autorenew"></a>

Checks if AWS Shield Advanced is enabled in your AWS account and this subscription is set to automatically renew. The rule is COMPLIANT if Shield Advanced is enabled and auto renew is enabled.

**Note**
The API endpoint of AWS Shield Advanced is only available in US East (N. Virginia) Region. This rule should only be scheduled to run in the US East (N. Virginia) Region.

**Identifier:** SHIELD\_ADVANCED\_ENABLED\_AUTORENEW

**Trigger type:** Periodic

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1529c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
