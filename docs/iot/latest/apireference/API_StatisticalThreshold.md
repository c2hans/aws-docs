---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_StatisticalThreshold.html
---

# StatisticalThreshold
<a name="API_StatisticalThreshold"></a>

A statistical ranking (percentile) that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.

## Contents
<a name="API_StatisticalThreshold_Contents"></a>

 ** statistic **   <a name="iot-Type-StatisticalThreshold-statistic"></a>
The percentile that resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (`durationSeconds`) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (`comparisonOperator`) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
Type: String
Pattern: `(p0|p0\.1|p0\.01|p1|p10|p50|p90|p99|p99\.9|p99\.99|p100)`
Required: No

## See Also
<a name="API_StatisticalThreshold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/StatisticalThreshold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/StatisticalThreshold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/StatisticalThreshold)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
