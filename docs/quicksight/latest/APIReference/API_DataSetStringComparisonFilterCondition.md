---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSetStringComparisonFilterCondition.html
---

# DataSetStringComparisonFilterCondition
<a name="API_DataSetStringComparisonFilterCondition"></a>

A filter condition that compares string values using operators like `EQUALS`, `CONTAINS`, or `STARTS_WITH`.

## Contents
<a name="API_DataSetStringComparisonFilterCondition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Operator **   <a name="QS-Type-DataSetStringComparisonFilterCondition-Operator"></a>
The comparison operator to use, such as `EQUALS`, `CONTAINS`, `STARTS_WITH`, `ENDS_WITH`, or their negations.
Type: String
Valid Values: `EQUALS | DOES_NOT_EQUAL | CONTAINS | DOES_NOT_CONTAIN | STARTS_WITH | ENDS_WITH`
Required: Yes

 ** Value **   <a name="QS-Type-DataSetStringComparisonFilterCondition-Value"></a>
The string value to compare against.
Type: [DataSetStringFilterValue](API_DataSetStringFilterValue.md) object
Required: No

## See Also
<a name="API_DataSetStringComparisonFilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSetStringComparisonFilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSetStringComparisonFilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSetStringComparisonFilterCondition)
