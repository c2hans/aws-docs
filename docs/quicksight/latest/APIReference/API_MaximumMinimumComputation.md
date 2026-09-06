---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_MaximumMinimumComputation.html
---

# MaximumMinimumComputation
<a name="API_MaximumMinimumComputation"></a>

The maximum and minimum computation configuration.

## Contents
<a name="API_MaximumMinimumComputation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComputationId **   <a name="QS-Type-MaximumMinimumComputation-ComputationId"></a>
The ID for a computation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Type **   <a name="QS-Type-MaximumMinimumComputation-Type"></a>
The type of computation. Choose one of the following options:
+ MAXIMUM: A maximum computation.
+ MINIMUM: A minimum computation.
Type: String
Valid Values: `MAXIMUM | MINIMUM`
Required: Yes

 ** Name **   <a name="QS-Type-MaximumMinimumComputation-Name"></a>
The name of a computation.
Type: String
Required: No

 ** Time **   <a name="QS-Type-MaximumMinimumComputation-Time"></a>
The time field that is used in a computation.
Type: [DimensionField](API_DimensionField.md) object
Required: No

 ** Value **   <a name="QS-Type-MaximumMinimumComputation-Value"></a>
The value field that is used in a computation.
Type: [MeasureField](API_MeasureField.md) object
Required: No

## See Also
<a name="API_MaximumMinimumComputation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/MaximumMinimumComputation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/MaximumMinimumComputation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/MaximumMinimumComputation)
