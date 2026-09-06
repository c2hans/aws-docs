---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/silo-for-any-resource.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Silo for any resource
<a name="silo-for-any-resource"></a>

 While we’ve focused in on a few key silo models here, it should be clear by now that any resource in your SaaS architecture can typically be deployed in a silo model. However, it should also be clear that the strategies and mechanisms for isolating each AWS service will often vary. Isolating Amazon DynamoDB data, for example, might mean creating separate tables for each tenant. Isolating in other storage models, might require you to create a separate cluster for each tenant. Even Amazon Simple Queue Service (Amazon SQS) and Amazon EventBridge have different approaches to how you might achieve isolation. While it’s beyond the scope of this paper to cover isolation strategies for each of these services, it’s important for SaaS developers to consider how and where it may be appropriate to silo any one of these services.

 The general rule of thumb here is to look at any resource and assess the noisy neighbor and security profile for that resource. You’ll have to weigh these isolation options against the added complexities, cost, operational burden, and service limits that may come with adopting a silo strategy for some part of your system. Finding the right balance is often key to the success of your system.
