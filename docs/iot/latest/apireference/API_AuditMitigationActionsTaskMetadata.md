---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuditMitigationActionsTaskMetadata.html
---

# AuditMitigationActionsTaskMetadata
<a name="API_AuditMitigationActionsTaskMetadata"></a>

Information about an audit mitigation actions task that is returned by `ListAuditMitigationActionsTasks`.

## Contents
<a name="API_AuditMitigationActionsTaskMetadata_Contents"></a>

 ** startTime **   <a name="iot-Type-AuditMitigationActionsTaskMetadata-startTime"></a>
The time at which the audit mitigation actions task was started.
Type: Timestamp
Required: No

 ** taskId **   <a name="iot-Type-AuditMitigationActionsTaskMetadata-taskId"></a>
The unique identifier for the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** taskStatus **   <a name="iot-Type-AuditMitigationActionsTaskMetadata-taskStatus"></a>
The current state of the audit mitigation actions task.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED | CANCELED`
Required: No

## See Also
<a name="API_AuditMitigationActionsTaskMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuditMitigationActionsTaskMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuditMitigationActionsTaskMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuditMitigationActionsTaskMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
