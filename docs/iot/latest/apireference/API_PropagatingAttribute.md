---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_PropagatingAttribute.html
---

# PropagatingAttribute
<a name="API_PropagatingAttribute"></a>

An object that represents the connection attribute, thing attribute, and the user property key.

## Contents
<a name="API_PropagatingAttribute_Contents"></a>

 ** connectionAttribute **   <a name="iot-Type-PropagatingAttribute-connectionAttribute"></a>
The attribute associated with the connection between a device and AWS IoT Core.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9:.]+`
Required: No

 ** thingAttribute **   <a name="iot-Type-PropagatingAttribute-thingAttribute"></a>
The user-defined thing attribute that is propagating for MQTT 5 message enrichment.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_.,@/:#-]+`
Required: No

 ** userPropertyKey **   <a name="iot-Type-PropagatingAttribute-userPropertyKey"></a>
The key of the user property key-value pair.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9:$.]+`
Required: No

## See Also
<a name="API_PropagatingAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/PropagatingAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/PropagatingAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/PropagatingAttribute)
