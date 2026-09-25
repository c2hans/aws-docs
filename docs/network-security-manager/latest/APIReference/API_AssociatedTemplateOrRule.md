---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AssociatedTemplateOrRule.html
---

# AssociatedTemplateOrRule
<a name="API_AssociatedTemplateOrRule"></a>

An association between a policy and either a template or a rule, as returned in outputs. Exactly one of `templateArn` or `ruleArn` is set. The corresponding request structure is `TemplateOrRuleReference`.

## Contents
<a name="API_AssociatedTemplateOrRule_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ruleArn **   <a name="networksecuritymanager-Type-AssociatedTemplateOrRule-ruleArn"></a>
The ARN of the associated rule.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: No

 ** templateArn **   <a name="networksecuritymanager-Type-AssociatedTemplateOrRule-templateArn"></a>
The ARN of the associated template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: No

## See Also
<a name="API_AssociatedTemplateOrRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AssociatedTemplateOrRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AssociatedTemplateOrRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AssociatedTemplateOrRule)
