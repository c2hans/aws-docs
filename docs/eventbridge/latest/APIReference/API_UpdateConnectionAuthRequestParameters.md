---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateConnectionAuthRequestParameters.html
---

# UpdateConnectionAuthRequestParameters
<a name="API_UpdateConnectionAuthRequestParameters"></a>

Contains the additional parameters to use for the connection.

## Contents
<a name="API_UpdateConnectionAuthRequestParameters_Contents"></a>

 ** ApiKeyAuthParameters **   <a name="eventbridge-Type-UpdateConnectionAuthRequestParameters-ApiKeyAuthParameters"></a>
The authorization parameters for API key authorization.
Type: [UpdateConnectionApiKeyAuthRequestParameters](API_UpdateConnectionApiKeyAuthRequestParameters.md) object
Required: No

 ** BasicAuthParameters **   <a name="eventbridge-Type-UpdateConnectionAuthRequestParameters-BasicAuthParameters"></a>
The authorization parameters for Basic authorization.
Type: [UpdateConnectionBasicAuthRequestParameters](API_UpdateConnectionBasicAuthRequestParameters.md) object
Required: No

 ** ConnectivityParameters **   <a name="eventbridge-Type-UpdateConnectionAuthRequestParameters-ConnectivityParameters"></a>
If you specify a private OAuth endpoint, the parameters for EventBridge to use when authenticating against the endpoint.
For more information, see [Authorization methods for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-auth.html) in the * *Amazon EventBridge User Guide* *.
Type: [ConnectivityResourceParameters](API_ConnectivityResourceParameters.md) object
Required: No

 ** InvocationHttpParameters **   <a name="eventbridge-Type-UpdateConnectionAuthRequestParameters-InvocationHttpParameters"></a>
The additional parameters to use for the connection.
Type: [ConnectionHttpParameters](API_ConnectionHttpParameters.md) object
Required: No

 ** OAuthParameters **   <a name="eventbridge-Type-UpdateConnectionAuthRequestParameters-OAuthParameters"></a>
The authorization parameters for OAuth authorization.
Type: [UpdateConnectionOAuthRequestParameters](API_UpdateConnectionOAuthRequestParameters.md) object
Required: No

## See Also
<a name="API_UpdateConnectionAuthRequestParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/UpdateConnectionAuthRequestParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/UpdateConnectionAuthRequestParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/UpdateConnectionAuthRequestParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
