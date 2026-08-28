---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-the-right-aws-service-for-your-microservice-endpoints/introduction.html
---

# Choosing the right AWS service for your microservice endpoints
<a name="introduction"></a>

*Deepika Kumar and Cecilia Yin, Amazon Web Services*

Many organizations embrace microservices architecture to build and modernize their web applications. Microservices empower small, nimble teams to take complete ownership of specific components of an application. These components communicate through well-defined HTTP and HTTPS endpoints. The endpoints often have unique requirements for request routing, availability, and deployment strategies such as blue/green and canary.

To address HTTP endpoint specific needs, AWS offers the following services:
+ [Application Load Balancer](app-load-balancer.md)
+ [Amazon API Gateway](api-gateway.md)
+ [AWS Lambda function URLs](function-urls.md)

This guide reviews the key capabilities and use cases of each service for creating HTTP endpoints to support your microservices. To help you make an informed design decision, the guide provides a [comparison](services-comparison.md) of these AWS services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
