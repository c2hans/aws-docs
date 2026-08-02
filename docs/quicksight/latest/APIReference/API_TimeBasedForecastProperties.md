---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TimeBasedForecastProperties.html
---

# TimeBasedForecastProperties
<a name="API_TimeBasedForecastProperties"></a>

The forecast properties setup of a forecast in the line chart.

## Contents
<a name="API_TimeBasedForecastProperties_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LowerBoundary **   <a name="QS-Type-TimeBasedForecastProperties-LowerBoundary"></a>
The lower boundary setup of a forecast computation.
Type: Double
Required: No

 ** PeriodsBackward **   <a name="QS-Type-TimeBasedForecastProperties-PeriodsBackward"></a>
The periods backward setup of a forecast computation.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** PeriodsForward **   <a name="QS-Type-TimeBasedForecastProperties-PeriodsForward"></a>
The periods forward setup of a forecast computation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** PredictionInterval **   <a name="QS-Type-TimeBasedForecastProperties-PredictionInterval"></a>
The prediction interval setup of a forecast computation.
Type: Integer
Valid Range: Minimum value of 50. Maximum value of 95.
Required: No

 ** Seasonality **   <a name="QS-Type-TimeBasedForecastProperties-Seasonality"></a>
The seasonality setup of a forecast computation. Choose one of the following options:
+  `NULL`: The input is set to `NULL`.
+  `NON_NULL`: The input is set to a custom value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 180.
Required: No

 ** UpperBoundary **   <a name="QS-Type-TimeBasedForecastProperties-UpperBoundary"></a>
The upper boundary setup of a forecast computation.
Type: Double
Required: No

## See Also
<a name="API_TimeBasedForecastProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TimeBasedForecastProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TimeBasedForecastProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TimeBasedForecastProperties)
