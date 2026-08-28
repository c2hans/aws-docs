---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-delete.html
---

# Deleting a table bucket
<a name="s3-tables-buckets-delete"></a>

You can use the Amazon S3 APIs, AWS Command Line Interface, or AWS SDKs to delete a table bucket. Before you delete a table bucket, you must first delete all namespaces and tables within the bucket.

**Important**
 When you delete a table bucket, you need to know the following:
Bucket deletion is permanent and can't be undone.
All data and configurations associated with the bucket are permanently lost.

## Using the AWS CLI
<a name="delete-table-bucket-CLI"></a>

This example shows how to delete a table bucket by using the AWS CLI. To use this example, replace the {{user input placeholders}} with your own information.

```
aws s3tables delete-table-bucket \
    --region {{us-east-2}} \
    --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-bucket1}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
