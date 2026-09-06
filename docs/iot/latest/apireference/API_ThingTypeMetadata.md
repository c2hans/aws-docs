---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ThingTypeMetadata.html
---

# ThingTypeMetadata
<a name="API_ThingTypeMetadata"></a>

The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when time was deprecated.

## Contents
<a name="API_ThingTypeMetadata_Contents"></a>

 ** creationDate **   <a name="iot-Type-ThingTypeMetadata-creationDate"></a>
The date and time when the thing type was created.
Type: Timestamp
Required: No

 ** deprecated **   <a name="iot-Type-ThingTypeMetadata-deprecated"></a>
Whether the thing type is deprecated. If **true**, no new things could be associated with this type.
Type: Boolean
Required: No

 ** deprecationDate **   <a name="iot-Type-ThingTypeMetadata-deprecationDate"></a>
The date and time when the thing type was deprecated.
Type: Timestamp
Required: No

## See Also
<a name="API_ThingTypeMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ThingTypeMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ThingTypeMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ThingTypeMetadata)
