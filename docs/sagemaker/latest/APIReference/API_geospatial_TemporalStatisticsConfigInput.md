---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_TemporalStatisticsConfigInput.html
---

# TemporalStatisticsConfigInput
<a name="API_geospatial_TemporalStatisticsConfigInput"></a>

The structure representing the configuration for Temporal Statistics operation.

## Contents
<a name="API_geospatial_TemporalStatisticsConfigInput_Contents"></a>

 ** Statistics **   <a name="sagemaker-Type-geospatial_TemporalStatisticsConfigInput-Statistics"></a>
The list of the statistics method options.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `MEAN | MEDIAN | STANDARD_DEVIATION`
Required: Yes

 ** GroupBy **   <a name="sagemaker-Type-geospatial_TemporalStatisticsConfigInput-GroupBy"></a>
The input for the temporal statistics grouping by time frequency option.
Type: String
Valid Values: `ALL | YEARLY`
Required: No

 ** TargetBands **   <a name="sagemaker-Type-geospatial_TemporalStatisticsConfigInput-TargetBands"></a>
The list of target band names for the temporal statistic to calculate.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_geospatial_TemporalStatisticsConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/TemporalStatisticsConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/TemporalStatisticsConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/TemporalStatisticsConfigInput)
