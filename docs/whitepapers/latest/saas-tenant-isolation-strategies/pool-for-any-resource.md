---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/pool-for-any-resource.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Pool for any resource
<a name="pool-for-any-resource"></a>

 Our coverage of pool here highlights the fundamental moving parts of implementing a pooled strategy. However, it does not touch on how pool might land in every AWS service. That is beyond the scope of this paper. That being said, the concepts and tradeoffs of pool isolation tend to be similar for most resources. As you look at the range of additional AWS services, you’ll find yourself balancing the available isolation mechanisms with the efficiency of having a resource that is shared by tenants. In an ideal scenario, you could use a pooled model for every resource and still achieve all of your isolation goals. The reality is, though, you’ll find scenarios where the isolation model for some resources will be challenging. In these cases, this may push you toward a silo model. That, or you’ll absorb the effort to use some flavor of application-enforced isolation to realize your isolation goals.
