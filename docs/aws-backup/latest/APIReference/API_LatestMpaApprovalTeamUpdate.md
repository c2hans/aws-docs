---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_LatestMpaApprovalTeamUpdate.html
---

# LatestMpaApprovalTeamUpdate
<a name="API_LatestMpaApprovalTeamUpdate"></a>

Contains information about the latest update to an MPA approval team association.

## Contents
<a name="API_LatestMpaApprovalTeamUpdate_Contents"></a>

 ** ExpiryDate **   <a name="Backup-Type-LatestMpaApprovalTeamUpdate-ExpiryDate"></a>
The date and time when the MPA approval team update will expire.
Type: Timestamp
Required: No

 ** InitiationDate **   <a name="Backup-Type-LatestMpaApprovalTeamUpdate-InitiationDate"></a>
The date and time when the MPA approval team update was initiated.
Type: Timestamp
Required: No

 ** MpaSessionArn **   <a name="Backup-Type-LatestMpaApprovalTeamUpdate-MpaSessionArn"></a>
The ARN of the MPA session associated with this update.
Type: String
Required: No

 ** Status **   <a name="Backup-Type-LatestMpaApprovalTeamUpdate-Status"></a>
The current status of the MPA approval team update.
Type: String
Valid Values: `PENDING | APPROVED | FAILED`
Required: No

 ** StatusMessage **   <a name="Backup-Type-LatestMpaApprovalTeamUpdate-StatusMessage"></a>
A message describing the current status of the MPA approval team update.
Type: String
Required: No

## See Also
<a name="API_LatestMpaApprovalTeamUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/LatestMpaApprovalTeamUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/LatestMpaApprovalTeamUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/LatestMpaApprovalTeamUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
