---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SqlApplicationConfigurationUpdate.html
---

# SqlApplicationConfigurationUpdate
<a name="API_SqlApplicationConfigurationUpdate"></a>

Describes updates to the input streams, destination streams, and reference data sources for a SQL-based Kinesis Data Analytics application.

## Contents
<a name="API_SqlApplicationConfigurationUpdate_Contents"></a>

 ** InputUpdates **   <a name="APIReference-Type-SqlApplicationConfigurationUpdate-InputUpdates"></a>
The array of [InputUpdate](API_InputUpdate.md) objects describing the new input streams used by the application.
Type: Array of [InputUpdate](API_InputUpdate.md) objects
Required: No

 ** OutputUpdates **   <a name="APIReference-Type-SqlApplicationConfigurationUpdate-OutputUpdates"></a>
The array of [OutputUpdate](API_OutputUpdate.md) objects describing the new destination streams used by the application.
Type: Array of [OutputUpdate](API_OutputUpdate.md) objects
Required: No

 ** ReferenceDataSourceUpdates **   <a name="APIReference-Type-SqlApplicationConfigurationUpdate-ReferenceDataSourceUpdates"></a>
The array of [ReferenceDataSourceUpdate](API_ReferenceDataSourceUpdate.md) objects describing the new reference data sources used by the application.
Type: Array of [ReferenceDataSourceUpdate](API_ReferenceDataSourceUpdate.md) objects
Required: No

## See Also
<a name="API_SqlApplicationConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SqlApplicationConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SqlApplicationConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SqlApplicationConfigurationUpdate)
