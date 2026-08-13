---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget OAuthCredentialProvider
<a name="aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider"></a>

An OAuth credential provider for gateway authentication. This structure contains the configuration for authenticating with the target endpoint using OAuth.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider-syntax.json"></a>

```
{
  "[CustomParameters](#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-customparameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[DefaultReturnUrl](#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-defaultreturnurl)" : {{String}},
  "[GrantType](#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-granttype)" : {{}},
  "[ProviderArn](#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-providerarn)" : {{String}},
  "[Scopes](#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-scopes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider-syntax.yaml"></a>

```
  [CustomParameters](#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-customparameters): {{
    {{Key}}: {{Value}}}}
  [DefaultReturnUrl](#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-defaultreturnurl): {{String}}
  [GrantType](#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-granttype): {{
    }}
  [ProviderArn](#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-providerarn): {{String}}
  [Scopes](#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-scopes): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider-properties"></a>

`CustomParameters`  <a name="cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-customparameters"></a>
The custom parameters for the OAuth credential provider. These parameters provide additional configuration for the OAuth authentication process.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultReturnUrl`  <a name="cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-defaultreturnurl"></a>
The URL where the end user's browser is redirected after obtaining the authorization code. Generally points to the customer's application.
*Required*: No
*Type*: String
*Pattern*: `^\w+:(\/?\/?)[^\s]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GrantType`  <a name="cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-granttype"></a>
Specifies the kind of credentials to use for authorization:
+ `CLIENT_CREDENTIALS` - Authorization with a client ID and secret.
+ `AUTHORIZATION_CODE` - Authorization with a token that is specific to an individual end user.
*Required*: No
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderArn`  <a name="cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-providerarn"></a>
The Amazon Resource Name (ARN) of the OAuth credential provider. This ARN identifies the provider in AWS.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:([^:]*):([^:]*):([^:]*):([0-9]{12})?:(.+)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scopes`  <a name="cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-scopes"></a>
The OAuth scopes for the credential provider. These scopes define the level of access requested from the OAuth provider.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
