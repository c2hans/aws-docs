---
source_url: https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-offer-product.html
---

# Offer product data feed
<a name="data-feed-offer-product"></a>

One offer can have several products, and one product can be included in different offers. This data feed lists information about the relationships between offers and products.

This data feed provides information about all product offers you've created as the seller of record.

When you add or remove a product from an offer, you create an offer revision.

The offer product data feed is refreshed every 24 hours, so new data is available daily.

The following table explains the names and descriptions of the data feed's columns. For information about the data feed history columns, see [Historization of the data](data-feed-details.md#data-feed-historization).

| Column name  | Description  |
| --- | --- |
| offer\_id | The friendly identifier of this offer.Can be used to join to the `offer_id` field of the `Offer` data feed. |
| offer\_revision | Combines with offer\_id field to form the foreign key to the offer revision. |
| product\_id | The friendly identifier of the product, this is the foreign key to the product that this offer exposes. Can be used to join to the `product_id` field of the `Product` data feed. |

## Example of Offer product data feed
<a name="data-feed-offer-product-sample-data"></a>

The following shows an example of the Offer product data feed.

| offer\_id  | offer\_revision | product\_id |
| --- | --- | --- |
| offer-dacpxznflfwin | 10 | prod-o4grxfafcxxxx |
| offer-gszhmle5npzip | 24 | prod-o4grxfafcxxxy |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
