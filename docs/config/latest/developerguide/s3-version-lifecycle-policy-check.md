---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/s3-version-lifecycle-policy-check.html
---

# s3-version-lifecycle-policy-check
<a name="s3-version-lifecycle-policy-check"></a>

Checks if Amazon Simple Storage Service (Amazon S3) version enabled buckets have lifecycle policy configured. The rule is NON\_COMPLIANT if Amazon S3 lifecycle policy is not enabled.

**Identifier:** S3\_VERSION\_LIFECYCLE\_POLICY\_CHECK

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

bucketNames (Optional)Type: CSV
Comma-separated list of Amazon S3 bucket names that have lifecycle policy enabled.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1433c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
