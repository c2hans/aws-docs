---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-paymentmanager.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentManager
<a name="aws-resource-bedrockagentcore-paymentmanager"></a>

Specifies a payment manager for Amazon Bedrock AgentCore. A payment manager configures authorization and AWS Identity and Access Management (IAM) role settings that govern payment operations performed by AI agents, including inbound request authentication through JSON Web Token (JWT) or IAM-based authorizers.

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-paymentmanager-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-paymentmanager-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::PaymentManager",
  "Properties" : {
      "[AuthorizerConfiguration](#cfn-bedrockagentcore-paymentmanager-authorizerconfiguration)" : {{AuthorizerConfiguration}},
      "[AuthorizerType](#cfn-bedrockagentcore-paymentmanager-authorizertype)" : {{String}},
      "[Description](#cfn-bedrockagentcore-paymentmanager-description)" : {{String}},
      "[Name](#cfn-bedrockagentcore-paymentmanager-name)" : {{String}},
      "[RoleArn](#cfn-bedrockagentcore-paymentmanager-rolearn)" : {{String}},
      "[Tags](#cfn-bedrockagentcore-paymentmanager-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-paymentmanager-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::PaymentManager
Properties:
  [AuthorizerConfiguration](#cfn-bedrockagentcore-paymentmanager-authorizerconfiguration): {{
    AuthorizerConfiguration}}
  [AuthorizerType](#cfn-bedrockagentcore-paymentmanager-authorizertype): {{String}}
  [Description](#cfn-bedrockagentcore-paymentmanager-description): {{String}}
  [Name](#cfn-bedrockagentcore-paymentmanager-name): {{String}}
  [RoleArn](#cfn-bedrockagentcore-paymentmanager-rolearn): {{String}}
  [Tags](#cfn-bedrockagentcore-paymentmanager-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrockagentcore-paymentmanager-properties"></a>

`AuthorizerConfiguration`  <a name="cfn-bedrockagentcore-paymentmanager-authorizerconfiguration"></a>
Represents inbound authorization configuration options used to authenticate incoming requests.
*Required*: No
*Type*: [AuthorizerConfiguration](aws-properties-bedrockagentcore-paymentmanager-authorizerconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuthorizerType`  <a name="cfn-bedrockagentcore-paymentmanager-authorizertype"></a>
The type of authorizer used to authenticate inbound requests to the payment manager. Valid values are `CUSTOM_JWT` and `AWS_IAM`.
*Required*: Yes
*Type*: String
*Allowed values*: `CUSTOM_JWT | AWS_IAM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-bedrockagentcore-paymentmanager-description"></a>
A description of the payment manager.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s]+$`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-paymentmanager-name"></a>
The name of the payment manager.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9]{0,47}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-bedrockagentcore-paymentmanager-rolearn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that the payment manager assumes to perform operations on your behalf.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrockagentcore-paymentmanager-tags"></a>
The tags for the payment manager.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-paymentmanager-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-paymentmanager-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-paymentmanager-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the payment manager. For example:

 `arn:aws:bedrock-agentcore:us-east-1:123456789012:payment-manager/MyPaymentManager-a1b2c3d4e5`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-paymentmanager-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-paymentmanager-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the payment manager was created.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp when the payment manager was last updated.

`PaymentManagerArn`  <a name="PaymentManagerArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the payment manager.

`PaymentManagerId`  <a name="PaymentManagerId-fn::getatt"></a>
The unique identifier of the payment manager.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the payment manager.
