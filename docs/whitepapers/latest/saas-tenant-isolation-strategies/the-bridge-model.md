---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/the-bridge-model.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# The bridge model
<a name="the-bridge-model"></a>

 While silo and pool have very distinct approaches to isolation, the isolation landscape for many SaaS providers is less absolute. As you look at real application problems and you decompose our systems into smaller services, you will often discover that your solution will require a mix of the silo and pool models. This mixed model is what we would refer to as a bridge model of isolation. The diagram in Figure 3 provides an example of how the bridge might be realized in a SaaS solution.

![Diagram showing the bridge isolation model with three tenants.](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/bridge-isolation.jpg)

 This diagram highlights how the bridge model enables you to combine of the silo and pool models. Here we have a monolithic architecture with classic web and application tiers. The web tier, for this solution, is deployed in a pool model that is shared by all tenants. While the web tier is shared, the underlying business logic and storage of our application are actually deployed in a silo model where each tenant has its own application tier and storage.

 Now, imagine we were to break this monolith into microservices. You can imagine that each of the various microservices in our system could leverage combinations of the silo and pool models. We’ll dig into that more as we get into the specifics of applying silo and pool with different AWS constructs. The key takeaway here is that your view of silo and pool will be much more granular for environments that are decomposed into a collection of services that have varying isolation requirements.

## Bridge model pros and cons
<a name="bridge-model-pros-and-cons"></a>

 The bridge model is more a hybrid model that focuses on enabling you to apply the silo or pool model where it makes sense. The idea here is that the values and tenets of silo isolation still apply to each of these areas of the system. As you think about pros and cons of the bridge model, then, you should be thinking about the tradeoffs of silo and pool models for each resource or layer of your architecture.
