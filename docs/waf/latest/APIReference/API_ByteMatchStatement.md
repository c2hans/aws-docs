---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchStatement.html
---

# ByteMatchStatement
<a name="API_ByteMatchStatement"></a>

A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is called a string match statement.

## Contents
<a name="API_ByteMatchStatement_Contents"></a>

 ** FieldToMatch **   <a name="WAF-Type-ByteMatchStatement-FieldToMatch"></a>
The part of the web request that you want AWS WAF to inspect.
Type: [FieldToMatch](API_FieldToMatch.md) object
Required: Yes

 ** PositionalConstraint **   <a name="WAF-Type-ByteMatchStatement-PositionalConstraint"></a>
The area within the portion of the web request that you want AWS WAF to search for `SearchString`. Valid values include the following:
 **CONTAINS**
The specified part of the web request must include the value of `SearchString`, but the location doesn't matter.
 **CONTAINS\_WORD**
The specified part of the web request must include the value of `SearchString`, and `SearchString` must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or \_). In addition, `SearchString` must be a word, which means that both of the following are true:
+  `SearchString` is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (\_). Examples include the value of a header and `;BadBot`.
+  `SearchString` is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (\_), for example, `BadBot;` and `-BadBot;`.
 **EXACTLY**
The value of the specified part of the web request must exactly match the value of `SearchString`.
 **STARTS\_WITH**
The value of `SearchString` must appear at the beginning of the specified part of the web request.
 **ENDS\_WITH**
The value of `SearchString` must appear at the end of the specified part of the web request.
Type: String
Valid Values: `EXACTLY | STARTS_WITH | ENDS_WITH | CONTAINS | CONTAINS_WORD`
Required: Yes

 ** SearchString **   <a name="WAF-Type-ByteMatchStatement-SearchString"></a>
A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in [FieldToMatch](API_FieldToMatch.md). The maximum length of the value is 200 bytes.
Valid values depend on the component that you specify for inspection in `FieldToMatch`:
+  `Method`: The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.
+  `UriPath`: The value that you want AWS WAF to search for in the URI path, for example, `/images/daily-ad.jpg`.
+  `JA3Fingerprint`: Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the request's JA3 fingerprint. The JA3 fingerprint is a 32-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. You can use this choice only with a string match `ByteMatchStatement` with the `PositionalConstraint` set to `EXACTLY`.

  You can obtain the JA3 fingerprint for client requests from the web ACL logs. If AWS WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see [Log fields](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) in the * AWS WAF Developer Guide*.
+  `HeaderOrder`: The list of header names to match for. AWS WAF creates a string that contains the ordered list of header names, from the headers in the web request, and then matches against that string.
If `SearchString` includes alphabetic characters A-Z and a-z, note that the value is case sensitive.
 **If you're using the AWS WAF API**
Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 200 bytes.
For example, suppose the value of `Type` is `HEADER` and the value of `Data` is `User-Agent`. If you want to search the `User-Agent` header for the value `BadBot`, you base64-encode `BadBot` using MIME base64-encoding and include the resulting value, `QmFkQm90`, in the value of `SearchString`.
 **If you're using the AWS CLI or one of the AWS SDKs**
The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.
Type: Base64-encoded binary data object
Required: Yes

 ** TextTransformations **   <a name="WAF-Type-ByteMatchStatement-TextTransformations"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the `FieldToMatch` request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, AWS WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents.
Type: Array of [TextTransformation](API_TextTransformation.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** PreParseTextTransformations **   <a name="WAF-Type-ByteMatchStatement-PreParseTextTransformations"></a>
Pre-parse text transformations normalize the raw query string before AWS WAF parses it into individual query arguments. They are applied before the standard text transformations. Pre-parse text transformations are only supported when `FieldToMatch` is `SingleQueryArgument` or `AllQueryArguments`. You can specify up to 10 pre-parse text transformations per rule statement.
Type: Array of [PreParseTextTransformation](API_PreParseTextTransformation.md) objects
Required: No

## See Also
<a name="API_ByteMatchStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ByteMatchStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ByteMatchStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ByteMatchStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
