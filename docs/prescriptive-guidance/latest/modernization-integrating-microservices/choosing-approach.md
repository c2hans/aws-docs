---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/choosing-approach.html
---

# Choosing your coordination approach
<a name="choosing-approach"></a>

Choreography and orchestration both have their uses when integrating microservices. Choose choreography within the boundary of a single microservice, where you have full control over dependencies. Choose orchestration when you work across microservice boundaries. For example, multiple microservices that participate in a distributed transaction will benefit from orchestration to account for rollback from failures. Microservices that handle events that might be of interest to other microservices will benefit from choreography and an event-driven architecture.

A common pattern for implementing rollback when multiple systems are involved in a single transaction is the saga pattern.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
