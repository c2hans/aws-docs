---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/introduction.html
---

# Networking connectivity options on AWS for SaaS offerings
<a name="introduction"></a>

*Tomas Sykora and Luca Schumann, Amazon Web Services*

This guide explores common scenarios for connecting consumer applications to software as a service (SaaS) providers. It discusses how to connect to resources that are on-premises, in the AWS Cloud, in other cloud service provider (CSP) clouds, or in hybrid architectures. These scenarios include the following:
+ Exposing web services over HTTPS
+ Exposing TCP-based services
+ Using [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) to implement publish-subscribe (Pub/Sub) and GraphQL APIs
+ Using AWS resources to expose WebSockets for real-time applications
+ Enabling bi-directional access for interactive service communication

By aligning with the best practices covered in this guide, SaaS providers can drive customer trust and support scalable, secure, and resilient access to SaaS offerings.

This guide also includes self-assessment criteria to help you evaluate how successfully you are meeting consumer networking requirements for your SaaS offering. Beyond connectivity patterns, you'll find comprehensive comparisons of AWS networking services, high-level architectural diagrams for various deployment scenarios, and practical guidance for how to select the right approach based on your specific business context. The guide explores security considerations for each networking option, discusses common pitfalls to avoid, and provides implementation recommendations that balance technical requirements with operational efficiency. Additionally, you'll find strategic frameworks for aligning your networking decisions with your business model, growth objectives, and regulatory compliance needs.

## Intended audience
<a name="audience"></a>

This guide is intended for SaaS providers. It helps cloud architects, product managers, and network engineers who are designing, implementing and optimizing network connectivity for SaaS offerings in the AWS Cloud. To understand the concepts and recommendations in this guide, you should be familiar with AWS fundamentals, core SaaS concepts, and high-level networking principles.

## Objectives
<a name="objectives"></a>

This guide discusses network architecture options and field-tested best practices that help consumers optimize access to SaaS offerings. Implementing the recommendations in this guide supports the following:
+ **Ease of integration** – Provide an uncomplicated customer journey from onboarding to production so that you can accelerate your customers' time to value and shorten their revenue recognition cycle.
+ **Adaptability** – Seamlessly integrate with your customers' existing network infrastructures by adapting to their evolving needs. This enhances your product's value proposition.
+ **Total cost of ownership** – Standardize network access to reduce change costs and costs per tenant. By improving deployment consistency, you can also reduce the time to perform root cause analysis or repair.
+ **Dependency management** – Understand dependencies, long-term implications, and trade-offs of the different network access options. This helps product leaders make well-informed product decisions.
+ **Composability and extendibility** – Decouple the development of core functionality from operational infrastructure. This helps development teams move faster and focus on creating value for your customers.
+ **Drive trust** – By providing resilient, fault-tolerant, secure, and scalable access to SaaS offerings, you can reduce regulatory risks and earn trust in your ability to support your customers' growth.
