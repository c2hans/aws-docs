---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-products-pages.html
---

# Manage product documentation in API Portal

On the product detail page, choose the **Documentation** tab. The **Product pages** panel lists the product's pages; the **Preview** panel shows the selected page as consumers will see it. A product has three kinds of pages.

**Note**
Changes to a product and its pages take effect in a documentation portal only after you publish the portal again. See [Preview, publish, and update a documentation portal](apiportal-portals-publish.md).

*Product overview page*
Every product has one. It introduces the product. You can edit its content but not its format.

*API reference pages (product API pages)*
You create one for each API in the product that you want to document. Its content is generated from the API definition and identified by method and path. You can override the operation name, the invoke URL, and the body text. Each page has a **Try it** setting; see [Enable try it for an API in API Portal](apiportal-products-try-it.md).

*Custom pages (product pages)*
Free-form Markdown pages for getting-started guides, authentication instructions, changelogs, and similar content. A product can have up to 40 product pages and up to 40 product API pages.

Page changes don't appear to consumers until you publish the documentation portals that include the product.

## Add pages to a product and set their order
<a name="apiportal-products-pages-sections"></a>

A new product API page or product page is a draft. Drafts don't appear in a documentation portal until you add them to a section of the product's documentation and publish the portal. You can group pages into named sections and control the order in which sections and pages appear.

**To add a draft page to a section**

1. Open the product and choose the **Documentation** tab. Drafts are listed under **Draft API reference pages** and **Draft documentation pages**.

1. Choose a draft page, and then click **Edit page**.

1. For **Section name**, enter the name of an existing section or a new one, for example `Pets`.

1. Click **Save changes**. The page moves out of drafts and appears under its section.

**To change the display order**

1. On the **Documentation** tab, click **Manage product navigation**.

1. Drag sections and pages into the order you want, and then click **Save changes**.

Using the AWS CLI or SDKs, set the section and display order when you create or update a page with `create-product-page`, `update-product-page`, `create-product-api-page`, or `update-product-api-page`.

Changes appear in a documentation portal only after you publish the portal again. See [Preview, publish, and update a documentation portal](apiportal-portals-publish.md).

## Create, edit, or delete a custom page
<a name="apiportal-products-pages-custom"></a>

**To create a custom page**

1. On the **Documentation** tab, under **Custom documentation pages**, choose **Create custom page**.

1. For **Page title**, enter a title.

1. For **Body**, enter the content in Markdown. The **Preview** panel shows the result.

1. Choose **Create product page**.

To edit a page, select it and choose **Edit page**. To delete it, choose **Delete page**.

```
aws apiportal create-product-page \
    --product-id {{product-id}} \
    --display-content '{"title":"Getting started","body":"# Overview\nHow to call the payments APIs."}' \
    --region us-east-1
```

## Edit an API reference page
<a name="apiportal-products-pages-api"></a>

**To override the generated content of an API reference page**

1. Under **Draft API reference pages** or **API reference pages**, select the page.

1. Choose **Edit page**.

1. Optionally change the **Operation name**, the **API URL** that consumers call, and the **Body**.

1. Choose **Save changes**.

If an API reference page shows a failed status, the underlying resource was deleted or its account left your organization. Delete the page, or remove the API from the product.

```
aws apiportal create-product-api-page \
    --product-id {{product-id}} \
    --managed-api-id {{managed-api-id}} \
    --display-content '{"overrides":{"operationName":"List orders","body":"Returns the caller'"'"'s open orders."}}' \
    --try-it-state DISABLED \
    --region us-east-1
```
