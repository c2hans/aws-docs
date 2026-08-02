---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_MetricDimensionGroups.html
---

# MetricDimensionGroups
<a name="API_MetricDimensionGroups"></a>

The available dimension information for a metric type.

## Contents
<a name="API_MetricDimensionGroups_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Groups **   <a name="performanceinsights-Type-MetricDimensionGroups-Groups"></a>
The available dimension groups for a metric type.
Type: Array of [DimensionGroupDetail](API_DimensionGroupDetail.md) objects
Required: No

 ** Metric **   <a name="performanceinsights-Type-MetricDimensionGroups-Metric"></a>
The metric type to which the dimension information belongs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_MetricDimensionGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/MetricDimensionGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/MetricDimensionGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/MetricDimensionGroups)
