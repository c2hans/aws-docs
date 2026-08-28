---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ExponentialRolloutRate.html
---

# ExponentialRolloutRate
<a name="API_ExponentialRolloutRate"></a>

Structure representing exponential rate of rollout for an over-the-air (OTA) task.

## Contents
<a name="API_ExponentialRolloutRate_Contents"></a>

 ** BaseRatePerMinute **   <a name="managedintegrations-Type-ExponentialRolloutRate-BaseRatePerMinute"></a>
The base rate per minute for the rollout of an over-the-air (OTA) task.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** IncrementFactor **   <a name="managedintegrations-Type-ExponentialRolloutRate-IncrementFactor"></a>
The incremental factor for increasing the rollout rate of an over-the-air (OTA) task.
Type: Double
Valid Range: Minimum value of 1.1. Maximum value of 5.
Required: No

 ** RateIncreaseCriteria **   <a name="managedintegrations-Type-ExponentialRolloutRate-RateIncreaseCriteria"></a>
The criteria for increasing the rollout rate of an over-the-air (OTA) task.
Type: [RolloutRateIncreaseCriteria](API_RolloutRateIncreaseCriteria.md) object
Required: No

## See Also
<a name="API_ExponentialRolloutRate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ExponentialRolloutRate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ExponentialRolloutRate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ExponentialRolloutRate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
