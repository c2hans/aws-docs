---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ThingTypeProperties.html
---

# ThingTypeProperties
<a name="API_ThingTypeProperties"></a>

The ThingTypeProperties contains information about the thing type including: a thing type description, and a list of searchable thing attribute names.

## Contents
<a name="API_ThingTypeProperties_Contents"></a>

 ** mqtt5Configuration **   <a name="iot-Type-ThingTypeProperties-mqtt5Configuration"></a>
The configuration to add user-defined properties to enrich MQTT 5 messages.
Type: [Mqtt5Configuration](API_Mqtt5Configuration.md) object
Required: No

 ** searchableAttributes **   <a name="iot-Type-ThingTypeProperties-searchableAttributes"></a>
A list of searchable thing attribute names.
Type: Array of strings
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_.,@/:#-]+`
Required: No

 ** thingTypeDescription **   <a name="iot-Type-ThingTypeProperties-thingTypeDescription"></a>
The description of the thing type.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[\p{Graph}\x20]*`
Required: No

## See Also
<a name="API_ThingTypeProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ThingTypeProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ThingTypeProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ThingTypeProperties)
