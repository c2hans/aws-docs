---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListAccountAssociationsFilter.html
---

# ListAccountAssociationsFilter
<a name="API_ListAccountAssociationsFilter"></a>

The filter on the account ID of the linked account, or any of the following:

 `MONITORED`: linked accounts that are associated to billing groups.

 `UNMONITORED`: linked accounts that are not associated to billing groups.

 `Billing Group Arn`: linked accounts that are associated to the provided Billing Group Arn.

## Contents
<a name="API_ListAccountAssociationsFilter_Contents"></a>

 ** AccountId **   <a name="billingconductor-Type-ListAccountAssociationsFilter-AccountId"></a>
The AWS account ID to filter on.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** AccountIds **   <a name="billingconductor-Type-ListAccountAssociationsFilter-AccountIds"></a>
 The list of AWS IDs to retrieve their associated billing group for a given time range.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Pattern: `[0-9]{12}`
Required: No

 ** Association **   <a name="billingconductor-Type-ListAccountAssociationsFilter-Association"></a>
 `MONITORED`: linked accounts that are associated to billing groups.
 `UNMONITORED`: linked accounts that are not associated to billing groups.
 `Billing Group Arn`: linked accounts that are associated to the provided Billing Group Arn.
Type: String
Pattern: `((arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}|MONITORED|UNMONITORED)`
Required: No

## See Also
<a name="API_ListAccountAssociationsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListAccountAssociationsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListAccountAssociationsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListAccountAssociationsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
