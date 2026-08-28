---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_MemberDetail.html
---

# MemberDetail
<a name="API_MemberDetail"></a>

Details about a member account in a behavior graph.

## Contents
<a name="API_MemberDetail_Contents"></a>

 ** AccountId **   <a name="detective-Type-MemberDetail-AccountId"></a>
The AWS account identifier for the member account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: No

 ** AdministratorId **   <a name="detective-Type-MemberDetail-AdministratorId"></a>
The AWS account identifier of the administrator account for the behavior graph.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: No

 ** DatasourcePackageIngestStates **   <a name="detective-Type-MemberDetail-DatasourcePackageIngestStates"></a>
The state of a data source package for the behavior graph.
Type: String to string map
Valid Keys: `DETECTIVE_CORE | EKS_AUDIT | ASFF_SECURITYHUB_FINDING`
Valid Values: `STARTED | STOPPED | DISABLED`
Required: No

 ** DisabledReason **   <a name="detective-Type-MemberDetail-DisabledReason"></a>
For member accounts with a status of `ACCEPTED_BUT_DISABLED`, the reason that the member account is not enabled.
The reason can have one of the following values:
+  `VOLUME_TOO_HIGH` - Indicates that adding the member account would cause the data volume for the behavior graph to be too high.
+  `VOLUME_UNKNOWN` - Indicates that Detective is unable to verify the data volume for the member account. This is usually because the member account is not enrolled in Amazon GuardDuty.
Type: String
Valid Values: `VOLUME_TOO_HIGH | VOLUME_UNKNOWN`
Required: No

 ** EmailAddress **   <a name="detective-Type-MemberDetail-EmailAddress"></a>
The AWS account root user email address for the member account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^.+@(?:(?:(?!-)[A-Za-z0-9-]{1,62})?[A-Za-z0-9]{1}\.)+[A-Za-z]{2,63}$`
Required: No

 ** GraphArn **   <a name="detective-Type-MemberDetail-GraphArn"></a>
The ARN of the behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: No

 ** InvitationType **   <a name="detective-Type-MemberDetail-InvitationType"></a>
The type of behavior graph membership.
For an organization account in the organization behavior graph, the type is `ORGANIZATION`.
For an account that was invited to a behavior graph, the type is `INVITATION`.
Type: String
Valid Values: `INVITATION | ORGANIZATION`
Required: No

 ** InvitedTime **   <a name="detective-Type-MemberDetail-InvitedTime"></a>
For invited accounts, the date and time that Detective sent the invitation to the account. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp
Required: No

 ** MasterId **   <a name="detective-Type-MemberDetail-MasterId"></a>
 *This member has been deprecated.*
The AWS account identifier of the administrator account for the behavior graph.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: No

 ** PercentOfGraphUtilization **   <a name="detective-Type-MemberDetail-PercentOfGraphUtilization"></a>
 *This member has been deprecated.*
The member account data volume as a percentage of the maximum allowed data volume. 0 indicates 0 percent, and 100 indicates 100 percent.
Note that this is not the percentage of the behavior graph data volume.
For example, the data volume for the behavior graph is 80 GB per day. The maximum data volume is 160 GB per day. If the data volume for the member account is 40 GB per day, then `PercentOfGraphUtilization` is 25. It represents 25% of the maximum allowed data volume.
Type: Double
Required: No

 ** PercentOfGraphUtilizationUpdatedTime **   <a name="detective-Type-MemberDetail-PercentOfGraphUtilizationUpdatedTime"></a>
 *This member has been deprecated.*
The date and time when the graph utilization percentage was last updated. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp
Required: No

 ** Status **   <a name="detective-Type-MemberDetail-Status"></a>
The current membership status of the member account. The status can have one of the following values:
+  `INVITED` - For invited accounts only. Indicates that the member was sent an invitation but has not yet responded.
+  `VERIFICATION_IN_PROGRESS` - For invited accounts only, indicates that Detective is verifying that the account identifier and email address provided for the member account match. If they do match, then Detective sends the invitation. If the email address and account identifier don't match, then the member cannot be added to the behavior graph.

  For organization accounts in the organization behavior graph, indicates that Detective is verifying that the account belongs to the organization.
+  `VERIFICATION_FAILED` - For invited accounts only. Indicates that the account and email address provided for the member account do not match, and Detective did not send an invitation to the account.
+  `ENABLED` - Indicates that the member account currently contributes data to the behavior graph. For invited accounts, the member account accepted the invitation. For organization accounts in the organization behavior graph, the Detective administrator account enabled the organization account as a member account.
+  `ACCEPTED_BUT_DISABLED` - The account accepted the invitation, or was enabled by the Detective administrator account, but is prevented from contributing data to the behavior graph. `DisabledReason` provides the reason why the member account is not enabled.
Invited accounts that declined an invitation or that were removed from the behavior graph are not included. In the organization behavior graph, organization accounts that the Detective administrator account did not enable are not included.
Type: String
Valid Values: `INVITED | VERIFICATION_IN_PROGRESS | VERIFICATION_FAILED | ENABLED | ACCEPTED_BUT_DISABLED`
Required: No

 ** UpdatedTime **   <a name="detective-Type-MemberDetail-UpdatedTime"></a>
The date and time that the member account was last updated. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp
Required: No

 ** VolumeUsageByDatasourcePackage **   <a name="detective-Type-MemberDetail-VolumeUsageByDatasourcePackage"></a>
Details on the volume of usage for each data source package in a behavior graph.
Type: String to [DatasourcePackageUsageInfo](API_DatasourcePackageUsageInfo.md) object map
Valid Keys: `DETECTIVE_CORE | EKS_AUDIT | ASFF_SECURITYHUB_FINDING`
Required: No

 ** VolumeUsageInBytes **   <a name="detective-Type-MemberDetail-VolumeUsageInBytes"></a>
 *This member has been deprecated.*
The data volume in bytes per day for the member account.
Type: Long
Required: No

 ** VolumeUsageUpdatedTime **   <a name="detective-Type-MemberDetail-VolumeUsageUpdatedTime"></a>
 *This member has been deprecated.*
The data and time when the member account data volume was last updated. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp
Required: No

## See Also
<a name="API_MemberDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/MemberDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/MemberDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/MemberDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
