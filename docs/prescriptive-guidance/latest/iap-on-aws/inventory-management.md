---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/inventory-management.html
---

# Inventory management
<a name="inventory-management"></a>

Service Catalog has its own internal inventory management capability that registers products when they are provisioned through product sharing and self-service. However, we recommend that you use [AWS Config](https://aws.amazon.com/config/) or [AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) and related services to manage your product-provisioned resources. These tools provide a more comprehensive and integrated approach to managing your provisioned Service Catalog products with the rest of your AWS infrastructure.  AWS Config lets you inventory and perform actions on provisioned products on the console or by using the AWS SDK API. AppRegistry, which is integrated with Application Manager, also provides inventory management for Service Catalog provisioned products.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
