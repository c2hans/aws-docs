---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sheetdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SheetDefinition
<a name="aws-properties-quicksight-dashboard-sheetdefinition"></a>

A sheet is an object that contains a set of visuals that are viewed together on one page in a paginated report. Every analysis and dashboard must contain at least one sheet.

## Syntax
<a name="aws-properties-quicksight-dashboard-sheetdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sheetdefinition-syntax.json"></a>

```
{
  "[ContentType](#cfn-quicksight-dashboard-sheetdefinition-contenttype)" : {{String}},
  "[Description](#cfn-quicksight-dashboard-sheetdefinition-description)" : {{String}},
  "[FilterControls](#cfn-quicksight-dashboard-sheetdefinition-filtercontrols)" : {{[ FilterControl, ... ]}},
  "[Images](#cfn-quicksight-dashboard-sheetdefinition-images)" : {{[ SheetImage, ... ]}},
  "[Layouts](#cfn-quicksight-dashboard-sheetdefinition-layouts)" : {{[ Layout, ... ]}},
  "[Name](#cfn-quicksight-dashboard-sheetdefinition-name)" : {{String}},
  "[ParameterControls](#cfn-quicksight-dashboard-sheetdefinition-parametercontrols)" : {{[ ParameterControl, ... ]}},
  "[SheetControlLayouts](#cfn-quicksight-dashboard-sheetdefinition-sheetcontrollayouts)" : {{[ SheetControlLayout, ... ]}},
  "[SheetId](#cfn-quicksight-dashboard-sheetdefinition-sheetid)" : {{String}},
  "[TextBoxes](#cfn-quicksight-dashboard-sheetdefinition-textboxes)" : {{[ SheetTextBox, ... ]}},
  "[Title](#cfn-quicksight-dashboard-sheetdefinition-title)" : {{String}},
  "[Visuals](#cfn-quicksight-dashboard-sheetdefinition-visuals)" : {{[ Visual, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sheetdefinition-syntax.yaml"></a>

```
  [ContentType](#cfn-quicksight-dashboard-sheetdefinition-contenttype): {{String}}
  [Description](#cfn-quicksight-dashboard-sheetdefinition-description): {{String}}
  [FilterControls](#cfn-quicksight-dashboard-sheetdefinition-filtercontrols): {{
    - FilterControl}}
  [Images](#cfn-quicksight-dashboard-sheetdefinition-images): {{
    - SheetImage}}
  [Layouts](#cfn-quicksight-dashboard-sheetdefinition-layouts): {{
    - Layout}}
  [Name](#cfn-quicksight-dashboard-sheetdefinition-name): {{String}}
  [ParameterControls](#cfn-quicksight-dashboard-sheetdefinition-parametercontrols): {{
    - ParameterControl}}
  [SheetControlLayouts](#cfn-quicksight-dashboard-sheetdefinition-sheetcontrollayouts): {{
    - SheetControlLayout}}
  [SheetId](#cfn-quicksight-dashboard-sheetdefinition-sheetid): {{String}}
  [TextBoxes](#cfn-quicksight-dashboard-sheetdefinition-textboxes): {{
    - SheetTextBox}}
  [Title](#cfn-quicksight-dashboard-sheetdefinition-title): {{String}}
  [Visuals](#cfn-quicksight-dashboard-sheetdefinition-visuals): {{
    - Visual}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sheetdefinition-properties"></a>

`ContentType`  <a name="cfn-quicksight-dashboard-sheetdefinition-contenttype"></a>
The layout content type of the sheet. Choose one of the following options:
+ `PAGINATED`: Creates a sheet for a paginated report.
+ `INTERACTIVE`: Creates a sheet for an interactive dashboard.
*Required*: No
*Type*: String
*Allowed values*: `PAGINATED | INTERACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-quicksight-dashboard-sheetdefinition-description"></a>
A description of the sheet.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterControls`  <a name="cfn-quicksight-dashboard-sheetdefinition-filtercontrols"></a>
The list of filter controls that are on a sheet.
For more information, see [Adding filter controls to analysis sheets](https://docs.aws.amazon.com/quicksight/latest/user/filter-controls.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [FilterControl](aws-properties-quicksight-dashboard-filtercontrol.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Images`  <a name="cfn-quicksight-dashboard-sheetdefinition-images"></a>
A list of images on a sheet.
*Required*: No
*Type*: Array of [SheetImage](aws-properties-quicksight-dashboard-sheetimage.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Layouts`  <a name="cfn-quicksight-dashboard-sheetdefinition-layouts"></a>
Layouts define how the components of a sheet are arranged.
For more information, see [Types of layout](https://docs.aws.amazon.com/quicksight/latest/user/types-of-layout.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [Layout](aws-properties-quicksight-dashboard-layout.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dashboard-sheetdefinition-name"></a>
The name of the sheet. This name is displayed on the sheet's tab in the Quick console.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterControls`  <a name="cfn-quicksight-dashboard-sheetdefinition-parametercontrols"></a>
The list of parameter controls that are on a sheet.
For more information, see [Using a Control with a Parameter in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/parameters-controls.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [ParameterControl](aws-properties-quicksight-dashboard-parametercontrol.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetControlLayouts`  <a name="cfn-quicksight-dashboard-sheetdefinition-sheetcontrollayouts"></a>
The control layouts of the sheet.
*Required*: No
*Type*: Array of [SheetControlLayout](aws-properties-quicksight-dashboard-sheetcontrollayout.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetId`  <a name="cfn-quicksight-dashboard-sheetdefinition-sheetid"></a>
The unique identifier of a sheet.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextBoxes`  <a name="cfn-quicksight-dashboard-sheetdefinition-textboxes"></a>
The text boxes that are on a sheet.
*Required*: No
*Type*: Array of [SheetTextBox](aws-properties-quicksight-dashboard-sheettextbox.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-dashboard-sheetdefinition-title"></a>
The title of the sheet.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visuals`  <a name="cfn-quicksight-dashboard-sheetdefinition-visuals"></a>
A list of the visuals that are on a sheet. Visual placement is determined by the layout of the sheet.
*Required*: No
*Type*: Array of [Visual](aws-properties-quicksight-dashboard-visual.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
