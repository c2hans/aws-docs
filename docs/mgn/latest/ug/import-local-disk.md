---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/import-local-disk.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Importing your data inventory from a local disk
<a name="import-local-disk"></a>

To import your inventory from a local disk, take the following steps:

1. Select **Import** from the left-hand navigation menu (under **Import and export**) and you’ll be navigated to the **Import inventory** tab.

1. Select **Import from local disk**.

1. Choose **Choose file** to select the CSV file from which you want to import the data.

1. Choose **Import**.

**Note**
The file will also be automatically imported to an S3 bucket created by MGN. It is highly recommended that you [apply Amazon S3 bucket security practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) where your CSV files are stored.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
