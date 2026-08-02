---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_MetricValue.html
---

# MetricValue
<a name="API_MetricValue"></a>

The value to be compared with the `metric`.

## Contents
<a name="API_MetricValue_Contents"></a>

 ** cidrs **   <a name="iot-Type-MetricValue-cidrs"></a>
If the `comparisonOperator` calls for a set of CIDRs, use this to specify that set to be compared with the `metric`.
Type: Array of strings
Length Constraints: Minimum length of 2. Maximum length of 43.
Pattern: `[a-fA-F0-9:\.\/]+`
Required: No

 ** count **   <a name="iot-Type-MetricValue-count"></a>
If the `comparisonOperator` calls for a numeric value, use this to specify that numeric value to be compared with the `metric`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** number **   <a name="iot-Type-MetricValue-number"></a>
 The numeral value of a metric.
Type: Double
Required: No

 ** numbers **   <a name="iot-Type-MetricValue-numbers"></a>
 The numeral values of a metric.
Type: Array of doubles
Required: No

 ** ports **   <a name="iot-Type-MetricValue-ports"></a>
If the `comparisonOperator` calls for a set of ports, use this to specify that set to be compared with the `metric`.
Type: Array of integers
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** strings **   <a name="iot-Type-MetricValue-strings"></a>
 The string values of a metric.
Type: Array of strings
Required: No

## See Also
<a name="API_MetricValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/MetricValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/MetricValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/MetricValue)
