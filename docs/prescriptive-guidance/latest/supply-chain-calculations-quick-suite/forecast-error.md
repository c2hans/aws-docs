---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/supply-chain-calculations-quick-suite/forecast-error.html
---

# Forecast error
<a name="forecast-error"></a>

Forecast error calculations provide a quantitative estimate of the quality of past forecasts, and a wide range of calculations are available to help you statistically express the accuracy of a forecast.

The following table contains standard forecast error calculations.

|
|
| Name | Description | Calculation |
| --- |--- |--- |
| Bias | Bias is a consistent error that causes a forecast to be either too high or too low. A forecast is biased if there is a consistent difference between the actual and forecasted demand in current and historical forecasts. This calculation returns the forecast error, measuring consistent over or under-forecasting. | `(Sum actuals - Sum forecast) / Sum actuals` |
| Mean | The arithmetic average of a group of values. | `Average(values)` |
| Mean absolute deviation (MAD) | MAD shows how large, on average, an error is in the forecast. However, because MAD returns the average error in units, it's sometimes not very useful for comparisons. MAD is the average of the absolute values of the deviations between observed values and expected values. | `Average(Abs(forecast - actual))` |
| Mean absolute percent error (MAPE) | MAPE expresses the forecast error in relation to sales volume. Basically, it tells you how many percentage points the forecasts are off, on average. MAPE might be the most commonly used forecasting metric when planning demand. | MAPE is computed by taking the MAD, dividing by the average demand, and then multiplying by 100.<br />`(1 / sample size) × ∑((actual - forecast) / actual) × 100` |
| Mean absolute scaled error (MASE) | MASE is the mean absolute error of the forecast values, divided by the mean absolute error of the in-sample naive forecast. MASE is the recommended calculation for determining comparative accuracy of forecasts. | `Average(Abs(forecast - actual)) / ((1 / sample size) × ∑((actual - forecast) / actual))` |
| Mean squared error (MSE) | MSE measures the average squared difference between the estimated values and the actual values. Divide the sum of the residuals by the total number of data points, and then take the square root of the quotient. | `(1 / sample size) × Σ(actual – forecast)^2` |
| Tracking signal | This calculation measures persistent bias, either under-forecasting or over-forecasting. Tracking signal is the ratio of the cumulative algebraic sum of the deviation between forecasts and actual values to the mean absolute deviation. You can use this calculation to alert you when the forecast model is biased. | Ratio of the cumulative sum of forecast errors (the deviations between the estimated forecasts and the actual values) to the mean absolute deviation. *Mean absolute deviation* is ratio of the cumulative absolute sum of forecast errors (forecast and actual values) to the number of periods. |
| Weighted mean absolute percent error (WMAPE) | WMAPE weights the forecast error by actual demand**. **It gives weight to the prioritized item, biasing the forecast error toward it. Because MAPE does not account for possible differences in priority between products or moments in time, WMAPE is often used. | `∑ (weight\|forecast – actual demand\|) / ∑ (weight\|actual demand\|)` |
