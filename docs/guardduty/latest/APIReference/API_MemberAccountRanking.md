---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_MemberAccountRanking.html
---

# MemberAccountRanking
<a name="API_MemberAccountRanking"></a>

Contains information about the position of a member account in a ranking.

## Contents
<a name="API_MemberAccountRanking_Contents"></a>

 ** accountId **   <a name="guardduty-Type-MemberAccountRanking-accountId"></a>
The AWS account ID of the member account.
Type: String
Required: No

 ** findingCount **   <a name="guardduty-Type-MemberAccountRanking-findingCount"></a>
The number of findings in the account.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** rank **   <a name="guardduty-Type-MemberAccountRanking-rank"></a>
The position of the account in the ranking.
Type: Integer
Required: No

 ** riskLevel **   <a name="guardduty-Type-MemberAccountRanking-riskLevel"></a>
The assessed risk level of the account. Possible values are `Info`, `Low`, `Medium`, `High`, and `Critical`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `Info | Low | Medium | High | Critical`
Required: No

 ** riskRationale **   <a name="guardduty-Type-MemberAccountRanking-riskRationale"></a>
The reason for the assessed risk level.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_MemberAccountRanking_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/MemberAccountRanking)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/MemberAccountRanking)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/MemberAccountRanking)
