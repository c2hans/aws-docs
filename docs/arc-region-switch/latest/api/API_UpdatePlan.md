---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlan.html
---

# UpdatePlan
<a name="API_UpdatePlan"></a>

Updates an existing Region switch plan. You can modify the plan's description, workflows, execution role, recovery time objective, associated alarms, and triggers.

## Request Parameters
<a name="API_UpdatePlan_RequestParameters"></a>

 ** arn **
The Amazon Resource Name (ARN) of the plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

 ** associatedAlarms **
The updated CloudWatch alarms associated with the plan.
Type: String to [AssociatedAlarm](API_AssociatedAlarm.md) object map
Required: No

 ** description **
The updated description for the Region switch plan.
Type: String
Required: No

 ** executionRole **
The updated IAM role ARN that grants Region switch the permissions needed to execute the plan steps.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: Yes

 ** recoveryTimeObjectiveMinutes **
The updated target recovery time objective (RTO) in minutes for the plan.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10080.
Required: No

 ** reportConfiguration **
The updated report configuration for the plan.
Type: [ReportConfiguration](API_ReportConfiguration.md) object
Required: No

 ** triggers **
The updated conditions that can automatically trigger the execution of the plan.
Type: Array of [Trigger](API_Trigger.md) objects
Required: No

 ** workflows **
The updated workflows for the Region switch plan.
Type: Array of [Workflow](API_Workflow.md) objects
Required: Yes

## Response Elements
<a name="API_UpdatePlan_ResponseElements"></a>

The following element is returned by the service.

 ** plan **
The details of the updated Region switch plan.
Type: [Plan](API_Plan.md) object

## Errors
<a name="API_UpdatePlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404
HTTP Status Code: 404

## See Also
<a name="API_UpdatePlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/UpdatePlan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
