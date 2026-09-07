---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/full-stack-isolation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Full stack isolation
<a name="full-stack-isolation"></a>

 The first model we’ll look at is full stack silo isolation. In this scenario, where a SaaS ISV requires all the resources of a tenant to be fully isolated, you will rely on more coarse-grained AWS constructs to isolate your tenants. The choices you make here will likely be largely influenced by the management, operations, and scaling profile of your environment. The following is a breakdown of the common full stack silo isolation mechanisms.

## Account silo isolation
<a name="account-silo-isolation"></a>

 The AWS account represents one strategy that can be used to isolate tenants in a silo model. The basic approach here is to deploy each tenant into an entirely separate account, linking each tenant account to a parent. All of the moving parts of each tenant stack are deployed with the stack and are operated in complete isolation. This account boundary of isolation is often appealing to those that are running in environments that demand a very easily described boundary each tenant. For a SaaS provider, the account isolation model can provide a compelling story to customers that are especially concerned about any possibility of cross-tenant access.

 Let’s take a closer look at a sample architecture that uses the account-based pool isolation model. The diagram in Figure 6 illustrates two tenants deployed into two separate accounts.

![Diagram showing account-based silos and isolation](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/account-based-silo-isolation.jpg)

 The architecture shown here is just an example. The actual infrastructure that lands in your account would vary based on the technologies that were part of your SaaS application’s technology stack. This could use containers, be serverless, or any mix of the various AWS architecture models. The key point here is that every tenant is running the same stack in each of these separate accounts.

 While there are merits to this model, it presents real challenges when it comes to scale and automation. There’s a rich collection of tools that can automate this experience. However, there are constraints on this automation. They key challenge here is often account limits. Some limits can be configured through automation. Others cannot. This issue becomes more complicated if you want to manage and maintain separate limits for each account.

## Virtual Private Cloud (VPC) silo isolation
<a name="virtual-private-cloud-vpc-silo-isolation"></a>

 The next level of isolation to consider is within a single account. This brings us into the realm of networking constructs where we essentially use the boundaries of the network for each of our siloed tenant environments. The Amazon Virtual Private Cloud (Amazon VPC) provides a natural mechanism for network-based isolation. The diagram shown in Figure 7 provides a sample of a VPC silo model:

![Diagram showing VPC silo isolation.](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/vpc-silo-isolation.png)

Here you’ll notice that we have two separate tenant environments, each hosted in its own VPC. The VPCs represented here using multiple availability zones to convey the typical AWS architecture best practices. As with accounts, the resources configured in each VPC could vary significantly for each SaaS provider. The key aspect of this solution is that the tenants are isolated from one another via the networking constructs that are enforced by the VPC.

 The VPC provides a compelling model for those that require siloed isolation. This gets us beyond some of the provisioning challenges of account-based isolation since the limits are owned by the account where these VPCs reside. While this gives creates a more centralized model for managing limits across all tenants, it does not eliminate limits challenges. With the VPC model, you would still need to proactively monitor limits and periodically increase them as needed. There are scenarios where a large number of tenants could exceed the hard limits for your environment. This model does have the upside of enabling you to place tags on your VPC and its resources to calculate tenant costs.

 While this model has advantages over account-based isolation, you’ll still want to think about scale. As the number of VPCs grows, the management and agility of this approach (and all silo models) decreases. Overall, though, the VPC tends to offer the best combination of options for companies that need to rely on a silo model.
