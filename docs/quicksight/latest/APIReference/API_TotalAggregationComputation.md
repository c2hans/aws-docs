---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TotalAggregationComputation.html
---

# TotalAggregationComputation
<a name="API_TotalAggregationComputation"></a>

The total aggregation computation configuration.

## Contents
<a name="API_TotalAggregationComputation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComputationId **   <a name="QS-Type-TotalAggregationComputation-ComputationId"></a>
The ID for a computation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Name **   <a name="QS-Type-TotalAggregationComputation-Name"></a>
The name of a computation.
Type: String
Required: No

 ** Value **   <a name="QS-Type-TotalAggregationComputation-Value"></a>
The value field that is used in a computation.
Type: [MeasureField](API_MeasureField.md) object
Required: No

## See Also
<a name="API_TotalAggregationComputation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TotalAggregationComputation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TotalAggregationComputation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TotalAggregationComputation)
