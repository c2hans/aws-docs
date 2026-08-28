---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/faq.html
---

# FAQ
<a name="faq"></a>

## When can I modernize my monolithic database as part of my modernization journey?
<a name="q1"></a>

You should focus on modernizing your monolithic database when you begin to decompose monolithic applications into microservices. Make sure that you create a strategy to split your database into multiple small databases that are aligned with your applications.

## Can I keep a legacy monolithic database for multiple microservices?
<a name="q2"></a>

Keeping a shared monolithic database for multiple microservices creates tight coupling, which means you can't independently deploy changes to your microservices, and that all schema changes must be coordinated among your microservices. Although you can use a relational data store as your monolithic database, NoSQL databases might be a better choice for some of your microservices.

## What should I consider when designing databases for a microservices architecture?
<a name="q3"></a>

You should design your application based on domains that align with your application's functionality. Make sure that you evaluate the application's functionality and decide if it requires a relational database schema. You should also consider using a NoSQL database, if it fits your requirements.

## What is a common pattern for maintaining data consistency across different microservices?
<a name="q4"></a>

The most common pattern is using an [event-driven architecture](https://aws.amazon.com/event-driven-architecture/).

## How do I maintain transaction automation?
<a name="q5"></a>

In a microservices architecture, a transaction consists of multiple local transactions handled by different microservices. If a local transaction fails, you need to roll back the successful transactions that were previously completed. You can use the [saga pattern](saga-pattern.md) to avoid this.

## Do I have to use a separate database for each microservice?
<a name="q6"></a>

The main advantage of a microservices architecture is loose coupling. Each microservice's persistent data must be kept private and accessible only through a microservice's API. Changes to the data schema must be carefully evaluated if your microservices share the same database.

## How can I keep a microservice's persistent data private if they all share a single database?
<a name="q7"></a>

If your microservices share a relational database, make sure that you have private tables for each microservice. You can also create individual schemas that are private to the individual microservices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
