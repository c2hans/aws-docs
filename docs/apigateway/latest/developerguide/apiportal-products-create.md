---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-products-create.html
---

# Create a product in API Portal

The following procedure creates a custom product, where you pick the APIs. To have API Portal pick them for you, see [Create a rule-based product in API Portal](apiportal-products-rules.md).

**To create a product**

1. In the main navigation pane, under **API Portal**, choose **Products**, and then choose **Create product**.

1. For **Product name**, enter a name. Optionally, enter a **Product description**.

1. For **Product type**, choose **Custom**. Choose **Next**.

1. On the **Select APIs** page, select managed APIs and choose **Add to product**. They move to the **Selected APIs** list. Choose **Next**.

1. Review the product and choose **Create product**.

The product detail page opens with tabs for **APIs**, **Documentation**, **Product sharing**, and **Tags**. Next, create an API reference page (a *product API page*) for each API that you want to document, and any custom pages (*product pages*); see [Manage product documentation in API Portal](apiportal-products-pages.md). Then add the product to a documentation portal ([Documentation portals in API Portal](apiportal-documentation-portals.md)).

Using the AWS CLI:

```
aws apiportal create-product \
    --display-name "Payments APIs" \
    --description "APIs for the payments platform" \
    --api-selection-configuration '{"apiSelectionMode":"CUSTOM"}' \
    --region us-east-1

aws apiportal associate-managed-apis \
    --product-id {{product-id}} \
    --managed-api-ids {{managed-api-id-1}} {{managed-api-id-2}} \
    --region us-east-1
```
