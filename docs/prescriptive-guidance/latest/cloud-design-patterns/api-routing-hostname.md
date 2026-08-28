---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing-hostname.html
---

# Hostname routing pattern
<a name="api-routing-hostname"></a>

Routing by hostname is a mechanism for isolating API services by giving each API its own hostname; for example, `service-a.api.example.com` or `service-a.example.com`.

## Typical use case
<a name="hostname-use-case"></a>

### Typical use case
<a name="typical-use-case.058bc9f8-738f-54d7-a8ce-2f91db7781b1"></a>

Routing by using hostnames reduces the amount of friction in releases, because nothing is shared between service teams. Teams are responsible for managing everything from DNS entries to service operations in production.

![Hostname routing.](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/76355efe-b416-4cdc-81f8-e94a2851e264.png)

## Pros
<a name="hostname-pros"></a>

Hostname routing is by far the most straightforward and scalable method for HTTP API routing. You can use any relevant AWS service to build an architecture that follows this method―you can create an architecture with [Amazon API Gateway](https://aws.amazon.com/api-gateway/), [AWS AppSync](https://aws.amazon.com/appsync/), [Application Load Balancers](https://aws.amazon.com/elasticloadbalancing/) and [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/), or any other HTTP-compliant service.

Teams can use hostname routing to fully own their subdomain. It also makes it easier to isolate, test, and orchestrate deployments for specific AWS Regions or versions; for example, `region.service-a.api.example.com` or `dev.region.service-a.api.example.com`.

## Cons
<a name="hostname-cons"></a>

When you use hostname routing, your consumers have to remember different hostnames to interact with each API that you expose. You can mitigate this issue by providing a client SDK. However, client SDKs come with their own set of challenges. For example, they have to support rolling updates, multiple languages, versioning, communicating breaking changes caused by security issues or bug fixes, documentation, and so on.

When you use hostname routing, you also need to register the subdomain or domain every time you create a new service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
