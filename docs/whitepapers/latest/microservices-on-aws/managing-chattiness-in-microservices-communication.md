---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/managing-chattiness-in-microservices-communication.html
---

# Managing chattiness in microservices communication
<a name="managing-chattiness-in-microservices-communication"></a>

*Chattiness* refers to excessive communication between microservices, which can cause inefficiency due to increased network latency. It's essential to manage chattiness effectively for a well-functioning system.

 Some key tools for managing chattiness are REST APIs, HTTP APIs and gRPC APIs. REST APIs offer a range of advanced features such as API keys, per-client throttling, request validation, AWS WAF integration, or private API endpoints. HTTP APIs are designed with minimal features and hence come at a lower price. For more details on this topic and a list of core features that are available in REST APIs and HTTP APIs, see [Choosing between REST APIs and HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html).

 Often, microservices use REST over HTTP for communication due to its widespread use. But in high-volume situations, REST's overhead can cause performance issues. It’s because the communication uses TCP handshake which is required for every new request. In such cases, gRPC API is a better choice. gRPC reduces the latency as it allows multiple requests over a single TCP connection. gRPC also supports bi-directional streaming, allowing clients and servers to send and receive messages at the same time. This leads to more efficient communication, especially for large or real-time data transfers.

 If chattiness persists despite choosing the right API type, it may be necessary to reevaluate your microservices architecture. Consolidating services or revising your domain model could reduce chattiness and improve efficiency.

## Using protocols and caching
<a name="using-protocols-and-caching"></a>

 Microservices often use protocols like gRPC and REST for communication (see the previous section on [Communication mechanisms](communication-mechanisms.md). ) gRPC uses HTTP/2 for transport, while REST typically uses HTTP/1.1. gRPC employs protocol buffers for serialization, while REST usually uses JSON or XML. To reduce latency and communication overhead, caching can be applied. Services like Amazon ElastiCache or the caching layer in API Gateway can help reduce the number of calls between microservices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
