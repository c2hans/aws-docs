---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-source.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Data sources
<a name="copy-parameters-data-source"></a>

You can load data from text files in an Amazon S3 bucket, in an Amazon EMR cluster, or on a remote host that your cluster can access using an SSH connection. You can also load data directly from a DynamoDB table.

The maximum size of a single input row from any source is 4 MB.

To export data from a table to a set of files in an Amazon S3, use the [UNLOAD](r_UNLOAD.md) command.

**Topics**
+ [COPY from Amazon S3](copy-parameters-data-source-s3.md)
+ [COPY from Amazon EMR](copy-parameters-data-source-emr.md)
+ [COPY from remote host (SSH)](copy-parameters-data-source-ssh.md)
+ [COPY from Amazon DynamoDB](copy-parameters-data-source-dynamodb.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
