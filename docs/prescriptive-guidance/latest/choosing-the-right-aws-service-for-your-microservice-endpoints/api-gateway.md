---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-the-right-aws-service-for-your-microservice-endpoints/api-gateway.html
---

# Amazon API Gateway
<a name="api-gateway"></a>

[Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) is an API management service that's primarily designed for creating, publishing, and managing REST, HTTP, and WebSocket APIs. Use API Gateway to take advantage of capabilities like AWS Lambda authorizers, request/response validation and transformation, usage plans, and built-in AWS WAF support. For more information, see [Features of API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html#api-gateway-overview-features) in the *Amazon API Gateway Developer Guide*.

## API Gateway use cases
<a name="api-gateway-use-cases"></a>

API Gateway is appropriate for the following use cases:
+ **API management** – Create, publish, maintain, monitor, and secure APIs. Consolidate and expose well-structured and well-documented APIs. Simplify the client experience by providing a single entry point for various services, providing a consistent view for the API consumer. API Gateway acts as a proxy to various AWS services, exposing them as RESTful APIs. API Gateway includes built-in security and control, including rate limiting based on usage plans, which makes it an excellent solution for serverless architecture.
+ **Third-party integrations** – Expose APIs to third-party developers or partners securely by using API keys, OAuth, or Lambda authorizers to control access and monetize your APIs. External as well as internal consumers can use the APIs exposed by this layer through the Amazon API Gateway [Serverless Developer Portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-developer-portal.html). The portal enables secure, scalable exposure of APIs to third-party developers and partners.
+ **Safeguarding backend resources from traffic surge** – Prevent abuse and ensure fair usage of your APIs by using rate limiting and throttling policies.
+ **IoT device communication** – Handle real-time two-way communication between IoT devices and cloud resources by using [WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-overview.html). This approach is important for IoT applications that require immediate data exchange, such as monitoring systems, instant alerts, and live device status updates. API Gateway supports multiple authentication and authorization mechanisms, and rate limiting for secure and efficient device interactions.
+ **Webhook and event handling** – Implement webhook endpoints to receive and process events from external systems, such as GitHub, Slack, or other software as a service (SaaS) applications.

The following diagram illustrates the integration between client-side applications and services by using API Gateway. For various types of clients, including web, mobile, and other services, API Gateway acts as a unified access point. It enables API access through public or private endpoints. Frequently requested data is cached to enhance performance, decrease backend load, and reduce latency. On the backend, it directs the incoming traffic to destinations such as Lambda functions, EC2 instances, other AWS services, public endpoints, or endpoints within a VPC.

![Amazon API Gateway for private, regional, and edge-optimized APIs.](http://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-the-right-aws-service-for-your-microservice-endpoints/images/guide-img/45387eb1-39dc-4dd7-a6b2-e3cd572b2949/images/164c936d-b1bb-431c-b99e-d82920640a75.png)

The following diagram shows how API Gateway processes, validates, and transforms requests securely before sending them to destinations. It offers well-crafted API operations with URLs, parameters, headers, and stage variables.

![Amazon API Gateway for HTTP endpoint and request/response validation and transformation.](http://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-the-right-aws-service-for-your-microservice-endpoints/images/guide-img/45387eb1-39dc-4dd7-a6b2-e3cd572b2949/images/22a2e723-a212-4a6c-add9-abc3f692cb30.png)

API Gateway has a strong security OAuth mechanism in place to confirm user identities and authorize access to services. It also has throttling and usage tiers to help manage traffic and prevent abuse by limiting the number of requests clients can make. The caching capabilities improve performance by storing frequently accessed data. Client SDK generation simplifies integration for developers by providing ready-to-use code libraries. API gateway supports different endpoint types, including edge, regional, and private endpoints. Additionally, API Gateway offers OpenAPI/Swagger support, which enables standardized API documentation and easier integration.
