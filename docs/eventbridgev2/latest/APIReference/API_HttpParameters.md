---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_HttpParameters.html
---

# HttpParameters
<a name="API_HttpParameters"></a>

HTTP invocation parameters for subscribers (API Gateway / API Destination). Values are forwarded to the HTTP endpoint.

## Contents
<a name="API_HttpParameters_Contents"></a>

 ** HeaderParameters **   <a name="eventbridgev2-Type-HttpParameters-HeaderParameters"></a>
Map of HTTP header names to values, sent with the request to an HTTP target.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 512.
Key Pattern: `([!#$%&'*+\-.^_`|~0-9a-zA-Z]+|\{%[\s\S]+?%\})`
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Value Pattern: `([ \t]*[\x20-\x7E]+([ \t]+[\x20-\x7E]+)*[ \t]*|\{%[\s\S]+?%\})`
Required: No

 ** InvocationTimeoutSeconds **   <a name="eventbridgev2-Type-HttpParameters-InvocationTimeoutSeconds"></a>
Timeout in seconds for each invocation of the target (1-30). String-typed (not integer) so the value may be a JSONata expression.
Type: String
Required: No

 ** PathParameterValues **   <a name="eventbridgev2-Type-HttpParameters-PathParameterValues"></a>
Values substituted, in order, for the path-parameter placeholders in an HTTP target's endpoint path.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Pattern: `(?!\s*$).+`
Required: No

 ** QueryStringParameters **   <a name="eventbridgev2-Type-HttpParameters-QueryStringParameters"></a>
Map of query-string parameter names to values, appended to the request to an HTTP target.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 512.
Key Pattern: `[^\x00-\x1F\x7F]+`
Value Length Constraints: Minimum length of 0. Maximum length of 512.
Value Pattern: `[^\x00-\x09\x0B\x0C\x0E-\x1F\x7F]+`
Required: No

## See Also
<a name="API_HttpParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/HttpParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/HttpParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/HttpParameters)
