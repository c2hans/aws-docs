---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_JobExecutionsRolloutConfig.html
---

# JobExecutionsRolloutConfig
<a name="API_JobExecutionsRolloutConfig"></a>

Allows you to create a staged rollout of a job.

## Contents
<a name="API_JobExecutionsRolloutConfig_Contents"></a>

 ** exponentialRate **   <a name="iot-Type-JobExecutionsRolloutConfig-exponentialRate"></a>
The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.
Type: [ExponentialRolloutRate](API_ExponentialRolloutRate.md) object
Required: No

 ** maximumPerMinute **   <a name="iot-Type-JobExecutionsRolloutConfig-maximumPerMinute"></a>
The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_JobExecutionsRolloutConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/JobExecutionsRolloutConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/JobExecutionsRolloutConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/JobExecutionsRolloutConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
