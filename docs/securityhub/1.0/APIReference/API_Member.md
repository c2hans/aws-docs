---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Member.html
---

# Member
<a name="API_Member"></a>

The details about a member account.

## Contents
<a name="API_Member_Contents"></a>

 ** AccountId **   <a name="securityhub-Type-Member-AccountId"></a>
The AWS account ID of the member account.
Type: String
Required: No

 ** AdministratorId **   <a name="securityhub-Type-Member-AdministratorId"></a>
The AWS account ID of the Security Hub CSPM administrator account associated with this member account.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Email **   <a name="securityhub-Type-Member-Email"></a>
The email address of the member account.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InvitedAt **   <a name="securityhub-Type-Member-InvitedAt"></a>
A timestamp for the date and time when the invitation was sent to the member account.
Type: Timestamp
Required: No

 ** MasterId **   <a name="securityhub-Type-Member-MasterId"></a>
 *This member has been deprecated.*
This is replaced by `AdministratorID`.
The AWS account ID of the Security Hub CSPM administrator account associated with this member account.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MemberStatus **   <a name="securityhub-Type-Member-MemberStatus"></a>
The status of the relationship between the member account and its administrator account.
The status can have one of the following values:
+  `Created` - Indicates that the administrator account added the member account, but has not yet invited the member account.
+  `Invited` - Indicates that the administrator account invited the member account. The member account has not yet responded to the invitation.
+  `Enabled` - Indicates that the member account is currently active. For manually invited member accounts, indicates that the member account accepted the invitation.
+  `Removed` - Indicates that the administrator account disassociated the member account.
+  `Resigned` - Indicates that the member account disassociated themselves from the administrator account.
+  `Deleted` - Indicates that the administrator account deleted the member account.
+  `AccountSuspended` - Indicates that an organization account was suspended from AWS at the same time that the administrator account tried to enable the organization account as a member account.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-Member-UpdatedAt"></a>
The timestamp for the date and time when the member account was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Member_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Member)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Member)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Member)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
