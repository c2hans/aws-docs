---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ConnectionAuthResponseParameters.html
---

# ConnectionAuthResponseParameters
<a name="API_ConnectionAuthResponseParameters"></a>

Tthe authorization parameters to use for the connection.

## Contents
<a name="API_ConnectionAuthResponseParameters_Contents"></a>

 ** ApiKeyAuthParameters **   <a name="eventbridge-Type-ConnectionAuthResponseParameters-ApiKeyAuthParameters"></a>
The API Key parameters to use for authorization.
Type: [ConnectionApiKeyAuthResponseParameters](API_ConnectionApiKeyAuthResponseParameters.md) object
Required: No

 ** BasicAuthParameters **   <a name="eventbridge-Type-ConnectionAuthResponseParameters-BasicAuthParameters"></a>
The authorization parameters for Basic authorization.
Type: [ConnectionBasicAuthResponseParameters](API_ConnectionBasicAuthResponseParameters.md) object
Required: No

 ** ConnectivityParameters **   <a name="eventbridge-Type-ConnectionAuthResponseParameters-ConnectivityParameters"></a>
For private OAuth authentication endpoints. The parameters EventBridge uses to authenticate against the endpoint.
For more information, see [Authorization methods for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-auth.html) in the * *Amazon EventBridge User Guide* *.
Type: [DescribeConnectionConnectivityParameters](API_DescribeConnectionConnectivityParameters.md) object
Required: No

 ** InvocationHttpParameters **   <a name="eventbridge-Type-ConnectionAuthResponseParameters-InvocationHttpParameters"></a>
Additional parameters for the connection that are passed through with every invocation to the HTTP endpoint.
Type: [ConnectionHttpParameters](API_ConnectionHttpParameters.md) object
Required: No

 ** OAuthParameters **   <a name="eventbridge-Type-ConnectionAuthResponseParameters-OAuthParameters"></a>
The OAuth parameters to use for authorization.
Type: [ConnectionOAuthResponseParameters](API_ConnectionOAuthResponseParameters.md) object
Required: No

## See Also
<a name="API_ConnectionAuthResponseParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ConnectionAuthResponseParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ConnectionAuthResponseParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ConnectionAuthResponseParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
