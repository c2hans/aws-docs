---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SessionActionDefinitionSummary.html
---

# SessionActionDefinitionSummary
<a name="API_SessionActionDefinitionSummary"></a>

The details of a session action definition.

## Contents
<a name="API_SessionActionDefinitionSummary_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** envEnter **   <a name="deadlinecloud-Type-SessionActionDefinitionSummary-envEnter"></a>
The environment to enter into.
Type: [EnvironmentEnterSessionActionDefinitionSummary](API_EnvironmentEnterSessionActionDefinitionSummary.md) object
Required: No

 ** envExit **   <a name="deadlinecloud-Type-SessionActionDefinitionSummary-envExit"></a>
The environment to exit from.
Type: [EnvironmentExitSessionActionDefinitionSummary](API_EnvironmentExitSessionActionDefinitionSummary.md) object
Required: No

 ** syncInputJobAttachments **   <a name="deadlinecloud-Type-SessionActionDefinitionSummary-syncInputJobAttachments"></a>
The session action definition summary for syncing input job attachments.
Type: [SyncInputJobAttachmentsSessionActionDefinitionSummary](API_SyncInputJobAttachmentsSessionActionDefinitionSummary.md) object
Required: No

 ** taskRun **   <a name="deadlinecloud-Type-SessionActionDefinitionSummary-taskRun"></a>
The task run.
Type: [TaskRunSessionActionDefinitionSummary](API_TaskRunSessionActionDefinitionSummary.md) object
Required: No

## See Also
<a name="API_SessionActionDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionActionDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionActionDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionActionDefinitionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
