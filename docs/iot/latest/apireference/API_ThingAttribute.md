---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ThingAttribute.html
---

# ThingAttribute
<a name="API_ThingAttribute"></a>

The properties of the thing, including thing name, thing type name, and a list of thing attributes.

## Contents
<a name="API_ThingAttribute_Contents"></a>

 ** attributes **   <a name="iot-Type-ThingAttribute-attributes"></a>
A list of thing attributes which are name-value pairs.
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_.,@/:#-]+`
Value Length Constraints: Maximum length of 800.
Value Pattern: `[a-zA-Z0-9_.,@/:#=\[\]-]*`
Required: No

 ** thingArn **   <a name="iot-Type-ThingAttribute-thingArn"></a>
The thing ARN.
Type: String
Required: No

 ** thingName **   <a name="iot-Type-ThingAttribute-thingName"></a>
The name of the thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** thingTypeName **   <a name="iot-Type-ThingAttribute-thingTypeName"></a>
The name of the thing type, if the thing has been associated with a type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** version **   <a name="iot-Type-ThingAttribute-version"></a>
The version of the thing record in the registry.
Type: Long
Required: No

## See Also
<a name="API_ThingAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ThingAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ThingAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ThingAttribute)
