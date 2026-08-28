---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJobExecutionsRolloutConfig.html
---

# AwsJobExecutionsRolloutConfig
<a name="API_AwsJobExecutionsRolloutConfig"></a>

Configuration for the rollout of OTA updates.

## Contents
<a name="API_AwsJobExecutionsRolloutConfig_Contents"></a>

 ** exponentialRate **   <a name="iot-Type-AwsJobExecutionsRolloutConfig-exponentialRate"></a>
The rate of increase for a job rollout. This parameter allows you to define an exponential rate increase for a job rollout.
Type: [AwsJobExponentialRolloutRate](API_AwsJobExponentialRolloutRate.md) object
Required: No

 ** maximumPerMinute **   <a name="iot-Type-AwsJobExecutionsRolloutConfig-maximumPerMinute"></a>
The maximum number of OTA update job executions started per minute.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

## See Also
<a name="API_AwsJobExecutionsRolloutConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AwsJobExecutionsRolloutConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AwsJobExecutionsRolloutConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AwsJobExecutionsRolloutConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
