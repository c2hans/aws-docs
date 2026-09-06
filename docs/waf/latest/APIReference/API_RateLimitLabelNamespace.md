---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RateLimitLabelNamespace.html
---

# RateLimitLabelNamespace
<a name="API_RateLimitLabelNamespace"></a>

Specifies a label namespace to use as an aggregate key for a rate-based rule. Each distinct fully qualified label name that has the specified label namespace contributes to the aggregation instance. If you use just one label namespace as your custom key, then each label name fully defines an aggregation instance.

This uses only labels that have been added to the request by rules that are evaluated before this rate-based rule in the web ACL.

For information about label namespaces and names, see [Label syntax and naming requirements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-requirements.html) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_RateLimitLabelNamespace_Contents"></a>

 ** Namespace **   <a name="WAF-Type-RateLimitLabelNamespace-Namespace"></a>
The namespace to use for aggregation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9A-Za-z_\-:]+:$`
Required: Yes

## See Also
<a name="API_RateLimitLabelNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RateLimitLabelNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RateLimitLabelNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RateLimitLabelNamespace)
