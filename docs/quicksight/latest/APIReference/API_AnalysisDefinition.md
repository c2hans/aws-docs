---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AnalysisDefinition.html
---

# AnalysisDefinition
<a name="API_AnalysisDefinition"></a>

The definition of an analysis.

## Contents
<a name="API_AnalysisDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSetIdentifierDeclarations **   <a name="QS-Type-AnalysisDefinition-DataSetIdentifierDeclarations"></a>
An array of dataset identifier declarations. This mapping allows the usage of dataset identifiers instead of dataset ARNs throughout analysis sub-structures.
Type: Array of [DataSetIdentifierDeclaration](API_DataSetIdentifierDeclaration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 ** AnalysisDefaults **   <a name="QS-Type-AnalysisDefinition-AnalysisDefaults"></a>
The configuration for default analysis settings.
Type: [AnalysisDefaults](API_AnalysisDefaults.md) object
Required: No

 ** CalculatedFields **   <a name="QS-Type-AnalysisDefinition-CalculatedFields"></a>
An array of calculated field definitions for the analysis.
Type: Array of [CalculatedField](API_CalculatedField.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** ColumnConfigurations **   <a name="QS-Type-AnalysisDefinition-ColumnConfigurations"></a>
 An array of analysis-level column configurations. Column configurations can be used to set default formatting for a column to be used throughout an analysis.
Type: Array of [ColumnConfiguration](API_ColumnConfiguration.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** FilterGroups **   <a name="QS-Type-AnalysisDefinition-FilterGroups"></a>
Filter definitions for an analysis.
For more information, see [Filtering Data in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/adding-a-filter.html) in the *Amazon Quick Suite User Guide*.
Type: Array of [FilterGroup](API_FilterGroup.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** Options **   <a name="QS-Type-AnalysisDefinition-Options"></a>
An array of option definitions for an analysis.
Type: [AssetOptions](API_AssetOptions.md) object
Required: No

 ** ParameterDeclarations **   <a name="QS-Type-AnalysisDefinition-ParameterDeclarations"></a>
An array of parameter declarations for an analysis.
Parameters are named variables that can transfer a value for use by an action or an object.
For more information, see [Parameters in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html) in the *Amazon Quick Suite User Guide*.
Type: Array of [ParameterDeclaration](API_ParameterDeclaration.md) objects
Array Members: Maximum number of 400 items.
Required: No

 ** QueryExecutionOptions **   <a name="QS-Type-AnalysisDefinition-QueryExecutionOptions"></a>
A structure that describes the query execution options.
Type: [QueryExecutionOptions](API_QueryExecutionOptions.md) object
Required: No

 ** Sheets **   <a name="QS-Type-AnalysisDefinition-Sheets"></a>
An array of sheet definitions for an analysis. Each `SheetDefinition` provides detailed information about a sheet within this analysis.
Type: Array of [SheetDefinition](API_SheetDefinition.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** StaticFiles **   <a name="QS-Type-AnalysisDefinition-StaticFiles"></a>
The static files for the definition.
Type: Array of [StaticFile](API_StaticFile.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** TooltipSheets **   <a name="QS-Type-AnalysisDefinition-TooltipSheets"></a>
An array of tooltip sheet definitions for an analysis. Each `TooltipSheetDefinition` provides detailed information about a tooltip sheet within this analysis.
Type: Array of [TooltipSheetDefinition](API_TooltipSheetDefinition.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** TopicIdentifierDeclarations **   <a name="QS-Type-AnalysisDefinition-TopicIdentifierDeclarations"></a>
An array of topic identifier declarations. This mapping allows the usage of topic identifiers instead of topic ARNs throughout analysis sub-structures.
Type: Array of [TopicIdentifierDeclaration](API_TopicIdentifierDeclaration.md) objects
Array Members: Maximum number of 50 items.
Required: No

## See Also
<a name="API_AnalysisDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AnalysisDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AnalysisDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AnalysisDefinition)
