---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_PardotConnectorProfileCredentials.html
---

# PardotConnectorProfileCredentials
<a name="API_PardotConnectorProfileCredentials"></a>

The connector-specific profile credentials required when using Salesforce Pardot.

## Contents
<a name="API_PardotConnectorProfileCredentials_Contents"></a>

 ** accessToken **   <a name="appflow-Type-PardotConnectorProfileCredentials-accessToken"></a>
The credentials used to access protected Salesforce Pardot resources.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `\S+`
Required: No

 ** clientCredentialsArn **   <a name="appflow-Type-PardotConnectorProfileCredentials-clientCredentialsArn"></a>
The secret manager ARN, which contains the client ID and client secret of the connected app.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:secretsmanager:.*:[0-9]+:.*`
Required: No

 ** oAuthRequest **   <a name="appflow-Type-PardotConnectorProfileCredentials-oAuthRequest"></a>
 Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.
Type: [ConnectorOAuthRequest](API_ConnectorOAuthRequest.md) object
Required: No

 ** refreshToken **   <a name="appflow-Type-PardotConnectorProfileCredentials-refreshToken"></a>
The credentials used to acquire new access tokens.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `\S+`
Required: No

## See Also
<a name="API_PardotConnectorProfileCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/PardotConnectorProfileCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/PardotConnectorProfileCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/PardotConnectorProfileCredentials)
