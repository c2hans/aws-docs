---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuditMitigationActionExecutionMetadata.html
---

# AuditMitigationActionExecutionMetadata
<a name="API_AuditMitigationActionExecutionMetadata"></a>

Returned by ListAuditMitigationActionsTask, this object contains information that describes a mitigation action that has been started.

## Contents
<a name="API_AuditMitigationActionExecutionMetadata_Contents"></a>

 ** actionId **   <a name="iot-Type-AuditMitigationActionExecutionMetadata-actionId"></a>
The unique identifier for the mitigation action being applied by the task.
Type: String
Required: No

 ** actionName **   <a name="iot-Type-AuditMitigationActionExecutionMetadata-actionName"></a>
The friendly name of the mitigation action being applied by the task.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** endTime **   <a name="iot-Type-AuditMitigationActionExecutionMetadata-endTime"></a>
The date and time when the task was completed or canceled. Blank if the task is still running.
Type: Timestamp
Required: No

 ** errorCode **   <a name="iot-Type-AuditMitigationActionExecutionMetadata-errorCode"></a>
If an error occurred, the code that indicates which type of error occurred.
Type: String
Required: No

 ** findingId **   <a name="iot-Type-AuditMitigationActionExecutionMetadata-findingId"></a>
The unique identifier for the findings to which the task and associated mitigation action are applied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** message **   <a name="iot-Type-AuditMitigationActionExecutionMetadata-message"></a>
If an error occurred, a message that describes the error.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** startTime **   <a name="iot-Type-AuditMitigationActionExecutionMetadata-startTime"></a>
The date and time when the task was started.
Type: Timestamp
Required: No

 ** status **   <a name="iot-Type-AuditMitigationActionExecutionMetadata-status"></a>
The current status of the task being executed.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED | CANCELED | SKIPPED | PENDING`
Required: No

 ** taskId **   <a name="iot-Type-AuditMitigationActionExecutionMetadata-taskId"></a>
The unique identifier for the task that applies the mitigation action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_AuditMitigationActionExecutionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuditMitigationActionExecutionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuditMitigationActionExecutionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuditMitigationActionExecutionMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
