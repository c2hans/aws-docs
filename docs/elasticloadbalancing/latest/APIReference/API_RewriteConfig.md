---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RewriteConfig.html
---

# RewriteConfig
<a name="API_RewriteConfig"></a>

Information about a rewrite transform. This transform matches a pattern and replaces it with the specified string.

## Contents
<a name="API_RewriteConfig_Contents"></a>

 ** Regex **
The regular expression to match in the input string. The maximum length of the string is 1,024 characters.
Type: String
Required: Yes

 ** Replace **
The replacement string to use when rewriting the matched input. The maximum length of the string is 1,024 characters. You can specify capture groups in the regular expression (for example, $1 and $2).
Type: String
Required: Yes

## See Also
<a name="API_RewriteConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/RewriteConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/RewriteConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/RewriteConfig)
