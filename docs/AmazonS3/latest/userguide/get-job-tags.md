---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/get-job-tags.html
---

# Getting the tags of a S3 Batch Operations job
<a name="get-job-tags"></a>

To retrieve the tags of an Amazon S3 Batch Operations job, you can use the `GetJobTagging` API operation. For more information, see the following examples.

## Using the AWS CLI
<a name="batch-ops-example-cli-job-tags-get-job-tagging"></a>

The following example gets the tags of a Batch Operations job using the AWS CLI. To use this example, replace the {{`user input placeholders`}} with your own information.

```
aws \
    s3control get-job-tagging \
    --account-id {{123456789012}} \
    --job-id {{Example-e25a-4ed2-8bee-7f8ed7fc2f1c}} \
    --region {{us-east-1}}
```

## Using the AWS SDK for Java
<a name="batch-ops-examples-java-job-with-tags-get"></a>

To get the tags of an S3 Batch Operations job using the AWS SDK for Java, you can use the S3Control client with the job ID to retrieve all tags associated with the batch operations job and return them as a list.

For examples of how to get job tags with the AWS SDK for Java, see [Get tags from a batch job](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_GetJobTagging_section.html) in the *Amazon S3 API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
