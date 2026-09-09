---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_WarmUpConfiguration.html
---

# WarmUpConfiguration
<a name="API_WarmUpConfiguration"></a>

The configuration settings that define the warm-up behavior for an alarm. Use these settings to delay alarm evaluation after you create or update the alarm, which reduces alarm noise while a new resource or service starts publishing data.

During the warm-up period, the alarm stays in `INSUFFICIENT_DATA` and does not perform alarm actions.

## Contents
<a name="API_WarmUpConfiguration_Contents"></a>

 ** WarmUpPeriodDurationInMinutes **   <a name="ACW-Type-WarmUpConfiguration-WarmUpPeriodDurationInMinutes"></a>
The length of the warm-up period, in minutes. After you create or update the alarm, the alarm stays in `INSUFFICIENT_DATA` for this duration. During this time, the alarm does not perform alarm actions.
You can change this value at any time, including after the warm-up period ends. If you change it after the warm-up period ends, the new value does not restart the warm-up period.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2880.
Required: Yes

 ** OnlyStartEvaluatingAfterWarmUpPeriodEnds **   <a name="ACW-Type-WarmUpConfiguration-OnlyStartEvaluatingAfterWarmUpPeriodEnds"></a>
Specifies whether the alarm waits for the full warm-up period before it starts to evaluate. The default is `false`. If `true`, the alarm waits the entire `WarmUpPeriodDurationInMinutes` before it starts to evaluate, even if metric data arrives earlier. If `false`, the alarm ends the warm-up period early. Evaluation begins as soon as the alarm has enough metric data to fill its evaluation window.
Type: Boolean
Required: No

## See Also
<a name="API_WarmUpConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/WarmUpConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/WarmUpConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/WarmUpConfiguration)
