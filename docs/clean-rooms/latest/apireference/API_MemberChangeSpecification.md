---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MemberChangeSpecification.html
---

# MemberChangeSpecification
<a name="API_MemberChangeSpecification"></a>

Specifies changes to collaboration membership, including adding new members with their abilities and display names.

## Contents
<a name="API_MemberChangeSpecification_Contents"></a>

 ** accountId **   <a name="API-Type-MemberChangeSpecification-accountId"></a>
The AWS account ID of the member to add to the collaboration.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** memberAbilities **   <a name="API-Type-MemberChangeSpecification-memberAbilities"></a>
The abilities granted to the collaboration member. These determine what actions the member can perform within the collaboration.
The following values are currently not supported: `CAN_QUERY` and `CAN_RUN_JOB`.
Set the value of `memberAbilities` to `[]` to allow a member to contribute data.
Set the value of `memberAbilities` to `[CAN_RECEIVE_RESULTS]` to allow a member to contribute data and receive results.
Set the value of `memberAbilities` to `[CAN_EXPORT_QUERY_ANALYSIS_LOG]` so that the member can export the analysis logs for a protected query. Having this ability isn't sufficient on its own: You can export logs only for queries that you ran or paid for.
Type: Array of strings
Valid Values: `CAN_QUERY | CAN_RECEIVE_RESULTS | CAN_RUN_JOB | CAN_EXPORT_QUERY_ANALYSIS_LOG`
Required: Yes

 ** displayName **   <a name="API-Type-MemberChangeSpecification-displayName"></a>
Specifies the display name that will be shown for this member in the collaboration. While this field is required when inviting new members, it becomes optional when modifying abilities of existing collaboration members.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: No

 ** mlMemberAbilities **   <a name="API-Type-MemberChangeSpecification-mlMemberAbilities"></a>
The ML member abilities for a collaboration member.
Type: [MLMemberAbilities](API_MLMemberAbilities.md) object
Required: No

 ** paymentConfiguration **   <a name="API-Type-MemberChangeSpecification-paymentConfiguration"></a>
An object representing the collaboration member's payment responsibilities set by the collaboration creator.
Type: [PaymentConfiguration](API_PaymentConfiguration.md) object
Required: No

## See Also
<a name="API_MemberChangeSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MemberChangeSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MemberChangeSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MemberChangeSpecification)
