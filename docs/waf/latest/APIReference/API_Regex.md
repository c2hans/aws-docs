---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_Regex.html
---

# Regex
<a name="API_Regex"></a>

A single regular expression. This is used in a [RegexPatternSet](API_RegexPatternSet.md) and also in the configuration for the AWS Managed Rules rule group `AWSManagedRulesAntiDDoSRuleSet`.

## Contents
<a name="API_Regex_Contents"></a>

 ** RegexString **   <a name="WAF-Type-Regex-RegexString"></a>
The string representing the regular expression. AWS WAF enforces a quota on the maximum number of characters in a regex pattern. For the current limit, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the * AWS WAF Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: No

## See Also
<a name="API_Regex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/Regex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/Regex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/Regex)
