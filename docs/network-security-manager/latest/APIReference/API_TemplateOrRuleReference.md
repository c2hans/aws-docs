---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_TemplateOrRuleReference.html
---

# TemplateOrRuleReference
<a name="API_TemplateOrRuleReference"></a>

A reference to either a template or a rule in a create or update request. Set exactly one of `templateIdentifier` or `ruleIdentifier`.

## Contents
<a name="API_TemplateOrRuleReference_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ruleIdentifier **   <a name="networksecuritymanager-Type-TemplateOrRuleReference-ruleIdentifier"></a>
The identifier of the rule. This is the rule's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1010.
Required: No

 ** templateIdentifier **   <a name="networksecuritymanager-Type-TemplateOrRuleReference-templateIdentifier"></a>
The identifier of the template. This is the template's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1010.
Required: No

## See Also
<a name="API_TemplateOrRuleReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/TemplateOrRuleReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/TemplateOrRuleReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/TemplateOrRuleReference)
