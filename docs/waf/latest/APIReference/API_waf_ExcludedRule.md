---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ExcludedRule.html
---

# ExcludedRule
<a name="API_waf_ExcludedRule"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The rule to exclude from a rule group. This is applicable only when the `ActivatedRule` refers to a `RuleGroup`. The rule must belong to the `RuleGroup` that is specified by the `ActivatedRule`.

## Contents
<a name="API_waf_ExcludedRule_Contents"></a>

 ** RuleId **   <a name="WAF-Type-waf_ExcludedRule-RuleId"></a>
The unique identifier for the rule to exclude from the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_waf_ExcludedRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/ExcludedRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/ExcludedRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/ExcludedRule)
