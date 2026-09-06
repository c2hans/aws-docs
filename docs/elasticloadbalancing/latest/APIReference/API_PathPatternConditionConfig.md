---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_PathPatternConditionConfig.html
---

# PathPatternConditionConfig
<a name="API_PathPatternConditionConfig"></a>

Information about a path pattern condition.

## Contents
<a name="API_PathPatternConditionConfig_Contents"></a>

 ** RegexValues.member.N **
The regular expressions to compare against the request URL. The maximum length of each string is 128 characters.
Type: Array of strings
Required: No

 ** Values.member.N **
The path patterns to compare against the request URL. The maximum length of each string is 128 characters. The comparison is case sensitive. The following wildcard characters are supported: \* (matches 0 or more characters) and ? (matches exactly 1 character).
If you specify multiple strings, the condition is satisfied if one of them matches the request URL. The path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use a [query string condition](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#query-string-conditions).
Type: Array of strings
Required: No

## See Also
<a name="API_PathPatternConditionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/PathPatternConditionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/PathPatternConditionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/PathPatternConditionConfig)
