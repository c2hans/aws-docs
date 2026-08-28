---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AutomationExecutionPreview.html
---

# AutomationExecutionPreview
<a name="API_AutomationExecutionPreview"></a>

Information about the results of the execution preview.

## Contents
<a name="API_AutomationExecutionPreview_Contents"></a>

 ** Regions **   <a name="systemsmanager-Type-AutomationExecutionPreview-Regions"></a>
Information about the AWS Regions targeted by the execution preview.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** StepPreviews **   <a name="systemsmanager-Type-AutomationExecutionPreview-StepPreviews"></a>
Information about the type of impact a runbook step would have on a resource.
+  `Mutating`: The runbook step would make changes to the targets through actions that create, modify, or delete resources.
+  `Non_Mutating`: The runbook step would retrieve data about resources but not make changes to them. This category generally includes `Describe*`, `List*`, `Get*`, and similar read-only API actions.
+  `Undetermined`: An undetermined step invokes executions performed by another orchestration service like AWS Lambda, AWS Step Functions, or AWS Systems Manager Run Command. An undetermined step might also call a third-party API. Systems Manager Automation doesn't know the outcome of the orchestration processes or third-party API executions, so the results of the steps are undetermined.
Type: String to integer map
Valid Keys: `Mutating | NonMutating | Undetermined`
Required: No

 ** TargetPreviews **   <a name="systemsmanager-Type-AutomationExecutionPreview-TargetPreviews"></a>
Information that provides a preview of what the impact of running the specified Automation runbook would be.
Type: Array of [TargetPreview](API_TargetPreview.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** TotalAccounts **   <a name="systemsmanager-Type-AutomationExecutionPreview-TotalAccounts"></a>
Information about the AWS accounts that were included in the execution preview.
Type: Integer
Required: No

## See Also
<a name="API_AutomationExecutionPreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AutomationExecutionPreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AutomationExecutionPreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AutomationExecutionPreview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
