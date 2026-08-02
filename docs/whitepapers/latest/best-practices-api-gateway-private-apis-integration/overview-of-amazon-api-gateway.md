---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/overview-of-amazon-api-gateway.html
---

# Overview of Amazon API Gateway
<a name="overview-of-amazon-api-gateway"></a>

 [Amazon API Gateway](https://aws.amazon.com/api-gateway/) is a fully managed service that helps you easily create, publish, maintain, monitor, and secure APIs at any scale. It provides three different types of APIs: *REST*, *WebSocket*, and *HTTP*. Depending on your business needs and architectural patterns, you can use one or more of the API types:
+  The **REST** API type has three endpoint types: edge-optimized, regional, and private. Edge-optimized and regional REST APIs are publicly accessible and serve requests over the internet. For customers who need to access an API in a private network, a private REST API is the preferred choice. REST APIs provide an easy means to secure APIs such as resource policies, IAM authentication, and custom authorizers. Private REST APIs now support custom domain names, enabling human-readable URLs and cross-account sharing through AWS [AWS Resource Access Manager](https://aws.amazon.com/ram/) (AWS RAM).
+  **WebSocket** APIs enable you to build real-time, two-way communication applications such as chat apps and streaming dashboards. Although there is no private endpoint type available, WebSocket APIs provide an option to create a route with a VPC link for private integration.
+  **HTTP** APIs are a lightweight, limited feature subset of REST APIs, with auto deployment and cross-origin resource sharing (CORS) support. HTTP API private integrations work with [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/), [Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/), and [AWS Cloud Map](https://aws.amazon.com/cloud-map/).
