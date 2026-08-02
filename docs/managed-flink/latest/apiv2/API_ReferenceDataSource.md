---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ReferenceDataSource.html
---

# ReferenceDataSource
<a name="API_ReferenceDataSource"></a>

For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.

## Contents
<a name="API_ReferenceDataSource_Contents"></a>

 ** ReferenceSchema **   <a name="APIReference-Type-ReferenceDataSource-ReferenceSchema"></a>
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
Type: [SourceSchema](API_SourceSchema.md) object
Required: Yes

 ** TableName **   <a name="APIReference-Type-ReferenceDataSource-TableName"></a>
The name of the in-application table to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** S3ReferenceDataSource **   <a name="APIReference-Type-ReferenceDataSource-S3ReferenceDataSource"></a>
Identifies the S3 bucket and object that contains the reference data. A SQL-based Kinesis Data Analytics application loads reference data only once. If the data changes, you call the [UpdateApplication](API_UpdateApplication.md) operation to trigger reloading of data into your application.
Type: [S3ReferenceDataSource](API_S3ReferenceDataSource.md) object
Required: No

## See Also
<a name="API_ReferenceDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ReferenceDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ReferenceDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ReferenceDataSource)
