---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MemberSummary.html
---

# MemberSummary
<a name="API_MemberSummary"></a>

The member object listed by the request.

## Contents
<a name="API_MemberSummary_Contents"></a>

 ** abilities **   <a name="API-Type-MemberSummary-abilities"></a>
The abilities granted to the collaboration member.
Type: Array of strings
Valid Values: `CAN_QUERY | CAN_RECEIVE_RESULTS | CAN_RUN_JOB | CAN_EXPORT_QUERY_ANALYSIS_LOG`
Required: Yes

 ** accountId **   <a name="API-Type-MemberSummary-accountId"></a>
The identifier used to reference members of the collaboration. Currently only supports AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** createTime **   <a name="API-Type-MemberSummary-createTime"></a>
The time when the member was created.
Type: Timestamp
Required: Yes

 ** displayName **   <a name="API-Type-MemberSummary-displayName"></a>
The member's display name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** paymentConfiguration **   <a name="API-Type-MemberSummary-paymentConfiguration"></a>
The collaboration member's payment responsibilities set by the collaboration creator.
Type: [PaymentConfiguration](API_PaymentConfiguration.md) object
Required: Yes

 ** status **   <a name="API-Type-MemberSummary-status"></a>
The status of the member.
Type: String
Valid Values: `INVITED | ACTIVE | LEFT | REMOVED`
Required: Yes

 ** updateTime **   <a name="API-Type-MemberSummary-updateTime"></a>
The time the member metadata was last updated.
Type: Timestamp
Required: Yes

 ** membershipArn **   <a name="API-Type-MemberSummary-membershipArn"></a>
The unique ARN for the member's associated membership, if present.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: No

 ** membershipId **   <a name="API-Type-MemberSummary-membershipId"></a>
The unique ID for the member's associated membership, if present.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** mlAbilities **   <a name="API-Type-MemberSummary-mlAbilities"></a>
Provides a summary of the ML abilities for the collaboration member.
Type: [MLMemberAbilities](API_MLMemberAbilities.md) object
Required: No

## See Also
<a name="API_MemberSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MemberSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MemberSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MemberSummary)
