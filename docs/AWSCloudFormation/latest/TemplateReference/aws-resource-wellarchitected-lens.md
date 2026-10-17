---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wellarchitected-lens.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::Lens
<a name="aws-resource-wellarchitected-lens"></a>

A lens return object.

## Syntax
<a name="aws-resource-wellarchitected-lens-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wellarchitected-lens-syntax.json"></a>

```
{
  "Type" : "AWS::WellArchitected::Lens",
  "Properties" : {
      "[JSONString](#cfn-wellarchitected-lens-jsonstring)" : {{String}},
      "[LensVersion](#cfn-wellarchitected-lens-lensversion)" : {{String}},
      "[Tags](#cfn-wellarchitected-lens-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-wellarchitected-lens-syntax.yaml"></a>

```
Type: AWS::WellArchitected::Lens
Properties:
  [JSONString](#cfn-wellarchitected-lens-jsonstring): {{
    String}}
  [LensVersion](#cfn-wellarchitected-lens-lensversion): {{String}}
  [Tags](#cfn-wellarchitected-lens-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-wellarchitected-lens-properties"></a>

`JSONString`  <a name="cfn-wellarchitected-lens-jsonstring"></a>
The JSON string representation of the lens content.
*Required*: No
*Type*: String
*Minimum*: `2`
*Maximum*: `500000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LensVersion`  <a name="cfn-wellarchitected-lens-lensversion"></a>
The version of a lens.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-wellarchitected-lens-tags"></a>
The tags assigned to the lens.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-wellarchitected-lens-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wellarchitected-lens-return-values"></a>

### Ref
<a name="aws-resource-wellarchitected-lens-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the lens ARN.

### Fn::GetAtt
<a name="aws-resource-wellarchitected-lens-return-values-fn--getatt"></a>

####
<a name="aws-resource-wellarchitected-lens-return-values-fn--getatt-fn--getatt"></a>

`Description`  <a name="Description-fn::getatt"></a>
The description of the lens.

`LensArn`  <a name="LensArn-fn::getatt"></a>
The ARN of a lens.

`LensId`  <a name="LensId-fn::getatt"></a>
The ID of the lens.

`Name`  <a name="Name-fn::getatt"></a>
The name of the lens.

`Owner`  <a name="Owner-fn::getatt"></a>
The AWS account ID that owns the lens.
