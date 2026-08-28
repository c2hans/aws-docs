---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MembershipSummary.html
---

# MembershipSummary
<a name="API_MembershipSummary"></a>

The membership object listed by the request.

## Contents
<a name="API_MembershipSummary_Contents"></a>

 ** arn **   <a name="API-Type-MembershipSummary-arn"></a>
The unique ARN for the membership.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-MembershipSummary-collaborationArn"></a>
The unique ARN for the membership's associated collaboration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationCreatorAccountId **   <a name="API-Type-MembershipSummary-collaborationCreatorAccountId"></a>
The identifier of the AWS principal that created the collaboration. Currently only supports AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** collaborationCreatorDisplayName **   <a name="API-Type-MembershipSummary-collaborationCreatorDisplayName"></a>
The display name of the collaboration creator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** collaborationId **   <a name="API-Type-MembershipSummary-collaborationId"></a>
The unique ID for the membership's collaboration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** collaborationName **   <a name="API-Type-MembershipSummary-collaborationName"></a>
The name for the membership's collaboration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** createTime **   <a name="API-Type-MembershipSummary-createTime"></a>
The time when the membership was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-MembershipSummary-id"></a>
The unique ID for the membership's collaboration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** memberAbilities **   <a name="API-Type-MembershipSummary-memberAbilities"></a>
The abilities granted to the collaboration member.
Type: Array of strings
Valid Values: `CAN_QUERY | CAN_RECEIVE_RESULTS | CAN_RUN_JOB | CAN_EXPORT_QUERY_ANALYSIS_LOG`
Required: Yes

 ** paymentConfiguration **   <a name="API-Type-MembershipSummary-paymentConfiguration"></a>
The payment responsibilities accepted by the collaboration member.
Type: [MembershipPaymentConfiguration](API_MembershipPaymentConfiguration.md) object
Required: Yes

 ** status **   <a name="API-Type-MembershipSummary-status"></a>
The status of the membership.
Type: String
Valid Values: `ACTIVE | REMOVED | COLLABORATION_DELETED`
Required: Yes

 ** updateTime **   <a name="API-Type-MembershipSummary-updateTime"></a>
The time the membership metadata was last updated.
Type: Timestamp
Required: Yes

 ** mlMemberAbilities **   <a name="API-Type-MembershipSummary-mlMemberAbilities"></a>
Provides a summary of the ML abilities for the collaboration member.
Type: [MLMemberAbilities](API_MLMemberAbilities.md) object
Required: No

## See Also
<a name="API_MembershipSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MembershipSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MembershipSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MembershipSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
