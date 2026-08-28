---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_HttpRequestConfiguration.html
---

# HttpRequestConfiguration
<a name="API_HttpRequestConfiguration"></a>

The configuration for an `HTTP_REQUEST` function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions for the request. For more information, see [HTTP\_REQUEST](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types-http-request.html) in the *MediaTailor User Guide*.

## Contents
<a name="API_HttpRequestConfiguration_Contents"></a>

 ** MethodType **   <a name="mediatailor-Type-HttpRequestConfiguration-MethodType"></a>
The HTTP method for the request. Valid values: `GET` and `POST`.
Type: String
Valid Values: `GET | POST`
Required: Yes

 ** RequestTimeoutMilliseconds **   <a name="mediatailor-Type-HttpRequestConfiguration-RequestTimeoutMilliseconds"></a>
The maximum time, in milliseconds, that MediaTailor waits for a response from the external service. If the call exceeds this timeout, MediaTailor sets the response status code to `null` and proceeds with output expression evaluation. Valid values: `100` to `2000`.
Type: Integer
Required: Yes

 ** Runtime **   <a name="mediatailor-Type-HttpRequestConfiguration-Runtime"></a>
The expression language used to evaluate expressions in the function configuration. Set this to `JSONata`.
Type: String
Valid Values: `JSONATA`
Required: Yes

 ** Url **   <a name="mediatailor-Type-HttpRequestConfiguration-Url"></a>
An expression that evaluates to the request URL. Use `{%...%}` delimiters for dynamic expressions. The maximum length after evaluation is 2,048 characters.
Type: String
Required: Yes

 ** Body **   <a name="mediatailor-Type-HttpRequestConfiguration-Body"></a>
An expression that evaluates to the request body. Used with `POST` requests. The maximum size after evaluation is 64 KB.
Type: String
Required: No

 ** Headers **   <a name="mediatailor-Type-HttpRequestConfiguration-Headers"></a>
A map of HTTP header names to expression values. MediaTailor evaluates each header value expression at runtime and includes the result in the outbound HTTP request. Maximum 50 headers.
Type: String to string map
Required: No

 ** Output **   <a name="mediatailor-Type-HttpRequestConfiguration-Output"></a>
A map of output bindings. Each key is a namespaced output path (such as `player_params.device_type` or `temp.identity`), and each value is an expression that MediaTailor evaluates at runtime. Output expressions in an `HTTP_REQUEST` function can reference the `response` object returned by the HTTP call. For more information about expression syntax, see [JSONata expression reference](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-jsonata.html) in the *MediaTailor User Guide*.
Type: String to string map
Required: No

## See Also
<a name="API_HttpRequestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/HttpRequestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/HttpRequestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/HttpRequestConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
