---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_SsmSendCommandConfiguration.html
---

# SsmSendCommandConfiguration
<a name="API_SsmSendCommandConfiguration"></a>

Configuration for an AWS Systems Manager `SendCommand` execution block in a Region switch plan. This execution block runs a Systems Manager document on the managed nodes that you target in each AWS Region of the plan.

## Contents
<a name="API_SsmSendCommandConfiguration_Contents"></a>

 ** regionDocuments **   <a name="regionswitch-Type-SsmSendCommandConfiguration-regionDocuments"></a>
The Systems Manager document and target configuration for each AWS Region in the plan. Provide an entry for each AWS Region that you want the command to run in.
Type: String to [SsmDocumentConfig](API_SsmDocumentConfig.md) object map
Map Entries: Maximum number of 2 items.
Key Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: Yes

 ** retryIntervalMinutes **   <a name="regionswitch-Type-SsmSendCommandConfiguration-retryIntervalMinutes"></a>
How often, in minutes, Region switch retries the command if it returns a failure.
Type: Float
Required: Yes

 ** timeoutMinutes **   <a name="regionswitch-Type-SsmSendCommandConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ungraceful **   <a name="regionswitch-Type-SsmSendCommandConfiguration-ungraceful"></a>
Specifies the settings that determine how the execution block behaves when the plan runs ungracefully, such as whether to skip the command.
Type: [SsmSendCommandUngraceful](API_SsmSendCommandUngraceful.md) object
Required: No

## See Also
<a name="API_SsmSendCommandConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/SsmSendCommandConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/SsmSendCommandConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/SsmSendCommandConfiguration)
