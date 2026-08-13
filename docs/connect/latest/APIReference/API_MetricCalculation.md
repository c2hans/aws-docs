---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MetricCalculation.html
---

# MetricCalculation
<a name="API_MetricCalculation"></a>

Contains the formula and component metrics that define a custom metric calculation.

## Contents
<a name="API_MetricCalculation_Contents"></a>

 ** Calculation **   <a name="connect-Type-MetricCalculation-Calculation"></a>
The formula expression that defines how the metric is calculated. Uses component aliases (for example, `100 * SUM(M1) / SUM(M2)`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** CalculationComponents **   <a name="connect-Type-MetricCalculation-CalculationComponents"></a>
The list of component metrics referenced in the calculation formula. Each component has an alias used in the formula expression.
Type: Array of [CalculationComponent](API_CalculationComponent.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

## See Also
<a name="API_MetricCalculation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MetricCalculation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MetricCalculation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MetricCalculation)
