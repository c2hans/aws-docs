---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-apikeycredentialprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ApiKeyCredentialProvider
<a name="aws-resource-bedrockagentcore-apikeycredentialprovider"></a>

Specifies an API key credential provider for Amazon Bedrock AgentCore. An API key credential provider stores and manages API keys that agents use to authenticate with external services and third-party APIs through AgentCore Gateway.

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-apikeycredentialprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-apikeycredentialprovider-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::ApiKeyCredentialProvider",
  "Properties" : {
      "[ApiKey](#cfn-bedrockagentcore-apikeycredentialprovider-apikey)" : {{String}},
      "[ApiKeySecretConfig](#cfn-bedrockagentcore-apikeycredentialprovider-apikeysecretconfig)" : {{SecretReference}},
      "[ApiKeySecretSource](#cfn-bedrockagentcore-apikeycredentialprovider-apikeysecretsource)" : {{String}},
      "[Name](#cfn-bedrockagentcore-apikeycredentialprovider-name)" : {{String}},
      "[Tags](#cfn-bedrockagentcore-apikeycredentialprovider-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-apikeycredentialprovider-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::ApiKeyCredentialProvider
Properties:
  [ApiKey](#cfn-bedrockagentcore-apikeycredentialprovider-apikey): {{String}}
  [ApiKeySecretConfig](#cfn-bedrockagentcore-apikeycredentialprovider-apikeysecretconfig): {{
    SecretReference}}
  [ApiKeySecretSource](#cfn-bedrockagentcore-apikeycredentialprovider-apikeysecretsource): {{String}}
  [Name](#cfn-bedrockagentcore-apikeycredentialprovider-name): {{String}}
  [Tags](#cfn-bedrockagentcore-apikeycredentialprovider-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrockagentcore-apikeycredentialprovider-properties"></a>

`ApiKey`  <a name="cfn-bedrockagentcore-apikeycredentialprovider-apikey"></a>
The API key to use for authentication. This value is encrypted and stored securely.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `65536`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeySecretConfig`  <a name="cfn-bedrockagentcore-apikeycredentialprovider-apikeysecretconfig"></a>
Property description not available.
*Required*: No
*Type*: [SecretReference](aws-properties-bedrockagentcore-apikeycredentialprovider-secretreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeySecretSource`  <a name="cfn-bedrockagentcore-apikeycredentialprovider-apikeysecretsource"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-apikeycredentialprovider-name"></a>
The name of the API key credential provider.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-_]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrockagentcore-apikeycredentialprovider-tags"></a>
A map of tag keys and values to assign to the API key credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-apikeycredentialprovider-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-apikeycredentialprovider-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-apikeycredentialprovider-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-apikeycredentialprovider-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-apikeycredentialprovider-return-values-fn--getatt-fn--getatt"></a>

`ApiKeySecretJsonKey`  <a name="ApiKeySecretJsonKey-fn::getatt"></a>
Property description not available.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The timestamp when the API key credential provider was created.

`CredentialProviderArn`  <a name="CredentialProviderArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the API key credential provider.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The timestamp when the API key credential provider was last updated.
