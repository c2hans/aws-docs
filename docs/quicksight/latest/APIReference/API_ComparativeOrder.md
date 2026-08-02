---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ComparativeOrder.html
---

# ComparativeOrder
<a name="API_ComparativeOrder"></a>

A structure that represents a comparative order.

## Contents
<a name="API_ComparativeOrder_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SpecifedOrder **   <a name="QS-Type-ComparativeOrder-SpecifedOrder"></a>
The list of columns to be used in the ordering.
Type: Array of strings
Required: No

 ** TreatUndefinedSpecifiedValues **   <a name="QS-Type-ComparativeOrder-TreatUndefinedSpecifiedValues"></a>
The treat of undefined specified values. Valid values for this structure are `LEAST` and `MOST`.
Type: String
Valid Values: `LEAST | MOST`
Required: No

 ** UseOrdering **   <a name="QS-Type-ComparativeOrder-UseOrdering"></a>
The ordering type for a column. Valid values for this structure are `GREATER_IS_BETTER`, `LESSER_IS_BETTER` and `SPECIFIED`.
Type: String
Valid Values: `GREATER_IS_BETTER | LESSER_IS_BETTER | SPECIFIED`
Required: No

## See Also
<a name="API_ComparativeOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ComparativeOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ComparativeOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ComparativeOrder)
