---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/opa-design-onboarding.html
---

# Tenant onboarding
<a name="opa-design-onboarding"></a>

The structure of OPA documents must allow for straightforward tenant onboarding without introducing cumbersome requirements. You can organize virtual documents in the OPA document model hierarchy with packages, and these packages can contain many rules. When you plan an OPA document model for a multi-tenant application, first determine which data is necessary for OPA to make a decision. You can provide data as input, pre-load it into OPA, or provide it from external data sources at decision time or periodically. For more information about using external data with OPA, see the section [Retrieving external data for a PDP in OPA](external-data-opa.md) later in this guide.

After you determine the data that is required to make a decision in OPA, consider how to implement OPA rules organized as packages, to make decisions with that data. For example, in a siloed SaaS model where each tenant might have unique requirements for how authorization decisions are made, you could implement tenant-specific OPA packages of rules.

![OPA document model for rules-per-tenant use case](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/38468c97-36f9-4198-8a8a-b0b7f2f956c2.png)

The downside of this approach is that you must add a new set of OPA rules, specific for each tenant, for each tenant that you add to your SaaS application. This is cumbersome and difficult to scale, but might be unavoidable depending on the requirements of your tenants.

Alternatively, in a pooled SaaS model, if all tenants make authorization decisions based on the same rules and use the same data structure, you could use standard OPA packages that have generally applicable rules to make it easier to onboard tenants and scale your OPA implementation.

![OPA document model for generalized rules](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/922303d5-7628-4a1d-b7d2-222f84618d5e.png)

Where possible, we recommend that you use generalized OPA rules and packages (or virtual documents) to make decisions based on standardized data provided by each tenant. This approach makes OPA easily scalable, because you only change the data provided to OPA for each tenant―not how OPA provides its decisions through its rules. It is only necessary to introduce a rules-per-tenant model when individual tenants require unique decisions or have to provide OPA with different data than other tenants.
