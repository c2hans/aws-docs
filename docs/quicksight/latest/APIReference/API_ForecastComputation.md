---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ForecastComputation.html
---

# ForecastComputation
<a name="API_ForecastComputation"></a>

The forecast computation configuration.

## Contents
<a name="API_ForecastComputation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComputationId **   <a name="QS-Type-ForecastComputation-ComputationId"></a>
The ID for a computation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** CustomSeasonalityValue **   <a name="QS-Type-ForecastComputation-CustomSeasonalityValue"></a>
The custom seasonality value setup of a forecast computation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 180.
Required: No

 ** LowerBoundary **   <a name="QS-Type-ForecastComputation-LowerBoundary"></a>
The lower boundary setup of a forecast computation.
Type: Double
Required: No

 ** Name **   <a name="QS-Type-ForecastComputation-Name"></a>
The name of a computation.
Type: String
Required: No

 ** PeriodsBackward **   <a name="QS-Type-ForecastComputation-PeriodsBackward"></a>
The periods backward setup of a forecast computation.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** PeriodsForward **   <a name="QS-Type-ForecastComputation-PeriodsForward"></a>
The periods forward setup of a forecast computation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** PredictionInterval **   <a name="QS-Type-ForecastComputation-PredictionInterval"></a>
The prediction interval setup of a forecast computation.
Type: Integer
Valid Range: Minimum value of 50. Maximum value of 95.
Required: No

 ** Seasonality **   <a name="QS-Type-ForecastComputation-Seasonality"></a>
The seasonality setup of a forecast computation. Choose one of the following options:
+  `AUTOMATIC`
+  `CUSTOM`: Checks the custom seasonality value.
Type: String
Valid Values: `AUTOMATIC | CUSTOM`
Required: No

 ** Time **   <a name="QS-Type-ForecastComputation-Time"></a>
The time field that is used in a computation.
Type: [DimensionField](API_DimensionField.md) object
Required: No

 ** UpperBoundary **   <a name="QS-Type-ForecastComputation-UpperBoundary"></a>
The upper boundary setup of a forecast computation.
Type: Double
Required: No

 ** Value **   <a name="QS-Type-ForecastComputation-Value"></a>
The value field that is used in a computation.
Type: [MeasureField](API_MeasureField.md) object
Required: No

## See Also
<a name="API_ForecastComputation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ForecastComputation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ForecastComputation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ForecastComputation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
