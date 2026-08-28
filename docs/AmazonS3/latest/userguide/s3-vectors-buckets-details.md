---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-buckets-details.html
---

# Viewing vector bucket attributes
<a name="s3-vectors-buckets-details"></a>

You can view detailed information about a vector bucket, including its properties, encryption settings and creation details using the Amazon S3 REST API, AWS SDKs, S3 Console, or the AWS Command Line Interface (AWS CLI). For more information about `GetVectorBucket`, see [GetVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucket.html) in the *Amazon S3 API Reference*.

## Using the S3 console
<a name="console-procedure"></a>

1. Sign in to the console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation pane, choose **Vector buckets**.

1. The console displays a list of all your vector buckets. Find a bucket based on the start of the bucket name, enter a vector bucket name or prefix in the search box above the bucket list. Once you locate your vector bucket, you can view detailed information about it, including its encryption settings, tags, and creation details in the **Properties** tab.

## Using the AWS CLI
<a name="cli-procedure"></a>

```
aws s3vectors get-vector-bucket --vector-bucket-name {{"amzn-s3-demo-vector-bucket"}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
