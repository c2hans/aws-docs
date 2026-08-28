---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant.html
---

# Tenant
<a name="tenant"></a>

 A tenant is the most fundamental construct of a SaaS environment. As a SaaS provider building an application, you are making this application available to your customers. Any customer that you sign up to use your SaaS environment is one of the tenants of your system. The sum total of all the customers using your SaaS environment are the tenants. Imagine, for example, that your organization has created an accounting service that you want to make available to other companies that will use your service to manage their businesses. Each one of these companies would be viewed as a tenant of your system.

 Upon signing up, a tenant will typically provide user information for the tenant administrator. This tenant administrator can then log into the system and configure it based on the needs of their business. This includes having the ability to add users to a given tenant environment.

 The software that is provided in this model is referred to as a multi-tenant SaaS system because each of the tenants of the service are consuming a single, shared system that supports the needs of these tenants through a unified experience. An update to the system, for example, would typically be applied to all tenants of that system.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
