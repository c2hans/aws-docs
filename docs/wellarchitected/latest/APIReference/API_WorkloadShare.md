---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_WorkloadShare.html
---

# WorkloadShare
<a name="API_WorkloadShare"></a>

A workload share return object.

## Contents
<a name="API_WorkloadShare_Contents"></a>

 ** PermissionType **   <a name="wellarchitected-Type-WorkloadShare-PermissionType"></a>
Permission granted on a share request.
Type: String
Valid Values: `READONLY | CONTRIBUTOR`
Required: No

 ** SharedBy **   <a name="wellarchitected-Type-WorkloadShare-SharedBy"></a>
An AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** SharedWith **   <a name="wellarchitected-Type-WorkloadShare-SharedWith"></a>
The AWS account ID, organization ID, or organizational unit (OU) ID with which the workload, lens, profile, or review template is shared.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 2048.
Required: No

 ** ShareId **   <a name="wellarchitected-Type-WorkloadShare-ShareId"></a>
The ID associated with the share.
Type: String
Pattern: `[0-9a-f]{32}`
Required: No

 ** Status **   <a name="wellarchitected-Type-WorkloadShare-Status"></a>
The status of the share request.
Type: String
Valid Values: `ACCEPTED | REJECTED | PENDING | REVOKED | EXPIRED | ASSOCIATING | ASSOCIATED | FAILED`
Required: No

 ** WorkloadId **   <a name="wellarchitected-Type-WorkloadShare-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

 ** WorkloadName **   <a name="wellarchitected-Type-WorkloadShare-WorkloadName"></a>
The name of the workload.
The name must be unique within an account within an AWS Region. Spaces and capitalization are ignored when checking for uniqueness.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

## See Also
<a name="API_WorkloadShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/WorkloadShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/WorkloadShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/WorkloadShare)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
