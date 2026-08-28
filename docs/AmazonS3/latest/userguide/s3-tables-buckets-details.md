---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-details.html
---

# Viewing details about an Amazon S3 table bucket
<a name="s3-tables-buckets-details"></a>

You can view the general details of an Amazon S3 table bucket, such as bucket owner and type, in the console or programmatically. You can view default encryption settings, and maintenance settings programmatically by using the S3 Tables REST API, AWS CLI or AWS SDKs.

## Viewing table bucket details
<a name="table-bucket-details-view"></a>

### Using the AWS CLI
<a name="table-bucket-details-CLI"></a>

This example shows how to get details about a table bucket by using the AWS CLI. To use this example, replace the {{user input placeholders}} with your own information.

```
aws s3tables get-table-bucket --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/amzn-s3-demo-table-bucket
```

### Using the S3 console
<a name="table-bucket-details-CLI"></a>

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Table buckets**.

1. Select your table bucket.

1. Select the **Properties** tab.

## Viewing table bucket encryption settings
<a name="table-bucket-encryption-view"></a>

For more information about table bucket encryption, see [Using server-side encryption with AWS KMS keys (SSE-KMS) in table buckets](s3-tables-kms-encryption.md).

### Using the AWS CLI
<a name="table-bucket-encryption-view-CLI"></a>

This example shows how to get details about encryption settings for a table bucket by using the AWS CLI. To use this example, replace the {{user input placeholders}} with your own information.

```
aws s3tables get-table-bucket-encryption --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/amzn-s3-demo-table-bucket
```

## Viewing table bucket maintenance configurations
<a name="table-bucket-maintenance-view"></a>

For information about maintenance settings, see [Maintenance for table buckets](s3-table-buckets-maintenance.md)

### Using the AWS CLI
<a name="table-bucket-maintenance-view-CLI"></a>

This example shows how to get details about maintenance configuration settings for a table bucket by using the AWS CLI. To use this example, replace the {{user input placeholders}} with your own information.

```
aws s3tables get-table-bucket-maintenance-configuration --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/amzn-s3-demo-table-bucket
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
