---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_IoTJobExponentialRolloutRate.html
---

# IoTJobExponentialRolloutRate
<a name="API_IoTJobExponentialRolloutRate"></a>

Contains information about an exponential rollout rate for a configuration deployment job.

## Contents
<a name="API_IoTJobExponentialRolloutRate_Contents"></a>

 ** baseRatePerMinute **   <a name="greengrassv2-Type-IoTJobExponentialRolloutRate-baseRatePerMinute"></a>
The minimum number of devices that receive a pending job notification, per minute, when the job starts. This parameter defines the initial rollout rate of the job.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** incrementFactor **   <a name="greengrassv2-Type-IoTJobExponentialRolloutRate-incrementFactor"></a>
The exponential factor to increase the rollout rate for the job.
This parameter supports up to one digit after the decimal (for example, you can specify `1.5`, but not `1.55`).
Type: Double
Valid Range: Minimum value of 1. Maximum value of 5.
Required: Yes

 ** rateIncreaseCriteria **   <a name="greengrassv2-Type-IoTJobExponentialRolloutRate-rateIncreaseCriteria"></a>
The criteria to increase the rollout rate for the job.
Type: [IoTJobRateIncreaseCriteria](API_IoTJobRateIncreaseCriteria.md) object
Required: Yes

## See Also
<a name="API_IoTJobExponentialRolloutRate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/IoTJobExponentialRolloutRate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/IoTJobExponentialRolloutRate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/IoTJobExponentialRolloutRate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
