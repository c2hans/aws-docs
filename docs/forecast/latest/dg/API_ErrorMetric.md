---
source_url: https://docs.aws.amazon.com/forecast/latest/dg/API_ErrorMetric.html
---

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# ErrorMetric
<a name="API_ErrorMetric"></a>

 Provides detailed error metrics to evaluate the performance of a predictor. This object is part of the [Metrics](API_Metrics.md) object.

## Contents
<a name="API_ErrorMetric_Contents"></a>

 ** ForecastType **   <a name="forecast-Type-ErrorMetric-ForecastType"></a>
 The Forecast type used to compute WAPE, MAPE, MASE, and RMSE.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 4.
Pattern: `(^0?\.\d\d?$|^mean$)`
Required: No

 ** MAPE **   <a name="forecast-Type-ErrorMetric-MAPE"></a>
The Mean Absolute Percentage Error (MAPE)
Type: Double
Required: No

 ** MASE **   <a name="forecast-Type-ErrorMetric-MASE"></a>
The Mean Absolute Scaled Error (MASE)
Type: Double
Required: No

 ** RMSE **   <a name="forecast-Type-ErrorMetric-RMSE"></a>
 The root-mean-square error (RMSE).
Type: Double
Required: No

 ** WAPE **   <a name="forecast-Type-ErrorMetric-WAPE"></a>
 The weighted absolute percentage error (WAPE).
Type: Double
Required: No

## See Also
<a name="API_ErrorMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/ErrorMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/ErrorMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/ErrorMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Forecast. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query forecast` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
