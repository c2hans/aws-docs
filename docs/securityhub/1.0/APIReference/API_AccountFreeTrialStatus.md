---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AccountFreeTrialStatus.html
---

# AccountFreeTrialStatus
<a name="API_AccountFreeTrialStatus"></a>

The free trial status of each Security Hub feature for an account.

## Contents
<a name="API_AccountFreeTrialStatus_Contents"></a>

 ** AccountId **   <a name="securityhub-Type-AccountFreeTrialStatus-AccountId"></a>
The AWS account identifier that the free trial statuses apply to.
Type: String
Pattern: `^[0-9]{12}$`
Required: Yes

 ** EvaluatedAt **   <a name="securityhub-Type-AccountFreeTrialStatus-EvaluatedAt"></a>
The date and time at which Security Hub evaluated the free trial statuses for this account. Every status in `FreeTrialStatuses` reflects this point in time.
Type: Timestamp
Required: Yes

 ** FreeTrialStatuses **   <a name="securityhub-Type-AccountFreeTrialStatus-FreeTrialStatuses"></a>
An array of free trial statuses, one for each feature that has a free trial period for the account. The array is empty if the account has no free trial to report.
Type: Array of [FreeTrialStatus](API_FreeTrialStatus.md) objects
Array Members: Maximum number of 50 items.
Required: Yes

## See Also
<a name="API_AccountFreeTrialStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AccountFreeTrialStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AccountFreeTrialStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AccountFreeTrialStatus)
