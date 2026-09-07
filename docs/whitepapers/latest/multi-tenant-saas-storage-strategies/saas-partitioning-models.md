---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/saas-partitioning-models.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# SaaS partitioning models
<a name="saas-partitioning-models"></a>

 To get started, you need a well-defined conceptual model to help you understand the various implementation strategies.

 The following figure shows the three basic models—silo, bridge, and pool—that are commonly used when partitioning tenant data in a SaaS environment.

 Each partitioning model takes a very different approach to managing, accessing, and separating tenant data. The following sections give a quick breakdown of the models, giving you the ability to explore the values and tenets of each model outside of the context of any specific storage technology.

![A diagram depicting SaaS partitioning models.](https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/images/partitioning-models.png)

## Silo model
<a name="silo-model"></a>

 In the silo model, storage of tenant data is fully isolated from any other tenant data. All constructs that are used to represent the tenant’s data are considered logically “unique” to that client, meaning that each tenant will generally have a distinct representation, monitoring, management, and security footprint.

## Bridge model
<a name="bridge-model"></a>

 The bridge model often represents an appealing compromise for SaaS developers. Bridge moves all of the tenant’s data into a single database, while still allowing some degree of variation and separation for each tenant. Typically, you achieve this by creating separate tables for each tenant and allow, each of which is allowed table to have its own representation of data (schema).

## Pool model
<a name="pool-model"></a>

 The pool model represents the all-in, multitenant model where tenants share all of the system’s storage constructs. Tenant data is placed into a common database and all tenants share a common representation (schema). This requires the introduction of a partitioning key that is used to scope and control access to tenant data. This model tends to simplify a SaaS solution’s provisioning, management, and update experience. It also fits well with the continuous delivery and agility goals that are essential to SaaS providers.

## Setting the backdrop
<a name="setting-the-backdrop"></a>

 The silo, bridge, and pool models provide the backdrop for our discussion. As you dig into each AWS storage technology, you’ll discover how the conceptual elements of these models are realized on a specific AWS storage technology. Some map very directly to these models; others require a bit more creativity to achieve each type of tenant isolation.

 It’s worth noting that these models are all equally valid. Although we’ll discuss the merits of each, the regulatory, business, and legacy dimensions of a given environment often play a big role in shaping the approach you ultimately select. The goal here is to simply bring visibility to the mechanics and tradeoffs associated with each approach.
