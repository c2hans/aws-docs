---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-dashboardversiondefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DashboardVersionDefinition
<a name="aws-properties-quicksight-dashboard-dashboardversiondefinition"></a>

The contents of a dashboard.

## Syntax
<a name="aws-properties-quicksight-dashboard-dashboardversiondefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-dashboardversiondefinition-syntax.json"></a>

```
{
  "[AnalysisDefaults](#cfn-quicksight-dashboard-dashboardversiondefinition-analysisdefaults)" : {{AnalysisDefaults}},
  "[CalculatedFields](#cfn-quicksight-dashboard-dashboardversiondefinition-calculatedfields)" : {{[ CalculatedField, ... ]}},
  "[ColumnConfigurations](#cfn-quicksight-dashboard-dashboardversiondefinition-columnconfigurations)" : {{[ ColumnConfiguration, ... ]}},
  "[DataSetIdentifierDeclarations](#cfn-quicksight-dashboard-dashboardversiondefinition-datasetidentifierdeclarations)" : {{[ DataSetIdentifierDeclaration, ... ]}},
  "[FilterGroups](#cfn-quicksight-dashboard-dashboardversiondefinition-filtergroups)" : {{[ FilterGroup, ... ]}},
  "[Options](#cfn-quicksight-dashboard-dashboardversiondefinition-options)" : {{AssetOptions}},
  "[ParameterDeclarations](#cfn-quicksight-dashboard-dashboardversiondefinition-parameterdeclarations)" : {{[ ParameterDeclaration, ... ]}},
  "[Sheets](#cfn-quicksight-dashboard-dashboardversiondefinition-sheets)" : {{[ SheetDefinition, ... ]}},
  "[StaticFiles](#cfn-quicksight-dashboard-dashboardversiondefinition-staticfiles)" : {{[ StaticFile, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-dashboardversiondefinition-syntax.yaml"></a>

```
  [AnalysisDefaults](#cfn-quicksight-dashboard-dashboardversiondefinition-analysisdefaults): {{
    AnalysisDefaults}}
  [CalculatedFields](#cfn-quicksight-dashboard-dashboardversiondefinition-calculatedfields): {{
    - CalculatedField}}
  [ColumnConfigurations](#cfn-quicksight-dashboard-dashboardversiondefinition-columnconfigurations): {{
    - ColumnConfiguration}}
  [DataSetIdentifierDeclarations](#cfn-quicksight-dashboard-dashboardversiondefinition-datasetidentifierdeclarations): {{
    - DataSetIdentifierDeclaration}}
  [FilterGroups](#cfn-quicksight-dashboard-dashboardversiondefinition-filtergroups): {{
    - FilterGroup}}
  [Options](#cfn-quicksight-dashboard-dashboardversiondefinition-options): {{
    AssetOptions}}
  [ParameterDeclarations](#cfn-quicksight-dashboard-dashboardversiondefinition-parameterdeclarations): {{
    - ParameterDeclaration}}
  [Sheets](#cfn-quicksight-dashboard-dashboardversiondefinition-sheets): {{
    - SheetDefinition}}
  [StaticFiles](#cfn-quicksight-dashboard-dashboardversiondefinition-staticfiles): {{
    - StaticFile}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-dashboardversiondefinition-properties"></a>

`AnalysisDefaults`  <a name="cfn-quicksight-dashboard-dashboardversiondefinition-analysisdefaults"></a>
Property description not available.
*Required*: No
*Type*: [AnalysisDefaults](aws-properties-quicksight-dashboard-analysisdefaults.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CalculatedFields`  <a name="cfn-quicksight-dashboard-dashboardversiondefinition-calculatedfields"></a>
An array of calculated field definitions for the dashboard.
*Required*: No
*Type*: Array of [CalculatedField](aws-properties-quicksight-dashboard-calculatedfield.md)
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnConfigurations`  <a name="cfn-quicksight-dashboard-dashboardversiondefinition-columnconfigurations"></a>
An array of dashboard-level column configurations. Column configurations are used to set the default formatting for a column that is used throughout a dashboard.
*Required*: No
*Type*: Array of [ColumnConfiguration](aws-properties-quicksight-dashboard-columnconfiguration.md)
*Minimum*: `0`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetIdentifierDeclarations`  <a name="cfn-quicksight-dashboard-dashboardversiondefinition-datasetidentifierdeclarations"></a>
An array of dataset identifier declarations. With this mapping,you can use dataset identifiers instead of dataset Amazon Resource Names (ARNs) throughout the dashboard's sub-structures.
*Required*: Yes
*Type*: Array of [DataSetIdentifierDeclaration](aws-properties-quicksight-dashboard-datasetidentifierdeclaration.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterGroups`  <a name="cfn-quicksight-dashboard-dashboardversiondefinition-filtergroups"></a>
The filter definitions for a dashboard.
For more information, see [Filtering Data in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/adding-a-filter.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [FilterGroup](aws-properties-quicksight-dashboard-filtergroup.md)
*Minimum*: `0`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Options`  <a name="cfn-quicksight-dashboard-dashboardversiondefinition-options"></a>
An array of option definitions for a dashboard.
*Required*: No
*Type*: [AssetOptions](aws-properties-quicksight-dashboard-assetoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterDeclarations`  <a name="cfn-quicksight-dashboard-dashboardversiondefinition-parameterdeclarations"></a>
The parameter declarations for a dashboard. Parameters are named variables that can transfer a value for use by an action or an object.
For more information, see [Parameters in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [ParameterDeclaration](aws-properties-quicksight-dashboard-parameterdeclaration.md)
*Minimum*: `0`
*Maximum*: `400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sheets`  <a name="cfn-quicksight-dashboard-dashboardversiondefinition-sheets"></a>
An array of sheet definitions for a dashboard.
*Required*: No
*Type*: Array of [SheetDefinition](aws-properties-quicksight-dashboard-sheetdefinition.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticFiles`  <a name="cfn-quicksight-dashboard-dashboardversiondefinition-staticfiles"></a>
The static files for the definition.
*Required*: No
*Type*: Array of [StaticFile](aws-properties-quicksight-dashboard-staticfile.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
