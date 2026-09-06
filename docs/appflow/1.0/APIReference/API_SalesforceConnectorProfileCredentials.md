---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SalesforceConnectorProfileCredentials.html
---

# SalesforceConnectorProfileCredentials
<a name="API_SalesforceConnectorProfileCredentials"></a>

 The connector-specific profile credentials required when using Salesforce.

## Contents
<a name="API_SalesforceConnectorProfileCredentials_Contents"></a>

 ** accessToken **   <a name="appflow-Type-SalesforceConnectorProfileCredentials-accessToken"></a>
 The credentials used to access protected Salesforce resources.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `\S+`
Required: No

 ** clientCredentialsArn **   <a name="appflow-Type-SalesforceConnectorProfileCredentials-clientCredentialsArn"></a>
 The secret manager ARN, which contains the client ID and client secret of the connected app.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:secretsmanager:.*:[0-9]+:.*`
Required: No

 ** jwtToken **   <a name="appflow-Type-SalesforceConnectorProfileCredentials-jwtToken"></a>
A JSON web token (JWT) that authorizes Amazon AppFlow to access your Salesforce records.
Type: String
Length Constraints: Maximum length of 8000.
Pattern: `^([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_\-\+\/=]*)`
Required: No

 ** oAuth2GrantType **   <a name="appflow-Type-SalesforceConnectorProfileCredentials-oAuth2GrantType"></a>
Specifies the OAuth 2.0 grant type that Amazon AppFlow uses when it requests an access token from Salesforce. Amazon AppFlow requires an access token each time it attempts to access your Salesforce records.
You can specify one of the following values:
AUTHORIZATION\_CODE
Amazon AppFlow passes an authorization code when it requests the access token from Salesforce. Amazon AppFlow receives the authorization code from Salesforce after you log in to your Salesforce account and authorize Amazon AppFlow to access your records.
JWT\_BEARER
Amazon AppFlow passes a JSON web token (JWT) when it requests the access token from Salesforce. You provide the JWT to Amazon AppFlow when you define the connection to your Salesforce account. When you use this grant type, you don't need to log in to your Salesforce account to authorize Amazon AppFlow to access your records.
The CLIENT\_CREDENTIALS value is not supported for Salesforce.
Type: String
Valid Values: `CLIENT_CREDENTIALS | AUTHORIZATION_CODE | JWT_BEARER`
Required: No

 ** oAuthRequest **   <a name="appflow-Type-SalesforceConnectorProfileCredentials-oAuthRequest"></a>
 The OAuth requirement needed to request security tokens from the connector endpoint.
Type: [ConnectorOAuthRequest](API_ConnectorOAuthRequest.md) object
Required: No

 ** refreshToken **   <a name="appflow-Type-SalesforceConnectorProfileCredentials-refreshToken"></a>
 The credentials used to acquire new access tokens.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `\S+`
Required: No

## See Also
<a name="API_SalesforceConnectorProfileCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/SalesforceConnectorProfileCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/SalesforceConnectorProfileCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/SalesforceConnectorProfileCredentials)
