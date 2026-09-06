---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/conclusion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Conclusion
<a name="conclusion"></a>

 The storage needs of SaaS customers aren’t simple. The reality of SaaS is that your business’s domain, customers, and legacy considerations affect how you determine which combination of multitenant storage options best meet the needs of your business.

 Although there is no single strategy that universally fits every environment, it is clear that some models do align better with the core tenets of the SaaS delivery model. In general, the pool-based approaches to storage—on any AWS storage technology—align well with the need for a unified approach to managing and operating a multitenant environment. Having all your tenants in one shared repository and representation streamlines and unifies your approach’s operational and deployment footprint, enabling cross-tenant views of health and performance.

 The silo and bridge models certainly have their place and, for some SaaS providers, are absolutely required. The key here is that, if you head down this path, agility can get more complicated. Some AWS storage technologies are better positioned to support isolated tenant storage schemes. Building a silo model on Amazon RDS, for example, is less complex than it is on DynamoDB. Generally, whenever you rely on linked accounts as your partitioning model, you will tackle more provisioning, management, and scaling challenges.

 Beyond the mechanics of achieving multitenancy, think about how the profile of each AWS storage technology can fit with the varying needs of your multitenant application’s functionality. Consider how tenants will access the data and how the shape of that data will need to evolve to meet the needs of your tenants. The more you can decompose your application into autonomous services, the better positioned you are to pick and choose separate storage strategies for each service.

 After exploring these services and portioning schemes, you should have a much better sense of the patterns and inflection points that will guide your selection of a multitenant storage strategy. AWS equips SaaS providers with a rich palette of services and constructs that can be combined to address any number of multitenant storage needs.
