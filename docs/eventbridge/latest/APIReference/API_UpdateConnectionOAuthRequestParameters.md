---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateConnectionOAuthRequestParameters.html
---

# UpdateConnectionOAuthRequestParameters
<a name="API_UpdateConnectionOAuthRequestParameters"></a>

The OAuth request parameters to use for the connection.

## Contents
<a name="API_UpdateConnectionOAuthRequestParameters_Contents"></a>

 ** AuthorizationEndpoint **   <a name="eventbridge-Type-UpdateConnectionOAuthRequestParameters-AuthorizationEndpoint"></a>
The URL to the authorization endpoint when OAuth is specified as the authorization type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^((%[0-9A-Fa-f]{2}|[-()_.!~*';/?:@\x26=+$,A-Za-z0-9])+)([).!';/?:,])?$`
Required: No

 ** ClientParameters **   <a name="eventbridge-Type-UpdateConnectionOAuthRequestParameters-ClientParameters"></a>
The client parameters to use for the connection when OAuth is specified as the authorization type.
Type: [UpdateConnectionOAuthClientRequestParameters](API_UpdateConnectionOAuthClientRequestParameters.md) object
Required: No

 ** HttpMethod **   <a name="eventbridge-Type-UpdateConnectionOAuthRequestParameters-HttpMethod"></a>
The method used to connect to the HTTP endpoint.
Type: String
Valid Values: `GET | POST | PUT`
Required: No

 ** OAuthHttpParameters **   <a name="eventbridge-Type-UpdateConnectionOAuthRequestParameters-OAuthHttpParameters"></a>
The additional HTTP parameters used for the OAuth authorization request.
Type: [ConnectionHttpParameters](API_ConnectionHttpParameters.md) object
Required: No

## See Also
<a name="API_UpdateConnectionOAuthRequestParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/UpdateConnectionOAuthRequestParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/UpdateConnectionOAuthRequestParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/UpdateConnectionOAuthRequestParameters)
