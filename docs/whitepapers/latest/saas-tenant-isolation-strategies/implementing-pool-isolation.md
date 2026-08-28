---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/implementing-pool-isolation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implementing pool isolation
<a name="implementing-pool-isolation"></a>

 The pool model is often the most appealing to SaaS providers. The efficiency, agility, and cost profile of pool is frequently what motivates providers to deliver in this model. Of course, as we move resources into a shared model, we have a much more challenging isolation story to tell. There is often a fundamental mismatch between the tools and mechanisms that provide isolation and the nature of tenants consuming a shared resource. This is further complicated by the fact that each resource we need to isolate in the pool model may require a different approach to enforcing isolation. While these challenges are real, they should *not* represent an opportunity to somehow relax your isolation requirements. This just means you’ll have to work a bit harder to find the right combination of tools and construct to isolate some resources in a pooled model.

 Before we dig into some specific pool isolation techniques, let’s get a clear picture of how the pool model changes our approach to isolation. Generally, when we talk about isolating AWS resources, we focus on how AWS Identity and Access Management (IAM) can be used to control the interactions between resources. For a silo model, in fact, IAM represents a perfectly good model for expressing your tenant isolation policies. With the pool model, though, using these IAM constructs can be a bit more involved. The diagram in Figure 12 provides illustration of how silo and pool require separate isolation mindsets.

![Diagram showing IAM and scoping access.](http://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/iam-and-scoping-access.jpg)

Here’s you’ll see two different ways of apply IAM policies to scope access of compute constructs. On the left we have two siloed deployments where tenants are running in their own infrastructure. These tenants are both accessing some other resource (in this case storage). When these instances were deployed, they were configured with separate IAM instance profiles for each tenant (tenant 1 and tenant 2). Since this binding was created at deployment time, we can be sure that these instances will be prevented from accessing the resources of another tenant.

 On the right you’ll see an example where we’ve deployed compute nodes in a pooled model. The compute that is running here will be running on behalf of all tenants. This reality directly impacts how we can scope the IAM profile for the compute that is deployed here. Instead of constraining the compute to a specific tenant, we must deploy these compute nodes with a profile that is open enough to support all tenants. This wider scope is where we run into the real challenges of the pool model. Now, we’ll need to come up with new ways to implement the scoping of access that is enforced by your SaaS solution.

 Given this unique aspect of pool isolation, you’ll find that the options for implementing pool isolation will vary significantly. While it’s beyond the scope of this paper to explore all the permutations of pool isolation, we can examine some common patterns to get a better feel for the different strategies that are often applied. The sections that follow will provide an overview of these strategies.

**Topics**
+ [Run-time, policy-based isolation with IAM](run-time-policy-based-isolation-with-iam.md)
+ [Scaling and managing pool isolation policies](scaling-and-managing-pool-isolation-policies.md)
+ [Pooled storage isolation strategies](pooled-storage-isolation-strategies.md)
+ [Application-enforced pool isolation](application-enforced-pool-isolation.md)
+ [Pool for any resource](pool-for-any-resource.md)
+ [Hiding the details of pooled isolation](hiding-the-details-of-pooled-isolation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
