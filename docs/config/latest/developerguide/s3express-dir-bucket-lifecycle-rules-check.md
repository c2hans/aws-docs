---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/s3express-dir-bucket-lifecycle-rules-check.html
---

# s3express-dir-bucket-lifecycle-rules-check
<a name="s3express-dir-bucket-lifecycle-rules-check"></a>

Checks if lifecycle rules are configured for an Amazon S3 Express directory bucket. The rule is NON\_COMPLIANT if there is no active lifecycle configuration rules or the configuration does not match with the parameter values.

**Identifier:** S3EXPRESS\_DIR\_BUCKET\_LIFECYCLE\_RULES\_CHECK

**Resource Types:** AWS::S3Express::DirectoryBucket

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), US East (Ohio), Europe (Ireland), US East (N. Virginia), Asia Pacific (Tokyo), US West (Oregon) Region

**Parameters:**

targetExpirationDays (Optional)Type: int
Number of days after creation when objects are deleted from Amazon S3 Express directory buckets.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1375c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
