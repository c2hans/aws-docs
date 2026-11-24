---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-documentation-portals.html
---

# Documentation portals in API Portal

A documentation portal is the branded website that your API consumers visit. It contains one or more products, has its own authorization and domain settings, and serves a snapshot that you publish. The **Documentation portals** page lists your portals with their status (Published, Publish in progress, or Disabled), when they were modified, and when they were last published. Your existing API Gateway portals also appear on this page; see [API Portal and API Gateway Portals](apiportal-how-it-fits.md#apiportal-how-it-fits-portals).

## Considerations
<a name="apiportal-documentation-portals-considerations"></a>
+ A documentation portal is a snapshot. Changes to products, pages, design, or authorization don't appear to consumers until you publish again.
+ A portal can include up to 200 products, from your account or shared with you.
+ Portal authorization controls who can view the portal. It doesn't change the access controls on the APIs that the portal documents.
+ A documentation portal is billed from the time it's created until it's deleted, whether or not it's published. See [How API Portal is billed](apiportal-how-it-fits.md#apiportal-how-it-fits-pricing).
+ Portals are served by CloudFront. A custom domain name requires an ACM certificate in the us-east-1 Region.
