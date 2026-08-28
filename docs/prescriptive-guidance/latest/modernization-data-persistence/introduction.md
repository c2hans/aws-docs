---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/introduction.html
---

# Enabling data persistence in microservices
<a name="introduction"></a>

*Tabby Ward and Balaji Mohan, Amazon Web Services*

Organizations constantly seek new processes to create growth opportunities and reduce time to market. You can increase your organization's agility and efficiency by modernizing your applications, software, and IT systems. Modernization also helps you deliver faster and better services to your customers.

Application modernization is a gateway to continuous improvement for your organization, and it begins by refactoring a monolithic application into a set of independently developed, deployed, and managed microservices. This process has the following steps:
+ [Decompose monoliths into microservices](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/welcome.html) – Use patterns to break down monolithic applications into microservices.
+ [Integrate microservices](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/welcome.html) – Integrate the newly created microservices into a [microservices architecture ](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/simple-microservices-architecture-on-aws.html)by using [Amazon Web Services (AWS) serverless services](https://aws.amazon.com/serverless/).
+ **Enable data persistence for microservices architecture** – Promote [polyglot persistence](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/simple-microservices-architecture-on-aws.html) among your microservices by decentralizing their [data stores](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/data-store.html).

Although you can use a monolithic application architecture for some use cases, modern application features often don't work in a monolithic architecture. For example, the entire application can't remain available while you upgrade individual components, and you can't scale individual components to resolve bottlenecks or [hotspots](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-hotspots-detection.html) (relatively dense regions in your application's data). Monoliths can become large, unmanageable applications, and significant effort and coordination is required among multiple teams to introduce small changes.

Legacy applications typically use a centralized monolithic database, which makes schema changes difficult, creates a technology lock-in with vertical scaling as the only way to respond to growth, and imposes a single point of failure. A monolithic database also prevents you from building the decentralized and independent components required for implementing a microservices architecture.

Previously, a typical architectural approach was to model all user requirements in one relational database that was used by the monolithic application. This approach was supported by popular relational database architecture, and application architects usually designed the relational schema at the earliest stages of the development process, built a highly normalized schema, and then sent it to the developer team. However, this meant that the database drove the data model for the application use case, instead of the other way round.

By choosing to decentralize your data stores, you promote [polyglot persistence among your microservices](https://docs.aws.amazon.com/whitepapers/latest/modern-application-development-on-aws/polyglot-persistence.html), and identify your data storage technology based on the data access patterns and other requirements of your microservices. Each microservice has its own data store and can be independently scaled with low-impact schema changes, and data is gated through the microservice's API. Breaking down a monolithic database is not easy, and one of the biggest challenges is structuring your data to achieve the best possible performance. Decentralized polyglot persistence also typically results in eventual data consistency, and other potential challenges that require a thorough evaluation include data synchronization during transactions, transactional integrity, data duplication, and joins and latency.

This guide is for application owners, business owners, architects, technical leads, and project managers. The guide provides the following six patterns to enable data persistence among your microservices:
+ Database-per-service pattern
+ API composition pattern
+ CQRS pattern
+ Event sourcing pattern
+ Saga pattern
  + For steps to implement the saga pattern by using AWS Step Functions, see the pattern [Implement the serverless saga pattern by using AWS Step Functions](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-the-serverless-saga-pattern-by-using-aws-step-functions.html) on the AWS Prescriptive Guidance website.
+ Shared-database-per-service pattern

The guide is part of a content series that covers the application modernization approach recommended by AWS. The series also includes:
+ [Phased approach to modernizing applications in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-phased-approach/)
+ [Evaluating modernization readiness for applications in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-assessing-applications/welcome.html)
+ [Decomposing monoliths into microservices](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/welcome.html)
+ [Integrating microservices by using AWS serverless services](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/welcome.html)

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

Many organizations find that innovating and improving the user experience is negatively impacted by monolithic applications, databases, and technologies. Legacy applications and databases reduce your options for adopting modern technology frameworks, and constrain your competitiveness and innovation. However, when you modernize applications and their data stores, they become easier to scale and faster to develop. A decoupled data strategy improves fault tolerance and resiliency, which helps accelerate the time to market for your new application features.

You should expect the following six outcomes from promoting data persistence among your microservices:
+ Remove legacy monolithic databases from your application portfolio.
+ Improve fault tolerance, resiliency, and availability for your applications.
+ Shorten your time to market for new application features.
+ Reduce your overall licensing expenses and operational costs.
+ Take advantage of open-source solutions (for example, [MySQL](https://www.mysql.com/) or [PostgreSQL](https://www.postgresql.org/)).
+ Build highly scalable and distributed applications by choosing from more than [15 purpose-built database engines on the AWS Cloud](https://aws.amazon.com/products/databases/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
