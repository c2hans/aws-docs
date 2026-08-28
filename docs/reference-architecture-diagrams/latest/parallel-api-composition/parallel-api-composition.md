---
source_url: https://docs.aws.amazon.com/reference-architecture-diagrams/latest/parallel-api-composition/parallel-api-composition.html
---

# Parallel API Composition in AWS
<a name="parallel-api-composition"></a>

Publication date: **May 17, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to call multiple downstream API endpoints, in parallel or in sequence, to compose a single aggregated response. You build a generic, parameterized circuit-breaker workflow using [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) Express Workflows and use command query responsibility segregation (CQRS) to maintain a persistent eventually-consistent cache.

## Parallel API Composition in AWS
<a name="diagram1"></a>

![Architecture diagram showing parallel API composition using Amazon API Gateway, AWS Step Functions Express Workflows, AWS Lambda, and Amazon EventBridge.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/parallel-api-composition/images/parallel-api-composition.png)

The following steps describe the architecture:

1. Create an API gateway using [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) to allow clients to send synchronous web requests to your microservices.

1. Use Step Functions Express Workflows to create a workflow with parallel steps that invoke multiple microservices at the same time.

1. Use an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function to compose the multiple responses from downstream microservices into a single aggregated response for clients.

1. Handle parallel requests with circuit breakers built with parameterized nested Step Functions Express Workflows to increase resilience.

1. Use API Gateway to proxy HTTP requests when invoking on-premises microservices.

1. Create an Amazon MemoryDB for Redis database to cache microservice responses using the [write-through caching pattern](https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/caching-patterns.html). When a downstream microservice becomes unavailable or its latency reaches a threshold, the circuit closes and reads all responses directly from cache.

1. Complement cached data with domain events from downstream microservices using the CQRS pattern. Create an event bus with [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html), then handle events with a Lambda function to persist the domain aggregates in MemoryDB.

1. Enable the API Gateway response cache and adjust time-to-live (TTL) values and filters according to each request type to increase performance.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date |
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | May 17, 2022 |

**Note**
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Reference Architecture Diagrams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query reference-architecture-diagrams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
