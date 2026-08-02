---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryScheduleInput.html
---

# CanaryScheduleInput
<a name="API_CanaryScheduleInput"></a>

This structure specifies how often a canary is to make runs and the date and time when it should stop making runs.

## Contents
<a name="API_CanaryScheduleInput_Contents"></a>

 ** Expression **   <a name="synthetics-Type-CanaryScheduleInput-Expression"></a>
A `rate` expression or a `cron` expression that defines how often the canary is to run.
For a rate expression, The syntax is `rate(number unit)`. *unit* can be `minute`, `minutes`, or `hour`.
For example, `rate(1 minute)` runs the canary once a minute, `rate(10 minutes)` runs it once every 10 minutes, and `rate(1 hour)` runs it once every hour. You can specify a frequency between `rate(1 minute)` and `rate(1 hour)`.
Specifying `rate(0 minute)` or `rate(0 hour)` is a special value that causes the canary to run only once when it is started.
Use `cron(expression)` to specify a cron expression. You can't schedule a canary to wait for more than a year before running. For information about the syntax for cron expressions, see [ Scheduling canary runs using cron](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** DurationInSeconds **   <a name="synthetics-Type-CanaryScheduleInput-DurationInSeconds"></a>
How long, in seconds, for the canary to continue making regular runs according to the schedule in the `Expression` value. If you specify 0, the canary continues making runs until you stop it. If you omit this field, the default of 0 is used.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 31622400.
Required: No

 ** RetryConfig **   <a name="synthetics-Type-CanaryScheduleInput-RetryConfig"></a>
A structure that contains the retry configuration for a canary
Type: [RetryConfigInput](API_RetryConfigInput.md) object
Required: No

## See Also
<a name="API_CanaryScheduleInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CanaryScheduleInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CanaryScheduleInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CanaryScheduleInput)
