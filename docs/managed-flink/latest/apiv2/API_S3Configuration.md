---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_S3Configuration.html
---

# S3Configuration
<a name="API_S3Configuration"></a>

For a SQL-based Kinesis Data Analytics application, provides a description of an Amazon S3 data source, including the Amazon Resource Name (ARN) of the S3 bucket and the name of the Amazon S3 object that contains the data.

## Contents
<a name="API_S3Configuration_Contents"></a>

 ** BucketARN **   <a name="APIReference-Type-S3Configuration-BucketARN"></a>
The ARN of the S3 bucket that contains the data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** FileKey **   <a name="APIReference-Type-S3Configuration-FileKey"></a>
The name of the object that contains the data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_S3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/S3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/S3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/S3Configuration)
