---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateConnectionOAuthRequestParameters.html
---

# CreateConnectionOAuthRequestParameters
<a name="API_CreateConnectionOAuthRequestParameters"></a>

Contains the OAuth authorization parameters to use for the connection.

## Contents
<a name="API_CreateConnectionOAuthRequestParameters_Contents"></a>

 ** AuthorizationEndpoint **   <a name="eventbridge-Type-CreateConnectionOAuthRequestParameters-AuthorizationEndpoint"></a>
The URL to the authorization endpoint when OAuth is specified as the authorization type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^((%[0-9A-Fa-f]{2}|[-()_.!~*';/?:@\x26=+$,A-Za-z0-9])+)([).!';/?:,])?$`
Required: Yes

 ** ClientParameters **   <a name="eventbridge-Type-CreateConnectionOAuthRequestParameters-ClientParameters"></a>
The client parameters for OAuth authorization.
Type: [CreateConnectionOAuthClientRequestParameters](API_CreateConnectionOAuthClientRequestParameters.md) object
Required: Yes

 ** HttpMethod **   <a name="eventbridge-Type-CreateConnectionOAuthRequestParameters-HttpMethod"></a>
The method to use for the authorization request.
Type: String
Valid Values: `GET | POST | PUT`
Required: Yes

 ** OAuthHttpParameters **   <a name="eventbridge-Type-CreateConnectionOAuthRequestParameters-OAuthHttpParameters"></a>
Details about the additional parameters to use for the connection.
Type: [ConnectionHttpParameters](API_ConnectionHttpParameters.md) object
Required: No

## See Also
<a name="API_CreateConnectionOAuthRequestParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/CreateConnectionOAuthRequestParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/CreateConnectionOAuthRequestParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/CreateConnectionOAuthRequestParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
