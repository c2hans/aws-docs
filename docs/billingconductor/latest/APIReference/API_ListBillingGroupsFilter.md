---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListBillingGroupsFilter.html
---

# ListBillingGroupsFilter
<a name="API_ListBillingGroupsFilter"></a>

The filter that specifies the billing groups and pricing plans to retrieve billing group information.

## Contents
<a name="API_ListBillingGroupsFilter_Contents"></a>

 ** Arns **   <a name="billingconductor-Type-ListBillingGroupsFilter-Arns"></a>
The list of billing group Amazon Resource Names (ARNs) to retrieve information.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: No

 ** AutoAssociate **   <a name="billingconductor-Type-ListBillingGroupsFilter-AutoAssociate"></a>
Specifies if this billing group will automatically associate newly added AWS accounts that join your consolidated billing family.
Type: Boolean
Required: No

 ** BillingGroupTypes **   <a name="billingconductor-Type-ListBillingGroupsFilter-BillingGroupTypes"></a>
 Filter billing groups by their type.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `STANDARD | TRANSFER_BILLING`
Required: No

 ** Names **   <a name="billingconductor-Type-ListBillingGroupsFilter-Names"></a>
 Filter billing groups by their names.
Type: Array of [StringSearch](API_StringSearch.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** PricingPlan **   <a name="billingconductor-Type-ListBillingGroupsFilter-PricingPlan"></a>
The pricing plan Amazon Resource Names (ARNs) to retrieve information.
Type: String
Pattern: `arn:aws(-cn)?:billingconductor::(aws|[0-9]{12}):pricingplan/(BasicPricingPlan|Passthrough|[a-zA-Z0-9]{10})`
Required: No

 ** PrimaryAccountIds **   <a name="billingconductor-Type-ListBillingGroupsFilter-PrimaryAccountIds"></a>
 A list of primary account IDs to filter the billing groups.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `[0-9]{12}`
Required: No

 ** ResponsibilityTransferArns **   <a name="billingconductor-Type-ListBillingGroupsFilter-ResponsibilityTransferArns"></a>
 Filter billing groups by their responsibility transfer ARNs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Pattern: `arn:[a-z0-9][a-z0-9-.]{0,62}:organizations::\d{12}:transfer/o-[a-z0-9]{10,32}/(billing)/(inbound|outbound)/rt-[0-9a-z]{8,32}`
Required: No

 ** Statuses **   <a name="billingconductor-Type-ListBillingGroupsFilter-Statuses"></a>
 A list of billing groups to retrieve their current status for a specific time range
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `ACTIVE | PRIMARY_ACCOUNT_MISSING | PENDING`
Required: No

## See Also
<a name="API_ListBillingGroupsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListBillingGroupsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListBillingGroupsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListBillingGroupsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
