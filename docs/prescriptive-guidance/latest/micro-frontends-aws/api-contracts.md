---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/api-contracts.html
---

# API contracts
<a name="api-contracts"></a>

Each micro-frontend is a system capable of encapsulating opinions, logic, and complexity. Cross-cutting concerns usually include the following:
+ **Design systems** ‒ Tooling to develop UIs distributed as libraries
+ **Composition** ‒ The way a micro-frontend needs to interact with an application shell to render and to inherit its context
+ **Logic handling** ‒ Interaction with APIs to handle persistent state
+ **Interactivity with other micro-frontends** ‒ Scenarios such as publishing and consuming events or navigating from one micro-frontend to another

To accelerate consumption and troubleshooting, it's common to invest in standardizing the way these interfaces are declared and documented, including micro-frontend dependencies. Wikis curated by humans are a good start. A more scalable approach is to store this information as structured metadata in code. You can then centralize it for consumption by using automation to track historic changes and provide full-text search.

When micro-frontends involve a large number of teams, you need a strategy to coordinate between teams. Sharing API contracts in a unified way becomes a must because it reduces communication overhead and improves developer experience.

[OpenAPI](https://www.openapis.org/) is a specification language for HTTP APIs that supports defining API interfaces and contracts in a unified way. You can implement REST APIs by [using OpenAPI in Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html). You can also use a wide variety of open source frameworks that you can host in containers or virtual machines. A significant advantage is that OpenAPI can automatically generate documentation in a consistent format, so multiple teams can share knowledge with a minimal initial investment.

When multiple teams work on micro-frontends, they often form groups. In these groups, people can meet and learn from each other while thinking about and contributing to the bigger picture. These initiatives typically define and document ownership boundaries, discuss cross-cutting concerns, and identify early on any duplication of efforts to solve common problems.
