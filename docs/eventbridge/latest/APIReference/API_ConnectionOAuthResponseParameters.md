---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ConnectionOAuthResponseParameters.html
---

# ConnectionOAuthResponseParameters
<a name="API_ConnectionOAuthResponseParameters"></a>

The response parameters when OAuth is specified as the authorization type.

## Contents
<a name="API_ConnectionOAuthResponseParameters_Contents"></a>

 ** AuthorizationEndpoint **   <a name="eventbridge-Type-ConnectionOAuthResponseParameters-AuthorizationEndpoint"></a>
The URL to the HTTP endpoint that authorized the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^((%[0-9A-Fa-f]{2}|[-()_.!~*';/?:@\x26=+$,A-Za-z0-9])+)([).!';/?:,])?$`
Required: No

 ** ClientParameters **   <a name="eventbridge-Type-ConnectionOAuthResponseParameters-ClientParameters"></a>
Details about the client parameters returned when OAuth is specified as the authorization type.
Type: [ConnectionOAuthClientResponseParameters](API_ConnectionOAuthClientResponseParameters.md) object
Required: No

 ** HttpMethod **   <a name="eventbridge-Type-ConnectionOAuthResponseParameters-HttpMethod"></a>
The method used to connect to the HTTP endpoint.
Type: String
Valid Values: `GET | POST | PUT`
Required: No

 ** OAuthHttpParameters **   <a name="eventbridge-Type-ConnectionOAuthResponseParameters-OAuthHttpParameters"></a>
The additional HTTP parameters used for the OAuth authorization request.
Type: [ConnectionHttpParameters](API_ConnectionHttpParameters.md) object
Required: No

## See Also
<a name="API_ConnectionOAuthResponseParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ConnectionOAuthResponseParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ConnectionOAuthResponseParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ConnectionOAuthResponseParameters)
