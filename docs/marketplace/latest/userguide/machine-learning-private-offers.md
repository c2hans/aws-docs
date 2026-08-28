---
source_url: https://docs.aws.amazon.com/marketplace/latest/userguide/machine-learning-private-offers.html
---

# Creating private offers for machine learning products
<a name="machine-learning-private-offers"></a>

 You can negotiate and offer a private offer directly to customers for your machine learning products. For more information on private offers, see [Preparing a private offer for your AWS Marketplace product](private-offers-overview.md).

**Prerequisites:**
+  You must have a paid listing in AWS Marketplace.
+  You must have access to AWS Partner Central.

**To create a private offer for a machine learning product:**

1.  Sign in to AWS Partner Central.

1. Choose **Private offers**, and then choose **Create private offer**

1.  On the **Create private offer** page, select the product that you want to create a private offer for. You can only create offers for available products.

1.  On the **Offer details** page:

   1.  Enter the offer name and description.

   1.  Select the renewal option.

   1.  Set the offer expiration date. Offers expire at 23:59:59 UTC on the set date.

1. Choose **Next** twice.

1.  On the **Configure offer pricing and duration** page, specify:
   +  Pricing option

     (For more information, see [Private offers for ML products](https://docs.aws.amazon.com/marketplace/latest/userguide/private-offers-supported-product-types.html#ml-private-offers))
   + Usage or contract duration
   + Offer currency
   + Pricing dimensions.

     (For usage pricing, the usage based rates only apply during the offer term. For contracts, the usage based rates only apply when the contract term expires and are perpetual.)
**Note**
For more information on installment plans, see [Private offer installment plans](installment-plans.md).

1. Choose **Next**.

1. On the **Add buyers** page, enter the AWS account IDs for your buyers. Then choose **Next**.
**Important**
For linked accounts to benefit from a private offer:
Include the payer AWS account ID.
The payer account must accept the hourly terms of the private offer first.
After the payer account accepts, linked accounts can then accept the private offer.

1. On the **Configure legal terms and offer documents** page, add any custom terms, then choose **Next**.
**Note**
 You can add up to five files (legal terms, statement of work, bill of materials, pricing sheet, or addendums). The system combines these into one document.

1. On the **Review and create** page, verify the offer details and choose **Create offer**.

1. After the offer appears on the **Manage private offers** page, open the **Actions** menu, choose **Copy offer URL**, and email it to the buyer.
**Note**
 Offers may take time to publish. You can edit offers on the **Manage private offers** page until a buyer accepts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
