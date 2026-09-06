---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuditMitigationActionsTaskTarget.html
---

# AuditMitigationActionsTaskTarget
<a name="API_AuditMitigationActionsTaskTarget"></a>

Used in MitigationActionParams, this information identifies the target findings to which the mitigation actions are applied. Only one entry appears.

## Contents
<a name="API_AuditMitigationActionsTaskTarget_Contents"></a>

 ** auditCheckToReasonCodeFilter **   <a name="iot-Type-AuditMitigationActionsTaskTarget-auditCheckToReasonCodeFilter"></a>
Specifies a filter in the form of an audit check and set of reason codes that identify the findings from the audit to which the audit mitigation actions task apply.
Type: String to array of strings map
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

 ** auditTaskId **   <a name="iot-Type-AuditMitigationActionsTaskTarget-auditTaskId"></a>
If the task will apply a mitigation action to findings from a specific audit, this value uniquely identifies the audit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** findingIds **   <a name="iot-Type-AuditMitigationActionsTaskTarget-findingIds"></a>
If the task will apply a mitigation action to one or more listed findings, this value uniquely identifies those findings.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_AuditMitigationActionsTaskTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuditMitigationActionsTaskTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuditMitigationActionsTaskTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuditMitigationActionsTaskTarget)
