---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CodeRemediationTask.html
---

# CodeRemediationTask
<a name="API_CodeRemediationTask"></a>

Represents a code remediation task that was initiated to fix a security finding.

## Contents
<a name="API_CodeRemediationTask_Contents"></a>

 ** status **   <a name="securityagent-Type-CodeRemediationTask-status"></a>
The current status of the code remediation task.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED`
Required: Yes

 ** statusReason **   <a name="securityagent-Type-CodeRemediationTask-statusReason"></a>
The reason for the current status of the code remediation task.
Type: String
Required: No

 ** taskDetails **   <a name="securityagent-Type-CodeRemediationTask-taskDetails"></a>
The list of details for the code remediation task, including repository name, code diff link, and pull request link.
Type: Array of [CodeRemediationTaskDetails](API_CodeRemediationTaskDetails.md) objects
Required: No

## See Also
<a name="API_CodeRemediationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CodeRemediationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CodeRemediationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CodeRemediationTask)
