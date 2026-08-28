---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing.html
---

# API routing patterns
<a name="api-routing"></a>

In agile development environments, autonomous teams (for example squads and tribes) own one or more services that include many microservices. The teams expose these services as APIs to allow their consumers to interact with their group of services and actions.

There are three major methods for exposing HTTP APIs to upstream consumers by using hostnames and paths:

|
|
| Method | Description | Example |
| --- |--- |--- |
| [Hostname routing](api-routing-hostname.md) | Expose each service as a hostname. | `billing.api.example.com` |
| [Path routing](api-routing-path.md) | Expose each service as a path. | `api.example.com/billing` |
| [Header-based routing](api-routing-http-header.md) | Expose each service as an HTTP header. | `x-example-action: something` |

This section outlines typical use cases for these three routing methods and their trade-offs to help you decide which method best fits your requirements and organizational structure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
