---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_AbortConfigCriteria.html
---

# AbortConfigCriteria
<a name="API_AbortConfigCriteria"></a>

Structure representing one abort config criteria.

## Contents
<a name="API_AbortConfigCriteria_Contents"></a>

 ** Action **   <a name="managedintegrations-Type-AbortConfigCriteria-Action"></a>
The action taken by the abort configuration.
Type: String
Valid Values: `CANCEL`
Required: No

 ** FailureType **   <a name="managedintegrations-Type-AbortConfigCriteria-FailureType"></a>
Over-the-air (OTA) task abort criteria failure type.
Type: String
Valid Values: `FAILED | REJECTED | TIMED_OUT | ALL`
Required: No

 ** MinNumberOfExecutedThings **   <a name="managedintegrations-Type-AbortConfigCriteria-MinNumberOfExecutedThings"></a>
The minimum number of things that must receive task execution notifications before the task can be aborted.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** ThresholdPercentage **   <a name="managedintegrations-Type-AbortConfigCriteria-ThresholdPercentage"></a>
The minimum percentage of over-the-air (OTA) task execution failures that must occur to initiate the last abort.
Type: Double
Valid Range: Maximum value of 100.
Required: No

## See Also
<a name="API_AbortConfigCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/AbortConfigCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/AbortConfigCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/AbortConfigCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
