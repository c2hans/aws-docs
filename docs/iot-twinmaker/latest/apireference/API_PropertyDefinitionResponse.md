---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyDefinitionResponse.html
---

# PropertyDefinitionResponse
<a name="API_PropertyDefinitionResponse"></a>

An object that contains response data from a property definition request.

## Contents
<a name="API_PropertyDefinitionResponse_Contents"></a>

 ** dataType **   <a name="tm-Type-PropertyDefinitionResponse-dataType"></a>
An object that contains information about the data type.
Type: [DataType](API_DataType.md) object
Required: Yes

 ** isExternalId **   <a name="tm-Type-PropertyDefinitionResponse-isExternalId"></a>
A Boolean value that specifies whether the property ID comes from an external data store.
Type: Boolean
Required: Yes

 ** isFinal **   <a name="tm-Type-PropertyDefinitionResponse-isFinal"></a>
A Boolean value that specifies whether the property definition can be updated.
Type: Boolean
Required: Yes

 ** isImported **   <a name="tm-Type-PropertyDefinitionResponse-isImported"></a>
A Boolean value that specifies whether the property definition is imported from an external data store.
Type: Boolean
Required: Yes

 ** isInherited **   <a name="tm-Type-PropertyDefinitionResponse-isInherited"></a>
A Boolean value that specifies whether the property definition is inherited from a parent entity.
Type: Boolean
Required: Yes

 ** isRequiredInEntity **   <a name="tm-Type-PropertyDefinitionResponse-isRequiredInEntity"></a>
A Boolean value that specifies whether the property is required in an entity.
Type: Boolean
Required: Yes

 ** isStoredExternally **   <a name="tm-Type-PropertyDefinitionResponse-isStoredExternally"></a>
A Boolean value that specifies whether the property is stored externally.
Type: Boolean
Required: Yes

 ** isTimeSeries **   <a name="tm-Type-PropertyDefinitionResponse-isTimeSeries"></a>
A Boolean value that specifies whether the property consists of time series data.
Type: Boolean
Required: Yes

 ** configuration **   <a name="tm-Type-PropertyDefinitionResponse-configuration"></a>
A mapping that specifies configuration information about the property.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Value Pattern: `.*`
Required: No

 ** defaultValue **   <a name="tm-Type-PropertyDefinitionResponse-defaultValue"></a>
An object that contains the default value.
Type: [DataValue](API_DataValue.md) object
Required: No

 ** displayName **   <a name="tm-Type-PropertyDefinitionResponse-displayName"></a>
A friendly name for the property.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*[^\u0000-\u001F\u007F]*.*`
Required: No

## See Also
<a name="API_PropertyDefinitionResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/PropertyDefinitionResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/PropertyDefinitionResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/PropertyDefinitionResponse)
