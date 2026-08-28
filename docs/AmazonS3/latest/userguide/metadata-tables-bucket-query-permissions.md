---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-bucket-query-permissions.html
---

# Permissions for querying metadata tables
<a name="metadata-tables-bucket-query-permissions"></a>

Before you can query your S3 Metadata journal and live inventory tables, you must have certain S3 Tables permissions. If your metadata tables have been encrypted with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS), you must also have the `kms:Decrypt` permission to decrypt the table data.

When you create your metadata table configuration, your metadata tables are stored in an AWS managed table bucket. All metadata table configurations in your account and in the same Region are stored in a single AWS managed table bucket named `aws-s3`.

To query metadata tables, you can use the following example policy. To use this policy, replace the `{{user input placeholders}}` with your own information.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"PermissionsToQueryMetadataTables",
         "Effect":"Allow",
         "Action":[
             "s3tables:GetTable",
             "s3tables:GetTableData",
             "s3tables:GetTableMetadataLocation",
             "kms:Decrypt"
         ],
         "Resource":[
            "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/aws-s3",
            "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/aws-s3/table/*",
            "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{01234567-89ab-cdef-0123-456789abcdef}}"
         ]
       }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
