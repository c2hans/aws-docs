---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ReferenceDataSourceDescription.html
---

# ReferenceDataSourceDescription
<a name="API_ReferenceDataSourceDescription"></a>

For a SQL-based Kinesis Data Analytics application, describes the reference data source configured for an application.

## Contents
<a name="API_ReferenceDataSourceDescription_Contents"></a>

 ** ReferenceId **   <a name="APIReference-Type-ReferenceDataSourceDescription-ReferenceId"></a>
The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the [CreateApplication](API_CreateApplication.md) or [UpdateApplication](API_UpdateApplication.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** S3ReferenceDataSourceDescription **   <a name="APIReference-Type-ReferenceDataSourceDescription-S3ReferenceDataSourceDescription"></a>
Provides the Amazon S3 bucket name, the object key name that contains the reference data.
Type: [S3ReferenceDataSourceDescription](API_S3ReferenceDataSourceDescription.md) object
Required: Yes

 ** TableName **   <a name="APIReference-Type-ReferenceDataSourceDescription-TableName"></a>
The in-application table name created by the specific reference data source configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** ReferenceSchema **   <a name="APIReference-Type-ReferenceDataSourceDescription-ReferenceSchema"></a>
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
Type: [SourceSchema](API_SourceSchema.md) object
Required: No

## See Also
<a name="API_ReferenceDataSourceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ReferenceDataSourceDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ReferenceDataSourceDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ReferenceDataSourceDescription)
