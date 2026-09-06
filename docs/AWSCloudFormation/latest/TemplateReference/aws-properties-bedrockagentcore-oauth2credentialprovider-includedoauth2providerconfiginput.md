---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider IncludedOauth2ProviderConfigInput
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput"></a>

Configuration settings for connecting to a supported OAuth2 provider. This includes client credentials and OAuth2 discovery information for providers that have built-in support.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-syntax.json"></a>

```
{
  "[AuthorizationEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-authorizationendpoint)" : {{String}},
  "[ClientId](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientid)" : {{String}},
  "[ClientSecret](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientsecret)" : {{String}},
  "[ClientSecretConfig](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientsecretconfig)" : {{SecretReference}},
  "[ClientSecretSource](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientsecretsource)" : {{String}},
  "[Issuer](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-issuer)" : {{String}},
  "[TokenEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-tokenendpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-syntax.yaml"></a>

```
  [AuthorizationEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-authorizationendpoint): {{String}}
  [ClientId](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientid): {{String}}
  [ClientSecret](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientsecret): {{String}}
  [ClientSecretConfig](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientsecretconfig): {{
    SecretReference}}
  [ClientSecretSource](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientsecretsource): {{String}}
  [Issuer](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-issuer): {{String}}
  [TokenEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-tokenendpoint): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-properties"></a>

`AuthorizationEndpoint`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-authorizationendpoint"></a>
OAuth2 authorization endpoint for your isolated OAuth2 application tenant. This is where users are redirected to authenticate and authorize access to their resources.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientid"></a>
The client ID for the supported OAuth2 provider. This identifier is assigned by the OAuth2 provider when you register your application.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientsecret"></a>
The client secret for the supported OAuth2 provider. This secret is assigned by the OAuth2 provider and used along with the client ID to authenticate your application.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecretConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientsecretconfig"></a>
A reference to the AWS Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL`.
*Required*: No
*Type*: [SecretReference](aws-properties-bedrockagentcore-oauth2credentialprovider-secretreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecretSource`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-clientsecretsource"></a>
The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-issuer"></a>
Token issuer of your isolated OAuth2 application tenant. This URL identifies the authorization server that issues tokens for this provider.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenEndpoint`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput-tokenendpoint"></a>
OAuth2 token endpoint for your isolated OAuth2 application tenant. This is where authorization codes are exchanged for access tokens.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
