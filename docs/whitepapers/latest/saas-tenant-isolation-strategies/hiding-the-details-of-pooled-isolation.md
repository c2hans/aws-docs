---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/hiding-the-details-of-pooled-isolation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hiding the details of pooled isolation
<a name="hiding-the-details-of-pooled-isolation"></a>

 As we mentioned previously, one key aspect of the pool model is that it relies on developers to conform to the overall model. Developers must, as a matter of convention, acquire the scoped context before accessing resources. Given the importance of compliance with this model, you’ll often see companies creating mechanisms that simplify a developer’s ability to align with the isolation policies adopted as part of a SaaS offering.

 The general approach here fits very much with common design best practices. This usually translates into the creation libraries, modules, or lightweight frameworks that are shared by teams. The goal here is to move the mechanics of acquiring a scoped context into shared constructs that can be leveraged across your team. This diagram in Figure 20 provides a conceptual view of this notion of hiding away the details of isolation.

![Diagram showing using libraries for isolation standardization.](http://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/using-libraries-for-isolation-standardization.jpg)

 Here you’ll see that we have two microservices (product and order) that need to acquire credential to comply with the pooled isolation model of our system. What we’ve done here is moved all of the code and details of this process to shared libraries (these are not separate microservices). When our microservice needs scoped credentials, it will call into the isolation manager, passing in a JWT token that that was supplied to the microservices. This isolation manager will then get the tenantId from the token manager, which owns all the logic associated with cracking open the JWT and extracting tenant information. It will then get the policy for this tenant from the policy manager and use that policy to get a set of tenant-scoped credentials. These credentials would then be returned to the calling service.

 There’s nothing especially unique about this approach. This is simply applying the basic strategy of ensuring that reusable constructs are extracted so they can be versioned and shared more universally by your team. The key concept here is that you should attempt to push as much of the details of tenant isolation away from the view of your developers, making as simple as possible for them to apply your isolation scheme.

 How you choose to implement this could also be influenced by the stack or compute construct that your application uses. With Lambda, for example, it may make sense to move these libraries to Lambda Layers where these horizontal concepts are versioned separately and universally referenced by you Lambda functions.

 You may also look to introduce mechanisms that will take this completely outside of the view of your developers, intercepting and acquiring these scoped credentials before you get into the implementation of your microservices. With some languages, for example, you could use aspects to intercept incoming requests, acquire the scoped credentials, and inject them into the microservice. With Lambda functions, there are various open source *wrapper* libraries that could be used to inject scoped credentials into a Lambda functions. For some, these strategies may provide a stricter model for enforcing isolation
