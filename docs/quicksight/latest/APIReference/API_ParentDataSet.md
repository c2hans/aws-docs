---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ParentDataSet.html
---

# ParentDataSet
<a name="API_ParentDataSet"></a>

References a parent dataset that serves as a data source, including its columns and metadata.

## Contents
<a name="API_ParentDataSet_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSetArn **   <a name="QS-Type-ParentDataSet-DataSetArn"></a>
The Amazon Resource Name (ARN) of the parent dataset.
Type: String
Required: Yes

 ** InputColumns **   <a name="QS-Type-ParentDataSet-InputColumns"></a>
The list of input columns available from the parent dataset.
Type: Array of [InputColumn](API_InputColumn.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2048 items.
Required: Yes

## See Also
<a name="API_ParentDataSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ParentDataSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ParentDataSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ParentDataSet)
