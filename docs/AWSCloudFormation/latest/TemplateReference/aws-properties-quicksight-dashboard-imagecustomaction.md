---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-imagecustomaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ImageCustomAction
<a name="aws-properties-quicksight-dashboard-imagecustomaction"></a>

A custom action defined on an image.

## Syntax
<a name="aws-properties-quicksight-dashboard-imagecustomaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-imagecustomaction-syntax.json"></a>

```
{
  "[ActionOperations](#cfn-quicksight-dashboard-imagecustomaction-actionoperations)" : {{[ ImageCustomActionOperation, ... ]}},
  "[CustomActionId](#cfn-quicksight-dashboard-imagecustomaction-customactionid)" : {{String}},
  "[Name](#cfn-quicksight-dashboard-imagecustomaction-name)" : {{String}},
  "[Status](#cfn-quicksight-dashboard-imagecustomaction-status)" : {{String}},
  "[Trigger](#cfn-quicksight-dashboard-imagecustomaction-trigger)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-imagecustomaction-syntax.yaml"></a>

```
  [ActionOperations](#cfn-quicksight-dashboard-imagecustomaction-actionoperations): {{
    - ImageCustomActionOperation}}
  [CustomActionId](#cfn-quicksight-dashboard-imagecustomaction-customactionid): {{String}}
  [Name](#cfn-quicksight-dashboard-imagecustomaction-name): {{String}}
  [Status](#cfn-quicksight-dashboard-imagecustomaction-status): {{String}}
  [Trigger](#cfn-quicksight-dashboard-imagecustomaction-trigger): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-imagecustomaction-properties"></a>

`ActionOperations`  <a name="cfn-quicksight-dashboard-imagecustomaction-actionoperations"></a>
A list of `ImageCustomActionOperations`.
This is a union type structure. For this structure to be valid, only one of the attributes can be defined.
*Required*: Yes
*Type*: Array of [ImageCustomActionOperation](aws-properties-quicksight-dashboard-imagecustomactionoperation.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomActionId`  <a name="cfn-quicksight-dashboard-imagecustomaction-customactionid"></a>
The ID of the custom action.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dashboard-imagecustomaction-name"></a>
The name of the custom action.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-quicksight-dashboard-imagecustomaction-status"></a>
The status of the custom action.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trigger`  <a name="cfn-quicksight-dashboard-imagecustomaction-trigger"></a>
The trigger of the `VisualCustomAction`.
Valid values are defined as follows:
+ `CLICK`: Initiates a custom action by a left pointer click on a data point.
+ `MENU`: Initiates a custom action by right pointer click from the menu.
*Required*: Yes
*Type*: String
*Allowed values*: `CLICK | MENU`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
