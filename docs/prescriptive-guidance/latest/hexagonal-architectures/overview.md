---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/overview.html
---

# Overview
<a name="overview"></a>

## Domain-driven design (DDD)
<a name="ddd"></a>

In [domain-driven design (DDD)](https://www.oreilly.com/library/view/implementing-domain-driven-design/9780133039900/), a domain is the core of the software system. The domain model is defined first, before you develop any other module, and it doesn't depend on other low-level modules. Instead, modules such as databases, the presentation layer, and external APIs all depend on the domain.   In DDD, architects decompose the solution into bounded contexts by using business logic-based decomposition instead of technical decomposition. The benefits of this approach are discussed in the *Targeted business outcomes *section.   DDD is easier to implement when teams use hexagonal architecture. In hexagonal architecture, the application core is the center of the application. It is decoupled from other modules through ports and adapters, and has no dependencies on other modules. This aligns perfectly with DDD, where a domain is the core of the application that solves a business problem. This guide proposes an approach where you model the core of the hexagonal architecture as the domain model of a bounded context. The next section describes hexagonal architecture in more detail.   This guide doesn't cover all aspects of DDD, which is a very broad topic. To gain a better understanding, you can review the DDD resources listed on the [Domain Language](https://www.domainlanguage.com/ddd/) website.

## Hexagonal architecture
<a name="hexagonal"></a>

Hexagonal architecture, also known as *ports and adapters* or *onion architecture*, is a principle of managing dependency inversion in software projects. Hexagonal architecture promotes a strong focus on the core domain business logic when developing software, and treats external integration points as secondary. Hexagonal architecture helps software engineers adopt good practices such as test-driven development (TDD), which, in turn, promotes [architecture evolution](https://dzone.com/articles/pattern-of-the-month-red-green-refactor), and helps you manage complex domains in the long term.   Let's compare hexagonal architecture to classical layered architecture, which is the most popular choice for modeling structured software projects. There are subtle but powerful differences between the two approaches.

In layered architecture, software projects are structured in tiers, which represent broad concerns such as business logic or presentation logic. This architecture uses a dependency hierarchy, where the top layers have dependencies on the layers below them, but not the other way around. In the following diagram, the presentation layer is responsible for user interactions, so it includes the user interface, APIs, command line interfaces, and similar components. The presentation layer has a dependency on the business layer, which implements domain logic. The business layer, in turn, has dependencies on the data access layer and on multiple external services.

![Classical layered architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/images/guide-img/b67c0cd8-adc6-4a04-a6b7-ed44f0888b3f/images/c4e2e441-5040-4eef-8f79-08679e26afd1.png)

The main disadvantage of this configuration is the dependency structure. For example, if the model for storing data in the database changes, this affects the data access interface. Any change to the data model also affects the business layer, which has a dependency on the data access interface. As a result, software engineers cannot make any infrastructure changes without affecting the domain logic. This, in turn, increases the likelihood of regression bugs.

Hexagonal architecture defines dependency relationships in a different way, as illustrated in the following diagram. It concentrates decision making around domain business logic, which defines all the interfaces. External components interact with the business logic through interfaces called *ports*. Ports are abstractions that define the interactions of the domain with the external world. Each infrastructure component must implement those ports, so changes in those components no longer affect the core domain logic.

![Hexagonal architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/images/guide-img/b67c0cd8-adc6-4a04-a6b7-ed44f0888b3f/images/a7fde5a7-2ea1-41aa-af5c-4040e31f2a4d.png)

The surrounding components are called *adapters*. An adapter is a proxy between the external world and the internal world, and implements a port defined in the domain. Adapters can be categorized in two groups: primary and secondary. Primary adapters are the entry points to the software component. They allow external actors, users, and services to interact with the core logic. AWS Lambda is a good example of a primary adapter. It integrates with multiple AWS services that can invoke the Lambda functions as entry points. Secondary adapters are external service library wrappers that handle communications with the external world. A good example of a secondary adapter is an Amazon DynamoDB client for data access.

## Targeted business outcomes
<a name="business-outcomes"></a>

The hexagonal architecture discussed in this guide helps you achieve the following objectives:
+ [Reduce time to market by improving the development cycle](improve-dev-cycle.md)
+ [Improve software quality](improve-software-quality.md)
+ [Adapt more easily to change](adapt-to-change.md)

These processes are discussed in detail in the following sections.
