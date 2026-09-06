---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_S3ReferenceDataSourceUpdate.html
---

# S3ReferenceDataSourceUpdate
<a name="API_S3ReferenceDataSourceUpdate"></a>

For a SQL-based Kinesis Data Analytics application, describes the Amazon S3 bucket name and object key name for an in-application reference table.

## Contents
<a name="API_S3ReferenceDataSourceUpdate_Contents"></a>

 ** BucketARNUpdate **   <a name="APIReference-Type-S3ReferenceDataSourceUpdate-BucketARNUpdate"></a>
The Amazon Resource Name (ARN) of the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** FileKeyUpdate **   <a name="APIReference-Type-S3ReferenceDataSourceUpdate-FileKeyUpdate"></a>
The object key name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3ReferenceDataSourceUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/S3ReferenceDataSourceUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/S3ReferenceDataSourceUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/S3ReferenceDataSourceUpdate)
