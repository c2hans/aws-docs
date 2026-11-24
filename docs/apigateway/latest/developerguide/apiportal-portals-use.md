---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-portals-use.html
---

# Use a documentation portal as a consumer

Consumers open the portal URL that you share with them. If the portal requires sign-in, they're redirected to the sign-in page for your Amazon Cognito user pool and, after signing in, see the products their access allows. The sidebar lists products; each product has an overview page, any custom pages, and one API reference page per operation. On an API reference page, consumers see the method, URL, and documentation, and, if try it is enabled, can send a request and view the response.

## Troubleshoot a portal
<a name="apiportal-portals-use-troubleshoot"></a>

The portal site can't be reached.
Make sure the portal is published. If it uses a custom domain, make sure the DNS record points to the portal's default domain name.

Consumers get a sign-in error.
Confirm the user pool, app client, and domain on the portal match your user pool, that the portal URL is a callback URL on the app client, and that the user exists in the pool. Publish again after changes.

A signed-in consumer sees no products.
With fine-grained access control, the consumer's group role must allow `apiportal:GetProduct` on the products. Check their group membership and the role's policy.

Pages or products are missing or outdated.
Publish the portal again. The live portal is a snapshot from the last publish.

Try it fails.
Confirm try it is enabled on the page and the portal is published (not a preview), and that the consumer's inputs satisfy the API's own authorization.
