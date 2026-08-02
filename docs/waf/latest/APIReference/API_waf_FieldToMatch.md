---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_FieldToMatch.html
---

# FieldToMatch
<a name="API_waf_FieldToMatch"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies where in a web request to look for `TargetString`.

## Contents
<a name="API_waf_FieldToMatch_Contents"></a>

 ** Type **   <a name="WAF-Type-waf_FieldToMatch-Type"></a>
The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:
+  `HEADER`: A specified request header, for example, the value of the `User-Agent` or `Referer` header. If you choose `HEADER` for the type, specify the name of the header in `Data`.
+  `METHOD`: The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, and `PUT`.
+  `QUERY_STRING`: A query string, which is the part of a URL that appears after a `?` character, if any.
+  `URI`: The path component of the URI. This does not include the query string or fragment components of the URI. For information, see [Uniform Resource Identifier (URI): Generic Syntax](https://tools.ietf.org/html/rfc3986).
+  `BODY`: The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first `8192` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see [CreateSizeConstraintSet](API_waf_CreateSizeConstraintSet.md).
+  `SINGLE_QUERY_ARG`: The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion*. The maximum length for `SINGLE_QUERY_ARG` is 30 characters.
+  `ALL_QUERY_ARGS`: Similar to `SINGLE_QUERY_ARG`, but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in `TargetString`.
Type: String
Valid Values: `URI | QUERY_STRING | HEADER | METHOD | BODY | SINGLE_QUERY_ARG | ALL_QUERY_ARGS`
Required: Yes

 ** Data **   <a name="WAF-Type-waf_FieldToMatch-Data"></a>
When the value of `Type` is `HEADER`, enter the name of the header that you want AWS WAF to search, for example, `User-Agent` or `Referer`. The name of the header is not case sensitive.
When the value of `Type` is `SINGLE_QUERY_ARG`, enter the name of the parameter that you want AWS WAF to search, for example, `UserName` or `SalesRegion`. The parameter name is not case sensitive.
If the value of `Type` is any other value, omit `Data`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_waf_FieldToMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/FieldToMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/FieldToMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/FieldToMatch)
