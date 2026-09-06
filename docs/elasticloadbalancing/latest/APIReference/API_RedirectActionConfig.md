---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RedirectActionConfig.html
---

# RedirectActionConfig
<a name="API_RedirectActionConfig"></a>

Information about a redirect action.

A URI consists of the following components: protocol://hostname:port/path?query. You must modify at least one of the following components to avoid a redirect loop: protocol, hostname, port, or path. Any components that you do not modify retain their original values.

You can reuse URI components using the following reserved keywords:
+ \#{protocol}
+ \#{host}
+ \#{port}
+ \#{path} (the leading "/" is removed)
+ \#{query}

For example, you can change the path to "/new/\#{path}", the hostname to "example.\#{host}", or the query to "\#{query}&value=xyz".

## Contents
<a name="API_RedirectActionConfig_Contents"></a>

 ** StatusCode **
The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
Type: String
Valid Values: `HTTP_301 | HTTP_302`
Required: Yes

 ** Host **
The hostname. This component is not percent-encoded. The hostname can contain \#{host}.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Path **
The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain \#{host}, \#{path}, and \#{port}.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Port **
The port. You can specify a value from 1 to 65535 or \#{port}.
Type: String
Required: No

 ** Protocol **
The protocol. You can specify HTTP, HTTPS, or \#{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You can't redirect HTTPS to HTTP.
Type: String
Pattern: `^(HTTPS?|#\{protocol\})$`
Required: No

 ** Query **
The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?", as it is automatically added. You can specify any of the reserved keywords.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_RedirectActionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/RedirectActionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/RedirectActionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/RedirectActionConfig)
