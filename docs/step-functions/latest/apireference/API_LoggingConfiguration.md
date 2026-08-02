---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_LoggingConfiguration.html
---

# LoggingConfiguration
<a name="API_LoggingConfiguration"></a>

The `LoggingConfiguration` data type is used to set CloudWatch Logs options.

## Contents
<a name="API_LoggingConfiguration_Contents"></a>

 ** destinations **   <a name="StepFunctions-Type-LoggingConfiguration-destinations"></a>
An array of objects that describes where your execution history events will be logged. Limited to size 1. Required, if your log level is not set to `OFF`.
Type: Array of [LogDestination](API_LogDestination.md) objects
Required: No

 ** includeExecutionData **   <a name="StepFunctions-Type-LoggingConfiguration-includeExecutionData"></a>
Determines whether execution data is included in your log. When set to `false`, data is excluded.
Type: Boolean
Required: No

 ** level **   <a name="StepFunctions-Type-LoggingConfiguration-level"></a>
Defines which category of execution history events are logged.
Type: String
Valid Values: `ALL | ERROR | FATAL | OFF`
Required: No

## See Also
<a name="API_LoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/LoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/LoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/LoggingConfiguration)
