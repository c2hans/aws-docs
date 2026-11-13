---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AccountOverview.html
---

# AccountOverview
<a name="API_AccountOverview"></a>

Contains overview information about an account, including its findings and, for an organization, its member accounts.

## Contents
<a name="API_AccountOverview_Contents"></a>

 ** accountId **   <a name="guardduty-Type-AccountOverview-accountId"></a>
The AWS account ID.
Type: String
Required: No

 ** accountRankings **   <a name="guardduty-Type-AccountOverview-accountRankings"></a>
A ranking of member accounts.
Type: Array of [MemberAccountRanking](API_MemberAccountRanking.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** accountStatus **   <a name="guardduty-Type-AccountOverview-accountStatus"></a>
The status of the account.
Type: String
Required: No

 ** affectedAccountCount **   <a name="guardduty-Type-AccountOverview-affectedAccountCount"></a>
The number of accounts that have findings.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** delegatedAdminAccountId **   <a name="guardduty-Type-AccountOverview-delegatedAdminAccountId"></a>
The account ID of the GuardDuty delegated administrator account.
Type: String
Required: No

 ** detectorId **   <a name="guardduty-Type-AccountOverview-detectorId"></a>
The ID of the detector of the account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** region **   <a name="guardduty-Type-AccountOverview-region"></a>
The AWS Region of the detector.
Type: String
Required: No

 ** totalFindings **   <a name="guardduty-Type-AccountOverview-totalFindings"></a>
The total number of findings.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** totalMemberAccounts **   <a name="guardduty-Type-AccountOverview-totalMemberAccounts"></a>
The total number of member accounts.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_AccountOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AccountOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AccountOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AccountOverview)
