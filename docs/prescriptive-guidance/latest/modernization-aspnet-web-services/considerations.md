---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/considerations.html
---

# Other considerations
<a name="considerations"></a>

So far, we've discussed using API Gateway and Windows containers to modernize your legacy ASP.NET web services on AWS. Here are some other considerations to take into account:
+ Security
+ Remodeling service domains
+ Sequencing web service upgrades when there are many services to modernize

These are discussed in the following sections.

## Authentication and authorization
<a name="security"></a>

Modern APIs generally leverage token-based (JSON Web Token or JWT) authentication and authorization standards such as OAuth 2.0 and OpenID Connect, whereas legacy ASP.NET web services traditionally relied on either basic authentication or Windows-integrated authentication to a Windows Active Directory domain. As a best practice, in cases where the old and new authentication and authorization approaches are incompatible, we recommend that you upgrade these security mechanisms in place before you modernize your web service on AWS. Attempting to map identities or trying to securely transfer security state between the old and new systems might not be a significant effort, but it might introduce security vulnerabilities.

## Domain-driven design
<a name="ddd"></a>

When breaking a monolith into individual services, domain-driven design (DDD) is a best practice that is often used to model systems into cohesive business domains. DDD is an approach to developing software for complex needs by connecting the implementation to an evolving model of the core business concepts. Its premise is to place the project's primary focus on the core domain and domain logic, and to base system designs on a model that reflects the business. If you use DDD when you are modernizing an existing, monolithic application, you need to work backward from the features and user flows of the monolith. You can use DDD in combination with the strangler pattern to guide the process of breaking the monolith and determining which services to strangle, hence the term *domain-driven design*.

## Interim states and target state
<a name="states"></a>

When you're modernizing more than a few ASP.NET web services on AWS, it is a good practice to first define what your target state architecture will be after all services are modernized. However, the target state architecture isn't necessarily the end state or the final state, because business contexts change often and the system target state should be updated as needed to stay aligned with the business goals. When you've defined the target state, you can work backward from there to define interim-state architectures that incrementally fulfill the target state vision. You can think of these interim-state architectures as the progression of the strangler fig vine up the tree as it encounters and engulfs major portions of the host tree. Interim-state architectures often introduce temporary or overlapping constructs that will not be part of the end-state architecture in order to facilitate the evolution to the target state. The modernization of the SOAP-based ASP.NET web service provides an example of this: A Windows-based container is introduced temporarily to bridge the gap between calling systems that are dependent on the legacy service until they can be upgraded to the new REST API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
