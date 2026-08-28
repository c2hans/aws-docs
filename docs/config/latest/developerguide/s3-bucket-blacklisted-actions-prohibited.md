---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-blacklisted-actions-prohibited.html
---

# s3-bucket-blacklisted-actions-prohibited
<a name="s3-bucket-blacklisted-actions-prohibited"></a>

Checks if an Amazon Simple Storage Service (Amazon S3) bucket policy does not allow blocklisted bucket-level and object-level actions on resources in the bucket for principals from other AWS accounts. For example, the rule checks that the Amazon S3 bucket policy does not allow another AWS account to perform any `s3:GetBucket*` actions and `s3:DeleteObject` on any object in the bucket. The rule is NON\_COMPLIANT if any blocklisted actions are allowed by the Amazon S3 bucket policy.

**Note**
The rule will only check for entities in the Principal property and does not take into account any conditionals under the Condition property in a policy

**Identifier:** S3\_BUCKET\_BLACKLISTED\_ACTIONS\_PROHIBITED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

blacklistedActionPatternType: CSV
Comma-separated list of blacklisted action patterns, for example, s3:GetBucket\* and s3:DeleteObject.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1387c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
