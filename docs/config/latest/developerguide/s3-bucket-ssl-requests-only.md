---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-ssl-requests-only.html
---

# s3-bucket-ssl-requests-only
<a name="s3-bucket-ssl-requests-only"></a>

Checks if S3 buckets have policies that require requests to use SSL/TLS. The rule is NON\_COMPLIANT if any S3 bucket has policies allowing HTTP requests.

**Identifier:** S3\_BUCKET\_SSL\_REQUESTS\_ONLY

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1411c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
