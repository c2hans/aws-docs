---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchStatus.html
---

# PatchStatus
<a name="API_PatchStatus"></a>

Information about the approval status of a patch.

## Contents
<a name="API_PatchStatus_Contents"></a>

 ** ApprovalDate **   <a name="systemsmanager-Type-PatchStatus-ApprovalDate"></a>
The date the patch was approved (or will be approved if the status is `PENDING_APPROVAL`).
Type: Timestamp
Required: No

 ** ComplianceLevel **   <a name="systemsmanager-Type-PatchStatus-ComplianceLevel"></a>
The compliance severity level for a patch.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNSPECIFIED`
Required: No

 ** DeploymentStatus **   <a name="systemsmanager-Type-PatchStatus-DeploymentStatus"></a>
The approval status of a patch.
Type: String
Valid Values: `APPROVED | PENDING_APPROVAL | EXPLICIT_APPROVED | EXPLICIT_REJECTED`
Required: No

## See Also
<a name="API_PatchStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PatchStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PatchStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PatchStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
