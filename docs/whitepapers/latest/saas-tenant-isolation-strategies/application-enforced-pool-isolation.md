---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/application-enforced-pool-isolation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Application-enforced pool isolation
<a name="application-enforced-pool-isolation"></a>

 Most of our attention so far has been on strategies for using IAM as the foundation our pooled isolation model. And, while IAM often represents a great fit for isolating resources, there can also be scenarios where IAM may not support the flavor of isolation that your application requires. This is where you may have to fall back and look at introducing other frameworks or tools to control access to your application’s pooled resources.

 Application-enforced isolation typically includes some model where you express policies (much like you do with IAM). These same frameworks often include policy enforcement mechanisms that will sit between you and your resources, authorizing your access to the resources. The diagram in Figure 19 provides a high-level conceptual view of the moving parts that might be part of an application-enforced policy model.

![Diagram showing application-enforced pool isolation.](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/application-enforced-pool-isolation.jpg)

 In this example, your tenant would authenticate against an identity provider and introduce some construct that will identify the policies that were defined for this specific user (this could also happen in a downstream process). The key here is that the policies would then be connected to your user’s identity, enabling downstream operations apply these policies in the context of a given user. Once you’ve authenticated, your identity would flow through the services of your system. Here there would need to be a library or process that would sit between your code and the resource you’re attempting to access, applying the policies that were bound to you as a user.

**Note**
This approach is only meant to represent a conceptual model. The strategies that are employed by each framework might take a different approach to expressing and applying their policies.

 It’s worth noting that the boundaries of policy-based isolation and role-based access control (RBAC) often get blurred as part of this discussion. The tooling here, in fact, often contributes to this confusion. As a generality, though, we wouldn’t want to equate RBAC to tenant isolation. In many cases, RBAC has a functional mapping where user roles (defined by an application) are used to control access to a system’s functionality. That scope is different than drawing boundaries of isolation between the tenants of your system, which is less about a functional goal and more about preventing one tenant from accessing another tenant’s data.
