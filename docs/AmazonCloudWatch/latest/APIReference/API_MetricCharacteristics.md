---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricCharacteristics.html
---

# MetricCharacteristics
<a name="API_MetricCharacteristics"></a>

This object includes parameters that you can use to provide information to CloudWatch to help it build more accurate anomaly detection models.

## Contents
<a name="API_MetricCharacteristics_Contents"></a>

 ** PeriodicSpikes **   <a name="ACW-Type-MetricCharacteristics-PeriodicSpikes"></a>
Set this parameter to `true` if values for this metric consistently include spikes that should not be considered to be anomalies. With this set to `true`, CloudWatch will expect to see spikes that occurred consistently during the model training period, and won't flag future similar spikes as anomalies.
Type: Boolean
Required: No

## See Also
<a name="API_MetricCharacteristics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricCharacteristics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricCharacteristics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricCharacteristics)
