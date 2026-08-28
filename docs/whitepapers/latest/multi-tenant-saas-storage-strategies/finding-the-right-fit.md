---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/finding-the-right-fit.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Finding the right fit
<a name="finding-the-right-fit"></a>

 Selecting a multitenant partitioning storage model strategy is influenced by many different factors. If you are migrating from an existing solution, you might favor adopting a silo model because it creates the simplest and cleanest way to transition to multitenancy without rewriting your SaaS application. If you have regulatory or industry dynamics that demand a more isolated model, the efficiency and agility of the pool model might unlock your path to an environment that embraces rapid and continual releases. The key here is to acknowledge that the strategy you select will be driven by a combination of the business and technical considerations in your environment.

 In the following sections, we highlight the strengths and weaknesses of each model and provide you with a well-defined set of data points to use as part of your broader assessment. You’ll learn how each model influences your ability to align with the agility goals that are often at the core of adopting a SaaS model. When selecting an architectural strategy for your SaaS environment, consider how that strategy impacts your ability to rapidly build, deliver, and deploy versions in a zero downtime environment.

## Assessing tradeoffs
<a name="assessing-tradeoffs"></a>

 If you were to put the three partitioning models—silo, bridge, and pool—on a spectrum, you’d see the natural tensions associated with adopting any one of these strategies. The qualities that are listed as strengths for one model are often represented as weaknesses in another model. For example, the tenets and value system of the silo model are often in opposition to those of the pool model.

![A diagram depicting the partitioning model tradeoffs.](http://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/images/partitioning-tradeoffs.png)

 The preceding figure highlights these competing tenets. Across the top of the diagram, you’ll see the three partitioning models represented. On the left are the pros and cons associated with the silo model. On the right, we provide similar lists for the pool model. The bridge model is a bit of a hybrid of these considerations and, as such, represents a mix of the pros and cons shown at the extremes.

 **Silo model tradeoffs**

 Representing tenant data in completely separate databases can be appealing. In addition to simplifying migration of existing single-tenant solutions, this approach also addresses concerns some tenants might have about operating a fully shared infrastructure.

### Pros
<a name="pros"></a>
+  **Silo is appealing for SaaS solutions that have strict regulatory and security constraints** — In these environments, your SaaS customers have very specific expectations about how their data must be isolated from other tenants. The silo model lets you offer your tenants an option to create a more concrete boundary between tenant data, and provides your customers with a sense that their data is stored in a more dedicated model.
+  **Cross-tenant impacts can be limited** — The idea here is that, via the isolation of the silo model, you can ensure that the activity of one tenant does not impact another tenant. This model allows for tenant-specific tuning, where the database performance SLAs of your system can be tailored to the needs of a given tenant. The knobs and dials that are used to tune the database also generally have a more natural mapping to the silo model, which makes it simpler to configure a tenant-centric experience.
+  **Availability is managed at the tenant level, minimizing tenant exposure to outages** — With each tenant in their own database, you don’t have to be concerned that a database outage might cascade across all of your tenants. If one tenant has data issues, they are unlikely to adversely impact any of the other tenants of the system.

### Cons
<a name="cons"></a>
+  **Provisioning and management is more complex** — Any time you introduce a per-tenant piece of infrastructure, you’re also introducing another moving part that must be provisioned and managed on a tenant-by-tenant basis. You can imagine, for example, how a siloed database solution might impact the tenant onboarding experience for your system. Your signup process will require automation that creates and configures a database during the onboarding process. It’s certainly achievable, but it adds a layer of complexity and a potential point of failure in your SaaS environment.
+  **Your ability to view and react to tenant activity is undermined** — With SaaS, you might want a management and monitoring experience that provides a cross-tenant view of system health. You want to proactively anticipate database performance issues and react with policies in a more holistic way. However, the silo model makes you work harder to find and introduce tooling to create an aggregated, system-wide view of health that spans all tenants.
+  **The distributed nature of a silo model impacts your ability to effectively analyze and assess performance trends across tenants** — With each tenant storing data in its own silo, you can only manage and tune service loads in a tenant-centric model. This essentially leads to the introduction of a set of one-off settings and policies that you have to manage and tune independently. This can be both inefficient and could impose overhead that undermines your ability to respond quickly to customer needs.
+  **Silo limits cost optimization** — Perhaps the most significant downside, the one-off nature of the silo model tends to limit your ability to tune your consumption of storage resources.

## Pool model tradeoffs
<a name="pool-model-tradeoffs"></a>

 The pool model represents the ultimate all-in commitment to the SaaS lifestyle. With the pool model, your focus is squarely on having a unified approach to your tenants that lets you streamline tenant storage provisioning, migration, management, and monitoring.

### Pros
<a name="pros-1"></a>
+  **Agility** — Once all of your tenant data is centralized in one storage construct, you are in a much better position to create tooling and a lifecycle that supports a streamlined, universal approach to rapidly deploying storage solutions for all of your tenants. This agility also extends to your onboarding process. With the pool model, you don’t need to provision separate storage infrastructure for each tenant that signs up for your SaaS service. You can simply provision your new tenant and use that tenant’s ID as the index to access the tenant’s data from the shared storage model used by all of your tenants.
+  **Storage monitoring and management is simpler** — In the pool model, it’s much more natural to put tooling and aggregated analytics into place to summarize tenant storage activity. The everyday tools you’d use to manage a single storage model can be leveraged here to build a comprehensive, cross-tenant view of your system’s health. With the pool model, you are in a much better position to introduce global policies that can be used to proactively respond to system events. Generally, the unification of data into a single database and shared representation simplifies many aspects of the multitenant storage, deployment, and management experience.
+  **Additional options help optimize the cost footprint of your SaaS solutions** — The costs opportunities often show up in the form of performance tuning. You might, for example, have throughput optimization that is applied across all tenants as one policy (instead of managing separate policies on a tenant-by-tenant basis).
+  **Pool improves deployment automation and operational agility** — The shared nature of the pool model generally reduces the overall complexity of your database deployment automation, which aligns nicely with the SaaS demand for continual and frequent releases of new product capabilities.

### Cons
<a name="cons-1"></a>
+  **Agility means a higher bar for managing scale and availability** — Imagine the impact of a storage outage in a pooled multitenant environment. Now, instead of having one customer down, *all* of your customers are down. This is why organizations that adopt a pool model also tend to invest much more heavily in the automation and testing of their environments. A pooled solution demands proactive monitoring solutions and robust versioning, data, and schema migration. Releases must go smoothly and tenant issues need to be captured and surfaced efficiently.
+  **Pool challenges management of tenant data distribution** — In some instances, the size and distribution of tenant data can also become a challenge with pooled storage. Tenants tend to impose widely varying levels of load on your system and these variations can undermine your storage performance. The pool model requires more thought about the mechanisms that you will employ to account for these variations in tenant load. The size and distribution of data can also influence how you approach data migration. These issues are typically unique to a given storage technology and need to be addressed on a case-by-case basis.
+  **The shared nature of the pooled environment can meet resistance in some domains** — For some SaaS products, customers will demand a silo model to address their regulatory and internal data protection requirements.

## Hybrid: The business compromise
<a name="hybrid-the-business-compromise"></a>

 For many organizations, the choice of a strategy is not as simple as selecting the silo, bridge, or pool model. Your tenants and your business are going to have a significant influence on how you approach selection of a storage strategy.

 In some cases, a team might identify a small collection of their tenants that require the silo or bridge model. Once they’ve made this determination, they assume that they have to implement all of the storage with that model. This artificially limits your ability to embrace those tenants that may be open to a pool model. In fact, it may add cost or complexity for a tier of tenants that aren’t demanding the attributes of the silo or bridge model.

 One possible compromise is to build a solution that fully supports pooled storage as your foundation. Then, you can carve out a separate database for those tenants that demand a siloed storage solution. The following figure provides an example of this approach in action.

![A diagram depicting hybrid silo/pool storage .](http://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/images/hybrid-solo-pool-storage.png)

 Here, we have two tenants (Tenant 1 and Tenant 2) that are leveraging a silo model, and the remaining tenants are running in a pooled storage model. This is magically abstracted away by a data access layer that hides developers from the tenant’s underlying storage.

 Although this can add a level of complexity to your data access layer and management profile, it can also offer your business a way to tier your offering to represent the best of both worlds.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
