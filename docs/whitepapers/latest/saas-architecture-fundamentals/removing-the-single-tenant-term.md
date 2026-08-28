---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/removing-the-single-tenant-term.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Removing the single-tenant term
<a name="removing-the-single-tenant-term"></a>

 As part of using the term *multi-tenant*, it’s only natural for people to want to use the term *single-tenant* to describe SaaS environments. However, given the backdrop outlined previously, the term *single-tenant* creates confusion.

 Is the preceding diagram a single-tenant environment? While each tenant technically has its own stack, these tenants are still being operated and managed in a multi-tenant model. This is why the term *single-tenant* is generally avoided. Instead, all environments are characterized as multi-tenant, as they are just implementing some variation of tenancy where some or all of the resources are shared or dedicated.

## Introducing silo and pool
<a name="introducing-silo-and-pool"></a>

 With all these variations of models and given the challenges around the term *multi-tenancy*, we have introduced some terminology that lets us more accurately capture and describe the different models that are used when building a SaaS.

 Two terms that we use to characterize the use of resources in a SaaS environment are *silo* and *pool*. These terms allow us to label the nature of SaaS environments, using *multi-tenant* as an over-arching description that can be applied to any number of underlying models.

 At the most basic level, the term *silo* is meant to describe scenarios where a resource is dedicated to a given tenant. Conversely, the *pool* model is used to describe scenarios where a resource is shared by tenants.

 As we look at how the silo and pool terms are used, it’s important to be clear that silo and pool are not all-or-nothing concepts. Silo and pool could apply to an entire tenant’s stack of resources, or it could be applied selectively to parts of your overall SaaS environment. So, if we say some resource is using a *silo* model, that does not mean all resources in that environment are siloed. The same holds true for how we would use the term *pooled*.

 The following diagram provides an example of how siloed and pooled models are used more granularly in a SaaS environment:

![A diagram depicting silo and pool models .](http://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/images/silo-and-pool-models.png)

 This diagram includes a series of samples that are meant to illustrate the more targeted nature of the silo and pool models. If you follow this from left to right, you’ll see that we start out with an order microservice. This microservice has siloed compute and pooled storage. It interacts with a product service that has pooled compute and pooled storage.

 The product service then interacts with an invoice microservice that has pooled compute and siloed storage. This service sends messages via queues to the shipping service. The queues are deployed in a siloed model.

 Finally, the shipping microservice acquires messages from the siloed queues. It uses pooled compute and storage.

 While this may seem a bit convoluted, the goal is to highlight the granular nature of the silo and pool concepts. As you look to design and build your SaaS solution, it’s expected that you would make these silo and pool decisions based on the needs of your domain and your customers.

 Noisy neighbor, isolation, tiering, and a host of other reasons might influence how and when you choose to apply the silo or pooled model.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
