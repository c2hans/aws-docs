---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-products-share.html
---

# Share products across accounts in API Portal

You can share a product with other AWS accounts using AWS Resource Access Manager (AWS RAM), so that a documentation portal owner in another account can include your product in their portal. You keep control of the product's APIs and pages; the portal owner can't change them. With shared products, one team can run a central portal for the whole organization while each team documents its own APIs.

## Considerations
<a name="apiportal-products-share-considerations"></a>
+ Accounts in the same AWS Organizations organization accept shares automatically when resource sharing is enabled for the organization. Other accounts have 12 hours to accept the invitation.
+ A product that is shared with you can't be shared again.
+ If you unshare a product that a portal includes, the portal fails to publish until its owner removes the product.
+ APIs documented through a product shared from another organization are billed through the portal only and aren't credited against the portal owner's discovery charge. See [How API Portal is billed](apiportal-how-it-fits.md#apiportal-how-it-fits-pricing).

## Share your product
<a name="apiportal-products-share-owner"></a>

**To share a product**

1. On the product detail page, choose the **Product sharing** tab, and then **Create resource share**.

1. In AWS RAM, enter a name, keep the product selected, and under **Principals** enter the account IDs or organizational units to share with. Choose **Create resource share**.

```
aws ram create-resource-share \
    --name "payments-apis" \
    --resource-arns arn:aws:apiportal:us-east-1:{{111122223333}}:products/{{product-id}} \
    --principals {{444455556666}} \
    --region us-east-1
```

## Add a shared product to your documentation portal
<a name="apiportal-products-share-consumer"></a>

**To add a shared product**

1. If the share came from outside your organization, accept the invitation in the AWS RAM console within 12 hours.

1. Under **API Portal**, choose **Documentation portals**, and then choose your portal.

1. On the **Products** tab, choose **Add products**, select the shared product (shown with its owner account), and choose **Add**.

1. Publish the portal.

To list the products shared with you using the AWS CLI, run `aws apiportal list-products --resource-owner OTHER_ACCOUNTS`.
