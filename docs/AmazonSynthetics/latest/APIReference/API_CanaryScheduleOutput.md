---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryScheduleOutput.html
---

# CanaryScheduleOutput
<a name="API_CanaryScheduleOutput"></a>

How long, in seconds, for the canary to continue making regular runs according to the schedule in the `Expression` value.

## Contents
<a name="API_CanaryScheduleOutput_Contents"></a>

 ** DurationInSeconds **   <a name="synthetics-Type-CanaryScheduleOutput-DurationInSeconds"></a>
How long, in seconds, for the canary to continue making regular runs after it was created. The runs are performed according to the schedule in the `Expression` value.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 31622400.
Required: No

 ** Expression **   <a name="synthetics-Type-CanaryScheduleOutput-Expression"></a>
A `rate` expression or a `cron` expression that defines how often the canary is to run.
For a rate expression, The syntax is `rate(number unit)`. *unit* can be `minute`, `minutes`, or `hour`.
For example, `rate(1 minute)` runs the canary once a minute, `rate(10 minutes)` runs it once every 10 minutes, and `rate(1 hour)` runs it once every hour. You can specify a frequency between `rate(1 minute)` and `rate(1 hour)`.
Specifying `rate(0 minute)` or `rate(0 hour)` is a special value that causes the canary to run only once when it is started.
Use `cron(expression)` to specify a cron expression. For information about the syntax for cron expressions, see [ Scheduling canary runs using cron](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** RetryConfig **   <a name="synthetics-Type-CanaryScheduleOutput-RetryConfig"></a>
A structure that contains the retry configuration for a canary
Type: [RetryConfigOutput](API_RetryConfigOutput.md) object
Required: No

## See Also
<a name="API_CanaryScheduleOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CanaryScheduleOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CanaryScheduleOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CanaryScheduleOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
