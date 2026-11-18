---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/introduction.html
---

# Understanding and implementing micro-frontends on AWS
<a name="introduction"></a>

*Luca Mezzalira, Matteo Figus, Alexander Guensche, and Harun Hasdal, Amazon Web Services*

As organizations strive for agility and scalability, the conventional monolithic architecture often becomes a bottleneck, hindering rapid development and deployment. Micro-frontends mitigate this by breaking down complex user interfaces into smaller, independent components that can be developed, tested, and deployed autonomously. This approach enhances the efficiency of development teams and facilitates collaboration between backend and frontend, fostering an end-to-end alignment of distributed systems.

This prescriptive guidance helps IT leaders, product owners, and architects across diverse professional domains understand micro-frontend architecture and build micro-frontend applications on Amazon Web Services (AWS).

## Overview
<a name="overview"></a>

Micro-frontends are an architecture built on the decomposition of application frontends into independently developed and deployed artifacts. When you split large frontends into autonomous software artifacts, you can encapsulate business logic and reduce dependencies. This supports faster and more frequent delivery of product increments.

Micro-frontends are similar to *microservices*. In fact, the term micro-frontend is derived from the term microservice, and it aims to convey the notion of a microservice as a frontend. While a microservices architecture typically combines a distributed system in the backend with a monolithic frontend, micro-frontends are self-contained distributed frontend services. These services can be set up in two ways:
+ Frontend-only, integrating with a shared API layer behind which runs a microservices architecture
+ Full-stack, meaning that each micro-frontend has its own backend implementation

The following diagram shows a traditional microservices architecture, with a frontend monolith that uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) to connect to backend microservices.

![Client-side frontend monolith connecting to server-side microservices.](https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/55b8482c-7e32-4fd5-ac14-eea66e86b1a5.png)

The following diagram shows a micro-frontend architecture with different implementations of microservices.

![Client-side integration layer front-end modules and server-side microservices.](https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/da7b5e30-d3d5-400d-b3c1-466f2971a877.png)

As shown in the previous diagram, you can use micro-frontends with client-side rendering or server-side rendering architectures:
+ Client-side rendered micro-frontends can directly consume APIs exposed by a centralized Amazon API Gateway endpoint.
+ The team can create a backend-for-frontend (BFF) inside the bounded context to reduce the chattiness of the frontend toward the APIs.
+ On the server-side, micro-frontends can be expressed with a server-side approach augmented on the client side by using a technique called hydration. When the browser renders a page, the associated JavaScript is hydrated to allow interactions with UI elements, such as clicking a button.
+ Micro-frontends can render on the backend and use hyperlinks to route toward a new part of a website.

Micro-frontends are well suited for organizations that want to do the following:
+ Scale with multiple teams working on the same project.
+ Embrace decentralization of decision making, empowering developers to innovate inside the identified systems boundaries.

This approach can reduce the cognitive load on teams, because they become responsible for specific parts of the system. It can improve business agility because teams can modify one part of the system without disrupting the rest.

Micro-frontends are a distinct architectural approach. Although there are different ways to build micro-frontends, they all have common traits:
+ A micro-frontend architecture is composed of multiple independent elements. The structure is similar to the modularization that happens with microservices on the backend.
+ A micro-frontend is responsible for the frontend implementation within its bounded context, which comprises the following:
  + User interface
  + Data
  + State or session
  + Business logic
  + Flow

A bounded context is an internally consistent system with carefully designed boundaries that mediate what can enter and exit. A micro-frontend should share as little business logic and data with other micro-frontends as possible. Where sharing is necessary, use clearly defined interfaces such as custom events or reactive streams. However, for some cross-cutting concerns such as a design system or logging libraries, intentional sharing is acceptable.

A recommended pattern is to build micro-frontends by using cross-functional teams. This means that each micro-frontend is developed by the same team working from the backend to the frontend. Team ownership is crucial, from coding to the operationalization of the system in production.

This guidance doesn't recommend one particular approach. Instead, it discusses different patterns, best practices, trade-offs, and architectural and organizational considerations.
