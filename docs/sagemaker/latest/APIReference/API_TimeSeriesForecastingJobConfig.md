---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesForecastingJobConfig.html
---

# TimeSeriesForecastingJobConfig
<a name="API_TimeSeriesForecastingJobConfig"></a>

The collection of settings used by an AutoML job V2 for the time-series forecasting problem type.

## Contents
<a name="API_TimeSeriesForecastingJobConfig_Contents"></a>

 ** ForecastFrequency **   <a name="sagemaker-Type-TimeSeriesForecastingJobConfig-ForecastFrequency"></a>
The frequency of predictions in a forecast.
Valid intervals are an integer followed by Y (Year), M (Month), W (Week), D (Day), H (Hour), and min (Minute). For example, `1D` indicates every day and `15min` indicates every 15 minutes. The value of a frequency must not overlap with the next larger frequency. For example, you must use a frequency of `1H` instead of `60min`.
The valid values for each frequency are the following:
+ Minute - 1-59
+ Hour - 1-23
+ Day - 1-6
+ Week - 1-4
+ Month - 1-11
+ Year - 1
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `1Y|Y|([1-9]|1[0-1])M|M|[1-4]W|W|[1-6]D|D|([1-9]|1[0-9]|2[0-3])H|H|([1-9]|[1-5][0-9])min`
Required: Yes

 ** ForecastHorizon **   <a name="sagemaker-Type-TimeSeriesForecastingJobConfig-ForecastHorizon"></a>
The number of time-steps that the model predicts. The forecast horizon is also called the prediction length. The maximum forecast horizon is the lesser of 500 time-steps or 1/4 of the time-steps in the dataset.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** TimeSeriesConfig **   <a name="sagemaker-Type-TimeSeriesForecastingJobConfig-TimeSeriesConfig"></a>
The collection of components that defines the time-series.
Type: [TimeSeriesConfig](API_TimeSeriesConfig.md) object
Required: Yes

 ** CandidateGenerationConfig **   <a name="sagemaker-Type-TimeSeriesForecastingJobConfig-CandidateGenerationConfig"></a>
Stores the configuration information for how model candidates are generated using an AutoML job V2.
Type: [CandidateGenerationConfig](API_CandidateGenerationConfig.md) object
Required: No

 ** CompletionCriteria **   <a name="sagemaker-Type-TimeSeriesForecastingJobConfig-CompletionCriteria"></a>
How long a job is allowed to run, or how many candidates a job is allowed to generate.
Type: [AutoMLJobCompletionCriteria](API_AutoMLJobCompletionCriteria.md) object
Required: No

 ** FeatureSpecificationS3Uri **   <a name="sagemaker-Type-TimeSeriesForecastingJobConfig-FeatureSpecificationS3Uri"></a>
A URL to the Amazon S3 data source containing additional selected features that complement the target, itemID, timestamp, and grouped columns set in `TimeSeriesConfig`. When not provided, the AutoML job V2 includes all the columns from the original dataset that are not already declared in `TimeSeriesConfig`. If provided, the AutoML job V2 only considers these additional columns as a complement to the ones declared in `TimeSeriesConfig`.
You can input `FeatureAttributeNames` (optional) in JSON format as shown below:
 `{ "FeatureAttributeNames":["col1", "col2", ...] }`.
You can also specify the data type of the feature (optional) in the format shown below:
 `{ "FeatureDataTypes":{"col1":"numeric", "col2":"categorical" ... } }`
Autopilot supports the following data types: `numeric`, `categorical`, `text`, and `datetime`.
These column keys must not include any column set in `TimeSeriesConfig`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** ForecastQuantiles **   <a name="sagemaker-Type-TimeSeriesForecastingJobConfig-ForecastQuantiles"></a>
The quantiles used to train the model for forecasts at a specified quantile. You can specify quantiles from `0.01` (p1) to `0.99` (p99), by increments of 0.01 or higher. Up to five forecast quantiles can be specified. When `ForecastQuantiles` is not provided, the AutoML job uses the quantiles p10, p50, and p90 as default.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 2. Maximum length of 4.
Pattern: `(^p[1-9]\d?$)`
Required: No

 ** HolidayConfig **   <a name="sagemaker-Type-TimeSeriesForecastingJobConfig-HolidayConfig"></a>
The collection of holiday featurization attributes used to incorporate national holiday information into your forecasting model.
Type: Array of [HolidayConfigAttributes](API_HolidayConfigAttributes.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Transformations **   <a name="sagemaker-Type-TimeSeriesForecastingJobConfig-Transformations"></a>
The transformations modifying specific attributes of the time-series, such as filling strategies for missing values.
Type: [TimeSeriesTransformations](API_TimeSeriesTransformations.md) object
Required: No

## See Also
<a name="API_TimeSeriesForecastingJobConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TimeSeriesForecastingJobConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TimeSeriesForecastingJobConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TimeSeriesForecastingJobConfig)
