---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-paymentcredentialprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider
<a name="aws-resource-bedrockagentcore-paymentcredentialprovider"></a>

Specifies a payment credential provider for Amazon Bedrock AgentCore. A payment credential provider stores and manages credentials for third-party payment vendors used by AI agents. Credentials are encrypted and stored in AWS Secrets Manager.

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-paymentcredentialprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-paymentcredentialprovider-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::PaymentCredentialProvider",
  "Properties" : {
      "[CredentialProviderVendor](#cfn-bedrockagentcore-paymentcredentialprovider-credentialprovidervendor)" : {{String}},
      "[Name](#cfn-bedrockagentcore-paymentcredentialprovider-name)" : {{String}},
      "[ProviderConfigurationInput](#cfn-bedrockagentcore-paymentcredentialprovider-providerconfigurationinput)" : {{PaymentProviderConfigurationInput}},
      "[Tags](#cfn-bedrockagentcore-paymentcredentialprovider-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-paymentcredentialprovider-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::PaymentCredentialProvider
Properties:
  [CredentialProviderVendor](#cfn-bedrockagentcore-paymentcredentialprovider-credentialprovidervendor): {{String}}
  [Name](#cfn-bedrockagentcore-paymentcredentialprovider-name): {{String}}
  [ProviderConfigurationInput](#cfn-bedrockagentcore-paymentcredentialprovider-providerconfigurationinput): {{
    PaymentProviderConfigurationInput}}
  [Tags](#cfn-bedrockagentcore-paymentcredentialprovider-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrockagentcore-paymentcredentialprovider-properties"></a>

`CredentialProviderVendor`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-credentialprovidervendor"></a>
The payment vendor for the credential provider. Valid values are `CoinbaseCDP`.
*Required*: Yes
*Type*: String
*Allowed values*: `CoinbaseCDP | StripePrivy`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-name"></a>
A unique name for the payment credential provider.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-_]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProviderConfigurationInput`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-providerconfigurationinput"></a>
The vendor-specific configuration input, containing API credentials that are stored as secrets in AWS Secrets Manager. This property is write-only and isn't returned on read.
*Required*: No
*Type*: [PaymentProviderConfigurationInput](aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-tags"></a>
The tags for the payment credential provider.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-paymentcredentialprovider-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-paymentcredentialprovider-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-paymentcredentialprovider-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the payment credential provider. For example:

 `arn:aws:bedrock-agentcore:us-east-1:123456789012:token-vault/default/paymentcredentialprovider/MyProvider`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-paymentcredentialprovider-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-paymentcredentialprovider-return-values-fn--getatt-fn--getatt"></a>

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The timestamp when the payment credential provider was created.

`CredentialProviderArn`  <a name="CredentialProviderArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the payment credential provider.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The timestamp when the payment credential provider was last updated.
