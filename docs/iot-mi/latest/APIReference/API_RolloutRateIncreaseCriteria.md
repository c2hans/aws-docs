---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_RolloutRateIncreaseCriteria.html
---

# RolloutRateIncreaseCriteria
<a name="API_RolloutRateIncreaseCriteria"></a>

Structure representing rollout config criteria.

## Contents
<a name="API_RolloutRateIncreaseCriteria_Contents"></a>

 ** numberOfNotifiedThings **   <a name="managedintegrations-Type-RolloutRateIncreaseCriteria-numberOfNotifiedThings"></a>
The threshold for number of notified things that will initiate the increase in rate of rollout.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** numberOfSucceededThings **   <a name="managedintegrations-Type-RolloutRateIncreaseCriteria-numberOfSucceededThings"></a>
The threshold for number of succeeded things that will initiate the increase in rate of rollout.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_RolloutRateIncreaseCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/RolloutRateIncreaseCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/RolloutRateIncreaseCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/RolloutRateIncreaseCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
