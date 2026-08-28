---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/product-visibility.html
---

# Product visibility in AWS Data Exchange
<a name="product-visibility"></a>

New products initially have limited visibility, accessible only to allowlisted accounts and the product creator. After testing and validation, you can publish your product to make it available in the AWS Marketplace catalog for all buyers. Products in AWS Marketplace can have the following status values:
+ **Staging** – This status indicates an incomplete product for which you're still adding information. After you first save and exit the self-service experience, AWS Marketplace creates an unpublished product containing information from the completed steps. From this status, you can continue to add information or modify submitted details.
+ **Limited** – A product attains this status after it's submitted to AWS Marketplace and passes all validation checks. At this point, the product has a detail page accessible only to your account and allowlisted entities. You can conduct product testing through this detail page.
+ **Public** – When you're prepared to make your product visible to buyers for subscription, update the product visibility in the console. Once processed, the product transitions from **Limited** to **Public** status.
+ **Restricted** – To prevent new users from subscribing to your product, you can restrict it by updating the visibility settings. A **Restricted** status allows existing allowlisted users to continue using the product, but it will no longer be visible to the public or available to new users.

## Updating product visibility
<a name="updating-product-visibility"></a>

1. Sign in to your seller account in the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/).

1. Go to the **Data Products** page and select your product.

1. Choose **Request changes**, select **Update product visibilty**, and then select **Public** or **Restricted**.

1. Review your changes and choose **Submit**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
