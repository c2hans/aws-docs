---
source_url: https://docs.aws.amazon.com/marketplace/latest/buyerguide/multi-currency-invoicing.html
---

# Multi-currency invoicing and payment considerations
<a name="multi-currency-invoicing"></a>

When working with private offers in multiple currencies, several payment and invoicing considerations apply:
+ As an AWS customer, you can select a currency as your preferred currency for AWS Marketplace invoices that are priced in USD. This preference is based on your location. For more information about supported currencies, see [Supported currencies](buyer-paying-for-products.md#supported-currencies).
+ You can use payment profiles to manage payment methods when receiving invoices from multiple AWS service providers (seller of record). You can create payment profiles configured for each AWS service provider, specifying the currency and preferred payment method. For more information, see [Managing your payment profiles](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-paymentprofiles.html) in the *AWS Billing User Guide*.
+ If you purchase a private offer that is priced in non-USD currency, that invoice will override both your preferred currency and the currency in payment profiles. An invoice will be generated in the offer currency.

**Important**
Check with your finance, accounting, and operations teams in your organization regarding these different payment and currency constructs before accepting a private offer from AWS Marketplace.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
