---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/inventory-management.html
---

# Inventory management
<a name="inventory-management"></a>

Service Catalog has its own internal inventory management capability that registers products when they are provisioned through product sharing and self-service. However, we recommend that you use [AWS Config](https://aws.amazon.com/config/) or [AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) and related services to manage your product-provisioned resources. These tools provide a more comprehensive and integrated approach to managing your provisioned Service Catalog products with the rest of your AWS infrastructure.  AWS Config lets you inventory and perform actions on provisioned products on the console or by using the AWS SDK API. AppRegistry, which is integrated with Application Manager, also provides inventory management for Service Catalog provisioned products.
