---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensDataExport.html
---

# StorageLensDataExport
<a name="API_control_StorageLensDataExport"></a>

A container to specify the properties of your S3 Storage Lens metrics export, including the destination, schema, and format.

## Contents
<a name="API_control_StorageLensDataExport_Contents"></a>

 ** CloudWatchMetrics **   <a name="AmazonS3-Type-control_StorageLensDataExport-CloudWatchMetrics"></a>
A container for enabling Amazon CloudWatch publishing for S3 Storage Lens metrics.
Type: [CloudWatchMetrics](API_control_CloudWatchMetrics.md) data type
Required: No

 ** S3BucketDestination **   <a name="AmazonS3-Type-control_StorageLensDataExport-S3BucketDestination"></a>
A container for the bucket where the S3 Storage Lens metrics export will be located.
This bucket must be located in the same Region as the storage lens configuration.
Type: [S3BucketDestination](API_control_S3BucketDestination.md) data type
Required: No

 ** StorageLensTableDestination **   <a name="AmazonS3-Type-control_StorageLensDataExport-StorageLensTableDestination"></a>
A container for configuring S3 Storage Lens data exports to read-only S3 table buckets.
Type: [StorageLensTableDestination](API_control_StorageLensTableDestination.md) data type
Required: No

## See Also
<a name="API_control_StorageLensDataExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensDataExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensDataExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensDataExport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
