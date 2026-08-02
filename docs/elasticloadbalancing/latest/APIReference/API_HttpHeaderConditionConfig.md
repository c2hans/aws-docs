---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_HttpHeaderConditionConfig.html
---

# HttpHeaderConditionConfig
<a name="API_HttpHeaderConditionConfig"></a>

Information about an HTTP header condition.

There is a set of standard HTTP header fields. You can also define custom HTTP header fields.

## Contents
<a name="API_HttpHeaderConditionConfig_Contents"></a>

 ** HttpHeaderName **
The name of the HTTP header field. The maximum length is 40 characters. The header name is case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not supported.
You can't use an HTTP header condition to specify the host header. Instead, use a [host condition](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#host-conditions).
Type: String
Required: No

 ** RegexValues.member.N **
The regular expression to compare against the HTTP header. The maximum length of each string is 128 characters.
Type: Array of strings
Required: No

 ** Values.member.N **
The strings to compare against the value of the HTTP header. The maximum length of each string is 128 characters. The comparison strings are case insensitive. The following wildcard characters are supported: \* (matches 0 or more characters) and ? (matches exactly 1 character).
If the same header appears multiple times in the request, we search them in order until a match is found.
If you specify multiple strings, the condition is satisfied if one of the strings matches the value of the HTTP header. To require that all of the strings are a match, create one condition per string.
Type: Array of strings
Required: No

## See Also
<a name="API_HttpHeaderConditionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/HttpHeaderConditionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/HttpHeaderConditionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/HttpHeaderConditionConfig)
