---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SelfUpgradeRequestDetail.html
---

# SelfUpgradeRequestDetail
<a name="API_SelfUpgradeRequestDetail"></a>

Details of a self-upgrade request.

## Contents
<a name="API_SelfUpgradeRequestDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreationTime **   <a name="QS-Type-SelfUpgradeRequestDetail-CreationTime"></a>
The time when the self-upgrade request was created.
Type: Long
Required: No

 ** lastUpdateAttemptTime **   <a name="QS-Type-SelfUpgradeRequestDetail-lastUpdateAttemptTime"></a>
The time of the last update attempt for the self-upgrade request.
Type: Long
Required: No

 ** lastUpdateFailureReason **   <a name="QS-Type-SelfUpgradeRequestDetail-lastUpdateFailureReason"></a>
The reason for the last update failure, if applicable.
Type: String
Required: No

 ** OriginalRole **   <a name="QS-Type-SelfUpgradeRequestDetail-OriginalRole"></a>
The original role of the user before the upgrade.
Type: String
Valid Values: `ADMIN | AUTHOR | READER | RESTRICTED_AUTHOR | RESTRICTED_READER | ADMIN_PRO | AUTHOR_PRO | READER_PRO`
Required: No

 ** RequestedRole **   <a name="QS-Type-SelfUpgradeRequestDetail-RequestedRole"></a>
The role that the user is requesting to upgrade to.
Type: String
Valid Values: `ADMIN | AUTHOR | READER | RESTRICTED_AUTHOR | RESTRICTED_READER | ADMIN_PRO | AUTHOR_PRO | READER_PRO`
Required: No

 ** RequestNote **   <a name="QS-Type-SelfUpgradeRequestDetail-RequestNote"></a>
An optional note explaining the reason for the self-upgrade request.
Type: String
Required: No

 ** RequestStatus **   <a name="QS-Type-SelfUpgradeRequestDetail-RequestStatus"></a>
The status of the self-upgrade request.
Type: String
Valid Values: `PENDING | APPROVED | DENIED | UPDATE_FAILED | VERIFY_FAILED`
Required: No

 ** UpgradeRequestId **   <a name="QS-Type-SelfUpgradeRequestDetail-UpgradeRequestId"></a>
The ID of the self-upgrade request.
Type: String
Required: No

 ** UserName **   <a name="QS-Type-SelfUpgradeRequestDetail-UserName"></a>
The username of the user who initiated the self-upgrade request.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: No

## See Also
<a name="API_SelfUpgradeRequestDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SelfUpgradeRequestDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SelfUpgradeRequestDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SelfUpgradeRequestDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
