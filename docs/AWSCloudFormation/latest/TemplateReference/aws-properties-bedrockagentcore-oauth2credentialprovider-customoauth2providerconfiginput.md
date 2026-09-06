---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider CustomOauth2ProviderConfigInput
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput"></a>

Input configuration for a custom OAuth2 provider.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-syntax.json"></a>

```
{
  "[ClientAuthenticationMethod](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientauthenticationmethod)" : {{String}},
  "[ClientId](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientid)" : {{String}},
  "[ClientSecret](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientsecret)" : {{String}},
  "[ClientSecretConfig](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientsecretconfig)" : {{SecretReference}},
  "[ClientSecretSource](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientsecretsource)" : {{String}},
  "[OauthDiscovery](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-oauthdiscovery)" : {{Oauth2Discovery}},
  "[OnBehalfOfTokenExchangeConfig](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-onbehalfoftokenexchangeconfig)" : {{OnBehalfOfTokenExchangeConfig}},
  "[PrivateEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-privateendpoint)" : {{PrivateEndpoint}},
  "[PrivateEndpointOverrides](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-privateendpointoverrides)" : {{[ PrivateEndpointOverride, ... ]}},
  "[PrivateKeyJwtConfig](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-privatekeyjwtconfig)" : {{PrivateKeyJwtConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-syntax.yaml"></a>

```
  [ClientAuthenticationMethod](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientauthenticationmethod): {{String}}
  [ClientId](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientid): {{String}}
  [ClientSecret](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientsecret): {{String}}
  [ClientSecretConfig](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientsecretconfig): {{
    SecretReference}}
  [ClientSecretSource](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientsecretsource): {{String}}
  [OauthDiscovery](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-oauthdiscovery): {{
    Oauth2Discovery}}
  [OnBehalfOfTokenExchangeConfig](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-onbehalfoftokenexchangeconfig): {{
    OnBehalfOfTokenExchangeConfig}}
  [PrivateEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-privateendpoint): {{
    PrivateEndpoint}}
  [PrivateEndpointOverrides](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-privateendpointoverrides): {{
    - PrivateEndpointOverride}}
  [PrivateKeyJwtConfig](#cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-privatekeyjwtconfig): {{
    PrivateKeyJwtConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-properties"></a>

`ClientAuthenticationMethod`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientauthenticationmethod"></a>
The client authentication method to use when authenticating with the token endpoint.
*Required*: No
*Type*: String
*Allowed values*: `CLIENT_SECRET_BASIC | CLIENT_SECRET_POST | AWS_IAM_ID_TOKEN_JWT | PRIVATE_KEY_JWT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientid"></a>
The client ID for the custom OAuth2 provider.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientsecret"></a>
The client secret for the custom OAuth2 provider.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecretConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientsecretconfig"></a>
A reference to the AWS Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL`.
*Required*: No
*Type*: [SecretReference](aws-properties-bedrockagentcore-oauth2credentialprovider-secretreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecretSource`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-clientsecretsource"></a>
The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OauthDiscovery`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-oauthdiscovery"></a>
The OAuth2 discovery information for the custom provider.
*Required*: Yes
*Type*: [Oauth2Discovery](aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2discovery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnBehalfOfTokenExchangeConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-onbehalfoftokenexchangeconfig"></a>
The configuration for on-behalf-of token exchange. This enables authentication flows that use RFC 8693 token exchange or RFC 7523 JWT authorization grants.
*Required*: No
*Type*: [OnBehalfOfTokenExchangeConfig](aws-properties-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateEndpoint`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-privateendpoint"></a>
The default private endpoint for the custom OAuth2 provider, enabling secure connectivity through a VPC Lattice resource configuration.
*Required*: No
*Type*: [PrivateEndpoint](aws-properties-bedrockagentcore-oauth2credentialprovider-privateendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateEndpointOverrides`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-privateendpointoverrides"></a>
The private endpoint overrides for the custom OAuth2 provider configuration.
*Required*: No
*Type*: Array of [PrivateEndpointOverride](aws-properties-bedrockagentcore-oauth2credentialprovider-privateendpointoverride.md)
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateKeyJwtConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput-privatekeyjwtconfig"></a>
The private\_key\_jwt client authentication configuration for this credential provider. When specified, the credential provider uses JWT client assertions to authenticate with the token endpoint.
*Required*: No
*Type*: [PrivateKeyJwtConfig](aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
