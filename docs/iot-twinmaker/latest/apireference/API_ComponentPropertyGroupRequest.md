---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ComponentPropertyGroupRequest.html
---

# ComponentPropertyGroupRequest
<a name="API_ComponentPropertyGroupRequest"></a>

The component property group request.

## Contents
<a name="API_ComponentPropertyGroupRequest_Contents"></a>

 ** groupType **   <a name="tm-Type-ComponentPropertyGroupRequest-groupType"></a>
The group type.
Type: String
Valid Values: `TABULAR`
Required: No

 ** propertyNames **   <a name="tm-Type-ComponentPropertyGroupRequest-propertyNames"></a>
The property names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** updateType **   <a name="tm-Type-ComponentPropertyGroupRequest-updateType"></a>
The update type.
Type: String
Valid Values: `UPDATE | DELETE | CREATE`
Required: No

## See Also
<a name="API_ComponentPropertyGroupRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ComponentPropertyGroupRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ComponentPropertyGroupRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ComponentPropertyGroupRequest)
