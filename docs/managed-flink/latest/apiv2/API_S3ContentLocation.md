---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_S3ContentLocation.html
---

# S3ContentLocation
<a name="API_S3ContentLocation"></a>

For a Managed Service for Apache Flink application provides a description of an Amazon S3 object, including the Amazon Resource Name (ARN) of the S3 bucket, the name of the Amazon S3 object that contains the data, and the version number of the Amazon S3 object that contains the data.

## Contents
<a name="API_S3ContentLocation_Contents"></a>

 ** BucketARN **   <a name="APIReference-Type-S3ContentLocation-BucketARN"></a>
The Amazon Resource Name (ARN) for the S3 bucket containing the application code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** FileKey **   <a name="APIReference-Type-S3ContentLocation-FileKey"></a>
The file key for the object containing the application code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ObjectVersion **   <a name="APIReference-Type-S3ContentLocation-ObjectVersion"></a>
The version of the object containing the application code.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3ContentLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/S3ContentLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/S3ContentLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/S3ContentLocation)
