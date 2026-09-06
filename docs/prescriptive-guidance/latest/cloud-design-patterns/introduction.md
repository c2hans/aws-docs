---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/introduction.html
---

# Cloud design patterns, architectures, and implementations
<a name="introduction"></a>

*Anitha Deenadayalan, Amazon Web Services*

This guide provides guidance for implementing commonly used modernization design patterns by using AWS services. An increasing number of modern applications are designed by using microservices architectures to achieve scalability, improve release velocity, reduce the scope of impact for changes, and reduce regression. This leads to improved developer productivity and increased agility, better innovation, and an increased focus on business needs. Microservices architectures also support the use of the best technology for the service and the database, and promote polyglot code and polyglot persistence.

Traditionally, monolithic applications run in a single process, use one data store, and run on servers that scale vertically. In comparison, modern microservice applications are fine-grained, have independent fault domains, run as services across the network, and can use more than one data store depending on the use case. The services scale horizontally, and a single transaction might span multiple databases. Development teams must focus on network communication, polyglot persistence, horizontal scaling, eventual consistency, and transaction handling across the data stores when developing applications by using microservices architectures. Therefore, modernization patterns are critical for solving commonly occurring problems in modern application development, and they help accelerate software delivery.

This guide provides a technical reference for cloud architects, technical leads, application and business owners, and developers who want to choose the right cloud architecture for design patterns based on well-architected best practices. Each pattern discussed in this guide addresses one or more known scenarios in microservices architectures. The guide discusses the issues and considerations associated with each pattern, provides a high-level architectural implementation, and describes the AWS implementation for the pattern. Open source GitHub samples and workshop links are provided where available.

The guide covers the following patterns:
+ [Anti-corruption layer](acl.md)
+ [API routing patterns](api-routing.md):
  + [Hostname routing](api-routing-hostname.md)
  + [Path routing](api-routing-path.md)
  + [HTTP header routing](api-routing-http-header.md)
+ [Circuit breaker](circuit-breaker.md)
+ [Event sourcing](event-sourcing-pattern.md)
+ [Hexagonal architecture](hexagonal-architecture.md)
+ [Publish-subscribe](publish-subscribe.md)
+ [Retry with backoff](retry-backoff.md)
+ [Saga patterns](saga-patterns.md):
  + [Saga choreography](saga-choreography.md)
  + [Saga orchestration](saga-orchestration.md)
+ [Scatter-gather](scatter-gather.md)
+ [Strangler fig](strangler-fig.md)
+ [Transactional outbox](transactional-outbox.md)

## Targeted business outcomes
<a name="targeted-business-outcomes.4261aab2-0ba0-5dfc-8adf-e79494ae8b4b"></a>

By using the patterns discussed in this guide to modernize your applications, you can:
+ Design and implement reliable, secure, operationally efficient architectures that are optimized for cost and performance.
+ Reduce the cycle time for use cases that require these patterns, so you can focus on organization-specific challenges instead.
+ Accelerate development by standardizing pattern implementations by using AWS services.
+ Help your developers build modern applications without inheriting technical debt.

### Attachments
<a name="attachments-48f618e4-d8ad-490f-982b-7b304dbf76c9"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
