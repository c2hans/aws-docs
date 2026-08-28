---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-imagecustomaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ImageCustomAction
<a name="aws-properties-quicksight-template-imagecustomaction"></a>

A custom action defined on an image.

## Syntax
<a name="aws-properties-quicksight-template-imagecustomaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-imagecustomaction-syntax.json"></a>

```
{
  "[ActionOperations](#cfn-quicksight-template-imagecustomaction-actionoperations)" : {{[ ImageCustomActionOperation, ... ]}},
  "[CustomActionId](#cfn-quicksight-template-imagecustomaction-customactionid)" : {{String}},
  "[Name](#cfn-quicksight-template-imagecustomaction-name)" : {{String}},
  "[Status](#cfn-quicksight-template-imagecustomaction-status)" : {{String}},
  "[Trigger](#cfn-quicksight-template-imagecustomaction-trigger)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-imagecustomaction-syntax.yaml"></a>

```
  [ActionOperations](#cfn-quicksight-template-imagecustomaction-actionoperations): {{
    - ImageCustomActionOperation}}
  [CustomActionId](#cfn-quicksight-template-imagecustomaction-customactionid): {{String}}
  [Name](#cfn-quicksight-template-imagecustomaction-name): {{String}}
  [Status](#cfn-quicksight-template-imagecustomaction-status): {{String}}
  [Trigger](#cfn-quicksight-template-imagecustomaction-trigger): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-imagecustomaction-properties"></a>

`ActionOperations`  <a name="cfn-quicksight-template-imagecustomaction-actionoperations"></a>
A list of `ImageCustomActionOperations`.
This is a union type structure. For this structure to be valid, only one of the attributes can be defined.
*Required*: Yes
*Type*: Array of [ImageCustomActionOperation](aws-properties-quicksight-template-imagecustomactionoperation.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomActionId`  <a name="cfn-quicksight-template-imagecustomaction-customactionid"></a>
The ID of the custom action.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-template-imagecustomaction-name"></a>
The name of the custom action.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-quicksight-template-imagecustomaction-status"></a>
The status of the custom action.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trigger`  <a name="cfn-quicksight-template-imagecustomaction-trigger"></a>
The trigger of the `VisualCustomAction`.
Valid values are defined as follows:
+ `CLICK`: Initiates a custom action by a left pointer click on a data point.
+ `MENU`: Initiates a custom action by right pointer click from the menu.
*Required*: Yes
*Type*: String
*Allowed values*: `CLICK | MENU`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
