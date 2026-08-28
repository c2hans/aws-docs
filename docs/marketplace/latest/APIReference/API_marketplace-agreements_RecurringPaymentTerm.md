---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_RecurringPaymentTerm.html
---

# RecurringPaymentTerm
<a name="API_marketplace-agreements_RecurringPaymentTerm"></a>

Defines a pricing model where customers are charged a fixed recurring price at the end of each billing period.

## Contents
<a name="API_marketplace-agreements_RecurringPaymentTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** billingPeriod **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RecurringPaymentTerm-billingPeriod"></a>
Defines the recurrence at which buyers are charged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RecurringPaymentTerm-currencyCode"></a>
Defines the currency for the prices mentioned in this term.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RecurringPaymentTerm-id"></a>
The unique identifier for the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** price **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RecurringPaymentTerm-price"></a>
Amount charged to the buyer every billing period.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RecurringPaymentTerm-type"></a>
Type of the term being updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_RecurringPaymentTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/RecurringPaymentTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/RecurringPaymentTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/RecurringPaymentTerm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
