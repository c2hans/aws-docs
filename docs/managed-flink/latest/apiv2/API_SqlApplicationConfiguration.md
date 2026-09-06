---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SqlApplicationConfiguration.html
---

# SqlApplicationConfiguration
<a name="API_SqlApplicationConfiguration"></a>

Describes the inputs, outputs, and reference data sources for a SQL-based Kinesis Data Analytics application.

## Contents
<a name="API_SqlApplicationConfiguration_Contents"></a>

 ** Inputs **   <a name="APIReference-Type-SqlApplicationConfiguration-Inputs"></a>
The array of [Input](API_Input.md) objects describing the input streams used by the application.
Type: Array of [Input](API_Input.md) objects
Required: No

 ** Outputs **   <a name="APIReference-Type-SqlApplicationConfiguration-Outputs"></a>
The array of [Output](API_Output.md) objects describing the destination streams used by the application.
Type: Array of [Output](API_Output.md) objects
Required: No

 ** ReferenceDataSources **   <a name="APIReference-Type-SqlApplicationConfiguration-ReferenceDataSources"></a>
The array of [ReferenceDataSource](API_ReferenceDataSource.md) objects describing the reference data sources used by the application.
Type: Array of [ReferenceDataSource](API_ReferenceDataSource.md) objects
Required: No

## See Also
<a name="API_SqlApplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SqlApplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SqlApplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SqlApplicationConfiguration)
