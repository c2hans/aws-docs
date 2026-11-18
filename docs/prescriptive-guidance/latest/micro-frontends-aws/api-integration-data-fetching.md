---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/api-integration-data-fetching.html
---

# API integration ‒ Backend for frontend
<a name="api-integration-data-fetching"></a>

The [Backends for Frontends (BFF) pattern](https://aws.amazon.com/blogs/mobile/backends-for-frontends-pattern/) is typically used in microservices environments. In the context of micro-frontends, a BFF is a server-side service that belongs to a micro-frontend. Not all micro-frontends need to have a BFF. However, if you're using a BFF, it must run inside the same bounded context and not be shared across other bounded contexts.

Unlike a traditional service, a BFF doesn't follow a domain model. Instead, it's an API layer for the micro-frontend to preprocess data before it reaches the client. Areas where this is useful include the following:
+ Authorization toward private APIs
+ Aggregation of data from different sources
+ Transformation of data to reduce network load and to ease the consumption of data by the client

As such, the micro-frontend owns a BFF, not the domain service tier. You can deploy BFFs by using the following:
+ [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/welcome.html) GraphQL APIs
+ A set of AWS Lambda functions
+ A container running on [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/), or AWS App Runner

The following diagram shows that without the BFF pattern, micro-frontends must connect to individual microservice API endpoints to fetch and aggregate data.

![Dashboard app that first fetches transactions and then fetches prices from decoupled microservices.](https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/32e37d0c-d342-4ec8-9be2-bf1a61777fcf.png)

Instead, with the BFF pattern in the following diagram, micro-frontends can communicate with their own backend and fetch aggregated data.

![The transactions view fetches aggregated data, including price information, from the BFF.](https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/1cc136d8-f429-470e-9d8b-bfd52dc4aba8.png)

Teams can develop BFFs for different channels such as mobile, web, or specific views. Each BFF can optimize backend interactions by reducing the number of network calls between the client and backend services.
