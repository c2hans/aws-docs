---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/import-s3.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Importing your data inventory from an S3 bucket
<a name="import-s3"></a>

To import your inventory from an S3 bucket, take the following steps:

1. Select **Import** from the left-hand navigation menu (under **Import and export**) and you’ll be navigated to the **Import inventory** tab.

1. Select **Import from S3**.

1. Choose **Browse** to choose the Amazon S3 storage source from which you want to import the data.

1. Choose **Import**.

**Note**
It is highly recommended that you [apply Amazon S3 bucket security practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) where your CSV files are stored.

[Learn more about S3 permissions and policies.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
