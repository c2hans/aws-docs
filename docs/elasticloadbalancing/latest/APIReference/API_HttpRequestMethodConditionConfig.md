---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_HttpRequestMethodConditionConfig.html
---

# HttpRequestMethodConditionConfig
<a name="API_HttpRequestMethodConditionConfig"></a>

Information about an HTTP method condition.

HTTP defines a set of request methods, also referred to as HTTP verbs. For more information, see the [HTTP Method Registry](https://www.iana.org/assignments/http-methods/http-methods.xhtml). You can also define custom HTTP methods.

## Contents
<a name="API_HttpRequestMethodConditionConfig_Contents"></a>

 ** Values.member.N **
The name of the request method. The maximum length is 40 characters. The allowed characters are A-Z, hyphen (-), and underscore (\_). The comparison is case sensitive. Wildcards are not supported; therefore, the method name must be an exact match.
If you specify multiple strings, the condition is satisfied if one of the strings matches the HTTP request method. We recommend that you route GET and HEAD requests in the same way, because the response to a HEAD request may be cached.
Type: Array of strings
Required: No

## See Also
<a name="API_HttpRequestMethodConditionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/HttpRequestMethodConditionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/HttpRequestMethodConditionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/HttpRequestMethodConditionConfig)
