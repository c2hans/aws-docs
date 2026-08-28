---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-listobjectsExamples.html
---

# Listing objects from a directory bucket
<a name="directory-buckets-objects-listobjectsExamples"></a>

 The following code examples show how to list objects in an Amazon S3 directory bucket by using the `ListObjectsV2` API operation.

## Using the AWS CLI
<a name="directory-download-object-cli"></a>

The following `list-objects-v2` example command shows how you can use the AWS CLI to list objects from Amazon S3. This command lists objects from the directory bucket `{{bucket-base-name}}--{{zone-id}}--x-s3`. To run this command, replace the `{{user input placeholders}}` with your own information.

```
aws s3api list-objects-v2 --bucket {{bucket-base-name}}--{{zone-id}}--x-s3
```

For more information, see [list-objects-v2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects-v2.html) in the *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
