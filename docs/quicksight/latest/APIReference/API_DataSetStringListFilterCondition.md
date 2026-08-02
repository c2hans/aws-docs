---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSetStringListFilterCondition.html
---

# DataSetStringListFilterCondition
<a name="API_DataSetStringListFilterCondition"></a>

A filter condition that includes or excludes string values from a specified list.

## Contents
<a name="API_DataSetStringListFilterCondition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Operator **   <a name="QS-Type-DataSetStringListFilterCondition-Operator"></a>
The list operator to use, either `INCLUDE` to match values in the list or `EXCLUDE` to filter out values in the list.
Type: String
Valid Values: `INCLUDE | EXCLUDE`
Required: Yes

 ** Values **   <a name="QS-Type-DataSetStringListFilterCondition-Values"></a>
The list of string values to include or exclude in the filter.
Type: [DataSetStringListFilterValue](API_DataSetStringListFilterValue.md) object
Required: No

## See Also
<a name="API_DataSetStringListFilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSetStringListFilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSetStringListFilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSetStringListFilterCondition)
