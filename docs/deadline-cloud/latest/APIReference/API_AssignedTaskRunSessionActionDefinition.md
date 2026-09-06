---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssignedTaskRunSessionActionDefinition.html
---

# AssignedTaskRunSessionActionDefinition
<a name="API_AssignedTaskRunSessionActionDefinition"></a>

The specific task, step, and parameters to include.

## Contents
<a name="API_AssignedTaskRunSessionActionDefinition_Contents"></a>

 ** parameters **   <a name="deadlinecloud-Type-AssignedTaskRunSessionActionDefinition-parameters"></a>
The parameters to include.
Type: String to [TaskParameterValue](API_TaskParameterValue.md) object map
Required: Yes

 ** stepId **   <a name="deadlinecloud-Type-AssignedTaskRunSessionActionDefinition-stepId"></a>
The step ID.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

 ** taskId **   <a name="deadlinecloud-Type-AssignedTaskRunSessionActionDefinition-taskId"></a>
The task ID.
Type: String
Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: No

## See Also
<a name="API_AssignedTaskRunSessionActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssignedTaskRunSessionActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssignedTaskRunSessionActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssignedTaskRunSessionActionDefinition)
