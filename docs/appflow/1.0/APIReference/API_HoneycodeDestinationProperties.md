---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_HoneycodeDestinationProperties.html
---

# HoneycodeDestinationProperties
<a name="API_HoneycodeDestinationProperties"></a>

 The properties that are applied when Amazon Honeycode is used as a destination.

## Contents
<a name="API_HoneycodeDestinationProperties_Contents"></a>

 ** object **   <a name="appflow-Type-HoneycodeDestinationProperties-object"></a>
 The object specified in the Amazon Honeycode flow destination.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** errorHandlingConfig **   <a name="appflow-Type-HoneycodeDestinationProperties-errorHandlingConfig"></a>
 The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.
Type: [ErrorHandlingConfig](API_ErrorHandlingConfig.md) object
Required: No

## See Also
<a name="API_HoneycodeDestinationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/HoneycodeDestinationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/HoneycodeDestinationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/HoneycodeDestinationProperties)
