---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SourceTable.html
---

# SourceTable
<a name="API_SourceTable"></a>

A source table that provides initial data from either a physical table or parent dataset.

## Contents
<a name="API_SourceTable_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSet **   <a name="QS-Type-SourceTable-DataSet"></a>
A parent dataset that serves as the data source instead of a physical table.
Type: [ParentDataSet](API_ParentDataSet.md) object
Required: No

 ** PhysicalTableId **   <a name="QS-Type-SourceTable-PhysicalTableId"></a>
The identifier of the physical table that serves as the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-]*`
Required: No

## See Also
<a name="API_SourceTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SourceTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SourceTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SourceTable)
