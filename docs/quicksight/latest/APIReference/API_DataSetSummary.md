---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSetSummary.html
---

# DataSetSummary
<a name="API_DataSetSummary"></a>

Dataset summary.

## Contents
<a name="API_DataSetSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-DataSetSummary-Arn"></a>
The Amazon Resource Name (ARN) of the dataset.
Type: String
Required: No

 ** ColumnLevelPermissionRulesApplied **   <a name="QS-Type-DataSetSummary-ColumnLevelPermissionRulesApplied"></a>
A value that indicates if the dataset has column level permission configured.
Type: Boolean
Required: No

 ** CreatedTime **   <a name="QS-Type-DataSetSummary-CreatedTime"></a>
The time that this dataset was created.
Type: Timestamp
Required: No

 ** DataSetId **   <a name="QS-Type-DataSetSummary-DataSetId"></a>
The ID of the dataset.
Type: String
Required: No

 ** ImportMode **   <a name="QS-Type-DataSetSummary-ImportMode"></a>
A value that indicates whether you want to import the data into SPICE.
Type: String
Valid Values: `SPICE | DIRECT_QUERY`
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-DataSetSummary-LastUpdatedTime"></a>
The last time that this dataset was updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-DataSetSummary-Name"></a>
A display name for the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** RowLevelPermissionDataSet **   <a name="QS-Type-DataSetSummary-RowLevelPermissionDataSet"></a>
The row-level security configuration for the dataset in the legacy data preparation experience.
Type: [RowLevelPermissionDataSet](API_RowLevelPermissionDataSet.md) object
Required: No

 ** RowLevelPermissionDataSetMap **   <a name="QS-Type-DataSetSummary-RowLevelPermissionDataSetMap"></a>
The row-level security configuration for the dataset in the new data preparation experience.
Type: String to [RowLevelPermissionDataSet](API_RowLevelPermissionDataSet.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[0-9a-zA-Z-]*`
Required: No

 ** RowLevelPermissionTagConfigurationApplied **   <a name="QS-Type-DataSetSummary-RowLevelPermissionTagConfigurationApplied"></a>
Whether or not the row level permission tags are applied.
Type: Boolean
Required: No

 ** UseAs **   <a name="QS-Type-DataSetSummary-UseAs"></a>
The usage of the dataset.
Type: String
Valid Values: `RLS_RULES`
Required: No

## See Also
<a name="API_DataSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSetSummary)
