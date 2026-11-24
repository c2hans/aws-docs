---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-products-update-delete.html
---

# Update or delete a product in API Portal

On the product detail page, choose **Edit** to change the name, description, or, for a rule-based product, the rules. For a custom product, choose the **APIs** tab and then **Manage** to add or remove managed APIs. You can't change a product from custom to rule-based or back. Republish any documentation portals that include the product for the changes to appear.

To delete a product, remove it from any documentation portals that include it, and then choose **Delete** on the product detail page. Deleting a product deletes its pages. It doesn't affect the managed APIs or the underlying resources.

```
aws apiportal disassociate-managed-apis --product-id {{product-id}} --managed-api-ids {{managed-api-id}} --region us-east-1
aws apiportal delete-product --product-id {{product-id}} --region us-east-1
```
