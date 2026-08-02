---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_BehaviorCriteria.html
---

# BehaviorCriteria
<a name="API_BehaviorCriteria"></a>

The criteria by which the behavior is determined to be normal.

## Contents
<a name="API_BehaviorCriteria_Contents"></a>

 ** comparisonOperator **   <a name="iot-Type-BehaviorCriteria-comparisonOperator"></a>
The operator that relates the thing measured (`metric`) to the criteria (containing a `value` or `statisticalThreshold`). Valid operators include:
+  `string-list`: `in-set` and `not-in-set`
+  `number-list`: `in-set` and `not-in-set`
+  `ip-address-list`: `in-cidr-set` and `not-in-cidr-set`
+  `number`: `less-than`, `less-than-equals`, `greater-than`, and `greater-than-equals`
Type: String
Valid Values: `less-than | less-than-equals | greater-than | greater-than-equals | in-cidr-set | not-in-cidr-set | in-port-set | not-in-port-set | in-set | not-in-set`
Required: No

 ** consecutiveDatapointsToAlarm **   <a name="iot-Type-BehaviorCriteria-consecutiveDatapointsToAlarm"></a>
If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** consecutiveDatapointsToClear **   <a name="iot-Type-BehaviorCriteria-consecutiveDatapointsToClear"></a>
If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** durationSeconds **   <a name="iot-Type-BehaviorCriteria-durationSeconds"></a>
Use this to specify the time duration over which the behavior is evaluated, for those criteria that have a time dimension (for example, `NUM_MESSAGES_SENT`). For a `statisticalThreshhold` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank. Cannot be used with list-based metric datatypes.
Type: Integer
Required: No

 ** mlDetectionConfig **   <a name="iot-Type-BehaviorCriteria-mlDetectionConfig"></a>
 The configuration of an ML Detect
Type: [MachineLearningDetectionConfig](API_MachineLearningDetectionConfig.md) object
Required: No

 ** statisticalThreshold **   <a name="iot-Type-BehaviorCriteria-statisticalThreshold"></a>
A statistical ranking (percentile)that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
Type: [StatisticalThreshold](API_StatisticalThreshold.md) object
Required: No

 ** value **   <a name="iot-Type-BehaviorCriteria-value"></a>
The value to be compared with the `metric`.
Type: [MetricValue](API_MetricValue.md) object
Required: No

## See Also
<a name="API_BehaviorCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/BehaviorCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/BehaviorCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/BehaviorCriteria)
