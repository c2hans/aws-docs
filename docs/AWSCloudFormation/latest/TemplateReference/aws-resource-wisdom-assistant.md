---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-assistant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::Assistant
<a name="aws-resource-wisdom-assistant"></a>

Specifies an Connect Customer Wisdom assistant.

## Syntax
<a name="aws-resource-wisdom-assistant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-assistant-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::Assistant",
  "Properties" : {
      "[Description](#cfn-wisdom-assistant-description)" : {{String}},
      "[Name](#cfn-wisdom-assistant-name)" : {{String}},
      "[ServerSideEncryptionConfiguration](#cfn-wisdom-assistant-serversideencryptionconfiguration)" : {{ServerSideEncryptionConfiguration}},
      "[Tags](#cfn-wisdom-assistant-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-wisdom-assistant-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-assistant-syntax.yaml"></a>

```
Type: AWS::Wisdom::Assistant
Properties:
  [Description](#cfn-wisdom-assistant-description): {{String}}
  [Name](#cfn-wisdom-assistant-name): {{String}}
  [ServerSideEncryptionConfiguration](#cfn-wisdom-assistant-serversideencryptionconfiguration): {{
    ServerSideEncryptionConfiguration}}
  [Tags](#cfn-wisdom-assistant-tags): {{
    - Tag}}
  [Type](#cfn-wisdom-assistant-type): {{String}}
```

## Properties
<a name="aws-resource-wisdom-assistant-properties"></a>

`Description`  <a name="cfn-wisdom-assistant-description"></a>
The description of the assistant.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-wisdom-assistant-name"></a>
The name of the assistant.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerSideEncryptionConfiguration`  <a name="cfn-wisdom-assistant-serversideencryptionconfiguration"></a>
The configuration information for the customer managed key used for encryption. The customer managed key must have a policy that allows `kms:CreateGrant` and `kms:DescribeKey` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow `kms:Decrypt`, `kms:GenerateDataKey*`, and `kms:DescribeKey` permissions to the `connect.amazonaws.com` service principal. For more information about setting up a customer managed key for Wisdom, see [Enable Connect Customer Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html).
*Required*: No
*Type*: [ServerSideEncryptionConfiguration](aws-properties-wisdom-assistant-serversideencryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-wisdom-assistant-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-wisdom-assistant-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-wisdom-assistant-type"></a>
The type of assistant.
*Required*: Yes
*Type*: String
*Allowed values*: `AGENT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-wisdom-assistant-return-values"></a>

### Ref
<a name="aws-resource-wisdom-assistant-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the assistant ID.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-wisdom-assistant-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-wisdom-assistant-return-values-fn--getatt-fn--getatt"></a>

`AssistantArn`  <a name="AssistantArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the assistant.

`AssistantId`  <a name="AssistantId-fn::getatt"></a>
The ID of the Wisdom assistant.
