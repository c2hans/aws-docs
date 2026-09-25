---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-layercustomaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template LayerCustomAction
<a name="aws-properties-quicksight-template-layercustomaction"></a>

A layer custom action.

## Syntax
<a name="aws-properties-quicksight-template-layercustomaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-layercustomaction-syntax.json"></a>

```
{
  "[ActionOperations](#cfn-quicksight-template-layercustomaction-actionoperations)" : {{[ LayerCustomActionOperation, ... ]}},
  "[CustomActionId](#cfn-quicksight-template-layercustomaction-customactionid)" : {{String}},
  "[Name](#cfn-quicksight-template-layercustomaction-name)" : {{String}},
  "[Status](#cfn-quicksight-template-layercustomaction-status)" : {{String}},
  "[Trigger](#cfn-quicksight-template-layercustomaction-trigger)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-layercustomaction-syntax.yaml"></a>

```
  [ActionOperations](#cfn-quicksight-template-layercustomaction-actionoperations): {{
    - LayerCustomActionOperation}}
  [CustomActionId](#cfn-quicksight-template-layercustomaction-customactionid): {{String}}
  [Name](#cfn-quicksight-template-layercustomaction-name): {{String}}
  [Status](#cfn-quicksight-template-layercustomaction-status): {{String}}
  [Trigger](#cfn-quicksight-template-layercustomaction-trigger): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-layercustomaction-properties"></a>

`ActionOperations`  <a name="cfn-quicksight-template-layercustomaction-actionoperations"></a>
A list of `LayerCustomActionOperations`.
This is a union type structure. For this structure to be valid, only one of the attributes can be defined.
*Required*: Yes
*Type*: Array of [LayerCustomActionOperation](aws-properties-quicksight-template-layercustomactionoperation.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomActionId`  <a name="cfn-quicksight-template-layercustomaction-customactionid"></a>
The ID of the custom action.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-template-layercustomaction-name"></a>
The name of the custom action.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-quicksight-template-layercustomaction-status"></a>
The status of the `LayerCustomAction`.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trigger`  <a name="cfn-quicksight-template-layercustomaction-trigger"></a>
The trigger of the `LayerCustomAction`.
Valid values are defined as follows:
+ `DATA_POINT_CLICK`: Initiates a custom action by a left pointer click on a data point.
+ `DATA_POINT_MENU`: Initiates a custom action by right pointer click from the menu.
*Required*: Yes
*Type*: String
*Allowed values*: `DATA_POINT_CLICK | DATA_POINT_MENU`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
