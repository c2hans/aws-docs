---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider Oauth2ProviderConfigOutput
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput"></a>

Contains the output configuration for an OAuth2 provider.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-syntax.json"></a>

```
{
  "[ClientAuthenticationMethod](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-clientauthenticationmethod)" : {{String}},
  "[ClientId](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-clientid)" : {{String}},
  "[OauthDiscovery](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-oauthdiscovery)" : {{Oauth2Discovery}},
  "[OnBehalfOfTokenExchangeConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-onbehalfoftokenexchangeconfig)" : {{OnBehalfOfTokenExchangeConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-syntax.yaml"></a>

```
  [ClientAuthenticationMethod](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-clientauthenticationmethod): {{String}}
  [ClientId](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-clientid): {{String}}
  [OauthDiscovery](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-oauthdiscovery): {{
    Oauth2Discovery}}
  [OnBehalfOfTokenExchangeConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-onbehalfoftokenexchangeconfig): {{
    OnBehalfOfTokenExchangeConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-properties"></a>

`ClientAuthenticationMethod`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-clientauthenticationmethod"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `CLIENT_SECRET_BASIC | CLIENT_SECRET_POST | AWS_IAM_ID_TOKEN_JWT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-clientid"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OauthDiscovery`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-oauthdiscovery"></a>
Property description not available.
*Required*: No
*Type*: [Oauth2Discovery](aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2discovery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnBehalfOfTokenExchangeConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfigoutput-onbehalfoftokenexchangeconfig"></a>
Property description not available.
*Required*: No
*Type*: [OnBehalfOfTokenExchangeConfig](aws-properties-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
