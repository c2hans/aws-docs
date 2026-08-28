---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-s3-dataevents-enabled.html
---

# cloudtrail-s3-dataevents-enabled
<a name="cloudtrail-s3-dataevents-enabled"></a>

Checks if at least one AWS CloudTrail trail is logging Amazon Simple Storage Service (Amazon S3) data events for all S3 buckets. The rule is NON\_COMPLIANT if there are trails or if no trails record S3 data events.

**Identifier:** CLOUDTRAIL\_S3\_DATAEVENTS\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

S3BucketNames (Optional)Type: String
Comma-separated list of S3 bucket names for which data events logging should be enabled. Default behavior checks for all S3 buckets.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d343c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
