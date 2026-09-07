---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/branch-by-abstraction.html
---

# Branch by abstraction pattern
<a name="branch-by-abstraction"></a>

The strangler fig pattern works well when you can intercept the calls at the perimeter of the monolith. However, if you want to  modernize components that exist deeper in the legacy application stack and have upstream dependencies, we recommend the branch by abstraction pattern. This pattern enables you to make changes to the existing code base to allow the modernized version to safely coexist alongside the legacy version without causing disruption.

To use the branch by abstraction pattern successfully, follow this process:

1. Identify monolith components that have upstream dependencies.

1. Create an abstraction layer that represents the interactions between the code to be modernized and its clients.

1. When the abstraction is in place, change the existing clients to use the new abstraction.

1. Create a new implementation of the abstraction with the reworked functionality outside the monolith.

1. Switch the abstraction to the new implementation when ready.

1. When the new implementation provides all necessary functionality to users and the monolith is no longer in use, clean up the older implementation.

The branch by abstraction pattern is often confused with [feature toggles](https://martinfowler.com/bliki/FeatureToggle.html), which also allow you to make changes to your system incrementally. The difference is that feature toggles are intended to allow the development of new features and keep those features invisible to users when the system is running. Feature toggles are thus used at deploy time or runtime to choose whether a particular feature or set of features is visible in the application. Branch by abstraction is a development technique and can be combined with feature toggles to switch between the old and new implementation.

The following table explains the advantages and disadvantages of using the branch by abstraction pattern.

|
|
| Advantages | Disadvantages |
| --- |--- |
| + Allows for incremental changes that are reversible in case anything goes wrong (backward compatible).<br />+ Lets you extract functionality that's deep inside the monolith when you can't intercept the calls to it at the edge of the monolith.<br />+ Allows multiple implementations to coexist in the software system.<br />+ Provides an easy way to implement a fallback mechanism by using an intermediate verification step to call both new and old functionality.<br />+ Supports continuous delivery, because your code is working at all times throughout the restructuring phase. | + Isn't suitable if data consistency is involved.<br />+ Requires changes to the existing system.<br />+ Might add more overhead to the development process, especially if the code base is poorly structured. (In many cases, the upside is worth the extra effort, and the larger the restructuring, the more important it is to consider using the branch by abstraction pattern.) |

The following illustration shows the branch by abstraction pattern for a *Notification* component in the insurance monolith. It starts by creating an abstract or interface for notification functionality. In small increments, existing clients are changed to use the new abstraction. This may require searching the code base for calls to APIs related to the *Notification* component. You create the new implementation of notification functionality as a microservice outside your monolith and host it in the modernized architecture. Inside your monolith, your newly created abstraction interface acts as a broker and calls out the new implementation. In small increments, you port notification functionality to the new implementation, which stays inactive until it's fully tested and ready. When the new implementation is ready, you switch your abstraction over to use it. You would want to use a switching mechanism that can be flipped easily (such as a feature toggle) so you can switch back to the old functionality easily if you encounter any problems. When the new implementation starts to provide all notification functionality to your users and the monolith is no longer in use, you can clean up the older implementation and remove any switching feature flag that you might have implemented.

![Branch by abstraction pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/images/guide-img/8e9fa68d-7532-4c4b-8c7b-74bc6afdb7b9/images/1ea411d1-a973-4ae9-b5d8-cce606a7906b.png)
