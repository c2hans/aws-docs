---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-activity-and-consumption.html
---

# Tenant Activity and Consumption
<a name="tenant-activity-and-consumption"></a>

 In multi-tenant SaaS environments, it’s important to have visibility into how tenants are using your application and imposing load on your system’s architecture. Tracking this information at the tenant level allows you to assess your system’s ability to effectively scale and support the constantly evolving workloads being placed on your environment. The metrics and insights that are collected from a SaaS system are frequently referred to as tenant activity and consumption.

## Metering and Billing
<a name="metering-and-billing"></a>

 SaaS products are often sold in a pay-as-you-go model where the cost of a product is determined based on the consumption profile of a customer. This model allows customers to have a pricing model that is more tightly coupled to the value and load they are placing on a SaaS system. In this mode, SaaS providers will define and introduce metering mechanism that will measure consumption. This metering data is typically sent to a billing system that aggregates the billing information and generates a bill. Consumption-based pricing represents one model for pricing that can be combined with additional pricing strategies (subscription, for example).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
