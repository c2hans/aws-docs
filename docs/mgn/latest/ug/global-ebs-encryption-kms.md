---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/global-ebs-encryption-kms.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Using an AWS KMS customer managed key for encryption in member account
<a name="global-ebs-encryption-kms"></a>

If you decide to use a customer managed key, or if your default Amazon EBS encryption key is a customer managed key in member account, you must add permissions to the AWSApplicationMigrationSharingRole\_<MANAGEMENT\_ACCOUNT\_ID> to allow management account to use it.

Using Administrator access, add these permissions to the AWSApplicationMigrationSharingRole\_<MANAGEMENT\_ACCOUNT\_ID>:

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
