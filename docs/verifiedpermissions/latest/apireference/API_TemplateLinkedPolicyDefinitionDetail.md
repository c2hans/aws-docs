---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_TemplateLinkedPolicyDefinitionDetail.html
---

# TemplateLinkedPolicyDefinitionDetail
<a name="API_TemplateLinkedPolicyDefinitionDetail"></a>

Contains information about a policy that was created by instantiating a policy template.

## Contents
<a name="API_TemplateLinkedPolicyDefinitionDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** policyTemplateId **   <a name="verifiedpermissions-Type-TemplateLinkedPolicyDefinitionDetail-policyTemplateId"></a>
The unique identifier of the policy template used to create this policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** principal **   <a name="verifiedpermissions-Type-TemplateLinkedPolicyDefinitionDetail-principal"></a>
The principal associated with this template-linked policy. Verified Permissions substitutes this principal for the `?principal` placeholder in the policy template when it evaluates an authorization request.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

 ** resource **   <a name="verifiedpermissions-Type-TemplateLinkedPolicyDefinitionDetail-resource"></a>
The resource associated with this template-linked policy. Verified Permissions substitutes this resource for the `?resource` placeholder in the policy template when it evaluates an authorization request.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

## See Also
<a name="API_TemplateLinkedPolicyDefinitionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/TemplateLinkedPolicyDefinitionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/TemplateLinkedPolicyDefinitionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/TemplateLinkedPolicyDefinitionDetail)
