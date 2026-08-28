---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_HTTPRequest.html
---

# HTTPRequest
<a name="API_waf_HTTPRequest"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The response from a [GetSampledRequests](API_waf_GetSampledRequests.md) request includes an `HTTPRequest` complex type that appears as `Request` in the response syntax. `HTTPRequest` contains information about one of the web requests that were returned by `GetSampledRequests`.

## Contents
<a name="API_waf_HTTPRequest_Contents"></a>

 ** ClientIP **   <a name="WAF-Type-waf_HTTPRequest-ClientIP"></a>
The IP address that the request originated from. If the `WebACL` is associated with an Amazon CloudFront distribution, this is the value of one of the following fields in CloudFront access logs:
+  `c-ip`, if the viewer did not use an HTTP proxy or a load balancer to send the request
+  `x-forwarded-for`, if the viewer did use an HTTP proxy or a load balancer to send the request
Type: String
Required: No

 ** Country **   <a name="WAF-Type-waf_HTTPRequest-Country"></a>
The two-letter country code for the country that the request originated from. For a current list of country codes, see the Wikipedia entry [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
Type: String
Required: No

 ** Headers **   <a name="WAF-Type-waf_HTTPRequest-Headers"></a>
A complex type that contains two values for each header in the sampled web request: the name of the header and the value of the header.
Type: Array of [HTTPHeader](API_waf_HTTPHeader.md) objects
Required: No

 ** HTTPVersion **   <a name="WAF-Type-waf_HTTPRequest-HTTPVersion"></a>
The HTTP version specified in the sampled web request, for example, `HTTP/1.1`.
Type: String
Required: No

 ** Method **   <a name="WAF-Type-waf_HTTPRequest-Method"></a>
The HTTP method specified in the sampled web request. Amazon CloudFront supports the following methods: `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, and `PUT`.
Type: String
Required: No

 ** URI **   <a name="WAF-Type-waf_HTTPRequest-URI"></a>
The path component of the URI. This does not include the query string or fragment components of the URI. For information, see [Uniform Resource Identifier (URI): Generic Syntax](https://tools.ietf.org/html/rfc3986).
Type: String
Required: No

## See Also
<a name="API_waf_HTTPRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/HTTPRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/HTTPRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/HTTPRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
