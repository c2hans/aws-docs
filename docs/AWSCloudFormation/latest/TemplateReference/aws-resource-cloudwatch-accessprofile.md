---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-accessprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AccessProfile
<a name="aws-resource-cloudwatch-accessprofile"></a>

Resource type definition for `AWS::CloudWatch::AccessProfile`

## Syntax
<a name="aws-resource-cloudwatch-accessprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-accessprofile-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::AccessProfile",
  "Properties" : {
      "[Description](#cfn-cloudwatch-accessprofile-description)" : {{String}},
      "[Name](#cfn-cloudwatch-accessprofile-name)" : {{String}},
      "[SpaceId](#cfn-cloudwatch-accessprofile-spaceid)" : {{String}},
      "[Tags](#cfn-cloudwatch-accessprofile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-accessprofile-syntax.yaml"></a>

```
Type: AWS::CloudWatch::AccessProfile
Properties:
  [Description](#cfn-cloudwatch-accessprofile-description): {{String}}
  [Name](#cfn-cloudwatch-accessprofile-name): {{String}}
  [SpaceId](#cfn-cloudwatch-accessprofile-spaceid): {{String}}
  [Tags](#cfn-cloudwatch-accessprofile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-accessprofile-properties"></a>

`Description`  <a name="cfn-cloudwatch-accessprofile-description"></a>
The description of the access profile.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-accessprofile-name"></a>
The name of the access profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9 _.:/=+@-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceId`  <a name="cfn-cloudwatch-accessprofile-spaceid"></a>
The unique identifier of the space the access profile belongs to.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudwatch-accessprofile-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-accessprofile-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-accessprofile-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-accessprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a unique identifier for this resource.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-accessprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-accessprofile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the access profile.

`AssumeStatus`  <a name="AssumeStatus-fn::getatt"></a>
Whether the calling principal is authorized to assume the access profile.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time the access profile was created.

`ProfileId`  <a name="ProfileId-fn::getatt"></a>
The unique identifier of the access profile.

`ProfileType`  <a name="ProfileType-fn::getatt"></a>
Whether the access profile is managed by the service or by the customer.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time the access profile was last updated.
