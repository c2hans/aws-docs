---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/s3_example_s3_DeleteBucketReplication_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteBucketReplication` with a CLI
<a name="s3_example_s3_DeleteBucketReplication_section"></a>

The following code examples show how to use `DeleteBucketReplication`.

------
#### [ CLI ]

**AWS CLI**
The following command deletes a replication configuration from a bucket named `amzn-s3-demo-bucket`:

```
aws s3api delete-bucket-replication --bucket {{amzn-s3-demo-bucket}}
```
+  For API details, see [DeleteBucketReplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-replication.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Deletes the replication configuration associated with the bucket named 'amzn-s3-demo-bucket'. Note that this operation requires permission for the s3:DeleteReplicationConfiguration action. You will be prompted for confirmation before the operation proceeds - to suppress confirmation, use the -Force switch.**

```
Remove-S3BucketReplication -BucketName amzn-s3-demo-bucket
```
+  For API details, see [DeleteBucketReplication](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Deletes the replication configuration associated with the bucket named 'amzn-s3-demo-bucket'. Note that this operation requires permission for the s3:DeleteReplicationConfiguration action. You will be prompted for confirmation before the operation proceeds - to suppress confirmation, use the -Force switch.**

```
Remove-S3BucketReplication -BucketName amzn-s3-demo-bucket
```
+  For API details, see [DeleteBucketReplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
