---
source_url: https://docs.aws.amazon.com/whitepapers/latest/reactive-systems-on-aws/reactive-systems-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Reactive Systems on AWS
<a name="reactive-systems-on-aws"></a>

Publication date: **November 1, 2021** ([Document history](document-history.md))

 Today, architects and developers are expected to implement highly scalable and resilient distributed system on Amazon Web Services (AWS). This whitepaper outlines best practices for designing a system based on reactive principles using the AWS Cloud and offers a reference architecture to guide organizations in the delivery of these systems.

## Introduction
<a name="introduction"></a>

Microservice application requirements have changed dramatically in recent years. Many modern applications are expected to handle petabytes of data, require close to 100% uptime, and deliver sub-second response time to users. Typical N-tier applications can’t deliver on these requirements. Today reactive architectures and reactive systems have been adopted by a growing number of enterprises, because it is necessary to design applications in a highly scalable and responsive way. But what exactly is a reactive system?

 The [Reactive Manifesto](https://www.reactivemanifesto.org/), describes the essential characteristics of reactive systems including: responsiveness, resiliency, elasticity, and being message driven.

 Being message driven is perhaps the most important characteristic of reactive systems. Asynchronous messaging helps in the design of loosely coupled systems, which is a key factor for scalability. In order to build highly resilient systems, it is important to isolate services from each other. Microservices are an architectural and organizational approach to software development where software is composed of small independent services that communicate over well-defined APIs. These services are owned by small, self-contained teams. Isolation and decoupling are an important aspect of the microservices pattern as well. This makes reactive systems and microservices a natural fit.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
