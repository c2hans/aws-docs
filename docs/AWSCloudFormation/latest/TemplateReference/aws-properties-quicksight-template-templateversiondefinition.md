---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-templateversiondefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TemplateVersionDefinition
<a name="aws-properties-quicksight-template-templateversiondefinition"></a>

The detailed definition of a template.

## Syntax
<a name="aws-properties-quicksight-template-templateversiondefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-templateversiondefinition-syntax.json"></a>

```
{
  "[AnalysisDefaults](#cfn-quicksight-template-templateversiondefinition-analysisdefaults)" : {{AnalysisDefaults}},
  "[CalculatedFields](#cfn-quicksight-template-templateversiondefinition-calculatedfields)" : {{[ CalculatedField, ... ]}},
  "[ColumnConfigurations](#cfn-quicksight-template-templateversiondefinition-columnconfigurations)" : {{[ ColumnConfiguration, ... ]}},
  "[DataSetConfigurations](#cfn-quicksight-template-templateversiondefinition-datasetconfigurations)" : {{[ DataSetConfiguration, ... ]}},
  "[FilterGroups](#cfn-quicksight-template-templateversiondefinition-filtergroups)" : {{[ FilterGroup, ... ]}},
  "[Options](#cfn-quicksight-template-templateversiondefinition-options)" : {{AssetOptions}},
  "[ParameterDeclarations](#cfn-quicksight-template-templateversiondefinition-parameterdeclarations)" : {{[ ParameterDeclaration, ... ]}},
  "[QueryExecutionOptions](#cfn-quicksight-template-templateversiondefinition-queryexecutionoptions)" : {{QueryExecutionOptions}},
  "[Sheets](#cfn-quicksight-template-templateversiondefinition-sheets)" : {{[ SheetDefinition, ... ]}},
  "[StaticFiles](#cfn-quicksight-template-templateversiondefinition-staticfiles)" : {{[ StaticFile, ... ]}},
  "[TopicConfigurations](#cfn-quicksight-template-templateversiondefinition-topicconfigurations)" : {{[ TopicConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-templateversiondefinition-syntax.yaml"></a>

```
  [AnalysisDefaults](#cfn-quicksight-template-templateversiondefinition-analysisdefaults): {{
    AnalysisDefaults}}
  [CalculatedFields](#cfn-quicksight-template-templateversiondefinition-calculatedfields): {{
    - CalculatedField}}
  [ColumnConfigurations](#cfn-quicksight-template-templateversiondefinition-columnconfigurations): {{
    - ColumnConfiguration}}
  [DataSetConfigurations](#cfn-quicksight-template-templateversiondefinition-datasetconfigurations): {{
    - DataSetConfiguration}}
  [FilterGroups](#cfn-quicksight-template-templateversiondefinition-filtergroups): {{
    - FilterGroup}}
  [Options](#cfn-quicksight-template-templateversiondefinition-options): {{
    AssetOptions}}
  [ParameterDeclarations](#cfn-quicksight-template-templateversiondefinition-parameterdeclarations): {{
    - ParameterDeclaration}}
  [QueryExecutionOptions](#cfn-quicksight-template-templateversiondefinition-queryexecutionoptions): {{
    QueryExecutionOptions}}
  [Sheets](#cfn-quicksight-template-templateversiondefinition-sheets): {{
    - SheetDefinition}}
  [StaticFiles](#cfn-quicksight-template-templateversiondefinition-staticfiles): {{
    - StaticFile}}
  [TopicConfigurations](#cfn-quicksight-template-templateversiondefinition-topicconfigurations): {{
    - TopicConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-templateversiondefinition-properties"></a>

`AnalysisDefaults`  <a name="cfn-quicksight-template-templateversiondefinition-analysisdefaults"></a>
Property description not available.
*Required*: No
*Type*: [AnalysisDefaults](aws-properties-quicksight-template-analysisdefaults.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CalculatedFields`  <a name="cfn-quicksight-template-templateversiondefinition-calculatedfields"></a>
An array of calculated field definitions for the template.
*Required*: No
*Type*: Array of [CalculatedField](aws-properties-quicksight-template-calculatedfield.md)
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnConfigurations`  <a name="cfn-quicksight-template-templateversiondefinition-columnconfigurations"></a>
 An array of template-level column configurations. Column configurations are used to set default formatting for a column that's used throughout a template.
*Required*: No
*Type*: Array of [ColumnConfiguration](aws-properties-quicksight-template-columnconfiguration.md)
*Minimum*: `0`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetConfigurations`  <a name="cfn-quicksight-template-templateversiondefinition-datasetconfigurations"></a>
An array of dataset configurations. These configurations define the required columns for each dataset used within a template.
*Required*: Yes
*Type*: Array of [DataSetConfiguration](aws-properties-quicksight-template-datasetconfiguration.md)
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterGroups`  <a name="cfn-quicksight-template-templateversiondefinition-filtergroups"></a>
Filter definitions for a template.
For more information, see [Filtering Data](https://docs.aws.amazon.com/quicksight/latest/user/filtering-visual-data.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [FilterGroup](aws-properties-quicksight-template-filtergroup.md)
*Minimum*: `0`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Options`  <a name="cfn-quicksight-template-templateversiondefinition-options"></a>
An array of option definitions for a template.
*Required*: No
*Type*: [AssetOptions](aws-properties-quicksight-template-assetoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterDeclarations`  <a name="cfn-quicksight-template-templateversiondefinition-parameterdeclarations"></a>
An array of parameter declarations for a template.
*Parameters* are named variables that can transfer a value for use by an action or an object.
For more information, see [Parameters in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [ParameterDeclaration](aws-properties-quicksight-template-parameterdeclaration.md)
*Minimum*: `0`
*Maximum*: `400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryExecutionOptions`  <a name="cfn-quicksight-template-templateversiondefinition-queryexecutionoptions"></a>
Property description not available.
*Required*: No
*Type*: [QueryExecutionOptions](aws-properties-quicksight-template-queryexecutionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sheets`  <a name="cfn-quicksight-template-templateversiondefinition-sheets"></a>
An array of sheet definitions for a template.
*Required*: No
*Type*: Array of [SheetDefinition](aws-properties-quicksight-template-sheetdefinition.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticFiles`  <a name="cfn-quicksight-template-templateversiondefinition-staticfiles"></a>
The static files for the definition.
*Required*: No
*Type*: Array of [StaticFile](aws-properties-quicksight-template-staticfile.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicConfigurations`  <a name="cfn-quicksight-template-templateversiondefinition-topicconfigurations"></a>
An array of topic configurations. These configurations define the required columns for each topic used within a template.
*Required*: No
*Type*: Array of [TopicConfiguration](aws-properties-quicksight-template-topicconfiguration.md)
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
