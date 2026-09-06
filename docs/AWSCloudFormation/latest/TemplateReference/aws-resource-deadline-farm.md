---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-farm.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Farm
<a name="aws-resource-deadline-farm"></a>

Creates a farm to allow space for queues and fleets. Farms are the space where the components of your renders gather and are pieced together in the cloud. Farms contain budgets and allow you to enforce permissions. Deadline Cloud farms are a useful container for large projects.

## Syntax
<a name="aws-resource-deadline-farm-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-farm-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::Farm",
  "Properties" : {
      "[CostScaleFactor](#cfn-deadline-farm-costscalefactor)" : {{Number}},
      "[Description](#cfn-deadline-farm-description)" : {{String}},
      "[DisplayName](#cfn-deadline-farm-displayname)" : {{String}},
      "[KmsKeyArn](#cfn-deadline-farm-kmskeyarn)" : {{String}},
      "[Tags](#cfn-deadline-farm-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-deadline-farm-syntax.yaml"></a>

```
Type: AWS::Deadline::Farm
Properties:
  [CostScaleFactor](#cfn-deadline-farm-costscalefactor): {{Number}}
  [Description](#cfn-deadline-farm-description): {{String}}
  [DisplayName](#cfn-deadline-farm-displayname): {{String}}
  [KmsKeyArn](#cfn-deadline-farm-kmskeyarn): {{String}}
  [Tags](#cfn-deadline-farm-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-deadline-farm-properties"></a>

`CostScaleFactor`  <a name="cfn-deadline-farm-costscalefactor"></a>
Property description not available.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-deadline-farm-description"></a>
A description of the farm that helps identify what the farm is used for.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-deadline-farm-displayname"></a>
The display name of the farm.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-deadline-farm-kmskeyarn"></a>
The ARN for the KMS key.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[-a-z]*:kms:.*:key/.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-deadline-farm-tags"></a>
The tags to add to your farm. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.
*Required*: No
*Type*: Array of [Tag](aws-properties-deadline-farm-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-deadline-farm-return-values"></a>

### Ref
<a name="aws-resource-deadline-farm-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the farm.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-deadline-farm-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-deadline-farm-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) assigned to the farm.

`FarmId`  <a name="FarmId-fn::getatt"></a>
The farm ID.
