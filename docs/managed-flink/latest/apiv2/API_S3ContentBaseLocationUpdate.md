---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_S3ContentBaseLocationUpdate.html
---

# S3ContentBaseLocationUpdate
<a name="API_S3ContentBaseLocationUpdate"></a>

The information required to update the S3 base location that holds the application.

## Contents
<a name="API_S3ContentBaseLocationUpdate_Contents"></a>

 ** BasePathUpdate **   <a name="APIReference-Type-S3ContentBaseLocationUpdate-BasePathUpdate"></a>
The updated S3 bucket path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9/!-_.*'()]+`
Required: No

 ** BucketARNUpdate **   <a name="APIReference-Type-S3ContentBaseLocationUpdate-BucketARNUpdate"></a>
The updated Amazon Resource Name (ARN) of the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

## See Also
<a name="API_S3ContentBaseLocationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/S3ContentBaseLocationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/S3ContentBaseLocationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/S3ContentBaseLocationUpdate)
