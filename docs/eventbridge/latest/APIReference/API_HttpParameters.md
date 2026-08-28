---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_HttpParameters.html
---

# HttpParameters
<a name="API_HttpParameters"></a>

These are custom parameter to be used when the target is an API Gateway APIs or EventBridge ApiDestinations. In the latter case, these are merged with any InvocationParameters specified on the Connection, with any values from the Connection taking precedence.

## Contents
<a name="API_HttpParameters_Contents"></a>

 ** HeaderParameters **   <a name="eventbridge-Type-HttpParameters-HeaderParameters"></a>
The headers that need to be sent as part of request invoking the API Gateway API or EventBridge ApiDestination.
Type: String to string map
Key Length Constraints: Maximum length of 512.
Key Pattern: `^[!#$%&'*+-.^_`|~0-9a-zA-Z]+$`
Value Length Constraints: Maximum length of 512.
Value Pattern: `^[ \t]*[\x20-\x7E]+([ \t]+[\x20-\x7E]+)*[ \t]*$`
Required: No

 ** PathParameterValues **   <a name="eventbridge-Type-HttpParameters-PathParameterValues"></a>
The path parameter values to be used to populate API Gateway API or EventBridge ApiDestination path wildcards ("\*").
Type: Array of strings
Pattern: `^(?!\s*$).+`
Required: No

 ** QueryStringParameters **   <a name="eventbridge-Type-HttpParameters-QueryStringParameters"></a>
The query string keys/values that need to be sent as part of request invoking the API Gateway API or EventBridge ApiDestination.
Type: String to string map
Key Length Constraints: Maximum length of 512.
Key Pattern: `[^\x00-\x1F\x7F]+`
Value Length Constraints: Maximum length of 512.
Value Pattern: `[^\x00-\x09\x0B\x0C\x0E-\x1F\x7F]+`
Required: No

## See Also
<a name="API_HttpParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/HttpParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/HttpParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/HttpParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
