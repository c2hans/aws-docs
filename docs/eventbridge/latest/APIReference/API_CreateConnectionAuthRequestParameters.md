---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateConnectionAuthRequestParameters.html
---

# CreateConnectionAuthRequestParameters
<a name="API_CreateConnectionAuthRequestParameters"></a>

The authorization parameters for the connection.

You must include only authorization parameters for the `AuthorizationType` you specify.

## Contents
<a name="API_CreateConnectionAuthRequestParameters_Contents"></a>

 ** ApiKeyAuthParameters **   <a name="eventbridge-Type-CreateConnectionAuthRequestParameters-ApiKeyAuthParameters"></a>
The API key authorization parameters to use for the connection.
Type: [CreateConnectionApiKeyAuthRequestParameters](API_CreateConnectionApiKeyAuthRequestParameters.md) object
Required: No

 ** BasicAuthParameters **   <a name="eventbridge-Type-CreateConnectionAuthRequestParameters-BasicAuthParameters"></a>
The Basic authorization parameters to use for the connection.
Type: [CreateConnectionBasicAuthRequestParameters](API_CreateConnectionBasicAuthRequestParameters.md) object
Required: No

 ** ConnectivityParameters **   <a name="eventbridge-Type-CreateConnectionAuthRequestParameters-ConnectivityParameters"></a>
If you specify a private OAuth endpoint, the parameters for EventBridge to use when authenticating against the endpoint.
For more information, see [Authorization methods for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-auth.html) in the * *Amazon EventBridge User Guide* *.
Type: [ConnectivityResourceParameters](API_ConnectivityResourceParameters.md) object
Required: No

 ** InvocationHttpParameters **   <a name="eventbridge-Type-CreateConnectionAuthRequestParameters-InvocationHttpParameters"></a>
The API key authorization parameters to use for the connection. Note that if you include additional parameters for the target of a rule via `HttpParameters`, including query strings, the parameters added for the connection take precedence.
Type: [ConnectionHttpParameters](API_ConnectionHttpParameters.md) object
Required: No

 ** OAuthParameters **   <a name="eventbridge-Type-CreateConnectionAuthRequestParameters-OAuthParameters"></a>
The OAuth authorization parameters to use for the connection.
Type: [CreateConnectionOAuthRequestParameters](API_CreateConnectionOAuthRequestParameters.md) object
Required: No

## See Also
<a name="API_CreateConnectionAuthRequestParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/CreateConnectionAuthRequestParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/CreateConnectionAuthRequestParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/CreateConnectionAuthRequestParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
