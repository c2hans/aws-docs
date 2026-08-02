---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_S3ApplicationCodeLocationDescription.html
---

# S3ApplicationCodeLocationDescription
<a name="API_S3ApplicationCodeLocationDescription"></a>

Describes the location of an application's code stored in an S3 bucket.

## Contents
<a name="API_S3ApplicationCodeLocationDescription_Contents"></a>

 ** BucketARN **   <a name="APIReference-Type-S3ApplicationCodeLocationDescription-BucketARN"></a>
The Amazon Resource Name (ARN) for the S3 bucket containing the application code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** FileKey **   <a name="APIReference-Type-S3ApplicationCodeLocationDescription-FileKey"></a>
The file key for the object containing the application code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ObjectVersion **   <a name="APIReference-Type-S3ApplicationCodeLocationDescription-ObjectVersion"></a>
The version of the object containing the application code.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3ApplicationCodeLocationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/S3ApplicationCodeLocationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/S3ApplicationCodeLocationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/S3ApplicationCodeLocationDescription)
