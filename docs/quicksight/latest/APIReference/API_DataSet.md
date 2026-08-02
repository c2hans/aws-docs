---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSet.html
---

# DataSet
<a name="API_DataSet"></a>

Dataset.

## Contents
<a name="API_DataSet_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-DataSet-Arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** ColumnGroups **   <a name="QS-Type-DataSet-ColumnGroups"></a>
Groupings of columns that work together in certain Quick Sight features. Currently, only geospatial hierarchy is supported.
Type: Array of [ColumnGroup](API_ColumnGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Required: No

 ** ColumnLevelPermissionRules **   <a name="QS-Type-DataSet-ColumnLevelPermissionRules"></a>
A set of one or more definitions of a ` [ColumnLevelPermissionRule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnLevelPermissionRule.html) `.
Type: Array of [ColumnLevelPermissionRule](API_ColumnLevelPermissionRule.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** ConsumedSpiceCapacityInBytes **   <a name="QS-Type-DataSet-ConsumedSpiceCapacityInBytes"></a>
The amount of SPICE capacity used by this dataset. This is 0 if the dataset isn't imported into SPICE.
Type: Long
Required: No

 ** CreatedTime **   <a name="QS-Type-DataSet-CreatedTime"></a>
The time that this dataset was created.
Type: Timestamp
Required: No

 ** DataPrepConfiguration **   <a name="QS-Type-DataSet-DataPrepConfiguration"></a>
The data preparation configuration associated with this dataset.
Type: [DataPrepConfiguration](API_DataPrepConfiguration.md) object
Required: No

 ** DataSetId **   <a name="QS-Type-DataSet-DataSetId"></a>
The ID of the dataset. Limited to 96 characters.
Type: String
Required: No

 ** DatasetParameters **   <a name="QS-Type-DataSet-DatasetParameters"></a>
The parameters that are declared in a dataset.
Type: Array of [DatasetParameter](API_DatasetParameter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** DataSetUsageConfiguration **   <a name="QS-Type-DataSet-DataSetUsageConfiguration"></a>
The usage configuration to apply to child datasets that reference this dataset as a source.
Type: [DataSetUsageConfiguration](API_DataSetUsageConfiguration.md) object
Required: No

 ** FieldFolders **   <a name="QS-Type-DataSet-FieldFolders"></a>
The folder that contains fields and nested subfolders for your dataset.
Type: String to [FieldFolder](API_FieldFolder.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** ImportMode **   <a name="QS-Type-DataSet-ImportMode"></a>
A value that indicates whether you want to import the data into SPICE.
Type: String
Valid Values: `SPICE | DIRECT_QUERY`
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-DataSet-LastUpdatedTime"></a>
The last time that this dataset was updated.
Type: Timestamp
Required: No

 ** LogicalTableMap **   <a name="QS-Type-DataSet-LogicalTableMap"></a>
Configures the combination and transformation of the data from the physical tables.
Type: String to [LogicalTable](API_LogicalTable.md) object map
Map Entries: Maximum number of 64 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[0-9a-zA-Z-]*`
Required: No

 ** Name **   <a name="QS-Type-DataSet-Name"></a>
A display name for the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** OutputColumns **   <a name="QS-Type-DataSet-OutputColumns"></a>
The list of columns after all transforms. These columns are available in templates, analyses, and dashboards.
Type: Array of [OutputColumn](API_OutputColumn.md) objects
Required: No

 ** PerformanceConfiguration **   <a name="QS-Type-DataSet-PerformanceConfiguration"></a>
The performance optimization configuration of a dataset.
Type: [PerformanceConfiguration](API_PerformanceConfiguration.md) object
Required: No

 ** PhysicalTableMap **   <a name="QS-Type-DataSet-PhysicalTableMap"></a>
Declares the physical tables that are available in the underlying data sources.
Type: String to [PhysicalTable](API_PhysicalTable.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 32 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[0-9a-zA-Z-]*`
Required: No

 ** RowLevelPermissionDataSet **   <a name="QS-Type-DataSet-RowLevelPermissionDataSet"></a>
The row-level security configuration for the dataset.
Type: [RowLevelPermissionDataSet](API_RowLevelPermissionDataSet.md) object
Required: No

 ** RowLevelPermissionTagConfiguration **   <a name="QS-Type-DataSet-RowLevelPermissionTagConfiguration"></a>
The element you can use to define tags for row-level security.
Type: [RowLevelPermissionTagConfiguration](API_RowLevelPermissionTagConfiguration.md) object
Required: No

 ** SemanticModelConfiguration **   <a name="QS-Type-DataSet-SemanticModelConfiguration"></a>
The semantic model configuration associated with this dataset.
Type: [SemanticModelConfiguration](API_SemanticModelConfiguration.md) object
Required: No

 ** UseAs **   <a name="QS-Type-DataSet-UseAs"></a>
The usage of the dataset.
Type: String
Valid Values: `RLS_RULES`
Required: No

## See Also
<a name="API_DataSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSet)
