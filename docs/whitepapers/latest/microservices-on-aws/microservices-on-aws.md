---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html
---

# Implementing Microservices on AWS
<a name="microservices-on-aws"></a>

Publication date: **July 31, 2023** ([Document history](document-revisions.md))

 Microservices offer a streamlined approach to software development that accelerates deployment, encourages innovation, enhances maintainability, and boosts scalability. This method relies on small, loosely coupled services that communicate through well-defined APIs, which are managed by autonomous teams. Adopting microservices offers benefits, such as improved scalability, resilience, flexibility, and faster development cycles.

 This whitepaper explores three popular microservices patterns: API driven, event driven, and data streaming. We provide an overview of each approach, outline microservices' key features, address the challenges in their development, and illustrate how Amazon Web Services (AWS) can help application teams tackle these obstacles.

 Considering the complex nature of topics like data store, asynchronous communication, and service discovery, you are encouraged to weigh your application's specific needs and use cases alongside the guidance provided when making architectural decisions.

## Introduction
<a name="introduction"></a>

 [Microservices](https://aws.amazon.com/microservices/) architectures combine successful and proven concepts from various fields, such as:
+  Agile software development
+  Service-oriented architectures
+  API-first design
+  Continuous Integration/Continuous Delivery (CI/CD)

 Often, microservices incorporate design patterns from the [Twelve-Factor App.](https://12factor.net/)

 While microservices offer many benefits, it's vital to assess your use case's unique requirements and associated costs. Monolithic architecture or alternative approaches may be more appropriate in some cases. Deciding between microservices or monoliths should be made on a case-by-case basis, considering factors like scale, complexity, and specific use cases.

 We first explore a highly scalable, fault-tolerant microservices architecture (user interface, microservices implementation, data store) and demonstrate how to build it on AWS using container technologies. We then suggest AWS services to implement a typical serverless microservices architecture, reducing operational complexity.

 Serverless is characterized by the following principles:
+  No infrastructure to provision or manage
+  Automatically scaling by unit of consumption
+  "Pay for value" billing model
+  Built-in availability and fault tolerance
+  Event Driven Architecture (EDA)

 Lastly, we examine the overall system and discuss cross-service aspects of a microservices architecture, such as distributed monitoring, logging, tracing, auditing, data consistency, and asynchronous communication.

 This document focuses on workloads running in the AWS Cloud, excluding hybrid scenarios and migration strategies. For information on migration strategies, refer to the [Container Migration Methodology whitepaper](https://d1.awsstatic.com/whitepapers/container-migration-methodology.pdf).

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 In the [Serverless Application Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html), we focus on best practices for architecting your serverless applications on AWS.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Modernizing to microservices
<a name="modernizing-to-microservices"></a>

 Microservices are essentially small, independent units that make up an application. Transitioning from traditional monolithic structures to microservices can follow [various strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decomposing-patterns.html).

 This transition also impacts the way your organization operates:
+  It encourages agile development, where teams work in quick cycles.
+  Teams are typically small, sometimes described as *two pizza teams*—small enough that two pizzas could feed the entire team.
+  Teams take full responsibility for their services, from creation to deployment and maintenance.
