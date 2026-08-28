---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_service_architecture_api_contracts.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL03-BP03 Provide service contracts per API
<a name="rel_service_architecture_api_contracts"></a>

 Service contracts are documented agreements between teams on service integration and include a machine-readable API definition, rate limits, and performance expectations. A versioning strategy allows your clients to continue using the existing API and migrate their applications to the newer API when they are ready. Deployment can happen anytime, as long as the contract is not violated. The service provider team can use the technology stack of their choice to satisfy the API contract. Similarly, the service consumer can use their own technology.

 Microservices take the concept of service-oriented architecture (SOA) to the point of creating services that have a minimal set of functionality. Each service publishes an API and design goals, limits, and other considerations for using the service. This establishes a *contract* with calling applications. This accomplishes three main benefits:
+  The service has a concise business problem to be served and a small team that owns the business problem. This allows for better organizational scaling.
+  The team can deploy at any time as long as they meet their API and other contract requirements.
+  The team can use any technology stack they want to as long as they meet their API and other contract requirements.

 Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. It handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management, authorization and access control, monitoring, and API version management. Using OpenAPI Specification (OAS), formerly known as the Swagger Specification, you can define your API contract and import it into API Gateway. With API Gateway, you can then version and deploy the APIs.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Provide service contracts per API Service contracts are documented agreements between teams on service integration and include a machine-readable API definition, rate limits, and performance expectations.
  +  [Amazon API Gateway: Configuring a REST API Using OpenAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html)
    +  A versioning strategy allows clients to continue using the existing API and migrate their applications to the newer API when they are ready.
    +  Amazon API Gateway is a fully managed service that makes it easy for developers to create APIs at any scale. Using the OpenAPI Specification (OAS), formerly known as the Swagger Specification, you can define your API contract and import it into API Gateway. With API Gateway, you can then version and deploy the APIs.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon API Gateway: Configuring a REST API Using OpenAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html)
+  [Bounded Context (a central pattern in Domain-Driven Design)](https://martinfowler.com/bliki/BoundedContext.html)
+  [Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/introduction.html)
+  [Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html)
+  [Microservices - a definition of this new architectural term](https://www.martinfowler.com/articles/microservices.html)
+  [Microservices on AWS](https://aws.amazon.com/microservices/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
