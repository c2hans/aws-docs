---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decompose-subdomain.html
---

# Decompose by subdomain
<a name="decompose-subdomain"></a>

This pattern uses a [domain-driven design (DDD)](https://en.wikipedia.org/wiki/Domain-driven_design) subdomain to decompose monoliths. This approach breaks down the organization's domain model into separate subdomains that are labeled as ***core*** (a key differentiator for the business), ***supporting*** (possibly related to business but not a differentiator), or ***generic*** (not business-specific). This pattern is appropriate for existing monolithic systems that have well-defined boundaries between subdomain-related modules. This means that you can decompose the monolith by repackaging existing modules as microservices but without significantly rewriting existing code. Each subdomain has a model, and the scope of that model is called a *bounded context*. Microservices are developed around this bounded context. The following table explains the advantages and disadvantages of using this pattern.

|
|
| Advantages | Disadvantages |
| --- |--- |
| + Loosely coupled architecture provides scalability, resilience, maintainability, extensibility, location transparency, protocol independence, and time independence.<br />+ Systems become more scalable and predictable. | + Can create too many microservices, which makes service discovery and integration difficult.<br />+ Business subdomains are difficult to identify because they require an in-depth understanding of the overall business. |

The following illustration shows how an insurance monolith can be decomposed into subdomains after it was decomposed by business capabilities.

![Decompose by subdomain pattern](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/images/guide-img/8e9fa68d-7532-4c4b-8c7b-74bc6afdb7b9/images/ee946899-05a3-485d-93d2-e7c97728917c.png)

The illustration shows that the *Sales* and *Marketing* services are broken down into smaller microservices. The *Purchasing* and *Claims* models are important business differentiators for *Sales*, and are split into two separate microservices. *Marketing* is decomposed by using supporting business functionalities such as *Campaigns*, *Analytics*, and *Reports*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
