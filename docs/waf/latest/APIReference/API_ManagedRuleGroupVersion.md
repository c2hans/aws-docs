---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ManagedRuleGroupVersion.html
---

# ManagedRuleGroupVersion
<a name="API_ManagedRuleGroupVersion"></a>

Describes a single version of a managed rule group.

## Contents
<a name="API_ManagedRuleGroupVersion_Contents"></a>

 ** LastUpdateTimestamp **   <a name="WAF-Type-ManagedRuleGroupVersion-LastUpdateTimestamp"></a>
The date and time that the managed rule group owner updated the rule group version information.
Type: Timestamp
Required: No

 ** Name **   <a name="WAF-Type-ManagedRuleGroupVersion-Name"></a>
The version name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[\w#:\.\-/]+$`
Required: No

## See Also
<a name="API_ManagedRuleGroupVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ManagedRuleGroupVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ManagedRuleGroupVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ManagedRuleGroupVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
