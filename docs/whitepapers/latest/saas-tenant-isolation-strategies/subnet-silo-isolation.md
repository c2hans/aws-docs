---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/subnet-silo-isolation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Subnet silo isolation
<a name="subnet-silo-isolation"></a>

 We started with accounts, then moved to VPC as our silo model. You can get even more granular with silo isolation by placing tenants in separate VPC subnets. With this approach, each tenant is placed in a separate subnet within a VPC. The diagram in Figure 8 provides an example of the subnet per tenant model.

![Diagram showing subnet silo isolation.](http://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/subnet-silo-isolation.png)

 Here you’ll see the same Multi-AZ VPC that we had with VPC isolation. However, now you’ll notice that the tenants are actually all within the subnets of a single VPC. The isolation of tenants in this model relies on network routing constructs to prevent any cross-tenant access.

 While this is a valid approach, it is not recommended as a preferred model. The scaling and management of this becomes unwieldy relatively quickly. If you have a small population of tenants, this may work out fine. Beyond that, we’d recommend using one of the other silo isolation models described here.

## Targeted silo isolation
<a name="targeted-silo-isolation"></a>

 As we mentioned above, silo isolation can also be applied in a much more granular fashion where selective elements of your SaaS solution are deployed in a silo model. Each microservice of your system and each resource those services touch has the option of being configured in a silo model of isolation. How that silo isolation is realized will vary across each service or construct that makes up your application. Let’s look at some sample microservice to better understand how these different dimensions of silo isolation might land in an actual application. The diagram in Figure 9 provides a view of these two models.

![Diagram showing microservice silo isolation.](http://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/microservice-silo-isolation.jpg)

In this diagram, you’ll see a system that has implemented three different microservices: product, order, and account. The deployment and storage models of each of these microservices highlights how isolation (for security or noisy neighbor) could land in a SaaS environment.

 Let’s review the isolation model for each of these services. The *product* microservice at the top right was deployed in a complete pooled model where both the compute and the storage are shared for all tenants. The table here reflects the fact that tenants all land here as separate items that are indexed in the same table. The assumption here is that we’ll be isolating this data with policies that can restrict access to tenant items in this table. The *order* microservice to the right of this item is only for tenants 1 through 3. This microservice is also implemented in a pooled model. The only difference here is that it is supporting a subset of tenants. Essentially, any tenant doesn’t get a dedicated (silo) deployment of the *order* microservice would be running in this pooled deployment (think of it as tenants 1..N with the exception of the few that get pulled out as silo microservices).

 For the purposes of this discussion, let’s focus on the siloed services which are represented by the dedicated *order* microservices (top right) and the *account* microservice (bottom). You’ll notice here that we’ve deployed standalone instances of the *order* microservice for tenants 4 and 5. The idea here is that these tenants had some requirements for the order processing (compliance, noisy neighbor, and etc.) that required this service to be deployed in a silo model. Here the compute and storage are both dedicated entirely to each of these tenants.

 Finally, at the bottom is the *account* microservice. It represents a silo model but only at the storage level. The compute of the microservice is shared by all tenants but each tenant has a dedicated *database* that holds its account data. In this scenario, the isolation concern was focused exclusively on separating the data. The compute was still enabled to be shared.

 In looking at this model, you can see how the silo discussion becomes much more granular. Security, noisy neighbor, and a variety of factors will determine how and when you might adopt a silo isolation model for your services. They key takeaway here is that silo is not an all-or-nothing decision. You can think about applying silo to specific *components* of your application and only absorb the challenges of silo where it’s actually needed. A potential customer, for example, may be demanding silo. However, after more a detailed discussion, you find out that there are a few specific areas of storage and processing that concern them. This enables you to get the efficiencies of the pool model for those parts of the system that do not require silo isolation. It also gives you the freedom to offer this as a tier to different tenants, supporting a mix of both silo and pool for individual services.
