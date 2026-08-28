---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sheetdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SheetDefinition
<a name="aws-properties-quicksight-analysis-sheetdefinition"></a>

A sheet is an object that contains a set of visuals that are viewed together on one page in a paginated report. Every analysis and dashboard must contain at least one sheet.

## Syntax
<a name="aws-properties-quicksight-analysis-sheetdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sheetdefinition-syntax.json"></a>

```
{
  "[ContentType](#cfn-quicksight-analysis-sheetdefinition-contenttype)" : {{String}},
  "[Description](#cfn-quicksight-analysis-sheetdefinition-description)" : {{String}},
  "[FilterControls](#cfn-quicksight-analysis-sheetdefinition-filtercontrols)" : {{[ FilterControl, ... ]}},
  "[Images](#cfn-quicksight-analysis-sheetdefinition-images)" : {{[ SheetImage, ... ]}},
  "[Layouts](#cfn-quicksight-analysis-sheetdefinition-layouts)" : {{[ Layout, ... ]}},
  "[Name](#cfn-quicksight-analysis-sheetdefinition-name)" : {{String}},
  "[ParameterControls](#cfn-quicksight-analysis-sheetdefinition-parametercontrols)" : {{[ ParameterControl, ... ]}},
  "[SheetControlLayouts](#cfn-quicksight-analysis-sheetdefinition-sheetcontrollayouts)" : {{[ SheetControlLayout, ... ]}},
  "[SheetId](#cfn-quicksight-analysis-sheetdefinition-sheetid)" : {{String}},
  "[TextBoxes](#cfn-quicksight-analysis-sheetdefinition-textboxes)" : {{[ SheetTextBox, ... ]}},
  "[Title](#cfn-quicksight-analysis-sheetdefinition-title)" : {{String}},
  "[Visuals](#cfn-quicksight-analysis-sheetdefinition-visuals)" : {{[ Visual, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sheetdefinition-syntax.yaml"></a>

```
  [ContentType](#cfn-quicksight-analysis-sheetdefinition-contenttype): {{String}}
  [Description](#cfn-quicksight-analysis-sheetdefinition-description): {{String}}
  [FilterControls](#cfn-quicksight-analysis-sheetdefinition-filtercontrols): {{
    - FilterControl}}
  [Images](#cfn-quicksight-analysis-sheetdefinition-images): {{
    - SheetImage}}
  [Layouts](#cfn-quicksight-analysis-sheetdefinition-layouts): {{
    - Layout}}
  [Name](#cfn-quicksight-analysis-sheetdefinition-name): {{String}}
  [ParameterControls](#cfn-quicksight-analysis-sheetdefinition-parametercontrols): {{
    - ParameterControl}}
  [SheetControlLayouts](#cfn-quicksight-analysis-sheetdefinition-sheetcontrollayouts): {{
    - SheetControlLayout}}
  [SheetId](#cfn-quicksight-analysis-sheetdefinition-sheetid): {{String}}
  [TextBoxes](#cfn-quicksight-analysis-sheetdefinition-textboxes): {{
    - SheetTextBox}}
  [Title](#cfn-quicksight-analysis-sheetdefinition-title): {{String}}
  [Visuals](#cfn-quicksight-analysis-sheetdefinition-visuals): {{
    - Visual}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sheetdefinition-properties"></a>

`ContentType`  <a name="cfn-quicksight-analysis-sheetdefinition-contenttype"></a>
The layout content type of the sheet. Choose one of the following options:
+ `PAGINATED`: Creates a sheet for a paginated report.
+ `INTERACTIVE`: Creates a sheet for an interactive dashboard.
*Required*: No
*Type*: String
*Allowed values*: `PAGINATED | INTERACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-quicksight-analysis-sheetdefinition-description"></a>
A description of the sheet.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterControls`  <a name="cfn-quicksight-analysis-sheetdefinition-filtercontrols"></a>
The list of filter controls that are on a sheet.
For more information, see [Adding filter controls to analysis sheets](https://docs.aws.amazon.com/quicksight/latest/user/filter-controls.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [FilterControl](aws-properties-quicksight-analysis-filtercontrol.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Images`  <a name="cfn-quicksight-analysis-sheetdefinition-images"></a>
A list of images on a sheet.
*Required*: No
*Type*: Array of [SheetImage](aws-properties-quicksight-analysis-sheetimage.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Layouts`  <a name="cfn-quicksight-analysis-sheetdefinition-layouts"></a>
Layouts define how the components of a sheet are arranged.
For more information, see [Types of layout](https://docs.aws.amazon.com/quicksight/latest/user/types-of-layout.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [Layout](aws-properties-quicksight-analysis-layout.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-analysis-sheetdefinition-name"></a>
The name of the sheet. This name is displayed on the sheet's tab in the Quick console.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterControls`  <a name="cfn-quicksight-analysis-sheetdefinition-parametercontrols"></a>
The list of parameter controls that are on a sheet.
For more information, see [Using a Control with a Parameter in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/parameters-controls.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [ParameterControl](aws-properties-quicksight-analysis-parametercontrol.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetControlLayouts`  <a name="cfn-quicksight-analysis-sheetdefinition-sheetcontrollayouts"></a>
The control layouts of the sheet.
*Required*: No
*Type*: Array of [SheetControlLayout](aws-properties-quicksight-analysis-sheetcontrollayout.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetId`  <a name="cfn-quicksight-analysis-sheetdefinition-sheetid"></a>
The unique identifier of a sheet.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextBoxes`  <a name="cfn-quicksight-analysis-sheetdefinition-textboxes"></a>
The text boxes that are on a sheet.
*Required*: No
*Type*: Array of [SheetTextBox](aws-properties-quicksight-analysis-sheettextbox.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-analysis-sheetdefinition-title"></a>
The title of the sheet.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visuals`  <a name="cfn-quicksight-analysis-sheetdefinition-visuals"></a>
A list of the visuals that are on a sheet. Visual placement is determined by the layout of the sheet.
*Required*: No
*Type*: Array of [Visual](aws-properties-quicksight-analysis-visual.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
