---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_OtaTaskExecutionRolloutConfig.html
---

# OtaTaskExecutionRolloutConfig
<a name="API_OtaTaskExecutionRolloutConfig"></a>

Over-the-air (OTA) task rollout config.

## Contents
<a name="API_OtaTaskExecutionRolloutConfig_Contents"></a>

 ** ExponentialRolloutRate **   <a name="managedintegrations-Type-OtaTaskExecutionRolloutConfig-ExponentialRolloutRate"></a>
Structure representing exponential rate of rollout for an over-the-air (OTA) task.
Type: [ExponentialRolloutRate](API_ExponentialRolloutRate.md) object
Required: No

 ** MaximumPerMinute **   <a name="managedintegrations-Type-OtaTaskExecutionRolloutConfig-MaximumPerMinute"></a>
The maximum number of things that will be notified of a pending task, per minute.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_OtaTaskExecutionRolloutConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/OtaTaskExecutionRolloutConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/OtaTaskExecutionRolloutConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/OtaTaskExecutionRolloutConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
