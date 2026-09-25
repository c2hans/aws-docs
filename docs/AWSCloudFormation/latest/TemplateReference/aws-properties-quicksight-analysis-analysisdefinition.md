---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-analysisdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis AnalysisDefinition
<a name="aws-properties-quicksight-analysis-analysisdefinition"></a>

The definition of an analysis.

## Syntax
<a name="aws-properties-quicksight-analysis-analysisdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-analysisdefinition-syntax.json"></a>

```
{
  "[AnalysisDefaults](#cfn-quicksight-analysis-analysisdefinition-analysisdefaults)" : {{AnalysisDefaults}},
  "[CalculatedFields](#cfn-quicksight-analysis-analysisdefinition-calculatedfields)" : {{[ CalculatedField, ... ]}},
  "[ColumnConfigurations](#cfn-quicksight-analysis-analysisdefinition-columnconfigurations)" : {{[ ColumnConfiguration, ... ]}},
  "[DataSetIdentifierDeclarations](#cfn-quicksight-analysis-analysisdefinition-datasetidentifierdeclarations)" : {{[ DataSetIdentifierDeclaration, ... ]}},
  "[FilterGroups](#cfn-quicksight-analysis-analysisdefinition-filtergroups)" : {{[ FilterGroup, ... ]}},
  "[Options](#cfn-quicksight-analysis-analysisdefinition-options)" : {{AssetOptions}},
  "[ParameterDeclarations](#cfn-quicksight-analysis-analysisdefinition-parameterdeclarations)" : {{[ ParameterDeclaration, ... ]}},
  "[QueryExecutionOptions](#cfn-quicksight-analysis-analysisdefinition-queryexecutionoptions)" : {{QueryExecutionOptions}},
  "[Sheets](#cfn-quicksight-analysis-analysisdefinition-sheets)" : {{[ SheetDefinition, ... ]}},
  "[StaticFiles](#cfn-quicksight-analysis-analysisdefinition-staticfiles)" : {{[ StaticFile, ... ]}},
  "[TopicIdentifierDeclarations](#cfn-quicksight-analysis-analysisdefinition-topicidentifierdeclarations)" : {{[ TopicIdentifierDeclaration, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-analysisdefinition-syntax.yaml"></a>

```
  [AnalysisDefaults](#cfn-quicksight-analysis-analysisdefinition-analysisdefaults): {{
    AnalysisDefaults}}
  [CalculatedFields](#cfn-quicksight-analysis-analysisdefinition-calculatedfields): {{
    - CalculatedField}}
  [ColumnConfigurations](#cfn-quicksight-analysis-analysisdefinition-columnconfigurations): {{
    - ColumnConfiguration}}
  [DataSetIdentifierDeclarations](#cfn-quicksight-analysis-analysisdefinition-datasetidentifierdeclarations): {{
    - DataSetIdentifierDeclaration}}
  [FilterGroups](#cfn-quicksight-analysis-analysisdefinition-filtergroups): {{
    - FilterGroup}}
  [Options](#cfn-quicksight-analysis-analysisdefinition-options): {{
    AssetOptions}}
  [ParameterDeclarations](#cfn-quicksight-analysis-analysisdefinition-parameterdeclarations): {{
    - ParameterDeclaration}}
  [QueryExecutionOptions](#cfn-quicksight-analysis-analysisdefinition-queryexecutionoptions): {{
    QueryExecutionOptions}}
  [Sheets](#cfn-quicksight-analysis-analysisdefinition-sheets): {{
    - SheetDefinition}}
  [StaticFiles](#cfn-quicksight-analysis-analysisdefinition-staticfiles): {{
    - StaticFile}}
  [TopicIdentifierDeclarations](#cfn-quicksight-analysis-analysisdefinition-topicidentifierdeclarations): {{
    - TopicIdentifierDeclaration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-analysisdefinition-properties"></a>

`AnalysisDefaults`  <a name="cfn-quicksight-analysis-analysisdefinition-analysisdefaults"></a>
Property description not available.
*Required*: No
*Type*: [AnalysisDefaults](aws-properties-quicksight-analysis-analysisdefaults.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CalculatedFields`  <a name="cfn-quicksight-analysis-analysisdefinition-calculatedfields"></a>
An array of calculated field definitions for the analysis.
*Required*: No
*Type*: Array of [CalculatedField](aws-properties-quicksight-analysis-calculatedfield.md)
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnConfigurations`  <a name="cfn-quicksight-analysis-analysisdefinition-columnconfigurations"></a>
 An array of analysis-level column configurations. Column configurations can be used to set default formatting for a column to be used throughout an analysis.
*Required*: No
*Type*: Array of [ColumnConfiguration](aws-properties-quicksight-analysis-columnconfiguration.md)
*Minimum*: `0`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetIdentifierDeclarations`  <a name="cfn-quicksight-analysis-analysisdefinition-datasetidentifierdeclarations"></a>
An array of dataset identifier declarations. This mapping allows the usage of dataset identifiers instead of dataset ARNs throughout analysis sub-structures.
*Required*: Yes
*Type*: Array of [DataSetIdentifierDeclaration](aws-properties-quicksight-analysis-datasetidentifierdeclaration.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterGroups`  <a name="cfn-quicksight-analysis-analysisdefinition-filtergroups"></a>
Filter definitions for an analysis.
For more information, see [Filtering Data in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/adding-a-filter.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [FilterGroup](aws-properties-quicksight-analysis-filtergroup.md)
*Minimum*: `0`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Options`  <a name="cfn-quicksight-analysis-analysisdefinition-options"></a>
An array of option definitions for an analysis.
*Required*: No
*Type*: [AssetOptions](aws-properties-quicksight-analysis-assetoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterDeclarations`  <a name="cfn-quicksight-analysis-analysisdefinition-parameterdeclarations"></a>
An array of parameter declarations for an analysis.
Parameters are named variables that can transfer a value for use by an action or an object.
For more information, see [Parameters in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html) in the *Amazon Quick Suite User Guide*.
*Required*: No
*Type*: Array of [ParameterDeclaration](aws-properties-quicksight-analysis-parameterdeclaration.md)
*Minimum*: `0`
*Maximum*: `400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryExecutionOptions`  <a name="cfn-quicksight-analysis-analysisdefinition-queryexecutionoptions"></a>
Property description not available.
*Required*: No
*Type*: [QueryExecutionOptions](aws-properties-quicksight-analysis-queryexecutionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sheets`  <a name="cfn-quicksight-analysis-analysisdefinition-sheets"></a>
An array of sheet definitions for an analysis. Each `SheetDefinition` provides detailed information about a sheet within this analysis.
*Required*: No
*Type*: Array of [SheetDefinition](aws-properties-quicksight-analysis-sheetdefinition.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticFiles`  <a name="cfn-quicksight-analysis-analysisdefinition-staticfiles"></a>
The static files for the definition.
*Required*: No
*Type*: Array of [StaticFile](aws-properties-quicksight-analysis-staticfile.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicIdentifierDeclarations`  <a name="cfn-quicksight-analysis-analysisdefinition-topicidentifierdeclarations"></a>
An array of topic identifier declarations. This mapping allows the usage of topic identifiers instead of topic ARNs throughout analysis sub-structures.
*Required*: No
*Type*: Array of [TopicIdentifierDeclaration](aws-properties-quicksight-analysis-topicidentifierdeclaration.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
