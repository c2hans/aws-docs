---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_LambdaEventSourceMappingConfiguration.html
---

# LambdaEventSourceMappingConfiguration
<a name="API_LambdaEventSourceMappingConfiguration"></a>

Configuration for AWS Lambda event source mappings used in a Region switch plan.

## Contents
<a name="API_LambdaEventSourceMappingConfiguration_Contents"></a>

 ** action **   <a name="regionswitch-Type-LambdaEventSourceMappingConfiguration-action"></a>
The action to take - whether to `enable` or `disable` an event source mapping.
Type: String
Valid Values: `enable | disable`
Required: Yes

 ** regionEventSourceMappings **   <a name="regionswitch-Type-LambdaEventSourceMappingConfiguration-regionEventSourceMappings"></a>
Per-region configuration for which Lambda event source mapping to enable or disable when activating or deactivating a region.
Type: String to [EventSourceMapping](API_EventSourceMapping.md) object map
Map Entries: Maximum number of 2 items.
Key Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: Yes

 ** timeoutMinutes **   <a name="regionswitch-Type-LambdaEventSourceMappingConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ungraceful **   <a name="regionswitch-Type-LambdaEventSourceMappingConfiguration-ungraceful"></a>
The settings for ungraceful execution.
Type: [LambdaEventSourceMappingUngraceful](API_LambdaEventSourceMappingUngraceful.md) object
Required: No

## See Also
<a name="API_LambdaEventSourceMappingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/LambdaEventSourceMappingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/LambdaEventSourceMappingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/LambdaEventSourceMappingConfiguration)
