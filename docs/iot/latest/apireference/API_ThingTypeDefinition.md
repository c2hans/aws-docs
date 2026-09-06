---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ThingTypeDefinition.html
---

# ThingTypeDefinition
<a name="API_ThingTypeDefinition"></a>

The definition of the thing type, including thing type name and description.

## Contents
<a name="API_ThingTypeDefinition_Contents"></a>

 ** thingTypeArn **   <a name="iot-Type-ThingTypeDefinition-thingTypeArn"></a>
The thing type ARN.
Type: String
Required: No

 ** thingTypeMetadata **   <a name="iot-Type-ThingTypeDefinition-thingTypeMetadata"></a>
The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated.
Type: [ThingTypeMetadata](API_ThingTypeMetadata.md) object
Required: No

 ** thingTypeName **   <a name="iot-Type-ThingTypeDefinition-thingTypeName"></a>
The name of the thing type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** thingTypeProperties **   <a name="iot-Type-ThingTypeDefinition-thingTypeProperties"></a>
The ThingTypeProperties for the thing type.
Type: [ThingTypeProperties](API_ThingTypeProperties.md) object
Required: No

## See Also
<a name="API_ThingTypeDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ThingTypeDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ThingTypeDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ThingTypeDefinition)
