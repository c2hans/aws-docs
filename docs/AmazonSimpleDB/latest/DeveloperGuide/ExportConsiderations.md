---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/ExportConsiderations.html
---

# Export Considerations
<a name="ExportConsiderations"></a>

## Exporting to a Different Region
<a name="CrossRegionExport"></a>

 You can export domain data to an Amazon S3 bucket in a different AWS Region. No additional parameters are required beyond specifying the bucket name and ensuring your IAM permissions allow cross-Region access. Standard Amazon S3 data transfer charges apply for cross-Region exports.

## Using Different Encryption Algorithms
<a name="EncryptionOptions"></a>

 You can specify the encryption algorithm for the exported data using the `--s3-sse-algorithm` parameter:

 **Default encryption (AES256/SSE-S3):**

```
aws simpledbv2 start-domain-export \
		    --domain-name 'myDomain' \
		    --s3-bucket 'my-export-bucket' \
		    --s3-bucket-owner '111122223333' \
		    --s3-sse-algorithm AES256
```

 **SSE-KMS with AWS managed key:**

```
aws simpledbv2 start-domain-export \
		    --domain-name 'myDomain' \
		    --s3-bucket 'my-export-bucket' \
		    --s3-bucket-owner '111122223333' \
		    --s3-sse-algorithm 'KMS'
```

 **SSE-KMS with customer managed key:**

```
aws simpledbv2 start-domain-export \
		    --domain-name 'myDomain' \
		    --s3-bucket 'my-export-bucket' \
		    --s3-bucket-owner '111122223333' \
		    --s3-sse-algorithm 'KMS' \
		    --s3-sse-kms-key-id 'arn:aws::kms:us-east-1:111122223333:key/1ff46940-e71b-4cba-85a8-d5cd935e2e53'
```

## Using a Custom Amazon S3 Key Prefix
<a name="CustomS3Prefix"></a>

 By default, exported data is written to the path `AWSSimpleDB/<exportId>/<domainName>/` in your Amazon S3 bucket. You can specify a custom prefix using the `--s3-key-prefix` parameter:

```
aws simpledbv2 start-domain-export \
		    --domain-name 'myDomain' \
		    --s3-bucket 'my-export-bucket' \
		    --s3-bucket-owner '111122223333' \
		    --s3-key-prefix 'exports/simpledb'
```

 With this prefix, data is written to `exports/simpledb/AWSSimpleDB/<exportId>/<domainName>/`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
