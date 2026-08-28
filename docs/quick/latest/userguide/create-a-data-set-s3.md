---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-set-s3.html
---

# Creating a dataset using Amazon S3 files
<a name="create-a-data-set-s3"></a>

To create a dataset using one or more text files (.csv, .tsv, .clf, or .elf) from Amazon S3, create a manifest for Quick Sight. Quick Sight uses this manifest to identify the files that you want to use and to the upload settings needed to import them. When you create a dataset using Amazon S3, the file data is automatically imported into [SPICE](spice.md).

You must grant Quick Sight access to any Amazon S3 buckets that you want to read files from. For information about granting Quick Sight access to AWS resources, see [Configuring Amazon Quick Sight access to AWS data sources](access-to-aws-resources.md).

**Topics**
+ [Supported formats for Amazon S3 manifest files](supported-manifest-file-format.md)
+ [Creating Amazon S3 datasets](create-a-data-set-s3-procedure.md)
+ [Datasets using S3 files in another AWS account](using-s3-files-in-another-aws-account.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
