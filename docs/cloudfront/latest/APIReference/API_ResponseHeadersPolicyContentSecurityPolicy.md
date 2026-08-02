---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyContentSecurityPolicy.html
---

# ResponseHeadersPolicyContentSecurityPolicy
<a name="API_ResponseHeadersPolicyContentSecurityPolicy"></a>

The policy directives and their values that CloudFront includes as values for the `Content-Security-Policy` HTTP response header.

For more information about the `Content-Security-Policy` HTTP response header, see [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) in the MDN Web Docs.

## Contents
<a name="API_ResponseHeadersPolicyContentSecurityPolicy_Contents"></a>

 ** ContentSecurityPolicy **   <a name="cloudfront-Type-ResponseHeadersPolicyContentSecurityPolicy-ContentSecurityPolicy"></a>
The policy directives and their values that CloudFront includes as values for the `Content-Security-Policy` HTTP response header.
Type: String
Required: Yes

 ** Override **   <a name="cloudfront-Type-ResponseHeadersPolicyContentSecurityPolicy-Override"></a>
A Boolean that determines whether CloudFront overrides the `Content-Security-Policy` HTTP response header received from the origin with the one specified in this response headers policy.
Type: Boolean
Required: Yes

## See Also
<a name="API_ResponseHeadersPolicyContentSecurityPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyContentSecurityPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyContentSecurityPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyContentSecurityPolicy)
