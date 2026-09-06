---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-design-tiered.html
---

# Tiered deployment model
<a name="avp-design-tiered"></a>

By creating a tiered deployment model, you can isolate high-priority "Enterprise Tier" tenants from the potentially higher volume of "Standard Tier" customers. In this model, you can roll out any changes deployed to policies in policy stores separately for each tier, which isolates each tier of customers from changes made outside of their tier. In the tiered deployment model, the policy stores are typically created as part of initial infrastructure provisioning for each tier instead of being deployed when a tenant is onboarded.

If your solution primarily uses a pooled isolation model, you might require additional isolation or customization. For example, you can create a "Premium Tier" where each tenant would get their own tenant tier infrastructure, which creates a siloed model by deploying a pooled instance with only one tenant. This could take the form of "Premium Tier Tenant A" and "Premium Tier Tenant B" infrastructures that are completely separated, including policy stores. This approach results in a siloed isolation model for the highest level of customers.

In the tiered deployment model, each policy store should follow the same isolation model, although it's deployed separately. Because there are multiple policy stores being used, you need to enforce a consistent way of sharing the policy store identifier that's associated with the tenant across the entire SaaS solution. As with the per-tenant policy store model, it's a good practice to map the tenant identifier to the user's SaaS identity during user registration.

The following diagram shows three tiers: `Standard Tier`, `Enterprise Tier`, and `Premium Tier 1`. Each tier is deployed separately in its own infrastructure and uses one shared policy store within the tier. The Standard and Enterprise Tiers contain multiple tenants. `TenantA` and `TenantB` are in the `Standard Tier`, and `TenantC` and `TenantD` are in the Enterprise Tier.

`Premium Tier 1` contains only `TenantP`, so you can serve the premium tenant as if the solution had a fully siloed isolation model and provide features such as customized policies. Onboarding a new premium tier customer would result in the creation of a `Premium Tier 2` infrastructure.

**Note**
The application, deployment, and tenant onboarding in the premium tier are identical to the standard and enterprise tiers. The only difference is that the premium tier onboarding workflow begins with the provisioning of a new tier infrastructure.

![Amazon Verified Permissions tiered deployment model](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/30d8589a-484e-437f-98ab-4bf5b8591b28.png)
