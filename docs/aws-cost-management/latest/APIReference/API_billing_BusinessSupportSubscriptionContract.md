---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BusinessSupportSubscriptionContract.html
---

# BusinessSupportSubscriptionContract
<a name="API_billing_BusinessSupportSubscriptionContract"></a>

A Business Support subscription contract for an account.

## Contents
<a name="API_billing_BusinessSupportSubscriptionContract_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-billing_BusinessSupportSubscriptionContract-accountId"></a>
The account ID associated with this subscription contract.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** contractEndDate **   <a name="awscostmanagement-Type-billing_BusinessSupportSubscriptionContract-contractEndDate"></a>
The end date of the subscription contract.
Type: Timestamp
Required: Yes

 ** contractStartDate **   <a name="awscostmanagement-Type-billing_BusinessSupportSubscriptionContract-contractStartDate"></a>
The start date of the subscription contract.
Type: Timestamp
Required: Yes

 ** planName **   <a name="awscostmanagement-Type-billing_BusinessSupportSubscriptionContract-planName"></a>
The name of the Support plan for this subscription contract. Valid values: `AWSSupportBusiness` (Business Support plan), `AWSSupportDeveloper` (Developer Support plan), `AWSSupportEssential` (Basic Support plan).
Type: String
Required: Yes

## See Also
<a name="API_billing_BusinessSupportSubscriptionContract_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BusinessSupportSubscriptionContract)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BusinessSupportSubscriptionContract)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BusinessSupportSubscriptionContract)
