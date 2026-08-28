---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuditTaskMetadata.html
---

# AuditTaskMetadata
<a name="API_AuditTaskMetadata"></a>

The audits that were performed.

## Contents
<a name="API_AuditTaskMetadata_Contents"></a>

 ** taskId **   <a name="iot-Type-AuditTaskMetadata-taskId"></a>
The ID of this audit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** taskStatus **   <a name="iot-Type-AuditTaskMetadata-taskStatus"></a>
The status of this audit. One of "IN\_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED | CANCELED`
Required: No

 ** taskType **   <a name="iot-Type-AuditTaskMetadata-taskType"></a>
The type of this audit. One of "ON\_DEMAND\_AUDIT\_TASK" or "SCHEDULED\_AUDIT\_TASK".
Type: String
Valid Values: `ON_DEMAND_AUDIT_TASK | SCHEDULED_AUDIT_TASK`
Required: No

## See Also
<a name="API_AuditTaskMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuditTaskMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuditTaskMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuditTaskMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
