---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SessionActionDefinition.html
---

# SessionActionDefinition
<a name="API_SessionActionDefinition"></a>

The definition of the session action.

## Contents
<a name="API_SessionActionDefinition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** envEnter **   <a name="deadlinecloud-Type-SessionActionDefinition-envEnter"></a>
The environment to enter into.
Type: [EnvironmentEnterSessionActionDefinition](API_EnvironmentEnterSessionActionDefinition.md) object
Required: No

 ** envExit **   <a name="deadlinecloud-Type-SessionActionDefinition-envExit"></a>
The environment to exit from.
Type: [EnvironmentExitSessionActionDefinition](API_EnvironmentExitSessionActionDefinition.md) object
Required: No

 ** syncInputJobAttachments **   <a name="deadlinecloud-Type-SessionActionDefinition-syncInputJobAttachments"></a>
The session action definition for syncing input job attachments.
Type: [SyncInputJobAttachmentsSessionActionDefinition](API_SyncInputJobAttachmentsSessionActionDefinition.md) object
Required: No

 ** taskRun **   <a name="deadlinecloud-Type-SessionActionDefinition-taskRun"></a>
The task run in the session.
Type: [TaskRunSessionActionDefinition](API_TaskRunSessionActionDefinition.md) object
Required: No

## See Also
<a name="API_SessionActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionActionDefinition)
