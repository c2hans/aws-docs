---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListBillingGroupCostReportsFilter.html
---

# ListBillingGroupCostReportsFilter
<a name="API_ListBillingGroupCostReportsFilter"></a>

The filter used to retrieve specific `BillingGroupCostReportElements`.

## Contents
<a name="API_ListBillingGroupCostReportsFilter_Contents"></a>

 ** BillingGroupArns **   <a name="billingconductor-Type-ListBillingGroupCostReportsFilter-BillingGroupArns"></a>
The list of Amazon Resource Names (ARNs) used to filter billing groups to retrieve reports.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: No

## See Also
<a name="API_ListBillingGroupCostReportsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListBillingGroupCostReportsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListBillingGroupCostReportsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListBillingGroupCostReportsFilter)
