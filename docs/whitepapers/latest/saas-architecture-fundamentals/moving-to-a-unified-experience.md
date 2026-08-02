---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/moving-to-a-unified-experience.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Moving to a unified experience
<a name="moving-to-a-unified-experience"></a>

 To address the needs of this classic software dilemma, organizations turn to a model that allows them to create a single, unified experience that allows customers to be managed and operated collectively.

 The following diagram provides a conceptual view of an environment where all of the customers are managed, onboarded, billed, and operated through a shared model.

![A diagram showing a conceptual view of an environment where all of the customers are managed, onboarded, billed, and operated through a shared model.](http://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/images/unified-environment.png)

 At first glance, this may not seem all that different than the prior model. However, as we dig in a bit further, you’ll see that there are fundamental, significant differences in these two approaches.

 First, you’ll notice that the customer environments have been renamed to tenants. This notion of a *tenant* is foundational to SaaS. The basic idea is that you have a single SaaS environment, and each one of your customers is viewed as a tenant of that environment, consuming the resources they need. A tenant could be a company with many users, or it could correlate directly to an individual user.

 To better understand the idea of a tenant, consider the idea of apartment or commercial buildings. The space in each of these building is rented out to individual tenants. The tenants rely on some of the shared resources of the building (water, power, and so on), paying for what they consume.

 SaaS tenants follow a similar pattern. You have the infrastructure of your SaaS environment, and tenants that consume the infrastructure of that environment. The amount of resources consumed by each tenant can vary. These tenants are also managed, billed, and operated collectively.

 If you turn back to the diagram, you’ll see the notion of tenancy brought to life. Here, tenants no longer have their own environment. Instead, all the tenants are housed and managed within the walls of one collective SaaS environment.

 The diagram also includes a range of shared services that surround your SaaS environment. These services are global to all of the tenants of your SaaS environment. This means that onboarding and identity, for example, are shared by all tenants of this environment. The same is true for management, operations, deployment, billing, and metrics.

 This idea of a unified set of services that are applied universally to all of your tenants is foundational to SaaS. By sharing these concepts, you’re able to address a number of the challenges that were associated with the classic model described above.

 Another key, somewhat subtle element of this diagram is that all of the tenants in this environment are running the same version of your application. Gone is the idea of having separate, one-off versions running for each customer. Having all tenants running the same version represents one of the fundamental distinguishing attributes of a SaaS environment.

 By having all customers running the same version of your product, you no longer face many of the challenges of a classic installed software model. In the unified model, new features can be deployed to all tenants by a single, shared process.

 This approach gives you the ability to employ a single pane of operational glass that can manage and operate all tenants. This lets you manage and monitor your tenants through a common operational experience, allowing new tenants to be added without adding incremental operational overhead. This is a core part of the SaaS value proposition that gives teams the ability to reduce operational expenses, and improve overall organizational agility.

 Imagine what it would mean to add 100 or 1,000 new customers in this model. Instead of worrying about how these new customers might erode margins and add complexity, you can view this growth as the opportunity it represents.

 Generally, the focus of SaaS is placed on how the application in the middle of this model is implemented. Businesses want to focus on how data is stored, how resources are shared, and so on. However, the reality is that, while these details are definitely important, there are many ways your application can be built and still present itself as a SaaS solution to your customers.

 What’s critical is the broader goal of having a single, unified experience that surrounds your tenant environments. Having this shared experience is what allows you to drive the growth, agility, and operational efficiency that is connected to the overall objectives of a SaaS business.
