---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinitionDetail.html
---

# PolicyDefinitionDetail
<a name="API_PolicyDefinitionDetail"></a>

A structure that describes a policy definition. It must always have either an `static` or a `templateLinked` element.

This data type is used as a response parameter for the [GetPolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicy.html) operation.

## Contents
<a name="API_PolicyDefinitionDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** static **   <a name="verifiedpermissions-Type-PolicyDefinitionDetail-static"></a>
Information about a static policy that wasn't created with a policy template.
Type: [StaticPolicyDefinitionDetail](API_StaticPolicyDefinitionDetail.md) object
Required: No

 ** templateLinked **   <a name="verifiedpermissions-Type-PolicyDefinitionDetail-templateLinked"></a>
Information about a template-linked policy that was created by instantiating a policy template.
Type: [TemplateLinkedPolicyDefinitionDetail](API_TemplateLinkedPolicyDefinitionDetail.md) object
Required: No

## See Also
<a name="API_PolicyDefinitionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/PolicyDefinitionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/PolicyDefinitionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/PolicyDefinitionDetail)
