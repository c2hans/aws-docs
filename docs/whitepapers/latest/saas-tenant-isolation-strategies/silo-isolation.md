---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/silo-isolation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Silo isolation
<a name="silo-isolation"></a>

 While SaaS providers are often focused on the value of sharing resources, there are still scenarios where a SaaS provider may choose to have some (or all) of their tenants deployed in a model where each tenant is running a fully siloed stack of resources. Some would say that this full-stack model does not represent a SaaS environment. However, if you’ve surrounded these separate stacks with shared identity, onboarding, metering, metrics, deployment, analytics, and operations, then we’d still say this is still a valid variant of SaaS that trades economies of scale and operational efficiency for compliance, business, or domain considerations. With this approach, isolation is an end-to-end construct that spans an entire customer stack. The diagram in Figure 1 provides a conceptual view of this view of isolation.

![Diagram showing a full stack view of isolation with three tenents.](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/full-stack-isolation.jpg)

This diagram highlights the basic footprint of the siloed deployment model. The technologies that are used run these stacks are mostly irrelevant here. This could be a monolith, it could be serverless, or it could be any mix of the various application architecture models. The key concept here is that we’re going to take whatever stack the tenant has and surround it with some construct to encapsulate all the moving parts of that stack. This becomes our boundary for isolation. As long as you can prevent a tenant from escaping their fully encapsulated environment, you’ve achieved the isolation.

 Generally, this model of isolation is a much simpler to enforce. There are often well-defined constructs that will enable you to implement a robust isolation model. While this model presents some real challenges to the cost and agility goals of a SaaS environment, it can be appealing to those that have very strict isolation requirements.

## Silo model pros and cons
<a name="silo-model-pros-and-cons"></a>

 Each SaaS environment and business domain has its own unique set of requirements that may make silo a fit. However, if you’re leaning in this direction, you’ll definitely want to factor in some of the challenges and overhead associated with the silo model. Below is a list of some of the pros and cons that you need to consider if you are exploring a silo model for your SaaS solution:

### Pros
<a name="pros"></a>
+  **Supporting challenging compliance models** – Some SaaS providers are selling into regulated environments that impose strict isolation requirements. The silo provides these ISVs with an option that enables them to offer to some or all of their tenants the option of being deployed in a dedicated model.
+  **No noisy neighbor concerns** – While all SaaS providers should be attempting to limit the impacts of noisy neighbor conditions, some customers will still express reservations about the potential of having their workloads impacted by the activity of other tenants using the system. Silo addresses this concern by offering a dedicated environment with no potential of noisy neighbor scenarios.
+  **Tenant cost tracking** – SaaS providers are often highly focused on understanding how each tenant is impacting their infrastructure costs. Calculating a cost per tenant can be challenging in some SaaS models. However, the coarse-grained nature of the silo model provides us with a simple way to capture and associate infrastructure costs with each tenant.
+  **Limited blast radius** – The silo model generally reduces your exposure when there may be some outage or event that surfaces in your SaaS solution. Since each SaaS provider is running in its own environment, any failures that occur within a given tenant’s environment will likely be constrained to that environment. While one tenant may experience an outage, the error may not cascade through the remaining tenants that are using your system.

### Cons
<a name="cons"></a>
+  **Scaling issues** – There are limits on the number of accounts that can be provisioned. This limit may exclude you from selecting the account-based model. There are also general concerns about how a rapidly growing number of accounts might undermine the management and operational experience of your SaaS environment. If you have 20 siloed accounts for each of your tenants, for example, that may be manageable. However, if you have a thousand tenants, that would likely begin to impact operational efficiency and agility.
+  **Cost** – With every tenant running in its own environment, we’re missing much of the cost efficiency that is traditionally associated with SaaS solutions. Even if these environments scale dynamically, you’ll likely have periods of the day when you’ll have idle resources that are going un-consumed. While this is a completely acceptable model, it undermines the ability of your organization to achieve the economies of scale and margin benefits that are essential to the SaaS model.
+  **Agility** – The move to SaaS is often directly motivated by a desire to innovate at a faster pace. This means adopting a model that enables the organization to respond and react to market dynamics at a rapid pace. A key part of this is being able to unify the customer experience and quickly deploy new features and capability. While there are measures that can be taken with the silo model to try to limit its impact on agility, the highly decentralized nature of the silo model adds complexity that impacts your ability to easily manage, operate, and support your tenants.
+  **Onboarding automation** – SaaS environments place a premium on automating the introduction of new tenants. Whether these tenants are being onboarded in a self-service model or using an internally managed provisioning process, you’ll still need automated onboarding. And, when you have separate silos for each tenant, this often becomes a much more heavyweight process. The provisioning of a new tenant will require the provisioning of new infrastructure and, potentially, the configuration of new account limits. These added moving parts introduce overhead that introduces additional dimensions of complexity into the overall onboarding automation, enabling you to focus less time on your customers.
+  **Decentralized management and monitoring** – Our goal with SaaS is to have a single pane of glass that lets us manage and monitor all tenant activity. This requirement is especially important when you have siloed tenant environments. The challenge here is that you must now aggregate the data from a more decentralized tenant footprint. While there are mechanisms that will enable you to create an aggregate view of your tenants, the effort and energy needed to build and manage this experience is more complex in a siloed model.
