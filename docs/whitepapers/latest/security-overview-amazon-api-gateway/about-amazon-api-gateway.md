---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-api-gateway/about-amazon-api-gateway.html
---

# About Amazon API Gateway
<a name="about-amazon-api-gateway"></a>

 Amazon API Gateway is a fully-managed service that enables developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the front door for applications to access data, business logic, or functionality from backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable near real-time, two-way communication applications. API Gateway supports a variety of backend integrations, enabling containerized, serverless, and traditional instance-based workloads.

 API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls. This includes traffic management, cross-origin resource sharing (CORS) support, authorization and access control, throttling, monitoring, caching, and API version management. API Gateway has no minimum fees or startup costs. You pay for the API calls you receive, and the amount of data transferred out. With the API Gateway tiered pricing model, your cost per million invocations reduces as your API usage scales.

## Benefits of Amazon API Gateway
<a name="benefits-of-amazon-api-gateway"></a>

 API Gateway offers a variety of benefits and capabilities:
+  **Unified front door** – Use API Gateway to compose unified APIs to a variety of integration types and microservices with advanced routing and transformation features.
+  **Security and governance built in** – API Gateway supports authorization using any form of bearer or JSON web tokens (JWTs), integration with [AWS Web Application Firewall](https://aws.amazon.com/waf/) (AWS WAF) for layer 7 request validation, and integration with [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) and [AWS Config](https://aws.amazon.com/config/) to enable auditing, logging, monitoring, and compliance out of the box.
+  **Standards built in** – API Gateway supports OpenAPI specification versions 2 and 3 for import and export of APIs, and authorization with native OpenID Connect and OAuth 2.0 token parsing.
+  **Regulatory compliance support** – Use API Gateway to build architectures and systems to meet requirements for regulatory compliance attestations including SOC, PCI, ISO, FedRAMP, HIPAA, and more.
+  **Observability built in** – Native integrations with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and [AWS X-Ray](https://aws.amazon.com/xray) provide extensive Amazon CloudWatch metrics, monitoring and alarming, and end-to-end tracing capabilities.
+  **API lifecycle management** – Use API Gateway to run multiple versions of the same API simultaneously, so that applications can continue to call previous API versions even after newer versions are published. API Gateway also helps you manage multiple release stages for each API version, such as alpha, beta, and production. Each API stage can be configured to interact with different backend endpoints based on your API setup. Stage and version management allow you to test new API versions while ensuring backward-compatibility as user communities transition to adopt the latest release.
+  **Streamlined developer experience** – An open-source developer portal enables streamlined API registration and onboarding processes. It issues API keys to authenticated users and enables them to interactively explore and test APIs. Third-party developers of your APIs can download generated client SDKs for a number of platforms. You can use these SDKs to test new APIs from your applications and distribute them to third-party developers. The generated SDKs handle API keys and sign requests using AWS credentials. API Gateway can generate client SDKs for numerous programming languages.
+  **Performance at any scale** – API Gateway is an always-on, scalable service that supports practically any load with no warm-up limitations. It provides you with the lowest possible latency for API requests and responses using cached content and by accelerating content delivery with global edge network locations using [Amazon CloudFront](https://aws.amazon.com/cloudfront/). It can also handle bursts of traffic for your workloads while throttling and authorizing API calls, to help ensure that backend operations can withstand traffic spikes and not be unnecessarily called.
+  **Pay for value pricing** – Cost savings are realized at scale through the API Gateway simple, tiered, price-per-million request pricing. You pay only for the requests made to your API, with no minimum.

## API types
<a name="api-types"></a>

 API Gateway supports multiple API types and a variety of architectural patterns:
+  **HTTP APIs** – Build stateless RESTful APIs optimized for serverless workloads and HTTP backends using HTTP APIs. HTTP APIs are the best choice for building APIs that require only API proxy functionality. If your APIs require API proxy functionality and API management features in a single solution, API Gateway also offers REST APIs.
+  **WebSocket APIs** – Build real-time, two-way communication applications, such as chat apps and streaming dashboards, with WebSocket APIs. API Gateway maintains a persistent connection to handle message transfer between your backend service and your clients.

## Endpoint types
<a name="endpoint-types"></a>

 Amazon API Gateway offers three types of endpoints:
+  **Private** **API endpoints** – Can be accessed only from your [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) and approved subnets using an interface VPC endpoint.
+  **Regional** **API endpoints** – Offload transport layer security (TLS) within the API deployment in your chosen AWS Region. This is suggested for use cases where API client calls originate in the same region, or for when you want to custom-manage an Amazon CloudFront distribution with a Regional API Gateway endpoint as your origin for dynamic content. This is the default selection for HTTP and WebSocket API Gateway endpoints.
+  **Edge-optimized** **API endpoints** – Provide API access to geographically distributed clients with managed edge network acceleration built-in. This is the default selection for REST API Gateway endpoints. It should not be used for APIs where clients consist of other services within the same Region, or when you require granular control of CloudFront CDN caching behaviors. Client TLS connections end at the CloudFront edge location where the API request is first routed, and AWS manages TLS communication between CloudFront and API Gateway instances.

## Cost for Amazon API Gateway-based applications
<a name="cost-for-amazon-api-gateway-based-applications"></a>

 With API Gateway, you pay only for invocation requests made to your APIs. There are no minimum fees or upfront commitments. For HTTP APIs and REST APIs, you pay only for the API calls you receive and the amount of data transferred out. There are no data transfer out charges for Private APIs, though [AWS PrivateLink](https://aws.amazon.com/privatelink/pricing/) charges apply when using Private APIs in API Gateway. API Gateway also provides optional data caching, charged at an hourly rate that varies based on the cache size you select. For WebSocket APIs, you pay only when your APIs are in use based on number of messages sent and received and connection minutes, as well as any data transfer.

 The API Gateway free tier includes one million HTTP API calls, one million REST API calls, one million messages, and 750,000 connection minutes per month for up to 12 months.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
