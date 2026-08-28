---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowTaskInvocationParameters.html
---

# MaintenanceWindowTaskInvocationParameters
<a name="API_MaintenanceWindowTaskInvocationParameters"></a>

The parameters for task execution.

## Contents
<a name="API_MaintenanceWindowTaskInvocationParameters_Contents"></a>

 ** Automation **   <a name="systemsmanager-Type-MaintenanceWindowTaskInvocationParameters-Automation"></a>
The parameters for an `AUTOMATION` task type.
Type: [MaintenanceWindowAutomationParameters](API_MaintenanceWindowAutomationParameters.md) object
Required: No

 ** Lambda **   <a name="systemsmanager-Type-MaintenanceWindowTaskInvocationParameters-Lambda"></a>
The parameters for a `LAMBDA` task type.
Type: [MaintenanceWindowLambdaParameters](API_MaintenanceWindowLambdaParameters.md) object
Required: No

 ** RunCommand **   <a name="systemsmanager-Type-MaintenanceWindowTaskInvocationParameters-RunCommand"></a>
The parameters for a `RUN_COMMAND` task type.
Type: [MaintenanceWindowRunCommandParameters](API_MaintenanceWindowRunCommandParameters.md) object
Required: No

 ** StepFunctions **   <a name="systemsmanager-Type-MaintenanceWindowTaskInvocationParameters-StepFunctions"></a>
The parameters for a `STEP_FUNCTIONS` task type.
Type: [MaintenanceWindowStepFunctionsParameters](API_MaintenanceWindowStepFunctionsParameters.md) object
Required: No

## See Also
<a name="API_MaintenanceWindowTaskInvocationParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowTaskInvocationParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowTaskInvocationParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowTaskInvocationParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
