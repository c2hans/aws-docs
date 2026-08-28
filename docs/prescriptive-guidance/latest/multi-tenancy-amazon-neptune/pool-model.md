---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/multi-tenancy-amazon-neptune/pool-model.html
---

# Pool-model multi-tenancy
<a name="pool-model"></a>

Sometimes it isn't necessary or feasible to implement the silo model because of cost or operational overhead:
+ You might not have the resources to maintain an individual cluster per tenant.
+ It might not be necessary to physically separate each tenant's data, and a logical separation is enough to meet their needs and compliance requirements.

The following diagram shows the pool model, with tenant data is placed in a single Amazon Neptune cluster, and all tenants share a common database.

![The architecture including IAM and a tenant policy.](http://docs.aws.amazon.com/prescriptive-guidance/latest/multi-tenancy-amazon-neptune/images/guide-img/d9a33330-1308-4d3e-b2de-9b5b65b34e0f/images/32d2bc8c-dcea-45e3-8b81-b0b85d7cb287.png)

This [pool-isolation model](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/pool-isolation.html) reduces the management overhead and can improve the operational efficiency because there are fewer clusters to manage. Also, compute resources can be shared across multiple customers instead of remaining idle during customer inactive periods.

When you use the pool model, there are two ways to model data. Your approach depends on whether you're building a labeled property graph (LPG) or a graph with the Resource Description Framework (RDF).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
