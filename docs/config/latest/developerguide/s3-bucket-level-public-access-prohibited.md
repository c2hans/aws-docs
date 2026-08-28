---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-level-public-access-prohibited.html
---

# s3-bucket-level-public-access-prohibited
<a name="s3-bucket-level-public-access-prohibited"></a>

Checks if S3 buckets are publicly accessible. The rule is NON\_COMPLIANT if an S3 bucket is not listed in the `excludedPublicBuckets` parameter and bucket level settings are public.

**Identifier:** S3\_BUCKET\_LEVEL\_PUBLIC\_ACCESS\_PROHIBITED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

excludedPublicBuckets (Optional)Type: CSV
Comma-separated list of known allowed public Amazon S3 bucket names.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1393c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
