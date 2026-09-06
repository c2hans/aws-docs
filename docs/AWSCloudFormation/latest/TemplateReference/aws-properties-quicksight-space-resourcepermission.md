---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-space-resourcepermission.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Space ResourcePermission
<a name="aws-properties-quicksight-space-resourcepermission"></a>

<a name="aws-properties-quicksight-space-resourcepermission-description"></a>The `ResourcePermission` property type specifies Property description not available. for an [AWS::QuickSight::Space](aws-resource-quicksight-space.md).

## Syntax
<a name="aws-properties-quicksight-space-resourcepermission-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-space-resourcepermission-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-space-resourcepermission-actions)" : {{[ String, ... ]}},
  "[Principal](#cfn-quicksight-space-resourcepermission-principal)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-space-resourcepermission-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-space-resourcepermission-actions): {{
    - String}}
  [Principal](#cfn-quicksight-space-resourcepermission-principal): {{String}}
```

## Properties
<a name="aws-properties-quicksight-space-resourcepermission-properties"></a>

`Actions`  <a name="cfn-quicksight-space-resourcepermission-actions"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principal`  <a name="cfn-quicksight-space-resourcepermission-principal"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
