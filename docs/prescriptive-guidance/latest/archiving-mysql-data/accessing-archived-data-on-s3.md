---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/accessing-archived-data-on-s3.html
---

# Accessing archived data on Amazon S3
<a name="accessing-archived-data-on-s3"></a>

Amazon S3 provides a number of tools for reading the contents of the data. However, depending on the storage class, a few preprocessing steps might be required. This section includes the following:
+ Reading archived S3 objects with Standard storage class by using AWS Glue
+ Reading an archived S3 object with the S3 Glacier storage classes by using S3 Batch Operations
+ Best practices

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
