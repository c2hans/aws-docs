---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_UpdateClippingDataSourceConfiguration.html
---

# UpdateClippingDataSourceConfiguration
<a name="API_UpdateClippingDataSourceConfiguration"></a>

Attaches a game to an event clipping output at the action's scheduled time. This is a type of ScheduleActionOperation, and the output must be an event clipping output.

## Contents
<a name="API_UpdateClippingDataSourceConfiguration_Contents"></a>

 ** dataSourceConfiguration **   <a name="elementalinference-Type-UpdateClippingDataSourceConfiguration-dataSourceConfiguration"></a>
The game that you want to attach to the output.
Type: [DataSourceConfiguration](API_DataSourceConfiguration.md) object
Required: Yes

 ** outputName **   <a name="elementalinference-Type-UpdateClippingDataSourceConfiguration-outputName"></a>
The name of the output that you want to attach the game to.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

## See Also
<a name="API_UpdateClippingDataSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/UpdateClippingDataSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/UpdateClippingDataSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/UpdateClippingDataSourceConfiguration)
