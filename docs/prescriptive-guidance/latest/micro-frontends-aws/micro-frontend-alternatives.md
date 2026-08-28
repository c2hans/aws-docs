---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/micro-frontend-alternatives.html
---

# Comparing micro-frontends with alternative architectures
<a name="micro-frontend-alternatives"></a>

As with all architectural strategies, the decision to adopt micro-frontends must be based on evaluation criteria that are guided by your organization's principles. Micro-frontends have advantages and disadvantages. If your organization decides to use micro-frontends, you must have strategies in place to address the challenges of distributed systems

When choosing an application architecture, the most popular alternatives to micro-frontends are monoliths, n-tier applications, and microservices in combination with a single-page application (SPA) frontend. These are all valid approaches, and each of them has advantages and disadvantages.

## Monoliths
<a name="monoliths"></a>

A small application that doesn't need frequent changes can be delivered very quickly as a monolith. Even in situations where significant growth is expected, a monolith is a natural first step. Later, the monolith can be either retired or refactored into a more flexible structure. By starting with a monolith, your organization can go to market, get customer feedback, and improve the product faster.

However, monolithic applications tend to degrade if not carefully maintained or as the codebase grows in size over time. When multiple teams significantly contribute to the same codebase, they rarely all contribute to its maintenance and operations. This results in an imbalance of responsibilities, which impacts velocity and causes inefficiencies. At the same time, inadvertent coupling between a monolith's modules leads to unintended side effects as the code base evolves. Those side effects can result in malfunctions and outages.

## N-tier applications
<a name="n-tier-applications"></a>

A more complex application that has a relatively static pace of evolution can be built as a three-tier architecture (presentation, application, data), with a REST or GraphQL layer between the frontend and backend. This is much more flexible, and teams for the different tiers can develop independently to some extent. The disadvantage of an n-tier application is that it's much more difficult to deploy functionality. The frontend and backend are decoupled through an API contract, so breaking changes must be deployed together or the API must be versioned.

Consider the following common scenario: If releasing a new feature requires a data schema change, it might take days for product owners to agree on a set of functionalities with a frontend team. Then the frontend team will ask the backend team to develop and release the functionality on their side. The backend team will work with the data owners to release a database schema update. Next, the backend team will release a new version of the API, so that the frontend team can develop and release their changes. In this scenario, propagating all changes to production might take weeks or even months, because each team has its own backlog, priorities, and mechanisms around developing, testing, and releasing changes.

## Microservices
<a name="microservices"></a>

In a microservices architecture, the backend is decomposed into small services, each addressing a particular business concern within a bounded context. Each microservice is also strongly decoupled from other services by exposing a clearly defined interface contract.

It's worth mentioning that bounded contexts and interface contracts should also exist in well-crafted monoliths and n-tier architectures. In a microservices architecture, however, communication happens over the network, usually the HTTP protocol, and services have dedicated runtime infrastructure. This supports independent development, delivery, and operation of each backend service.

## Choosing the approach for your requirements
<a name="choosing"></a>

Monoliths and n-tier architectures bundle multiple domain concerns into one technical artifact. This makes aspects such as dependencies and internal data flow easy to manage, but it makes delivery of new functionalities more difficult. To maintain a coherent code base, a team often invests time in refactoring and decoupling because of the large code base they have to handle.

Applications developed by a few teams might not need the additional complexity that comes with moving to micro-frontends. This is especially true if the teams are not paying the penalties of high coupling and long lead times to release changes.

In summary, more complex and distributed architectures are often the right choice for complex and fast-moving applications. For small to midsized applications, a distributed architecture isn't necessarily superior to a monolithic one, especially if the application will not dramatically evolve over a short period of time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
