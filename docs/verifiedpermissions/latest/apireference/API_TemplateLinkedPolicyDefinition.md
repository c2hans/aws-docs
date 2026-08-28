---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_TemplateLinkedPolicyDefinition.html
---

# TemplateLinkedPolicyDefinition
<a name="API_TemplateLinkedPolicyDefinition"></a>

Contains information about a policy created by instantiating a policy template.

## Contents
<a name="API_TemplateLinkedPolicyDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** policyTemplateId **   <a name="verifiedpermissions-Type-TemplateLinkedPolicyDefinition-policyTemplateId"></a>
The unique identifier of the policy template used to create this policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** principal **   <a name="verifiedpermissions-Type-TemplateLinkedPolicyDefinition-principal"></a>
The principal associated with this template-linked policy. Verified Permissions substitutes this principal for the `?principal` placeholder in the policy template when it evaluates an authorization request.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

 ** resource **   <a name="verifiedpermissions-Type-TemplateLinkedPolicyDefinition-resource"></a>
The resource associated with this template-linked policy. Verified Permissions substitutes this resource for the `?resource` placeholder in the policy template when it evaluates an authorization request.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

## See Also
<a name="API_TemplateLinkedPolicyDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/TemplateLinkedPolicyDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/TemplateLinkedPolicyDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/TemplateLinkedPolicyDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
