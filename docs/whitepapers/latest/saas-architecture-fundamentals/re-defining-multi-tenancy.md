---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/re-defining-multi-tenancy.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Re-defining multi-tenancy
<a name="re-defining-multi-tenancy"></a>

 The terms *multi-tenancy* and *SaaS* are often tightly connected. In some instances, organizations describe SaaS and multi-tenancy as the same thing. While this might seem natural, equating SaaS and multi-tenancy tends to lead teams to take a purely technical view of SaaS when, in reality, SaaS is more of a business model than an architecture strategy.

 To better understand this concept, let’s start with the classic view of multi-tenancy. In this purely infrastructure-focused view, multi-tenancy is used to describe how resources are shared by tenants to promote agility and cost efficiency.

 Suppose, for example, you have a microservice or an [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instance that is consumed by multiple tenants of your SaaS system. This service would be viewed as running in a multi-tenant model, because tenants are sharing use of the infrastructure that runs this service.

 The challenge of this definition is that it too directly attaches the technical notion of multi-tenancy to SaaS. It presumes that the defining characteristic of SaaS is that it must have shared, multi-tenant infrastructure. This view of SaaS begins to fall apart as we look at the various ways that SaaS is realized in different environments.

 The following diagram provides a view of a SaaS system that exposes some of the challenges we have with defining multi-tenancy.

 Here you’ll see the classic SaaS model described previously, with a series of application services surrounded by the shared services that allow you to manage and operate your tenants collectively.

 What’s new is the microservices that we’ve included. The diagram includes three sample microservices: *product*, *order*, and *catalog*. If you look closely at the tenancy model of each of these services, you’ll notice they all employ slightly different patterns of tenancy.

![A diagram depciting SaaS and multi-tenancy .](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/images/saas-multi-tenancy.png)

 The product service shares all of its resources (compute and storage) with all tenants. This aligns with the classic definition of multi-tenancy. However, if you look at the order service, you’ll see that it has shared compute, but separate storage for each tenant.

 The catalog service adds another variation where the compute is separate for every tenant (a separate microservice deployment for each tenant), but it shares the storage for all tenants.

 Variations of this nature are common in SaaS environments. [Noisy neighbor](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/noisy-neighbor.html), tiering models, isolation needs—these are amongst a list of reasons that you might selectively share or silo parts of your SaaS solution.

 Given these variations—and many of the other possibilities—it becomes more challenging to figure out how you should use the term *multi-tenant* to characterize this environment. Overall, as far the customer is concerned, this is a multi-tenant environment. However, if we use the most technical definition, some parts of this environment are multi-tenant and some are not.

 This is why it becomes necessary to move away from using the term *multi-tenant* to characterize SaaS environments. Instead, we can talk about how multi-tenancy is implemented within your application, but avoid using it to characterize a solution as being SaaS. If the term *multi-tenant* is to be used, it makes more sense to use it to describe the entire SaaS environment as being multi-tenant, knowing that some parts of the architecture may be shared and some may not. Overall, you are still operating and managing this environment in a multi-tenant model.

## The extreme case
<a name="the-extreme-case"></a>

 To better highlight this notion of tenancy, let’s look at a SaaS model that has tenants that share zero resources. The following diagram provides a sample SaaS environment that is employed by some SaaS providers.

![A diagram depicting stack per tenant.](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/images/stack-per-tenant.png)

 In this diagram, you’ll see that we still have our common environment surrounding these tenants. However, each tenant is deployed with a dedicated collection of resources. Nothing is shared by the tenants in this model.

 This example challenges what it means to be multi-tenant. Is this a multi-tenant environment even though none of the resources are shared? The tenants that consume this system have all the same expectations you’d have of a SaaS environment with shared resources. In fact, they may have no awareness of how their resources are deployed under the hood of the SaaS environment.

 Even though these tenants are running in a siloed infrastructure, they are still managed and operated collectively. They share one unified onboarding, identity, metrics, billing, and operational experience. Also, when a new version is released, it is deployed to all tenants. For this to work, you cannot allow one-off customization for individual tenants.

 This extreme example provides a good model for testing the notion of multi-tenant SaaS. While it may not realize all the efficiencies of shared infrastructure, it is an entirely valid multi-tenant SaaS environment. For some customers, their domain may dictate that some or all of their customers run in this model. That doesn’t mean they are not SaaS. If they use these shared services and all the tenants run the same version, this still complies with the foundational principles of SaaS.

 Given these parameters and this broader definition of SaaS, you can see the need to evolve the use of the term *multi-tenant*. It makes more sense to refer to any SaaS system that is managed and operated collectively as being *multi-tenant*. Then, you can defer to more granular terminology to describe how resources are shared or dedicated within the implementation of a SaaS solution.
