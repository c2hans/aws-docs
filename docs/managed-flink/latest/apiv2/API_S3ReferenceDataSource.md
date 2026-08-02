---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_S3ReferenceDataSource.html
---

# S3ReferenceDataSource
<a name="API_S3ReferenceDataSource"></a>

For a SQL-based Kinesis Data Analytics application, identifies the Amazon S3 bucket and object that contains the reference data.

A SQL-based Kinesis Data Analytics application loads reference data only once. If the data changes, you call the [UpdateApplication](API_UpdateApplication.md) operation to trigger reloading of data into your application.

## Contents
<a name="API_S3ReferenceDataSource_Contents"></a>

 ** BucketARN **   <a name="APIReference-Type-S3ReferenceDataSource-BucketARN"></a>
The Amazon Resource Name (ARN) of the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** FileKey **   <a name="APIReference-Type-S3ReferenceDataSource-FileKey"></a>
The object key name containing the reference data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3ReferenceDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/S3ReferenceDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/S3ReferenceDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/S3ReferenceDataSource)
