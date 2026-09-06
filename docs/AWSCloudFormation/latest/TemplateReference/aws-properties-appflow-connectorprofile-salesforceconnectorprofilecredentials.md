---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile SalesforceConnectorProfileCredentials
<a name="aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials"></a>

 The connector-specific profile credentials required when using Salesforce.

## Syntax
<a name="aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials-syntax.json"></a>

```
{
  "[AccessToken](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-accesstoken)" : {{String}},
  "[ClientCredentialsArn](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-clientcredentialsarn)" : {{String}},
  "[ConnectorOAuthRequest](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-connectoroauthrequest)" : {{ConnectorOAuthRequest}},
  "[JwtToken](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-jwttoken)" : {{String}},
  "[OAuth2GrantType](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-oauth2granttype)" : {{String}},
  "[RefreshToken](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-refreshtoken)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials-syntax.yaml"></a>

```
  [AccessToken](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-accesstoken): {{String}}
  [ClientCredentialsArn](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-clientcredentialsarn): {{String}}
  [ConnectorOAuthRequest](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-connectoroauthrequest): {{
    ConnectorOAuthRequest}}
  [JwtToken](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-jwttoken): {{String}}
  [OAuth2GrantType](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-oauth2granttype): {{String}}
  [RefreshToken](#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-refreshtoken): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials-properties"></a>

`AccessToken`  <a name="cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-accesstoken"></a>
 The credentials used to access protected Salesforce resources.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientCredentialsArn`  <a name="cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-clientcredentialsarn"></a>
 The secret manager ARN, which contains the client ID and client secret of the connected app.
*Required*: No
*Type*: String
*Pattern*: `arn:aws:secretsmanager:.*:[0-9]+:.*`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectorOAuthRequest`  <a name="cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-connectoroauthrequest"></a>
 Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.
*Required*: No
*Type*: [ConnectorOAuthRequest](aws-properties-appflow-connectorprofile-connectoroauthrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JwtToken`  <a name="cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-jwttoken"></a>
A JSON web token (JWT) that authorizes Amazon AppFlow to access your Salesforce records.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.[A-Za-z0-9-_.+/=]*$`
*Maximum*: `8000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2GrantType`  <a name="cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-oauth2granttype"></a>
Specifies the OAuth 2.0 grant type that Amazon AppFlow uses when it requests an access token from Salesforce. Amazon AppFlow requires an access token each time it attempts to access your Salesforce records.
You can specify one of the following values:
AUTHORIZATION\_CODE
Amazon AppFlow passes an authorization code when it requests the access token from Salesforce. Amazon AppFlow receives the authorization code from Salesforce after you log in to your Salesforce account and authorize Amazon AppFlow to access your records.
JWT\_BEARER
Amazon AppFlow passes a JSON web token (JWT) when it requests the access token from Salesforce. You provide the JWT to Amazon AppFlow when you define the connection to your Salesforce account. When you use this grant type, you don't need to log in to your Salesforce account to authorize Amazon AppFlow to access your records.
The CLIENT\_CREDENTIALS value is not supported for Salesforce.
*Required*: No
*Type*: String
*Allowed values*: `CLIENT_CREDENTIALS | AUTHORIZATION_CODE | JWT_BEARER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshToken`  <a name="cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-refreshtoken"></a>
 The credentials used to acquire new access tokens.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials--seealso"></a>
+ [SalesforceConnectorProfileCredentials](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SalesforceConnectorProfileCredentials.html) in the *Amazon AppFlow API Reference*.
