---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_S3ContentBaseLocationDescription.html
---

# S3ContentBaseLocationDescription
<a name="API_S3ContentBaseLocationDescription"></a>

The description of the S3 base location that holds the application.

## Contents
<a name="API_S3ContentBaseLocationDescription_Contents"></a>

 ** BucketARN **   <a name="APIReference-Type-S3ContentBaseLocationDescription-BucketARN"></a>
The Amazon Resource Name (ARN) of the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** BasePath **   <a name="APIReference-Type-S3ContentBaseLocationDescription-BasePath"></a>
The base path for the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9/!-_.*'()]+`
Required: No

## See Also
<a name="API_S3ContentBaseLocationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/S3ContentBaseLocationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/S3ContentBaseLocationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/S3ContentBaseLocationDescription)
