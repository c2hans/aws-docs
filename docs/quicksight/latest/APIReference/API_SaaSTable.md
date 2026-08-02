---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SaaSTable.html
---

# SaaSTable
<a name="API_SaaSTable"></a>

A table from a Software-as-a-Service (SaaS) data source, including connection details and column definitions.

## Contents
<a name="API_SaaSTable_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSourceArn **   <a name="QS-Type-SaaSTable-DataSourceArn"></a>
The Amazon Resource Name (ARN) of the SaaS data source.
Type: String
Required: Yes

 ** InputColumns **   <a name="QS-Type-SaaSTable-InputColumns"></a>
The list of input columns available from the SaaS table.
Type: Array of [InputColumn](API_InputColumn.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2048 items.
Required: Yes

 ** TablePath **   <a name="QS-Type-SaaSTable-TablePath"></a>
The hierarchical path to the table within the SaaS data source.
Type: Array of [TablePathElement](API_TablePathElement.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: Yes

## See Also
<a name="API_SaaSTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SaaSTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SaaSTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SaaSTable)
