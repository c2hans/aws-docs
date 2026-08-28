---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ExponentialRolloutRate.html
---

# ExponentialRolloutRate
<a name="API_ExponentialRolloutRate"></a>

Allows you to create an exponential rate of rollout for a job.

## Contents
<a name="API_ExponentialRolloutRate_Contents"></a>

 ** baseRatePerMinute **   <a name="iot-Type-ExponentialRolloutRate-baseRatePerMinute"></a>
The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** incrementFactor **   <a name="iot-Type-ExponentialRolloutRate-incrementFactor"></a>
The exponential factor to increase the rate of rollout for a job.
 AWS IoT Core supports up to one digit after the decimal (for example, 1.5, but not 1.55).
Type: Double
Valid Range: Minimum value of 1.1. Maximum value of 5.
Required: Yes

 ** rateIncreaseCriteria **   <a name="iot-Type-ExponentialRolloutRate-rateIncreaseCriteria"></a>
The criteria to initiate the increase in rate of rollout for a job.
Type: [RateIncreaseCriteria](API_RateIncreaseCriteria.md) object
Required: Yes

## See Also
<a name="API_ExponentialRolloutRate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ExponentialRolloutRate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ExponentialRolloutRate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ExponentialRolloutRate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
