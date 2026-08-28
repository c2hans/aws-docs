---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html
---

# FieldToMatch
<a name="API_FieldToMatch"></a>

Specifies a web request component to be used in a rule match statement or in a logging configuration.
+ In a rule statement, this is the part of the web request that you want AWS WAF to inspect. Include the single `FieldToMatch` type that you want to inspect, with additional specifications as needed, according to the type. You specify a single request component in `FieldToMatch` for each rule statement that requires it. To inspect more than one component of the web request, create a separate rule statement for each component.

  Example JSON for a `QueryString` field to match:

   ` "FieldToMatch": { "QueryString": {} }`

  Example JSON for a `Method` field to match specification:

   ` "FieldToMatch": { "Method": { "Name": "DELETE" } }`
+ In a logging configuration, this is used in the `RedactedFields` property to specify a field to redact from the logging records. For this use case, note the following:
  + Even though all `FieldToMatch` settings are available, the only valid settings for field redaction are `UriPath`, `QueryString`, `SingleHeader`, and `Method`.
  + In this documentation, the descriptions of the individual fields talk about specifying the web request component to inspect, but for field redaction, you are specifying the component type to redact from the logs.
  + If you have request sampling enabled, the redacted fields configuration for logging has no impact on sampling. You can only exclude fields from request sampling by disabling sampling in the web ACL visibility configuration or by configuring data protection for the web ACL.

## Contents
<a name="API_FieldToMatch_Contents"></a>

 ** AllQueryArguments **   <a name="WAF-Type-FieldToMatch-AllQueryArguments"></a>
Inspect all query arguments.
Type: [AllQueryArguments](API_AllQueryArguments.md) object
Required: No

 ** Body **   <a name="WAF-Type-FieldToMatch-Body"></a>
Inspect the request body as plain text. The request body immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
 AWS WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to AWS WAF for inspection.
+ For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).
+ For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL `AssociationConfig`, for additional processing fees.
+ For AWS Amplify, use the CloudFront limit.
For information about how to handle oversized request bodies, see the `Body` object configuration.
Type: [Body](API_Body.md) object
Required: No

 ** Cookies **   <a name="WAF-Type-FieldToMatch-Cookies"></a>
Inspect the request cookies. You must configure scope and pattern matching filters in the `Cookies` object, to define the set of cookies and the parts of the cookies that AWS WAF inspects.
Only the first 8 KB (8192 bytes) of a request's cookies and only the first 200 cookies are forwarded to AWS WAF for inspection by the underlying host service. You must configure how to handle any oversize cookie content in the `Cookies` object. AWS WAF applies the pattern matching filters to the cookies that it receives from the underlying host service.
Type: [Cookies](API_Cookies.md) object
Required: No

 ** HeaderOrder **   <a name="WAF-Type-FieldToMatch-HeaderOrder"></a>
Inspect a string containing the list of the request's header names, ordered as they appear in the web request that AWS WAF receives for inspection. AWS WAF generates the string and then uses that as the field to match component in its inspection. AWS WAF separates the header names in the string using colons and no added spaces, for example `host:user-agent:accept:authorization:referer`.
Type: [HeaderOrder](API_HeaderOrder.md) object
Required: No

 ** Headers **   <a name="WAF-Type-FieldToMatch-Headers"></a>
Inspect the request headers. You must configure scope and pattern matching filters in the `Headers` object, to define the set of headers to and the parts of the headers that AWS WAF inspects.
Only the first 8 KB (8192 bytes) of a request's headers and only the first 200 headers are forwarded to AWS WAF for inspection by the underlying host service. You must configure how to handle any oversize header content in the `Headers` object. AWS WAF applies the pattern matching filters to the headers that it receives from the underlying host service.
Type: [Headers](API_Headers.md) object
Required: No

 ** JA3Fingerprint **   <a name="WAF-Type-FieldToMatch-JA3Fingerprint"></a>
Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the request's JA3 fingerprint. The JA3 fingerprint is a 32-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. AWS WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation. Almost all web requests include this information.
You can use this choice only with a string match `ByteMatchStatement` with the `PositionalConstraint` set to `EXACTLY`.
You can obtain the JA3 fingerprint for client requests from the web ACL logs. If AWS WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see [Log fields](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) in the * AWS WAF Developer Guide*.
Provide the JA3 fingerprint string from the logs in your string match statement specification, to match with any future requests that have the same TLS configuration.
Type: [JA3Fingerprint](API_JA3Fingerprint.md) object
Required: No

 ** JA4Fingerprint **   <a name="WAF-Type-FieldToMatch-JA4Fingerprint"></a>
Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the request's JA4 fingerprint. The JA4 fingerprint is a 36-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. AWS WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation. Almost all web requests include this information.
You can use this choice only with a string match `ByteMatchStatement` with the `PositionalConstraint` set to `EXACTLY`.
You can obtain the JA4 fingerprint for client requests from the web ACL logs. If AWS WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see [Log fields](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) in the * AWS WAF Developer Guide*.
Provide the JA4 fingerprint string from the logs in your string match statement specification, to match with any future requests that have the same TLS configuration.
Type: [JA4Fingerprint](API_JA4Fingerprint.md) object
Required: No

 ** JsonBody **   <a name="WAF-Type-FieldToMatch-JsonBody"></a>
Inspect the request body as JSON. The request body immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
 AWS WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to AWS WAF for inspection.
+ For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).
+ For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL `AssociationConfig`, for additional processing fees.
+ For AWS Amplify, use the CloudFront limit.
For information about how to handle oversized request bodies, see the `JsonBody` object configuration.
Type: [JsonBody](API_JsonBody.md) object
Required: No

 ** Method **   <a name="WAF-Type-FieldToMatch-Method"></a>
Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.
Type: [Method](API_Method.md) object
Required: No

 ** QueryString **   <a name="WAF-Type-FieldToMatch-QueryString"></a>
Inspect the query string. This is the part of a URL that appears after a `?` character, if any.
Type: [QueryString](API_QueryString.md) object
Required: No

 ** SingleHeader **   <a name="WAF-Type-FieldToMatch-SingleHeader"></a>
Inspect a single header. Provide the name of the header to inspect, for example, `User-Agent` or `Referer`. This setting isn't case sensitive.
Example JSON: `"SingleHeader": { "Name": "haystack" }`
Alternately, you can filter and inspect all headers with the `Headers` `FieldToMatch` setting.
Type: [SingleHeader](API_SingleHeader.md) object
Required: No

 ** SingleQueryArgument **   <a name="WAF-Type-FieldToMatch-SingleQueryArgument"></a>
Inspect a single query argument. Provide the name of the query argument to inspect, such as *UserName* or *SalesRegion*. The name can be up to 30 characters long and isn't case sensitive.
Example JSON: `"SingleQueryArgument": { "Name": "myArgument" }`
Type: [SingleQueryArgument](API_SingleQueryArgument.md) object
Required: No

 ** UriFragment **   <a name="WAF-Type-FieldToMatch-UriFragment"></a>
Inspect fragments of the request URI. You must configure scope and pattern matching filters in the `UriFragment` object, to define the fragment of a URI that AWS WAF inspects.
Only the first 8 KB (8192 bytes) of a request's URI fragments and only the first 200 URI fragments are forwarded to AWS WAF for inspection by the underlying host service. You must configure how to handle any oversize URI fragment content in the `UriFragment` object. AWS WAF applies the pattern matching filters to the cookies that it receives from the underlying host service.
Type: [UriFragment](API_UriFragment.md) object
Required: No

 ** UriPath **   <a name="WAF-Type-FieldToMatch-UriPath"></a>
Inspect the request URI path. This is the part of the web request that identifies a resource, for example, `/images/daily-ad.jpg`.
Type: [UriPath](API_UriPath.md) object
Required: No

## See Also
<a name="API_FieldToMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/FieldToMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/FieldToMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/FieldToMatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
