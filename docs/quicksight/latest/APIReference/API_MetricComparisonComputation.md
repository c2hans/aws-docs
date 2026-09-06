---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_MetricComparisonComputation.html
---

# MetricComparisonComputation
<a name="API_MetricComparisonComputation"></a>

The metric comparison computation configuration.

## Contents
<a name="API_MetricComparisonComputation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComputationId **   <a name="QS-Type-MetricComparisonComputation-ComputationId"></a>
The ID for a computation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** FromValue **   <a name="QS-Type-MetricComparisonComputation-FromValue"></a>
The field that is used in a metric comparison from value setup.
Type: [MeasureField](API_MeasureField.md) object
Required: No

 ** Name **   <a name="QS-Type-MetricComparisonComputation-Name"></a>
The name of a computation.
Type: String
Required: No

 ** TargetValue **   <a name="QS-Type-MetricComparisonComputation-TargetValue"></a>
The field that is used in a metric comparison to value setup.
Type: [MeasureField](API_MeasureField.md) object
Required: No

 ** Time **   <a name="QS-Type-MetricComparisonComputation-Time"></a>
The time field that is used in a computation.
Type: [DimensionField](API_DimensionField.md) object
Required: No

## See Also
<a name="API_MetricComparisonComputation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/MetricComparisonComputation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/MetricComparisonComputation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/MetricComparisonComputation)
