---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SqlApplicationConfigurationDescription.html
---

# SqlApplicationConfigurationDescription
<a name="API_SqlApplicationConfigurationDescription"></a>

Describes the inputs, outputs, and reference data sources for a SQL-based Kinesis Data Analytics application.

## Contents
<a name="API_SqlApplicationConfigurationDescription_Contents"></a>

 ** InputDescriptions **   <a name="APIReference-Type-SqlApplicationConfigurationDescription-InputDescriptions"></a>
The array of [InputDescription](API_InputDescription.md) objects describing the input streams used by the application.
Type: Array of [InputDescription](API_InputDescription.md) objects
Required: No

 ** OutputDescriptions **   <a name="APIReference-Type-SqlApplicationConfigurationDescription-OutputDescriptions"></a>
The array of [OutputDescription](API_OutputDescription.md) objects describing the destination streams used by the application.
Type: Array of [OutputDescription](API_OutputDescription.md) objects
Required: No

 ** ReferenceDataSourceDescriptions **   <a name="APIReference-Type-SqlApplicationConfigurationDescription-ReferenceDataSourceDescriptions"></a>
The array of [ReferenceDataSourceDescription](API_ReferenceDataSourceDescription.md) objects describing the reference data sources used by the application.
Type: Array of [ReferenceDataSourceDescription](API_ReferenceDataSourceDescription.md) objects
Required: No

## See Also
<a name="API_SqlApplicationConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SqlApplicationConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SqlApplicationConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SqlApplicationConfigurationDescription)
