---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_InputSwitchConfiguration.html
---

# InputSwitchConfiguration
<a name="API_InputSwitchConfiguration"></a>

The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive.

## Contents
<a name="API_InputSwitchConfiguration_Contents"></a>

 ** MQCSInputSwitching **   <a name="mediapackage-Type-InputSwitchConfiguration-MQCSInputSwitching"></a>
When true, AWS Elemental MediaPackage performs input switching based on the MQCS. Default is false. This setting is valid only when `InputType` is `CMAF`.
Type: Boolean
Required: No

 ** PreferredInput **   <a name="mediapackage-Type-InputSwitchConfiguration-PreferredInput"></a>
For CMAF inputs, indicates which input MediaPackage should prefer when both inputs have equal MQCS scores. Select `1` to prefer the first ingest endpoint, or `2` to prefer the second ingest endpoint. If you don't specify a preferred input, MediaPackage uses its default switching behavior when MQCS scores are equal.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2.
Required: No

## See Also
<a name="API_InputSwitchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/InputSwitchConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/InputSwitchConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/InputSwitchConfiguration)
