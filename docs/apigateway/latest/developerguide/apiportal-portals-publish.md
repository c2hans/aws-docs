---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-portals-publish.html
---

# Preview, publish, and update a documentation portal

A documentation portal serves a snapshot of its products and pages taken when you publish. Preview shows you the current unpublished content first.

## Preview a portal
<a name="apiportal-portals-publish-preview"></a>

On the portal detail page, choose **Preview**. API Portal builds a short-lived preview and opens it as a consumer would see it. Preview doesn't save anything and doesn't affect the live portal. Try it isn't available in a preview.

## Publish a portal
<a name="apiportal-portals-publish-publish"></a>

**To publish a documentation portal**

1. On the portal detail page, choose **Publish portal**.

1. Optionally enter a **Description of changes**, and choose **Publish portal**.

1. Publishing takes several minutes. **Status** shows **Publish in progress**, then **Published**. Share the portal URL with your consumers.

If publishing fails, the status shows the reason: a product in the portal is no longer shared with you, the custom domain is in use by another distribution, or the certificate isn't in us-east-1. Fix the cause and publish again.

## Publish changes
<a name="apiportal-portals-publish-update"></a>

After you change a product, a page, the portal's products, design, domain, or authorization, the detail page shows that the portal has unpublished changes. Consumers keep seeing the previous snapshot until you choose **Publish portal** again. The portal details page lists each publish with its description.

```
aws apiportal update-portal-publish-status --portal-id {{portal-id}} --status PUBLISHED --description "Added orders product" --region us-east-1
aws apiportal get-portal --portal-id {{portal-id}} --query publishStatus --region us-east-1
```
