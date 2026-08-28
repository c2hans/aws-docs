---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ScheduleItem.html
---

# ScheduleItem
<a name="API_marketplace-agreements_ScheduleItem"></a>

An individual installment of the payment that includes the date and amount of the charge.

## Contents
<a name="API_marketplace-agreements_ScheduleItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** chargeAmount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ScheduleItem-chargeAmount"></a>
The price that the customer would pay on the scheduled date (chargeDate).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** chargeDate **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ScheduleItem-chargeDate"></a>
The date that the customer would pay the price defined in this payment schedule term. Invoices are generated on the date provided.
Type: Timestamp
Required: No

## See Also
<a name="API_marketplace-agreements_ScheduleItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ScheduleItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ScheduleItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ScheduleItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
