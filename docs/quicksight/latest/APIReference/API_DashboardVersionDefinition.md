---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DashboardVersionDefinition.html
---

# DashboardVersionDefinition
<a name="API_DashboardVersionDefinition"></a>

The contents of a dashboard.

## Contents
<a name="API_DashboardVersionDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSetIdentifierDeclarations **   <a name="QS-Type-DashboardVersionDefinition-DataSetIdentifierDeclarations"></a>
An array of dataset identifier declarations. With this mapping,you can use dataset identifiers instead of dataset Amazon Resource Names (ARNs) throughout the dashboard's sub-structures.
Type: Array of [DataSetIdentifierDeclaration](API_DataSetIdentifierDeclaration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 ** AnalysisDefaults **   <a name="QS-Type-DashboardVersionDefinition-AnalysisDefaults"></a>
The configuration for default analysis settings.
Type: [AnalysisDefaults](API_AnalysisDefaults.md) object
Required: No

 ** CalculatedFields **   <a name="QS-Type-DashboardVersionDefinition-CalculatedFields"></a>
An array of calculated field definitions for the dashboard.
Type: Array of [CalculatedField](API_CalculatedField.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** ColumnConfigurations **   <a name="QS-Type-DashboardVersionDefinition-ColumnConfigurations"></a>
An array of dashboard-level column configurations. Column configurations are used to set the default formatting for a column that is used throughout a dashboard.
Type: Array of [ColumnConfiguration](API_ColumnConfiguration.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** FilterGroups **   <a name="QS-Type-DashboardVersionDefinition-FilterGroups"></a>
The filter definitions for a dashboard.
For more information, see [Filtering Data in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/adding-a-filter.html) in the *Amazon Quick Suite User Guide*.
Type: Array of [FilterGroup](API_FilterGroup.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** Options **   <a name="QS-Type-DashboardVersionDefinition-Options"></a>
An array of option definitions for a dashboard.
Type: [AssetOptions](API_AssetOptions.md) object
Required: No

 ** ParameterDeclarations **   <a name="QS-Type-DashboardVersionDefinition-ParameterDeclarations"></a>
The parameter declarations for a dashboard. Parameters are named variables that can transfer a value for use by an action or an object.
For more information, see [Parameters in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html) in the *Amazon Quick Suite User Guide*.
Type: Array of [ParameterDeclaration](API_ParameterDeclaration.md) objects
Array Members: Maximum number of 400 items.
Required: No

 ** Sheets **   <a name="QS-Type-DashboardVersionDefinition-Sheets"></a>
An array of sheet definitions for a dashboard.
Type: Array of [SheetDefinition](API_SheetDefinition.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** StaticFiles **   <a name="QS-Type-DashboardVersionDefinition-StaticFiles"></a>
The static files for the definition.
Type: Array of [StaticFile](API_StaticFile.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** TooltipSheets **   <a name="QS-Type-DashboardVersionDefinition-TooltipSheets"></a>
An array of tooltip sheet definitions for a dashboard.
Type: Array of [TooltipSheetDefinition](API_TooltipSheetDefinition.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** TopicIdentifierDeclarations **   <a name="QS-Type-DashboardVersionDefinition-TopicIdentifierDeclarations"></a>
An array of topic identifier declarations. With this mapping, you can use topic identifiers instead of topic Amazon Resource Names (ARNs) throughout the dashboard's sub-structures.
Type: Array of [TopicIdentifierDeclaration](API_TopicIdentifierDeclaration.md) objects
Array Members: Maximum number of 50 items.
Required: No

## See Also
<a name="API_DashboardVersionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DashboardVersionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DashboardVersionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DashboardVersionDefinition)
