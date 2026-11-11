---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-space.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Space
<a name="aws-resource-cloudwatch-space"></a>

Resource Type definition for `AWS::CloudWatch::Space`. A space is where you work in CloudWatch Omni. It gives you access to telemetry from the account and Region in which the space is hosted, and controls who can see it.

## Syntax
<a name="aws-resource-cloudwatch-space-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-space-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::Space",
  "Properties" : {
      "[AgentCoreEvaluationRoleArn](#cfn-cloudwatch-space-agentcoreevaluationrolearn)" : {{String}},
      "[DataAccessRoleArn](#cfn-cloudwatch-space-dataaccessrolearn)" : {{String}},
      "[DomainId](#cfn-cloudwatch-space-domainid)" : {{String}},
      "[EncryptionConfiguration](#cfn-cloudwatch-space-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[Name](#cfn-cloudwatch-space-name)" : {{String}},
      "[Tags](#cfn-cloudwatch-space-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-space-syntax.yaml"></a>

```
Type: AWS::CloudWatch::Space
Properties:
  [AgentCoreEvaluationRoleArn](#cfn-cloudwatch-space-agentcoreevaluationrolearn): {{String}}
  [DataAccessRoleArn](#cfn-cloudwatch-space-dataaccessrolearn): {{String}}
  [DomainId](#cfn-cloudwatch-space-domainid): {{String}}
  [EncryptionConfiguration](#cfn-cloudwatch-space-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [Name](#cfn-cloudwatch-space-name): {{String}}
  [Tags](#cfn-cloudwatch-space-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-space-properties"></a>

`AgentCoreEvaluationRoleArn`  <a name="cfn-cloudwatch-space-agentcoreevaluationrolearn"></a>
The ARN of the IAM role used by AgentCore online evaluation. Absent when the space was created without one.
*Required*: No
*Type*: String
*Pattern*: `^arn:.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataAccessRoleArn`  <a name="cfn-cloudwatch-space-dataaccessrolearn"></a>
The ARN of the IAM role used for data access.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainId`  <a name="cfn-cloudwatch-space-domainid"></a>
The ID of the domain to create the space in.
*Required*: Yes
*Type*: String
*Pattern*: `^d-[0-9a-z]{1,25}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionConfiguration`  <a name="cfn-cloudwatch-space-encryptionconfiguration"></a>
How the space's data at rest is encrypted. Always populated.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-cloudwatch-space-encryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-space-name"></a>
A name that identifies the space.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]+(-[a-z0-9]+)*$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-space-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-space-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-space-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-space-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the value of the `Arn` property.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-space-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-space-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the space.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the space was created.

`OwnerAccountId`  <a name="OwnerAccountId-fn::getatt"></a>
AWS account ID that owns this space.

`Region`  <a name="Region-fn::getatt"></a>
The region where this space was created.

`SpaceId`  <a name="SpaceId-fn::getatt"></a>
The unique ID of the space.

`Status`  <a name="Status-fn::getatt"></a>
The status of the space.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the space was last updated.
