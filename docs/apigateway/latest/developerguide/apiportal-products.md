---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-products.html
---

# Products in API Portal

A product is a named group of managed APIs together with its documentation. Consumers browse a documentation portal by product. Every product has a product overview page, an API reference page for each API that you choose to document, and any custom pages that you write. You choose a product's APIs yourself, or let API Portal choose them with rules.

## Considerations
<a name="apiportal-products-considerations"></a>
+ Only managed APIs can be added to a product. Promote an API first. See [Managed APIs in API Portal](apiportal-managed-apis.md).
+ A product's API selection mode, custom or rule-based, is fixed when you create it.
+ A product can have up to 40 product pages and up to 40 product API pages. A documentation portal can include up to 200 products.
+ Changes to a product don't appear in a live documentation portal until you publish the portal again.
+ An API that was removed from a rule-based product's matches is kept in the product while it still has an API reference page; delete the page to let the rule remove it.
