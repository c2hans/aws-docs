---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/micro-frontend-concepts.html
---

# Foundational concepts
<a name="micro-frontend-concepts"></a>

Micro-frontend architecture is heavily inspired by three prior architectural concepts:
+ *Domain-driven design* is the mental model to structure complex applications into coherent domains.
+ *Distributed systems* are an approach for building applications as loosely coupled subsystems that are developed independently and run on their own dedicated infrastructure.
+ *Cloud computing* is an approach for running IT infrastructure as services with a pay-as-you-go model.

## Domain-driven design
<a name="domain-driven-design"></a>

Domain-driven design (DDD) is a paradigm developed by Eric Evans. In his 2003 book [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/gp/product/0321125215/), Evans postulates that software development should be driven by business concerns rather than technical ones. Evans proposes that IT projects first develop a *ubiquitous language* that helps technical and domain experts to find a shared understanding. Based on that language, they can formulate a mutually understood model of the business reality.

Obvious as that approach might be, many software projects suffer from a disconnect between business and IT. Those disconnects often cause significant misunderstandings, which lead to budgets overruns, decreased quality, or project failure.

Evans introduces multiple other important terms, one of which is the *bounded context*. A bounded context is a self-contained segment of a large IT application containing the solution or implementation to exactly one business concern. A large application will consist of multiple bounded contexts that are loosely coupled through integration patterns. Those bounded contexts can even have their own dialects of the ubiquitous language. For example, a *user* in the payment context of an application might have different aspects from a *user* in the delivery context because the notion of shipping would be irrelevant during payment.

Evans doesn't define how small or large a bounded context should be. The size is determined by the software project, and it might evolve over time. Good indicators of a context's boundaries are the degree of cohesion between the entities (domain objects) and the business logic.

In the context of micro-frontends, domain-driven design can be illustrated by the example of a complex web page such as a flight-booking page.

![Example flight-search web application with inputs for departure and arrival and a list of results.](https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/7517eb91-5a2e-4257-baaf-dfd84223d942.png)

On this page, the main building blocks are a search form, a filters panel, and the results list. To identify the boundaries, you must identify independent functional contexts. In addition, consider nonfunctional aspects, such as reusability, performance, and security. The most important indicator that "things that belong together" is their communication patterns. If some elements in an architecture must communicate frequently and exchange complex information, they likely share the same bounded context.

Individual UI elements such as buttons are not bounded contexts, because they are not functionally independent. Also, the entire page is not a good fit for a bounded context, because it can be broken down into smaller independent contexts. A reasonable approach is to treat the search form as one bounded context and to treat the results list as the second bounded context. Each of these two bounded contexts can now be implemented as a separate micro-frontend.

## Distributed systems
<a name="distributed-systems"></a>

To ease maintenance and to support the ability to evolve, the majority of nontrivial IT solutions are modular. In this case, modular means that IT systems consist of identifiable building blocks that are decoupled through interfaces to achieve separation of concerns.

In addition to being modular, distributed systems should be independent systems in their own right. In a merely modular system, each module is ideally encapsulated and exposes its functions through interfaces, but it can't be independently deployed or even be functional on its own. Also, modules generally follow the same lifecycle as other modules that are part of the same system. The building blocks of a distributed system, on the other hand, each have their own lifecycles. Applying the domain-driven design paradigm, each building block addresses one business domain or subdomain and lives in its own bounded context.

When distributed systems interact during build time, a common approach is to develop mechanisms for identifying issues quickly. For example, you might adopt typed languages and invest heavily in unit testing. Multiple teams can collaborate on the development and maintenance of modules, often distributed as libraries for systems to consume with tools such as npm, Apache Maven, NuGet, and pip.

During runtime, interacting distributed systems are typically owned by individual teams. Consuming dependencies causes operational complexity because of error handling, performance balancing, and security. Investments in integration testing and observability are fundamental to reducing risks.

The most popular examples of distributed systems today are microservices. In microservice architectures, backend services are domain-driven (rather than driven by technical concerns such as UI or authentication) and owned by autonomous teams. Micro-frontends share the same principles, extending the solution scope to the frontend.

## Cloud computing
<a name="cloud-computing"></a>

Cloud computing is a way of purchasing IT infrastructure as services with a pay-as-you-go model instead of building your own data centers and buying hardware to operate them on premises. Cloud computing offers several advantages:
+ Your organization gains significant business agility by being able to experiment with new technologies without having to make large, long-term financial commitments upfront.
+ By using a cloud provider such as AWS, your organization can access a broad portfolio of low-maintenance and highly integrable services (such as API gateways, databases, container orchestration, and cloud capabilities). Access to these services frees up your staff to focus on work that differentiates your organization from the competition.
+ When your organization is ready to roll out a solution globally, you can deploy the solution to cloud infrastructure around the world.

Cloud computing supports micro-frontends by providing highly managed infrastructure. This makes end-to-end ownership easier for cross-functional teams. While the team should have strong operations knowledge, the manual tasks of infrastructure provisioning, operating system updates, and networking would be a distraction.

Because micro-frontends live in bounded contexts, teams can choose the most suitable service to run them. For example, teams can choose between cloud functions and containers for compute, and they can choose between different flavors of SQL and NoSQL databases or in-memory caches. Teams can even build their micro-frontends on a highly integrated toolkit such as [AWS Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html), which comes with preconfigured building blocks for serverless infrastructure.
