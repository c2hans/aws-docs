---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ByteMatchTuple.html
---

# ByteMatchTuple
<a name="API_waf_ByteMatchTuple"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

## Contents
<a name="API_waf_ByteMatchTuple_Contents"></a>

 ** FieldToMatch **   <a name="WAF-Type-waf_ByteMatchTuple-FieldToMatch"></a>
The part of a web request that you want AWS WAF to search, such as a specified header or a query string. For more information, see [FieldToMatch](API_waf_FieldToMatch.md).
Type: [FieldToMatch](API_waf_FieldToMatch.md) object
Required: Yes

 ** PositionalConstraint **   <a name="WAF-Type-waf_ByteMatchTuple-PositionalConstraint"></a>
Within the portion of a web request that you want to search (for example, in the query string, if any), specify where you want AWS WAF to search. Valid values include the following:
 **CONTAINS**
The specified part of the web request must include the value of `TargetString`, but the location doesn't matter.
 **CONTAINS\_WORD**
The specified part of the web request must include the value of `TargetString`, and `TargetString` must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or \_). In addition, `TargetString` must be a word, which means one of the following:
+  `TargetString` exactly matches the value of the specified part of the web request, such as the value of a header.
+  `TargetString` is at the beginning of the specified part of the web request and is followed by a character other than an alphanumeric character or underscore (\_), for example, `BadBot;`.
+  `TargetString` is at the end of the specified part of the web request and is preceded by a character other than an alphanumeric character or underscore (\_), for example, `;BadBot`.
+  `TargetString` is in the middle of the specified part of the web request and is preceded and followed by characters other than alphanumeric characters or underscore (\_), for example, `-BadBot;`.
 **EXACTLY**
The value of the specified part of the web request must exactly match the value of `TargetString`.
 **STARTS\_WITH**
The value of `TargetString` must appear at the beginning of the specified part of the web request.
 **ENDS\_WITH**
The value of `TargetString` must appear at the end of the specified part of the web request.
Type: String
Valid Values: `EXACTLY | STARTS_WITH | ENDS_WITH | CONTAINS | CONTAINS_WORD`
Required: Yes

 ** TargetString **   <a name="WAF-Type-waf_ByteMatchTuple-TargetString"></a>
The value that you want AWS WAF to search for. AWS WAF searches for the specified string in the part of web requests that you specified in `FieldToMatch`. The maximum length of the value is 50 bytes.
Valid values depend on the values that you specified for `FieldToMatch`:
+  `HEADER`: The value that you want AWS WAF to search for in the request header that you specified in [FieldToMatch](API_waf_FieldToMatch.md), for example, the value of the `User-Agent` or `Referer` header.
+  `METHOD`: The HTTP method, which indicates the type of operation specified in the request. Amazon CloudFront supports the following methods: `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, and `PUT`.
+  `QUERY_STRING`: The value that you want AWS WAF to search for in the query string, which is the part of a URL that appears after a `?` character.
+  `URI`: The path component of the URI. This does not include the query string or fragment components of the URI. For information, see [Uniform Resource Identifier (URI): Generic Syntax](https://tools.ietf.org/html/rfc3986).
+  `BODY`: The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first `8192` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see [CreateSizeConstraintSet](API_waf_CreateSizeConstraintSet.md).
+  `SINGLE_QUERY_ARG`: The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion*. The maximum length for `SINGLE_QUERY_ARG` is 30 characters.
+  `ALL_QUERY_ARGS`: Similar to `SINGLE_QUERY_ARG`, but instead of inspecting a single parameter, AWS WAF inspects all parameters within the query string for the value or regex pattern that you specify in `TargetString`.
If `TargetString` includes alphabetic characters A-Z and a-z, note that the value is case sensitive.
 **If you're using the AWS WAF API**
Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
For example, suppose the value of `Type` is `HEADER` and the value of `Data` is `User-Agent`. If you want to search the `User-Agent` header for the value `BadBot`, you base64-encode `BadBot` using MIME base64-encoding and include the resulting value, `QmFkQm90`, in the value of `TargetString`.
 **If you're using the AWS CLI or one of the AWS SDKs**
The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.
Type: Base64-encoded binary data object
Required: Yes

 ** TextTransformation **   <a name="WAF-Type-waf_ByteMatchTuple-TextTransformation"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on `FieldToMatch` before inspecting it for a match.
You can only specify a single type of TextTransformation.
 **CMD\_LINE**
When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:
+ Delete the following characters: \\ " ' ^
+ Delete spaces before the following characters: / (
+ Replace the following characters with a space: , ;
+ Replace multiple spaces with one space
+ Convert uppercase letters (A-Z) to lowercase (a-z)
 **COMPRESS\_WHITE\_SPACE**
Use this option to replace the following characters with a space character (decimal 32):
+ \\f, formfeed, decimal 12
+ \\t, tab, decimal 9
+ \\n, newline, decimal 10
+ \\r, carriage return, decimal 13
+ \\v, vertical tab, decimal 11
+ non-breaking space, decimal 160
 `COMPRESS_WHITE_SPACE` also replaces multiple spaces with one space.
 **HTML\_ENTITY\_DECODE**
Use this option to replace HTML-encoded characters with unencoded characters. `HTML_ENTITY_DECODE` performs the following operations:
+ Replaces `(ampersand)quot;` with `"`
+ Replaces `(ampersand)nbsp;` with a non-breaking space, decimal 160
+ Replaces `(ampersand)lt;` with a "less than" symbol
+ Replaces `(ampersand)gt;` with `>`
+ Replaces characters that are represented in hexadecimal format, `(ampersand)#xhhhh;`, with the corresponding characters
+ Replaces characters that are represented in decimal format, `(ampersand)#nnnn;`, with the corresponding characters
 **LOWERCASE**
Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
 **URL\_DECODE**
Use this option to decode a URL-encoded value.
 **NONE**
Specify `NONE` if you don't want to perform any text transformations.
Type: String
Valid Values: `NONE | COMPRESS_WHITE_SPACE | HTML_ENTITY_DECODE | LOWERCASE | CMD_LINE | URL_DECODE`
Required: Yes

## See Also
<a name="API_waf_ByteMatchTuple_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/ByteMatchTuple)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/ByteMatchTuple)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/ByteMatchTuple)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
