---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/s3-access-point-public-access-blocks.html
---

# s3-access-point-public-access-blocks
<a name="s3-access-point-public-access-blocks"></a>

Checks if Amazon S3 access points have block public access settings enabled. The rule is NON\_COMPLIANT if block public access settings are not enabled for S3 access points.

**Identifier:** S3\_ACCESS\_POINT\_PUBLIC\_ACCESS\_BLOCKS

**Resource Types:** AWS::S3::AccessPoint

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

excludedAccessPoints (Optional)Type: CSV
Comma-separated list of names for allowed public Amazon S3 access points.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1379c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
