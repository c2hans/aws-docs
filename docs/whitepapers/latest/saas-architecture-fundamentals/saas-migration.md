---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/saas-migration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# SaaS migration
<a name="saas-migration"></a>

 Many of the providers that adopt SaaS migrate to SaaS from a traditional installed software model (described previously). For these providers, it’s especially important to have good alignment on the core principles of SaaS.

 Here, again, is where there can be some confusion about what it means to migrate to a SaaS model. Some, for example, view moving to the cloud as migrating to SaaS. Others view adding automation to their installation and provisioning process as achieving migration.

 It’s fair to say that every organization may start at a different spot, have different legacy considerations, and is likely facing different market and competitive pressures. This means that every migration will look different.

 Still, while every path is different, there are some areas where there are disconnects around the core principles that shape migration strategies. Having good alignment around the concepts and principles can have a significant impact on the overall success of your SaaS migration.

 Based on the concepts outlined previously, it should be clear that the move to SaaS starts with the business strategy and goals. This point can get lost in a migration setting where there is pressure to get to SaaS as quickly as possible.

 In this mode, organizations often view migration primarily as a technical exercise. The reality is, every SaaS migration should start with a clear view of the target customers, the service experience, the operational goals, and so on. Having a clearer focus on what your SaaS business needs to look like will have a profound impact on the shape, priorities, and path you take to migrate your solution to SaaS.

 Having this clear vision from the outset of your migration lays the foundation for how you migrate both the technology and the business as part of your move to SaaS. As you set out on this path, focus on those questions that can tell you the most about where you’re headed.

 The following table provides a view of the contrasting nature of technical and business migration mindsets.

* Table 1 — Technical first vs. business first migration *

|  The tech first mindset  |  The business first mindset  |
| --- | --- |
|  How do we isolate tenant data?  |  How can SaaS help us grow our business?  |
|  How do we connect users to tenants?  |  Which segments are we targeting?  |
|  How do we avoid noisy neighbor conditions?  |  What is the size and profile of these segments?  |
|  How do we do A/B testing?  |  What tiers will we need to support?  |
|  How do we scale based on tenant load?  |  What service experience are we targeting?  |
|  Which billing provider should we use?  |  What is our pricing and packaging strategy?  |

 On the left is an example of what a tech first migration mindset might look like. The engineering team is hyper-focused on chasing the classic multi-tenant topics that are certainly important to any SaaS architecture.

 The problem is that the answers to many of the questions on the left are often directly influenced by the answers to the question on the right. It’s unlikely that this point is new to anyone looking at migration. However, the reality is that many organizations start out by chasing the operational and cost efficiency as their first step, assuming the business bits will work themselves out.

 Within this migration strategy, there can also be confusion about how your legacy environment might be evolved to fit into a SaaS model. This too is an area where there are a multitude of options for migrating to SaaS. However, there is a common value system that we generally advocate for any migration.

 In our previous discussion of SaaS principles, we outlined different patterns and terminologies that are used to describe SaaS environments. One common theme spanning all of those solutions is this idea of having shared services that surround your application. Identity, onboarding, metrics, billing—these are all called out as common elements that are core to any SaaS environment.

 Now, as we look at migration, you’ll see that these same shared services play a key role in any migration story. The following diagram provides a conceptual view of the migration landscape.

![A diagram that depcits migrating to SaaS.](http://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/images/migrating-to-saas.png)

 This diagram represents the target experience for any migration path. It includes all the same shared services that were described previously. In the middle is a placeholder for your application.

 The key idea is that you can land any number of application models in the middle of this environment. Your first step in migration might have each tenant running in its own silo. Or, you may have some hybrid architecture where elements are siloed and other bits of functionality are addressed through a collection of modernized microservices.

 How much you initially modernize your application will vary based on the nature of your legacy environment, market needs, cost considerations, and so on. What doesn’t change is the introduction of these shared services.

 Any SaaS migration needs to support these foundational shared services to give your business the ability to operate in a SaaS model. All variations of the application architecture need SaaS identity, for example. You’ll need tenant-aware operations to manage and monitor your SaaS solution.

 Putting these shared services in place at the front of your migration allows you to present a SaaS experience to your customers—even if the underlying application is still running in a full stack silo for each tenant.

 The general goal is to get your application running in a SaaS model. Then, you can turn your attention to further modernization and refinement of your application. This approach also allows you to move the other parts of your business (marketing, sales, support, and so on) at a faster pace. More importantly, this allows you to begin to engage and collect customer feedback that can be used to shape the ongoing modernization of your environment.

 It’s important to note that the shared services that you put in place may not include every feature or mechanism you’ll ultimately need. The main goal is to create the shared mechanisms that are needed at the outset of your migration. This allows you to focus on the elements of the system that are essential to the evolution of your application architecture and your operational evolution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
