---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BillingGroupCostReportResultElement.html
---

# BillingGroupCostReportResultElement
<a name="API_BillingGroupCostReportResultElement"></a>

A paginated call to retrieve a list of summary reports of actual AWS charges and the calculated AWS charges, broken down by attributes.

## Contents
<a name="API_BillingGroupCostReportResultElement_Contents"></a>

 ** Arn **   <a name="billingconductor-Type-BillingGroupCostReportResultElement-Arn"></a>
The Amazon Resource Number (ARN) that uniquely identifies the billing group.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: No

 ** Attributes **   <a name="billingconductor-Type-BillingGroupCostReportResultElement-Attributes"></a>
The list of key-value pairs that represent the attributes by which the `BillingGroupCostReportResults` are grouped. For example, if you want the Amazon S3 service-level breakdown of a billing group for November 2023, the attributes list will contain a key-value pair of `"PRODUCT_NAME"` and `"S3"` and a key-value pair of `"BILLING_PERIOD"` and `"Nov 2023"`.
Type: Array of [Attribute](API_Attribute.md) objects
Required: No

 ** AWSCost **   <a name="billingconductor-Type-BillingGroupCostReportResultElement-AWSCost"></a>
The actual AWS charges for the billing group.
Type: String
Required: No

 ** Currency **   <a name="billingconductor-Type-BillingGroupCostReportResultElement-Currency"></a>
The displayed currency.
Type: String
Required: No

 ** Margin **   <a name="billingconductor-Type-BillingGroupCostReportResultElement-Margin"></a>
The billing group margin.
Type: String
Required: No

 ** MarginPercentage **   <a name="billingconductor-Type-BillingGroupCostReportResultElement-MarginPercentage"></a>
The percentage of the billing group margin.
Type: String
Required: No

 ** ProformaCost **   <a name="billingconductor-Type-BillingGroupCostReportResultElement-ProformaCost"></a>
The hypothetical AWS charges based on the associated pricing plan of a billing group.
Type: String
Required: No

## See Also
<a name="API_BillingGroupCostReportResultElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/BillingGroupCostReportResultElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/BillingGroupCostReportResultElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/BillingGroupCostReportResultElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
