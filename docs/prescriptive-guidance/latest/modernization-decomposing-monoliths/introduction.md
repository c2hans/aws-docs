---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/introduction.html
---

# Decomposing monoliths into microservices
<a name="introduction"></a>

*Tabby Ward and Dmitry Gulin, Amazon Web Services*

A migration to the Amazon Web Services (AWS) Cloud has [many advantages](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html), including technical and business agility, new revenue opportunities, and reduced costs. To fully benefit from these advantages, you should continuously modernize your organization's software by refactoring your monolithic applications into microservices. This process consists of three main steps:
+ **Decompose monoliths into microservices** – Use the decomposition patterns provided by this guide to break down monolithic applications into microservices.
+ [Integrate microservices ](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/welcome.html) – Integrate the newly created microservices into a [microservices architecture ](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/simple-microservices-architecture-on-aws.html)by using [AWS serverless services](https://aws.amazon.com/serverless/).
+ **Enable data persistence for microservices architecture** – Promote [polyglot persistence](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/simple-microservices-architecture-on-aws.html) among your microservices by decentralizing data stores.

Modernization typically involves two types of projects:
+ *Brownfield projects* involve developing and deploying a new software system within the context of existing or legacy systems.
+ *Greenfield projects*  involve creating a system from scratch for a completely new environment, without any legacy code involved.

For brownfield projects, one of the first steps in your application modernization journey is to decompose the monoliths in your portfolio into microservices.

Most applications begin as monoliths that are designed for a specific business use case. If the monolith's architecture doesn't enforce modular design, a monolith can remain a valid choice for applications that don't have clearly defined responsibilities within the boundaries of well-established domain knowledge. The central characteristic of a monolith as a single unit of deployment can also help mitigate design flaws, such as tight coupling or a lack of internal structure.

Although a monolith can be a valid option for some use cases, it is typically not suitable for a modern application. The poorly defined internal structures of a monolith can make it difficult to maintain code, which creates a steep learning curve for new developers and causes additional support costs. High coupling and low cohesion can significantly increase the time it takes to add new features, and you might be unable to scale individual components based on traffic patterns. Monoliths also require multiple teams to coordinate for one large release, which increases the collaboration and knowledge transfer burden. Finally, you can find that adding new features or building new user experiences becomes difficult when your business or your user base grows.

To avoid this, you can use decomposition patterns to break down monolithic applications, convert them into several microservices, and migrate them to a microservices architecture. A microservices architecture structures an application as a series of loosely coupled services. Microservices are designed to accelerate software development by enabling continuous delivery and continuous deployment (CI/CD) processes.

Before you begin the decomposition process, you should evaluate which monoliths to decompose. Make sure to include monoliths that have reliability or performance issues, or include multiple components in a tightly coupled architecture. We also recommend that you fully understand the business use case for the monolith, its technology, and its inter-dependencies with other applications.

This guide is for application owners, business owners, architects, technical leads, and project managers. It discusses the following six cloud-native patterns that are used to decompose monoliths, and describes the advantages and disadvantages of each one:
+ [Decompose by business capability](decompose-business-capability.md)
+ [Decompose by subdomain](decompose-subdomain.md)
+ [Decompose by transactions](decompose-transactions.md)
+ [Service per team pattern](service-per-team.md)
+ [Strangler fig pattern](strangler-fig.md)
+ [Branch by abstraction pattern](branch-by-abstraction.md)

The guide is part of a content series that covers the application modernization approach recommended by AWS. The series also includes:
+ [Phased approach to modernizing applications in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-phased-approach/)
+ [Evaluating modernization readiness for applications in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-assessing-applications/welcome.html)
+ [Integrating microservices by using AWS serverless services](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/welcome.html)

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

You should expect the following outcomes after you decompose your monoliths into microservices:
+ An efficient transition of your monolithic application into a microservices architecture.
+ Rapid adjustments to fluctuating business demand without interrupting core activities, such as high scalability, improved resiliency, continuous delivery, and failure isolation.
+ Faster innovation, because each microservice can be individually tested and deployed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
