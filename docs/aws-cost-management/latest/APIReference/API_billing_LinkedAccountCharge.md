---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_LinkedAccountCharge.html
---

# LinkedAccountCharge
<a name="API_billing_LinkedAccountCharge"></a>

Enterprise Support charges for a linked account.

## Contents
<a name="API_billing_LinkedAccountCharge_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-accountId"></a>
The linked account ID.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** billableSeconds **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-billableSeconds"></a>
The number of billable seconds in the billing period based on when the account was subscribed to Enterprise Support.
Type: Long
Required: Yes

 ** payerAccountId **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-payerAccountId"></a>
The payer account ID that is authorized to view Enterprise Support data for all accounts in its Support profile.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** proratedTotalSupportEligibleSpend **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-proratedTotalSupportEligibleSpend"></a>
The prorated total support-eligible spend based on when the account was subscribed to Enterprise Support.
Type: String
Required: Yes

 ** totalSeconds **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-totalSeconds"></a>
The total number of seconds in the billing period.
Type: Long
Required: Yes

 ** totalSupportEligibleSpend **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-totalSupportEligibleSpend"></a>
The total support-eligible spend for this account.
Type: String
Required: Yes

 ** accountType **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-accountType"></a>
The type of account.
Type: String
Required: No

 ** linkedTimePeriods **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-linkedTimePeriods"></a>
The time periods during which this account was linked.
Type: Array of [EnterpriseSupportTimePeriod](API_billing_EnterpriseSupportTimePeriod.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Required: No

 ** subscriptionTimePeriods **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-subscriptionTimePeriods"></a>
The subscription time periods for this account.
Type: Array of [EnterpriseSupportTimePeriod](API_billing_EnterpriseSupportTimePeriod.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Required: No

 ** supportEligibleSpendByService **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-supportEligibleSpendByService"></a>
The support-eligible spend broken down by service.
Type: Array of [ServiceLevelAccountUsage](API_billing_ServiceLevelAccountUsage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** totalSupportEligibleReservedInstanceSpend **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-totalSupportEligibleReservedInstanceSpend"></a>
The total support-eligible Reserved Instance spend for this account.
Type: String
Required: No

 ** totalSupportEligibleSavingsPlanSpend **   <a name="awscostmanagement-Type-billing_LinkedAccountCharge-totalSupportEligibleSavingsPlanSpend"></a>
The total support-eligible Savings Plan spend for this account.
Type: String
Required: No

## See Also
<a name="API_billing_LinkedAccountCharge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/LinkedAccountCharge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/LinkedAccountCharge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/LinkedAccountCharge)
