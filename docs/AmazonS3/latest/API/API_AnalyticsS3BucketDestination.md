---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnalyticsS3BucketDestination.html
---

# AnalyticsS3BucketDestination
<a name="API_AnalyticsS3BucketDestination"></a>

Contains information about where to publish the analytics results.

## Contents
<a name="API_AnalyticsS3BucketDestination_Contents"></a>

 ** Bucket **   <a name="AmazonS3-Type-AnalyticsS3BucketDestination-Bucket"></a>
The Amazon Resource Name (ARN) of the bucket to which data is exported.
Type: String
Required: Yes

 ** Format **   <a name="AmazonS3-Type-AnalyticsS3BucketDestination-Format"></a>
Specifies the file format used when exporting data to Amazon S3.
Type: String
Valid Values: `CSV`
Required: Yes

 ** BucketAccountId **   <a name="AmazonS3-Type-AnalyticsS3BucketDestination-BucketAccountId"></a>
The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not validated before exporting data.
 Although this value is optional, we strongly recommend that you set it to help prevent problems if the destination bucket ownership changes.
Type: String
Required: No

 ** Prefix **   <a name="AmazonS3-Type-AnalyticsS3BucketDestination-Prefix"></a>
The prefix to use when exporting data. The prefix is prepended to all results.
Type: String
Required: No

## See Also
<a name="API_AnalyticsS3BucketDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AnalyticsS3BucketDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AnalyticsS3BucketDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AnalyticsS3BucketDestination)
