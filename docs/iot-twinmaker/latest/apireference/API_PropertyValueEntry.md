---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyValueEntry.html
---

# PropertyValueEntry
<a name="API_PropertyValueEntry"></a>

An object that specifies information about time series property values. This object is used and consumed by the [BatchPutPropertyValues](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_BatchPutPropertyValues.html) action.

## Contents
<a name="API_PropertyValueEntry_Contents"></a>

 ** entityPropertyReference **   <a name="tm-Type-PropertyValueEntry-entityPropertyReference"></a>
An object that contains information about the entity that has the property.
Type: [EntityPropertyReference](API_EntityPropertyReference.md) object
Required: Yes

 ** propertyValues **   <a name="tm-Type-PropertyValueEntry-propertyValues"></a>
A list of objects that specify time series property values.
Type: Array of [PropertyValue](API_PropertyValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_PropertyValueEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/PropertyValueEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/PropertyValueEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/PropertyValueEntry)
