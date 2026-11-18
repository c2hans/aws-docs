---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/micro-frontend-alternatives.html
---

# Comparing micro-frontends with alternative architectures
<a name="micro-frontend-alternatives"></a>

As with all architectural strategies, base your decision to adopt micro-frontends on evaluation criteria that your organization's principles guide. Micro-frontends have advantages and disadvantages. If your organization decides to use micro-frontends, you must have strategies in place to address the challenges of distributed systems.

When choosing an application architecture, common alternatives to micro-frontends are monoliths, n-tier applications, and microservices in combination with a single-page application (SPA) frontend. These are all valid approaches, and each of them has advantages and disadvantages.

## Monoliths
<a name="monoliths"></a>

You can deliver a small application that doesn't need frequent changes quickly as a monolith. Even in situations where you expect significant growth, a monolith is a natural first step. Later, you can either retire the monolith or refactor it into a more flexible structure. By starting with a monolith, your organization can go to market, get customer feedback, and improve the product faster.

However, monolithic applications tend to degrade if teams don't carefully maintain them or as the codebase grows over time. When multiple teams contribute to the same codebase, not all of them contribute to its maintenance and operations. This results in an imbalance of responsibilities, which affects velocity and causes inefficiencies. At the same time, inadvertent coupling between a monolith's modules leads to unintended side effects as the codebase evolves. Those side effects can result in malfunctions and outages.

## N-tier applications
<a name="n-tier-applications"></a>

You can build a more complex application that has a relatively static pace of evolution as a three-tier architecture (presentation, application, data), with a REST or GraphQL layer between the frontend and backend. This approach is more flexible, and teams for the different tiers can develop independently to some extent. However, an n-tier application makes it more difficult to deploy functionality. An API contract decouples the frontend and backend, so you must deploy breaking changes together or version the API.

Consider the following common scenario. If releasing a new feature requires a data schema change, product owners might take days to agree with a frontend team on a set of functionalities. Then the frontend team asks the backend team to develop and release the functionality in the backend. The backend team works with the data owners to release a database schema update. Next, the backend team releases a new version of the API so that the frontend team can develop and release their changes. In this scenario, propagating all changes to production might take weeks or even months, because each team has its own backlog, priorities, and processes for developing, testing, and releasing changes.

## Microservices
<a name="microservices"></a>

A microservices architecture decomposes the backend into small services, each addressing a particular business concern within a bounded context. Each microservice also remains strongly decoupled from other services because it exposes a clearly defined interface contract.

Well-crafted monoliths and n-tier architectures should also use bounded contexts and interface contracts. In a microservices architecture, however, services communicate over the network, usually through the HTTP protocol, and have dedicated runtime infrastructure. This design supports independent development, delivery, and operation of each backend service.

## Choosing the approach for your requirements
<a name="choosing"></a>

Monoliths and n-tier architectures bundle multiple domain concerns into one technical artifact. This makes aspects such as dependencies and internal data flow easy to manage, but it makes delivery of new functionalities more difficult. Because of the size of the code base, a team often invests time in refactoring and decoupling to maintain coherence.

Applications developed by a few teams might not need the additional complexity that comes with moving to micro-frontends. This is especially true if the teams are not paying the penalties of high coupling and long lead times to release changes.

In summary, more complex and distributed architectures are often the right choice for complex and fast-moving applications. For small to midsized applications, a distributed architecture is not necessarily superior to a monolithic one, especially if the application will not dramatically evolve over a short period of time.
