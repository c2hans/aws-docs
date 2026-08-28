---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_TaskRunSessionActionDefinitionSummary.html
---

# TaskRunSessionActionDefinitionSummary
<a name="API_TaskRunSessionActionDefinitionSummary"></a>

The details of a task run in a session action.

## Contents
<a name="API_TaskRunSessionActionDefinitionSummary_Contents"></a>

 ** stepId **   <a name="deadlinecloud-Type-TaskRunSessionActionDefinitionSummary-stepId"></a>
The step ID.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

 ** parameters **   <a name="deadlinecloud-Type-TaskRunSessionActionDefinitionSummary-parameters"></a>
The parameters of a task run in a session action.
Type: String to [TaskParameterValue](API_TaskParameterValue.md) object map
Required: No

 ** taskId **   <a name="deadlinecloud-Type-TaskRunSessionActionDefinitionSummary-taskId"></a>
The task ID.
Type: String
Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: No

## See Also
<a name="API_TaskRunSessionActionDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TaskRunSessionActionDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TaskRunSessionActionDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TaskRunSessionActionDefinitionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
