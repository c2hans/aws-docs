---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MemberSpecification.html
---

# MemberSpecification
<a name="API_MemberSpecification"></a>

Basic metadata used to construct a new member.

## Contents
<a name="API_MemberSpecification_Contents"></a>

 ** accountId **   <a name="API-Type-MemberSpecification-accountId"></a>
The identifier used to reference members of the collaboration. Currently only supports AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** displayName **   <a name="API-Type-MemberSpecification-displayName"></a>
The member's display name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** memberAbilities **   <a name="API-Type-MemberSpecification-memberAbilities"></a>
The abilities granted to the collaboration member.
Type: Array of strings
Valid Values: `CAN_QUERY | CAN_RECEIVE_RESULTS | CAN_RUN_JOB | CAN_EXPORT_QUERY_ANALYSIS_LOG`
Required: Yes

 ** mlMemberAbilities **   <a name="API-Type-MemberSpecification-mlMemberAbilities"></a>
The ML abilities granted to the collaboration member.
Type: [MLMemberAbilities](API_MLMemberAbilities.md) object
Required: No

 ** paymentConfiguration **   <a name="API-Type-MemberSpecification-paymentConfiguration"></a>
The collaboration member's payment responsibilities set by the collaboration creator.
If the collaboration creator hasn't speciﬁed anyone as the member paying for query compute costs, then the member who can query is the default payer.
Type: [PaymentConfiguration](API_PaymentConfiguration.md) object
Required: No

## See Also
<a name="API_MemberSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MemberSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MemberSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MemberSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
