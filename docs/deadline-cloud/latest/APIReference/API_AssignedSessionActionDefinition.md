---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssignedSessionActionDefinition.html
---

# AssignedSessionActionDefinition
<a name="API_AssignedSessionActionDefinition"></a>

The definition of the assigned session action.

## Contents
<a name="API_AssignedSessionActionDefinition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** envEnter **   <a name="deadlinecloud-Type-AssignedSessionActionDefinition-envEnter"></a>
The environment a session starts on.
Type: [AssignedEnvironmentEnterSessionActionDefinition](API_AssignedEnvironmentEnterSessionActionDefinition.md) object
Required: No

 ** envExit **   <a name="deadlinecloud-Type-AssignedSessionActionDefinition-envExit"></a>
The environment a session exits from.
Type: [AssignedEnvironmentExitSessionActionDefinition](API_AssignedEnvironmentExitSessionActionDefinition.md) object
Required: No

 ** syncInputJobAttachments **   <a name="deadlinecloud-Type-AssignedSessionActionDefinition-syncInputJobAttachments"></a>
The job attachments to sync for the assigned session action.
Type: [AssignedSyncInputJobAttachmentsSessionActionDefinition](API_AssignedSyncInputJobAttachmentsSessionActionDefinition.md) object
Required: No

 ** taskRun **   <a name="deadlinecloud-Type-AssignedSessionActionDefinition-taskRun"></a>
The task run.
Type: [AssignedTaskRunSessionActionDefinition](API_AssignedTaskRunSessionActionDefinition.md) object
Required: No

## See Also
<a name="API_AssignedSessionActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssignedSessionActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssignedSessionActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssignedSessionActionDefinition)
