---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-generate-presigned-url-Examples.html
---

# Generating presigned URLs to share objects directory bucket
<a name="directory-buckets-objects-generate-presigned-url-Examples"></a>

 The following code examples show how to generate presigned URLs to share objects from an Amazon S3 directory bucket.

## Using the AWS CLI
<a name="directory-download-object-cli"></a>

The following example command shows how you can use the AWS CLI to generate a presigned URL for an object from Amazon S3. This command generates a presigned URL for an object `{{KEY_NAME}}` from the directory bucket `{{bucket-base-name}}--{{zone-id}}--x-s3`. To run this command, replace the `{{user input placeholders}}` with your own information.

```
aws s3 presign s3://{{bucket-base-name}}--{{zone-id}}--x-s3/{{KEY_NAME}} --expires-in 7200
```

For more information, see [presign](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html) in the *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
