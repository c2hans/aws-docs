---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/pool-isolation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Pool isolation
<a name="pool-isolation"></a>

 It’s pretty easy to see how the silo model of isolation maps very nicely for many SaaS companies. At the same, many companies that are moving to SaaS are seeking out the efficiency, agility, and cost benefits of being able to have their tenants share some or all of their underlying infrastructure. This shared infrastructure approach, which is referred to as a pool model, adds a level of complexity to the isolation story. The diagram in Figure 2 provides an illustration of the challenge associated with implementing isolation in a pooled model.

![Diagram showing pooled isolation.](http://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/pooled-isolation.jpg)

In this model, you’ll notice that our tenants are consuming infrastructure that is shared by all tenants. This enables the resources to scale in direct proportion to the actual load being imposed by the tenants. To the right of the diagram, we’ve zoomed into the compute of one of the services, highlighting the fact that tenants 1-N may all be running side-by-side within your shared compute at any given time. You’ll also notice that the storage in this example is also shared. Here we’ve represented a table that is indexed by individual tenant identifiers.

 Now, while this model is a perfectly good fit for SaaS providers, you can see how this complicates the overall isolation story. With resources being shared, it’s unclear what it would mean here to implement isolation. We can’t lean on the typical networking and IAM constructs to create boundaries between tenants.

 The key here is that—even though this is a more challenging environment to isolation—you cannot use this as a rationale to relax the isolation requirements of your environment. If anything, these shared model increases the chance for cross-tenant access and, as such, it represents an area that requires you to be especially diligent about ensuring that resources are isolated.

 As we dig deeper into the pool isolation model, you’ll see how this architectural footprint introduces a unique blend of challenges—each of which requires its own type of isolation constructs to successfully isolate a tenant’s resources.

## Pool model pros and cons
<a name="pool-model-pros-and-cons"></a>

 While having everything shared enables a lot of efficiency and optimization, it also requires SaaS providers to weigh some of the tradeoffs that come with adopting this model. In many cases, the pros and cons of the pool model end up surfacing as the inverse of pros and cons we covered for the silo model. The following is an outline of the key pros and cons that are typically associated with the pool isolation model.

### Pros
<a name="pros-1"></a>
+  **Agility** – As you move all tenants into a shared infrastructure model, you get all the natural efficiencies and simplicity that streamlines the agility of your SaaS offering. At its core, the pool model is all about enabling SaaS providers to manage, scale, and operate all of its tenants with one unified experience. Centralizing and standardizing the experience is foundational to enabling SaaS providers to easily manage and apply changes to all tenants without having to perform one-off tasks on a tenant-by-tenant basis. This operational efficiency is key to the overall agility footprint of your SaaS environment.
+  **Cost efficiency** – Many companies are drawn to SaaS for its cost efficiency. A big part of this cost efficiency is commonly associated with the pool model of isolation. In a pooled environment, your system will scale based on the actual load and activity of all of your tenants. If all the tenants are offline, your infrastructure costs should be minimal. The key concept here is that pooled environments can adjust to tenant load dynamically and enable you to better align tenant activity with resource consumption.
+  **Simplified management and operations** – The pool model of isolation gives me one view into all the tenants in my system. I can manage, update, and deploy all of my tenant through a single experience that touches all the tenants in my system. This makes most aspects of the management and operations footprint simpler.
+  **Innovation** – The agility that is enabled by the pooled isolation model also tends to be core to enabling SaaS providers to innovate at a faster pace. The more you move away from distributed management and the complexity of the silo model, the more you’re freed up to focus on the features and functions of your product.

### Cons
<a name="cons-1"></a>
+  **Noisy neighbor** – The more resources are shared, the more chances there are for one tenant to impact the experience of another. Any activity from one tenant that puts heavy load on the system, for example, has the potential to impact other tenants. A good multi-tenant architecture and design will try to limit these impacts, but there’s always some chance of a noisy neighbor condition impact one or more of your tenants in a pooled isolation model.
+  **Tenant cost tracking** – In a silo model, it’s much easier to attribute consumption of a resource to a specific tenant. However, in a pooled model, the attribution of resources consumption becomes more challenging. This pushes more work to each SaaS provider as they look for ways to instrument their systems and surface the granular data needed to effectively associate consumption with individual tenants.
+  **Blast radius** – Having all of your resources shared also introduces some operational risk. In the silo model, when one tenant had a failure, the impact of that failure could likely be limited to that one tenant. However, in a pooled environment, an outage will likely impact all the tenants of your system. This can have a significant impact on the business. This usually requires an even deeper commitment to building a resilient environment that can identify, surface, and gracefully recover from failures.
+  **Compliance pushback** – While there are measures you can take to isolate your tenants in a pool model, the notion of sharing infrastructure can create situations where customers may be unwilling to run in this model. This is especially true in environments where the compliance or regulatory rules for a domain impose strict constraints on the accessibility and isolation of resources. Even in these cases, though, this may mean some portion of the system will need to be siloed (see the bridge model below).
