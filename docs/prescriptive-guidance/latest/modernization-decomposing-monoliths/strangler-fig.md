---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/strangler-fig.html
---

# Strangler fig pattern
<a name="strangler-fig"></a>

The design patterns discussed so far in this guide apply to decomposing applications for greenfield projects. What about brownfield projects that involve big, monolithic applications? Applying the previous design patterns to them will be difficult, because breaking them into smaller pieces while they're being used actively is a big task.

The [strangler fig pattern](https://martinfowler.com/bliki/StranglerFigApplication.html) is a popular design pattern that was introduced by Martin Fowler, who was inspired by a certain type of fig that seeds itself in the upper branches of trees. The existing tree initially becomes a support structure for the new fig. The fig then sends its roots to the ground, gradually enveloping the original tree and leaving only the new, self-supporting fig in its place.

This pattern is commonly used to incrementally transform a monolithic application into microservices by replacing a particular functionality with a new service. The goal is for the legacy and new, modernized versions to coexist. The new system is initially supported by, and wraps, the existing system. This support gives the new system time to grow and to potentially replace the old system entirely.

The process to transition from a monolithic application to microservices by implementing the strangler fig pattern consists of three steps: transform, coexist, and eliminate:
+ *Transform* ‒ Identify and create modernized components either by porting or rewriting them in parallel with the legacy application.
+ *Coexist* ‒ Keep the monolith application for rollback. Intercept outside system calls by incorporating an HTTP proxy (for example, [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)) at the perimeter of your monolith and redirect the traffic to the modernized version. This helps you implement functionality incrementally.
+ *Eliminate* ‒ Retire the old functionality from the monolith as traffic is redirected away from the legacy monolith to the modernized service.

The following table explains the advantages and disadvantages of using the strangler fig pattern.

|
|
| Advantages | Disadvantages |
| --- |--- |
| + Allows for graceful migration from a service to one or more replacement services.<br />+ Keeps old services in play while refactoring to updated versions.<br />+ Provides the ability to add new services and functionalities while refactoring older services.<br />+ The pattern can be used for versioning of APIs.<br />+ The pattern can be used for legacy interactions for solutions that aren't or won't be upgraded. | + Isn't suitable for small systems where the complexity is low and the size is small.<br />+ Cannot be used in systems where requests to the backend system cannot be intercepted and routed.<br />+ The proxy or facade layer can become a single point of failure or a performance bottleneck if it isn't designed properly.<br />+ Requires a rollback plan for each refactored service to revert to the old way of doing things quickly and safely if things go wrong. |

The following illustration shows how a monolith can be split into microservices by applying the strangler fig pattern to an application architecture. Both systems function in parallel, but you'll start moving functionality outside the monolith code base and enhance it with new capabilities. These new capabilities give you the opportunity to architect microservices in a way that best suits your needs. You'll continue stripping out capabilities from the monolith until it's all replaced by microservices. At that point, you can eliminate the monolith application. The key point to note here is that both the monolith and the microservices will live together for a period of time.

![Strangler fig pattern](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/images/guide-img/8e9fa68d-7532-4c4b-8c7b-74bc6afdb7b9/images/d8fe6ffa-117b-453f-9d4e-b59ef5ddf4f4.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
