---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-accessgrant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AccessGrant
<a name="aws-resource-cloudwatch-accessgrant"></a>

Resource type definition for `AWS::CloudWatch::AccessGrant`

## Syntax
<a name="aws-resource-cloudwatch-accessgrant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-accessgrant-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::AccessGrant",
  "Properties" : {
      "[DomainId](#cfn-cloudwatch-accessgrant-domainid)" : {{String}},
      "[Name](#cfn-cloudwatch-accessgrant-name)" : {{String}},
      "[Permission](#cfn-cloudwatch-accessgrant-permission)" : {{String}},
      "[Principal](#cfn-cloudwatch-accessgrant-principal)" : {{AccessGrantPrincipal}},
      "[ScopedActions](#cfn-cloudwatch-accessgrant-scopedactions)" : {{[ ScopedActions, ... ]}},
      "[SpaceId](#cfn-cloudwatch-accessgrant-spaceid)" : {{String}},
      "[Tags](#cfn-cloudwatch-accessgrant-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-accessgrant-syntax.yaml"></a>

```
Type: AWS::CloudWatch::AccessGrant
Properties:
  [DomainId](#cfn-cloudwatch-accessgrant-domainid): {{String}}
  [Name](#cfn-cloudwatch-accessgrant-name): {{String}}
  [Permission](#cfn-cloudwatch-accessgrant-permission): {{String}}
  [Principal](#cfn-cloudwatch-accessgrant-principal): {{
    AccessGrantPrincipal}}
  [ScopedActions](#cfn-cloudwatch-accessgrant-scopedactions): {{
    - ScopedActions}}
  [SpaceId](#cfn-cloudwatch-accessgrant-spaceid): {{String}}
  [Tags](#cfn-cloudwatch-accessgrant-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-accessgrant-properties"></a>

`DomainId`  <a name="cfn-cloudwatch-accessgrant-domainid"></a>
The unique identifier of the domain that contains the space.
*Required*: Yes
*Type*: String
*Pattern*: `^d-[0-9a-z]{1,25}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cloudwatch-accessgrant-name"></a>
A name that identifies the access grant.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Permission`  <a name="cfn-cloudwatch-accessgrant-permission"></a>
The permission granted. Exactly one permission is granted per access grant.
*Required*: Yes
*Type*: String
*Allowed values*: `SPACE_ADMIN | READ | READ_WRITE_DELETE | CUSTOM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Principal`  <a name="cfn-cloudwatch-accessgrant-principal"></a>
Property description not available.
*Required*: Yes
*Type*: [AccessGrantPrincipal](aws-properties-cloudwatch-accessgrant-accessgrantprincipal.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScopedActions`  <a name="cfn-cloudwatch-accessgrant-scopedactions"></a>
Groups of actions to allow, each with the resource scopes and conditions that limit those actions.
*Required*: No
*Type*: [Array](aws-properties-cloudwatch-accessgrant-scopedactions.md) of [ScopedActions](aws-properties-cloudwatch-accessgrant-scopedactions.md)
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SpaceId`  <a name="cfn-cloudwatch-accessgrant-spaceid"></a>
The unique identifier of the space the access grant is scoped to.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudwatch-accessgrant-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-accessgrant-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudwatch-accessgrant-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-accessgrant-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the value of the `Arn` property.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-accessgrant-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-accessgrant-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
The AWS account ID that owns the access grant.

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the access grant.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time the access grant was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The principal that created the access grant.

`GrantId`  <a name="GrantId-fn::getatt"></a>
The unique identifier of the access grant.

`GrantType`  <a name="GrantType-fn::getatt"></a>
Whether the access grant is managed by the service or by the customer.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time the access grant was last updated.
