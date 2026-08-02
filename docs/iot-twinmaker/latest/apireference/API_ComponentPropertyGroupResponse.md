---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ComponentPropertyGroupResponse.html
---

# ComponentPropertyGroupResponse
<a name="API_ComponentPropertyGroupResponse"></a>

The component property group response.

## Contents
<a name="API_ComponentPropertyGroupResponse_Contents"></a>

 ** groupType **   <a name="tm-Type-ComponentPropertyGroupResponse-groupType"></a>
The group type.
Type: String
Valid Values: `TABULAR`
Required: Yes

 ** isInherited **   <a name="tm-Type-ComponentPropertyGroupResponse-isInherited"></a>
A Boolean value that specifies whether the property group is inherited from a parent entity
Type: Boolean
Required: Yes

 ** propertyNames **   <a name="tm-Type-ComponentPropertyGroupResponse-propertyNames"></a>
The names of properties
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: Yes

## See Also
<a name="API_ComponentPropertyGroupResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ComponentPropertyGroupResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ComponentPropertyGroupResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ComponentPropertyGroupResponse)
