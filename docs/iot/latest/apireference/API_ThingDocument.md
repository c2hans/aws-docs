---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ThingDocument.html
---

# ThingDocument
<a name="API_ThingDocument"></a>

The thing search index document.

## Contents
<a name="API_ThingDocument_Contents"></a>

 ** attributes **   <a name="iot-Type-ThingDocument-attributes"></a>
The attributes.
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_.,@/:#-]+`
Value Length Constraints: Maximum length of 800.
Value Pattern: `[a-zA-Z0-9_.,@/:#=\[\]-]*`
Required: No

 ** connectivity **   <a name="iot-Type-ThingDocument-connectivity"></a>
Indicates whether the thing is connected to the AWS IoT Core service.
Type: [ThingConnectivity](API_ThingConnectivity.md) object
Required: No

 ** deviceDefender **   <a name="iot-Type-ThingDocument-deviceDefender"></a>
Contains Device Defender data.
For more information about Device Defender, see [Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html).
Type: String
Required: No

 ** shadow **   <a name="iot-Type-ThingDocument-shadow"></a>
The unnamed shadow and named shadow.
For more information about shadows, see [AWS IoT Device Shadow service.](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html)
Type: String
Required: No

 ** thingGroupNames **   <a name="iot-Type-ThingDocument-thingGroupNames"></a>
Thing group and billing group names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** thingId **   <a name="iot-Type-ThingDocument-thingId"></a>
The thing ID.
Type: String
Required: No

 ** thingName **   <a name="iot-Type-ThingDocument-thingName"></a>
The thing name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** thingTypeName **   <a name="iot-Type-ThingDocument-thingTypeName"></a>
The thing type name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

## See Also
<a name="API_ThingDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ThingDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ThingDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ThingDocument)
