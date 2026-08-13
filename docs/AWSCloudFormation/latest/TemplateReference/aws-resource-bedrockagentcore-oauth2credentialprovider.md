---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-oauth2credentialprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider
<a name="aws-resource-bedrockagentcore-oauth2credentialprovider"></a>

Specifies an OAuth2 credential provider for Amazon Bedrock AgentCore. An OAuth2 credential provider manages OAuth2 client credentials, authorization codes, or token exchange flows that agents use to authenticate with external services through AgentCore Gateway.

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-oauth2credentialprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-oauth2credentialprovider-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::OAuth2CredentialProvider",
  "Properties" : {
      "[CredentialProviderVendor](#cfn-bedrockagentcore-oauth2credentialprovider-credentialprovidervendor)" : {{String}},
      "[Name](#cfn-bedrockagentcore-oauth2credentialprovider-name)" : {{String}},
      "[Oauth2ProviderConfigInput](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput)" : {{Oauth2ProviderConfigInput}},
      "[Tags](#cfn-bedrockagentcore-oauth2credentialprovider-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-oauth2credentialprovider-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::OAuth2CredentialProvider
Properties:
  [CredentialProviderVendor](#cfn-bedrockagentcore-oauth2credentialprovider-credentialprovidervendor): {{String}}
  [Name](#cfn-bedrockagentcore-oauth2credentialprovider-name): {{String}}
  [Oauth2ProviderConfigInput](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput): {{
    Oauth2ProviderConfigInput}}
  [Tags](#cfn-bedrockagentcore-oauth2credentialprovider-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrockagentcore-oauth2credentialprovider-properties"></a>

`CredentialProviderVendor`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-credentialprovidervendor"></a>
The vendor of the OAuth2 credential provider. This specifies which OAuth2 implementation to use.
*Required*: Yes
*Type*: String
*Allowed values*: `GoogleOauth2 | GithubOauth2 | SlackOauth2 | SalesforceOauth2 | MicrosoftOauth2 | CustomOauth2 | AtlassianOauth2 | LinkedinOauth2 | XOauth2 | OktaOauth2 | OneLoginOauth2 | PingOneOauth2 | FacebookOauth2 | YandexOauth2 | RedditOauth2 | ZoomOauth2 | TwitchOauth2 | SpotifyOauth2 | DropboxOauth2 | NotionOauth2 | HubspotOauth2 | CyberArkOauth2 | FusionAuthOauth2 | Auth0Oauth2 | CognitoOauth2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-name"></a>
The name of the OAuth2 credential provider. The name must be unique within your account.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-_]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Oauth2ProviderConfigInput`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput"></a>
Contains the input configuration for an OAuth2 provider.
*Required*: No
*Type*: [Oauth2ProviderConfigInput](aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-tags"></a>
A map of tag keys and values to assign to the OAuth2 credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-oauth2credentialprovider-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-oauth2credentialprovider-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-oauth2credentialprovider-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-oauth2credentialprovider-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-oauth2credentialprovider-return-values-fn--getatt-fn--getatt"></a>

`CallbackUrl`  <a name="CallbackUrl-fn::getatt"></a>
Property description not available.

`ClientSecretJsonKey`  <a name="ClientSecretJsonKey-fn::getatt"></a>
Property description not available.

`ClientSecretSource`  <a name="ClientSecretSource-fn::getatt"></a>
Property description not available.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
Property description not available.

`CredentialProviderArn`  <a name="CredentialProviderArn-fn::getatt"></a>
Property description not available.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.
