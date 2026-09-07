---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/isolation-transparency.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Isolation transparency
<a name="isolation-transparency"></a>

 We’ve talked about isolation mostly based on how it is realized within the design and architecture of your application. However, it’s important to also think about isolation from the perspective of the tenants of your system. Even though SaaS developers and architects are constantly weighing their isolation options, it’s still important to present tenants with a clear and consistent story around isolation that takes them away from the underlying details of your isolation strategy. The diagram in Figure 21 provides a conceptual view isolation that we want to present to customers.

![Diagram showing how to make isolation transparent.](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/making-isolation-transparent.png)

Here you’ll notice that we have two tenants that have resources. Some of the resources are deployed in a silo model (on the left and right). Other resources for these tenants are deployed in a pool model (in the overlapping portion of these two circles). The idea here is that, despite the fact that there is a mix of silo and pool here, your system offers a comprehensive approach to isolation that prevents any cross-tenant access. To your customer, they just need assurance that this isolation is in place. Ideally, they won’t need to know which resources are pooled and which are siloed.
