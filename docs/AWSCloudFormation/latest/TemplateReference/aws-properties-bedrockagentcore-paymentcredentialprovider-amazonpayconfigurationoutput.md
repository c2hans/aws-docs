---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider AmazonPayConfigurationOutput

<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-description"></a>The `AmazonPayConfigurationOutput` property type specifies Property description not available. for an [AWS::BedrockAgentCore::PaymentCredentialProvider](aws-resource-bedrockagentcore-paymentcredentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-syntax.json"></a>

```json
{
  "[AmazonPayRegion](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-amazonpayregion)" : {{String}},
  "[AuthorizationTokenArn](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-authorizationtokenarn)" : {{SecretInfo}},
  "[AuthorizationTokenJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-authorizationtokenjsonkey)" : {{String}},
  "[AuthorizationTokenSource](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-authorizationtokensource)" : {{String}},
  "[Environment](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-environment)" : {{String}},
  "[MerchantId](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-merchantid)" : {{String}},
  "[StoreId](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-storeid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-syntax.yaml"></a>

```yaml
  [AmazonPayRegion](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-amazonpayregion): {{String}}
  [AuthorizationTokenArn](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-authorizationtokenarn): {{
    SecretInfo}}
  [AuthorizationTokenJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-authorizationtokenjsonkey): {{String}}
  [AuthorizationTokenSource](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-authorizationtokensource): {{String}}
  [Environment](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-environment): {{String}}
  [MerchantId](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-merchantid): {{String}}
  [StoreId](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-storeid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-properties"></a>

`AmazonPayRegion`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-amazonpayregion"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `NA | EU | JP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationTokenArn`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-authorizationtokenarn"></a>
Property description not available.
*Required*: Yes
*Type*: [SecretInfo](aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationTokenJsonKey`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-authorizationtokenjsonkey"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationTokenSource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-authorizationtokensource"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-environment"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `LIVE | SANDBOX`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MerchantId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-merchantid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StoreId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput-storeid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
