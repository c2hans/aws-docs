---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/full-stack-silo-and-pool.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Full stack silo and pool
<a name="full-stack-silo-and-pool"></a>

 Silo and pool can also be used to describe an entire SaaS stack. In this approach, all the resources for a tenant are deployed in either a dedicated or shared manner. The following diagram provides an example of how this might land in a SaaS environment.

![A diagram depicting full stack silo and pool models.](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/images/silo-and-pool-models2.png)

 In this diagram, you’ll see that there are three different models for your full stack tenant deployments. First, you’ll see that there is a full stack pool environment. Tenants in this pool share all the resources (compute, storage, and so on).

 The other two stacks shown are meant to represent full stack siloed tenant environments. In this case, Tenant 3 and Tenant 4 are shown as each having their own dedicated stacks where none of the resources are shared with other tenants.

 This mix of silo and pooled models in the same SaaS environment isn’t all that atypical. Imagine, for example, that you have a set of basic tier tenants that pay a moderate price for using your system. These tenants are placed in the pooled environment.

 Meanwhile, you may also have premium tier tenants that are willing to pay more for the privilege of running in a silo. These customers are deployed with separate stacks (as shown in the diagram).

 Even in this model, where you may have allowed tenants to run in their own full stack silo, it would be essential that these siloes don’t allow any one-off variation or customization for these tenants. In all respects, each of these stacks should be running the same configuration of the stack, with the same version of the software. When a new version is released, it’s deployed to the pooled tenant environment, and each of the siloed environments.
