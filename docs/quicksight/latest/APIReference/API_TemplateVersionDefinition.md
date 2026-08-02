---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TemplateVersionDefinition.html
---

# TemplateVersionDefinition
<a name="API_TemplateVersionDefinition"></a>

The detailed definition of a template.

## Contents
<a name="API_TemplateVersionDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSetConfigurations **   <a name="QS-Type-TemplateVersionDefinition-DataSetConfigurations"></a>
An array of dataset configurations. These configurations define the required columns for each dataset used within a template.
Type: Array of [DataSetConfiguration](API_DataSetConfiguration.md) objects
Array Members: Maximum number of 30 items.
Required: Yes

 ** AnalysisDefaults **   <a name="QS-Type-TemplateVersionDefinition-AnalysisDefaults"></a>
The configuration for default analysis settings.
Type: [AnalysisDefaults](API_AnalysisDefaults.md) object
Required: No

 ** CalculatedFields **   <a name="QS-Type-TemplateVersionDefinition-CalculatedFields"></a>
An array of calculated field definitions for the template.
Type: Array of [CalculatedField](API_CalculatedField.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** ColumnConfigurations **   <a name="QS-Type-TemplateVersionDefinition-ColumnConfigurations"></a>
 An array of template-level column configurations. Column configurations are used to set default formatting for a column that's used throughout a template.
Type: Array of [ColumnConfiguration](API_ColumnConfiguration.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** FilterGroups **   <a name="QS-Type-TemplateVersionDefinition-FilterGroups"></a>
Filter definitions for a template.
For more information, see [Filtering Data](https://docs.aws.amazon.com/quicksight/latest/user/filtering-visual-data.html) in the *Amazon Quick Suite User Guide*.
Type: Array of [FilterGroup](API_FilterGroup.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** Options **   <a name="QS-Type-TemplateVersionDefinition-Options"></a>
An array of option definitions for a template.
Type: [AssetOptions](API_AssetOptions.md) object
Required: No

 ** ParameterDeclarations **   <a name="QS-Type-TemplateVersionDefinition-ParameterDeclarations"></a>
An array of parameter declarations for a template.
 *Parameters* are named variables that can transfer a value for use by an action or an object.
For more information, see [Parameters in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html) in the *Amazon Quick Suite User Guide*.
Type: Array of [ParameterDeclaration](API_ParameterDeclaration.md) objects
Array Members: Maximum number of 400 items.
Required: No

 ** QueryExecutionOptions **   <a name="QS-Type-TemplateVersionDefinition-QueryExecutionOptions"></a>
A structure that describes the query execution options.
Type: [QueryExecutionOptions](API_QueryExecutionOptions.md) object
Required: No

 ** Sheets **   <a name="QS-Type-TemplateVersionDefinition-Sheets"></a>
An array of sheet definitions for a template.
Type: Array of [SheetDefinition](API_SheetDefinition.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** StaticFiles **   <a name="QS-Type-TemplateVersionDefinition-StaticFiles"></a>
The static files for the definition.
Type: Array of [StaticFile](API_StaticFile.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** TooltipSheets **   <a name="QS-Type-TemplateVersionDefinition-TooltipSheets"></a>
An array of tooltip sheet definitions for a template.
Type: Array of [TooltipSheetDefinition](API_TooltipSheetDefinition.md) objects
Array Members: Maximum number of 50 items.
Required: No

## See Also
<a name="API_TemplateVersionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TemplateVersionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TemplateVersionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TemplateVersionDefinition)
