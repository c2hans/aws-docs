---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinitionItem.html
---

# PolicyDefinitionItem
<a name="API_PolicyDefinitionItem"></a>

A structure that describes a [PolicyDefinintion](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinintion.html). It will always have either an `StaticPolicy` or a `TemplateLinkedPolicy` element.

This data type is used as a response parameter for the [CreatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html) and [ListPolicies](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html) operations.

## Contents
<a name="API_PolicyDefinitionItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** static **   <a name="verifiedpermissions-Type-PolicyDefinitionItem-static"></a>
Information about a static policy that wasn't created with a policy template.
Type: [StaticPolicyDefinitionItem](API_StaticPolicyDefinitionItem.md) object
Required: No

 ** templateLinked **   <a name="verifiedpermissions-Type-PolicyDefinitionItem-templateLinked"></a>
Information about a template-linked policy that was created by instantiating a policy template.
Type: [TemplateLinkedPolicyDefinitionItem](API_TemplateLinkedPolicyDefinitionItem.md) object
Required: No

## See Also
<a name="API_PolicyDefinitionItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/PolicyDefinitionItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/PolicyDefinitionItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/PolicyDefinitionItem)
