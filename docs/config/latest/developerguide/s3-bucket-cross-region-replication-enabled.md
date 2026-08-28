---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-cross-region-replication-enabled.html
---

# s3-bucket-cross-region-replication-enabled
<a name="s3-bucket-cross-region-replication-enabled"></a>

Checks if you have enabled S3 Cross-Region Replication for your Amazon S3 buckets. The rule is NON\_COMPLIANT if there are no replication rules enabled for Cross-Region Replication.

**Identifier:** S3\_BUCKET\_CROSS\_REGION\_REPLICATION\_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1389c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
