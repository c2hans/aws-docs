---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterOperation.html
---

# FilterOperation
<a name="API_FilterOperation"></a>

A transform operation that filters rows based on a condition.

## Contents
<a name="API_FilterOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ConditionExpression **   <a name="QS-Type-FilterOperation-ConditionExpression"></a>
An expression that must evaluate to a Boolean value. Rows for which the expression evaluates to true are kept in the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** DateFilterCondition **   <a name="QS-Type-FilterOperation-DateFilterCondition"></a>
A date-based filter condition within a filter operation.
Type: [DataSetDateFilterCondition](API_DataSetDateFilterCondition.md) object
Required: No

 ** NumericFilterCondition **   <a name="QS-Type-FilterOperation-NumericFilterCondition"></a>
A numeric-based filter condition within a filter operation.
Type: [DataSetNumericFilterCondition](API_DataSetNumericFilterCondition.md) object
Required: No

 ** StringFilterCondition **   <a name="QS-Type-FilterOperation-StringFilterCondition"></a>
A string-based filter condition within a filter operation.
Type: [DataSetStringFilterCondition](API_DataSetStringFilterCondition.md) object
Required: No

## See Also
<a name="API_FilterOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterOperation)
