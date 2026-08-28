---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_service_architecture_business_domains.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL03-BP02 Build services focused on specific business domains and functionality
<a name="rel_service_architecture_business_domains"></a>

 Service-oriented architecture (SOA) builds services with well-delineated functions defined by business needs. Microservices use domain models and bounded context to limit this further so that each service does just one thing. Focusing on specific functionality enables you to differentiate the reliability requirements of different services, and target investments more specifically. A concise business problem and having a small team associated with each service also enables easier organizational scaling.

 In designing a microservice architecture, it’s helpful to use Domain-Driven Design (DDD) to model the business problem using entities. For example, for the Amazon.com website, entities might include package, delivery, schedule, price, discount, and currency. Then the model is further divided into smaller models using [*Bounded Context*](https://martinfowler.com/bliki/BoundedContext.html), where entities that share similar features and attributes are grouped together. So, using the Amazon.com example package, delivery, and schedule would be part of the shipping context, while price, discount, and currency are part of the pricing context. With the model divided into contexts, a template for how to boundary microservices emerges.

![Model template for how to boundary microservices](http://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/images/building-services.png)

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Design your workload based on your business domains and their respective functionality. Focusing on specific functionality enables you to differentiate the reliability requirements of different services, and target investments more specifically. A concise business problem and having a small team associated with each service also enables easier organizational scaling.
  +  Perform Domain Analysis to map out a domain-driven design (DDD) for your workload. Then you can choose an architecture type to meet your workload’s needs.
    +  [How to break a Monolith into Microservices](https://martinfowler.com/articles/break-monolith-into-microservices.html)
    +  [Getting Started with DDD when Surrounded by Legacy Systems](https://domainlanguage.com/wp-content/uploads/2016/04/GettingStartedWithDDDWhenSurroundedByLegacySystemsV1.pdf)
    +  [Eric Evans “Domain-Driven Design: Tackling Complexity in the Heart of Software”](https://www.amazon.com/gp/product/0321125215)
    +  [Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/introduction.html)
+ Decompose your services into smallest possible components. With microservices architecture you can separate your workload into components with the minimal functionality to enable organizational scaling and agility.
  +  Define the API for the workload and its design goals, limits, and any other considerations for use.
    +  Define the API.
      +  The API definition should allow for growth and additional parameters.
    +  Define the designed availabilities.
      + Your API may have multiple design goals for different features.
    +  Establish limits
      +  Use testing to define the limits of your workload capabilities.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon API Gateway: Configuring a REST API Using OpenAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html)
+  [Bounded Context (a central pattern in Domain-Driven Design)](https://martinfowler.com/bliki/BoundedContext.html)
+  [Eric Evans “Domain-Driven Design: Tackling Complexity in the Heart of Software”](https://www.amazon.com/gp/product/0321125215)
+  [Getting Started with DDD when Surrounded by Legacy Systems](https://domainlanguage.com/wp-content/uploads/2016/04/GettingStartedWithDDDWhenSurroundedByLegacySystemsV1.pdf)
+  [How to break a Monolith into Microservices](https://martinfowler.com/articles/break-monolith-into-microservices.html)
+  [Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/introduction.html)
+  [Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html)
+  [Microservices - a definition of this new architectural term](https://www.martinfowler.com/articles/microservices.html)
+  [Microservices on AWS](https://aws.amazon.com/microservices/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
