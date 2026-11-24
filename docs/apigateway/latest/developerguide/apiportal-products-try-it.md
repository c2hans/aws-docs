---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-products-try-it.html
---

# Enable try it for an API in API Portal

When **Try it** is enabled on an API reference page, consumers can enter parameters and send a request to the operation from the documentation portal, and see the response.

## Considerations
<a name="apiportal-products-try-it-considerations"></a>
+ Try it calls the API's invoke URL with the consumer's inputs. Enable it only for APIs that are safe to call from a browser, such as non-production stages, because portal visitors can invoke the operation.
+ Try it isn't available when you preview a portal; it works only on a published portal.
+ The API's own authorization still applies. If the API requires credentials that the consumer doesn't have, the call fails.
+ Try it is off by default for new API reference pages.

**To enable try it**

1. On the product's **Documentation** tab, select the API reference page.

1. Choose **Edit page**, set **Try it** to **Enabled**, and save.

1. Publish the documentation portals that include the product.
