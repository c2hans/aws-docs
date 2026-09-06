---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider GithubOauth2ProviderConfigInput
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput"></a>

Input configuration for a GitHub OAuth2 provider.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-syntax.json"></a>

```
{
  "[ClientId](#cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientid)" : {{String}},
  "[ClientSecret](#cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientsecret)" : {{String}},
  "[ClientSecretConfig](#cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientsecretconfig)" : {{SecretReference}},
  "[ClientSecretSource](#cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientsecretsource)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-syntax.yaml"></a>

```
  [ClientId](#cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientid): {{String}}
  [ClientSecret](#cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientsecret): {{String}}
  [ClientSecretConfig](#cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientsecretconfig): {{
    SecretReference}}
  [ClientSecretSource](#cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientsecretsource): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-properties"></a>

`ClientId`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientid"></a>
The client ID for the GitHub OAuth2 provider.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientsecret"></a>
The client secret for the GitHub OAuth2 provider.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecretConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientsecretconfig"></a>
A reference to the AWS Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL`.
*Required*: No
*Type*: [SecretReference](aws-properties-bedrockagentcore-oauth2credentialprovider-secretreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecretSource`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput-clientsecretsource"></a>
The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
