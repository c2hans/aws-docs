---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConnectorAuthorizationCodeProperties.html
---

# ConnectorAuthorizationCodeProperties
<a name="API_ConnectorAuthorizationCodeProperties"></a>

OAuth2 authorization code configuration that defines the properties needed for the Authorization Code grant type flow.

## Contents
<a name="API_ConnectorAuthorizationCodeProperties_Contents"></a>

 ** AuthorizationCode **   <a name="Glue-Type-ConnectorAuthorizationCodeProperties-AuthorizationCode"></a>
The authorization code received from the authorization server after user consent.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** AuthorizationCodeUrl **   <a name="Glue-Type-ConnectorAuthorizationCodeProperties-AuthorizationCodeUrl"></a>
The authorization endpoint URL where users will be redirected to grant authorization.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** ClientId **   <a name="Glue-Type-ConnectorAuthorizationCodeProperties-ClientId"></a>
The OAuth2 client identifier provided by the authorization server.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** ClientSecret **   <a name="Glue-Type-ConnectorAuthorizationCodeProperties-ClientSecret"></a>
The OAuth2 client secret provided by the authorization server.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** ContentType **   <a name="Glue-Type-ConnectorAuthorizationCodeProperties-ContentType"></a>
The content type to use for token exchange requests, such as application/x-www-form-urlencoded or application/json.
Type: String
Valid Values: `APPLICATION_JSON | URL_ENCODED`
Required: No

 ** Prompt **   <a name="Glue-Type-ConnectorAuthorizationCodeProperties-Prompt"></a>
The OAuth2 prompt parameter that controls the authorization server's behavior during user authentication.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** RedirectUri **   <a name="Glue-Type-ConnectorAuthorizationCodeProperties-RedirectUri"></a>
The redirect URI that must match the URI registered with the authorization server.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** RequestMethod **   <a name="Glue-Type-ConnectorAuthorizationCodeProperties-RequestMethod"></a>
The HTTP method to use when making token exchange requests, typically POST.
Type: String
Valid Values: `GET | POST`
Required: No

 ** Scope **   <a name="Glue-Type-ConnectorAuthorizationCodeProperties-Scope"></a>
The OAuth2 scope that defines the level of access requested for the authorization code flow.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** TokenUrl **   <a name="Glue-Type-ConnectorAuthorizationCodeProperties-TokenUrl"></a>
The token endpoint URL where the authorization code will be exchanged for an access token.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** TokenUrlParameters **   <a name="Glue-Type-ConnectorAuthorizationCodeProperties-TokenUrlParameters"></a>
Additional parameters to include in token URL requests as key-value pairs.
Type: Array of [ConnectorProperty](API_ConnectorProperty.md) objects
Required: No

## See Also
<a name="API_ConnectorAuthorizationCodeProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConnectorAuthorizationCodeProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConnectorAuthorizationCodeProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConnectorAuthorizationCodeProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
