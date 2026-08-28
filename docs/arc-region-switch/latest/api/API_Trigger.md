---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Trigger.html
---

# Trigger
<a name="API_Trigger"></a>

Defines a condition that can automatically trigger the execution of a Region switch plan.

## Contents
<a name="API_Trigger_Contents"></a>

 ** action **   <a name="regionswitch-Type-Trigger-action"></a>
The action to perform when the trigger fires. Valid values include `activate` and `deactivate`.
Type: String
Valid Values: `activate | deactivate | postRecovery`
Required: Yes

 ** conditions **   <a name="regionswitch-Type-Trigger-conditions"></a>
The conditions that must be met for the trigger to fire.
Type: Array of [TriggerCondition](API_TriggerCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** minDelayMinutesBetweenExecutions **   <a name="regionswitch-Type-Trigger-minDelayMinutesBetweenExecutions"></a>
The minimum time, in minutes, that must elapse between automatic executions of the plan.
Type: Integer
Required: Yes

 ** targetRegion **   <a name="regionswitch-Type-Trigger-targetRegion"></a>
The AWS Region for a trigger.
Type: String
Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: Yes

 ** description **   <a name="regionswitch-Type-Trigger-description"></a>
The description for a trigger.
Type: String
Required: No

## See Also
<a name="API_Trigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Trigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Trigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Trigger)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
